from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

import ssl
import smtplib
import jinja2
import pdfkit
import tempfile
import os
import sys
import shutil
import datetime
from django.conf import settings

from event.credentials import *
from django.views.generic.detail import DetailView
from event.models import Event, Enrollment, EventBond, EventRoute, EventHowknew, Warning, EventFormResponse

class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def find_option_model(self, code_name):

        MODELS = [EventBond, EventHowknew]

        for model in MODELS:
            if model.objects.filter(code_name=code_name).exists():
                return model

        return None


    def resolve_display_name(code_name):

        MODELS = [EventBond, EventHowknew]

        for model in MODELS:
            item = model.objects.filter(code_name=code_name).first()
            if item:
                return item.name 

        return code_name 

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        
        form_fields = []
        if event.form:
            form_fields = event.form.fields.all().order_by('order')

            for field in form_fields:

                if field.type == "select":

                    raw_list = [opt.strip() for opt in re.split(r'[;,]', field.options) if opt.strip()] if field.options else []

                    field.options_list = []

                    for opt in raw_list:

                        model_class = self.find_option_model(opt)

                        if model_class:
                            try:
                                item = model_class.objects.get(code_name=opt)
                                field.options_list.append({
                                    "value": item.code_name,
                                    "label": item.name
                                })
                            except model_class.DoesNotExist:
                                field.options_list.append({
                                    "value": opt,
                                    "label": opt
                                })
                        else:
                            field.options_list.append({
                                "value": opt,
                                "label": opt
                            })

        
        context['form_fields'] = form_fields
        context['bond'] = EventBond.objects.all()
        context['howKnew'] = EventHowknew.objects.all()
        context['events'] = Event.objects.all()
        context['event_routes'] = EventRoute.objects.filter(event=event, active=True)
        context['warnings'] = Warning.objects.filter(event=event)
        context['user_is_subscribed'] = event.participants.filter(id=self.request.user.id).exists() if self.request.user.is_authenticated else False
        
        return context

def enrollment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        try:
            # Verificar se o evento tem um formulário vinculado
            if not event.form:
                messages.error(request, 'Este evento não possui formulário de inscrição.')
                return redirect('events:event', pk=event_id)
            
            # Obter todos os campos do formulário
            form_fields = event.form.fields.all()
            
            # Validar campos obrigatórios do formulário dinâmico
            missing_required_fields = []
            for field in form_fields:
                if field.required:
                    field_value = request.POST.get(f'field_{field.id}')
                    if not field_value:
                        missing_required_fields.append(field.label)
            
            if missing_required_fields:
                messages.error(request, f'Por favor, preencha os campos obrigatórios: {", ".join(missing_required_fields)}')
                return redirect('events:event', pk=event_id)
            
            # Verificar se a rota existe e está ativa (se houver campo de rota)
            route_path_id = request.POST.get('route_path')
            route = None
            if route_path_id:
                try:
                    route = EventRoute.objects.get(id=route_path_id, event=event, active=True)
                except EventRoute.DoesNotExist:
                    messages.error(request, 'Rota selecionada não está disponível.')
                    return redirect('events:event', pk=event_id)
            
            # Criar enrollment (apenas com campos mínimos)
            enrollment = Enrollment.objects.create(
                user=request.user if request.user.is_authenticated else None,
                event=event,
                route=route,
                # Não inclua campos fixos como full_name, email, etc.
                # Esses dados virão dos campos dinâmicos
            )
            
            # Processar TODOS os campos dinâmicos do formulário
            for field in form_fields:
                field_value = request.POST.get(f'field_{field.id}')
                if field_value:  # Só cria resposta se houver valor
                    EventFormResponse.objects.create(
                        enrollment=enrollment,
                        field=field,
                        value=field_value
                    )
            
            # Sucesso
            messages.success(request, 'Inscrição realizada com sucesso!')
            if request.user.is_authenticated:
                event.participants.add(request.user)
                event.save()

            return redirect(reverse('events:enrollment_success') + f'?enrollment_id={enrollment.id}')
            
        except Exception as e:
            messages.error(request, f'Erro ao processar inscrição: {str(e)}')
            return redirect('events:event', pk=event_id)
    
    # Se não for POST, redireciona para a página do evento
    return redirect('events:event', pk=event_id)

def enrollment_success(request):
    enrollment_id = request.GET.get('enrollment_id')
    if not enrollment_id:
        # Handle error - no enrollment_id provided
        return render(request, 'error.html', {'message': 'ID de inscrição não fornecido'})
    
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    context = {
        'enrollment': enrollment,
        'event': enrollment.event,
    }
    return render(request, 'events/enrollment_success.html', context)

def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)

    if request.user == enrollment.user or request.user.is_staff:

        if hasattr(enrollment.event, "participants"):
            enrollment.event.participants.remove(request.user)

        enrollment.delete()

        messages.success(request, 'Inscrição cancelada com sucesso!')
    else:
        messages.error(request, 'Você não tem permissão para cancelar esta inscrição.')

    return redirect('users:profile')

# def enrollment2(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     if request.method == 'POST':
#         form = EnrollmentFormType2(request.POST, request.FILES)
#         if form.is_valid():
#             full_name = form.cleaned_data['full_name']  
#             email = form.cleaned_data['email']  
#             # send_email(email, full_name, event)
#             messages.success(request, 'Cadastro feito com Sucesso!')

#         else:
#             error_message = "\n".join(
#                 f"{str(form.fields[field_name].label)}: {error}"
#                 for field_name, error_list in form.errors.items()
#                 for error in error_list
#             )
#             messages.error(request, error_message)
#     else:
#         form = EnrollmentFormType2()
    
#     context = {
#         'event': event,
#         'form_2': form
#     }
    
#     return render(request, 'events/index.html', context)

# def enrollment3(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         form = enrollment3PasseioIfsulForm(request.POST, request.FILES)
#         mutable_form = form.data.copy()
        
#         try:
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, 'O email fornecido não é válido.')
#             mutable_form['email'] = ''
#             modified_form = enrollment3PasseioIfsulForm(mutable_form, request.FILES)
#             context = {
#                 'event': event,
#                 'form': modified_form,
#                 'bond': Bond.objects.all(),
#                 'howKnew': HowKnew.objects.all(),
#                 'routePath': RoutePath.objects.all(),
#                 'events': Event.objects.all()
#             }
            
#             return render(request, 'events/index.html', context)
        
        
#         if form.is_valid():
#             full_name = form.cleaned_data['full_name']  
#             email = form.cleaned_data['email']  
#             send_email(email, full_name, event)
#             form.save()
#             messages.success(request, 'Cadastro feito com Sucesso!')
#             return redirect('events:event', pk=event_id)
#         else:
#             error_message = "\n".join(
#                 f"{str(form.fields[field_name].label)}: {error}"
#                 for field_name, error_list in form.errors.items()
#                 for error in error_list
#             )
#             messages.error(request, error_message)
            
#             context = {
#                 'event': event,
#                 'form': form,
#                 'bond': Bond.objects.all(),
#                 'howKnew': HowKnew.objects.all(),
#                 'routePath': RoutePath.objects.all(),
#                 'events': Event.objects.all()
#             }
#             return render(request, 'events/index.html', context)
#     return redirect('events:event', pk=event_id)

# def enrollment4(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         form = enrollment4PasseioIfsulForm(request.POST, request.FILES)
#         mutable_form = form.data.copy()
        
#         try:
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, 'O email fornecido não é válido.')
#             mutable_form['email'] = ''
#             modified_form = enrollment4PasseioIfsulForm(mutable_form, request.FILES)
#             context = {
#                 'event': event,
#                 'form': modified_form,
#                 'bond': Bond.objects.all(),
#                 'howKnew': HowKnew.objects.all(),
#                 'routePath': RoutePath.objects.all(),
#                 'events': Event.objects.all()
#             }
            
#             return render(request, 'events/index.html', context)
#         except Exception as e:
#             messages.error(request, f"Ocorreu um erro: {str(e)}")
        
#         if form.is_valid():
#             full_name = form.cleaned_data['full_name']  
#             email = form.cleaned_data['email']  
            
#             try:
#                 send_email(email, full_name, event)
#             except Exception as e:
#                 messages.error(request, f"Ocorreu um erro ao enviar o e-mail: {str(e)}")
#                 return redirect('events:event', pk=event_id)
            
            
#             form.save()
#             messages.success(request, 'Cadastro feito com Sucesso!')
#             return redirect('events:event', pk=event_id)
#         else:
#             error_message = "\n".join(
#                 f"{str(form.fields[field_name].label)}: {error}"
#                 for field_name, error_list in form.errors.items()
#                 for error in error_list
#             )
#             messages.error(request, error_message)
            
#             context = {
#                 'event': event,
#                 'form': form,
#                 'bond': Bond.objects.all(),
#                 'howKnew': HowKnew.objects.all(),
#                 'routePath': RoutePath.objects.all(),
#                 'events': Event.objects.all()
#             }
#             return render(request, 'events/index.html', context)
#     return redirect('events:event', pk=event_id)

def download_pdf(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.pdf_file:
        pdf_path = event.pdf_file.path
        response = FileResponse(open(pdf_path, 'rb'))
        return response
    else:
        return render(request, 'pdf_not_found.html', {'event': event})
    
# def send_email(email, name, event):
#     email_sender = EMAIL
#     email_password = PASSWORD
#     email_receiver = email

#     subject = f'Confirmação de Inscrição no Evento {event.name}'
    
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('templates/events/email/mail.html')

#     template_params = {'name': name,'event': event.name}

#     html_body = template.render(**template_params)

#     em = MIMEMultipart("alternative")
#     em['From'] = email_sender
#     em['To'] = email_receiver
#     em['Cc'] = email_sender
#     em['Bcc'] = email_sender
#     em['Subject'] = subject

#     body = MIMEText(html_body, 'html')
#     em.attach(body)

#     certificate_pdf = generate_certificate(name, event)

#     pdf_attachment = MIMEApplication(certificate_pdf, _subtype="pdf")
#     pdf_attachment.add_header('Content-Disposition', 'attachment', filename='certificate.pdf')
#     em.attach(pdf_attachment)

#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, em.as_string())

def generate_certificate(name, event):
    options = {
        'page-size': 'A4',
        'orientation': 'Landscape',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': True,
        'allow': ['images'],
    }

    # locale.setlocale(locale.LC_TIME, 'pt_PT.utf8')
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    context = {'name': name, 'event': event.name, 'date': formatted_date}

    temp_dir = tempfile.mkdtemp()
    output_pdf = os.path.join(temp_dir, 'certificate.pdf')

    template_loader = jinja2.FileSystemLoader('.')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'templates/events/certificate.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    # Discover wkhtmltopdf executable:
    # 1) Use WKHTMLTOPDF_CMD env var if provided
    # 2) Fallback to PATH lookup via shutil.which
    # 3) On Unix-like systems, try the common /usr/bin/wkhtmltopdf
    # Prefer configuration from Django settings (loaded from .env via decouple)
    wkhtmltopdf_cmd = getattr(settings, 'WKHTMLTOPDF_CMD', None) or shutil.which('wkhtmltopdf')

    if not wkhtmltopdf_cmd:
        default_unix = '/usr/bin/wkhtmltopdf'
        if os.path.exists(default_unix):
            wkhtmltopdf_cmd = default_unix

    if not wkhtmltopdf_cmd:
        raise OSError(
            "wkhtmltopdf executable not found. Configure WKHTMLTOPDF_CMD in settings/.env or add it to PATH."
        )

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_cmd)
    try:
        pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)
    except OSError as e:
        raise OSError(f"Failed to run wkhtmltopdf at {wkhtmltopdf_cmd}: {e}")

    with open(output_pdf, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    os.remove(output_pdf)
    os.rmdir(temp_dir)

    return pdf_content

def get_certificate(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)

    event = enrollment.event

    user_is_participant = (
        request.user.is_authenticated
        and event.participants.filter(id=request.user.id).exists()
    )

    if user_is_participant:
        user_name = request.user.get_full_name() or request.user.first_name or request.user.username
        certificate_content = generate_certificate(user_name, event)
        filename = f'Certificado De Participação de Evento - RotaCRIC - {user_name}.pdf'

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.write(certificate_content)

        return response


def certificate_preview(request):
    """DEBUG-only: render certificate HTML in browser without forcing download."""
    if not settings.DEBUG:
        return HttpResponse(status=404)

    # Allow quick tweaks via query params during dev
    name = request.GET.get('name') or 'Participante Teste'
    event = request.GET.get('event') or 'Evento Exemplo'
    date = request.GET.get('date') or datetime.date.today().strftime('%d/%m/%Y')
    hours = request.GET.get('hours') or '4 horas'

    context = {
        'name': name,
        'event': event,
        'date': date,
        'hours': hours,
    }

    return render(request, 'events/certificate.html', context)