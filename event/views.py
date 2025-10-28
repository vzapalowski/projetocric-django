from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import ssl
import smtplib
import jinja2
import pdfkit
import tempfile
import os
import datetime

from event.credentials import *
from django.views.generic.detail import DetailView
from event.models import Event, Enrollment, EventBond, EventRoute, EventHowknew, Warning
# from event.forms import EnrollmentForm, EnrollmentFormType2, enrollment3PasseioIfsulForm

class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        
        # # Forms
        # if self.request.method == 'POST':
        #     context['form'] = EnrollmentForm(self.request.POST)
        #     context['form_2'] = EnrollmentFormType2(self.request.POST)
        #     context['form_3'] = enrollment3PasseioIfsulForm(self.request.POST)
        # else:
        #     context['form'] = EnrollmentForm()
        #     context['form_2'] = EnrollmentFormType2()
        #     context['form_3'] = enrollment3PasseioIfsulForm()
        
        # Dados do evento
        context['bond'] = EventBond.objects.all()
        context['howKnew'] = EventHowknew.objects.all()

        context['events'] = Event.objects.all()
        context['event_routes'] = EventRoute.objects.filter(event=event, active=True)
        context['warnings'] = Warning.objects.filter(event=event)
        
        return context

# def enrollment(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             full_name = form.cleaned_data['full_name']  
#             email = form.cleaned_data['email']  
#             # send_email(email, full_name, event)
#             form.save()
#             messages.success(request, 'Cadastro feito com Sucesso!')

#         else:
#             error_message = "\n".join(
#                 f"{str(form.fields[field_name].label)}: {error}"
#                 for field_name, error_list in form.errors.items()
#                 for error in error_list
#             )
#             messages.error(request, error_message)
#     else:
#         form = EnrollmentForm()
    
#     context = {
#         'event': event,
#         'form': form,
#         'bond': Bond.objects.all(),
#         'howKnew': HowKnew.objects.all(),
#         'routePath': RoutePath.objects.all()
#     }
    
#     return render(request, 'events/index.html', context)

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

# def generate_certificate(name, event):
#     options = {
#         'page-size': 'A4',
#         'margin-top': '0',
#         'margin-right': '0',
#         'margin-bottom': '0',
#         'margin-left': '0',
#         'encoding': "UTF-8",
#         'no-outline': None,
#         'enable-local-file-access': True,
#         'allow': ['images'],
#         'user-style-sheet': 'http://rota-cric.charqueadas.ifsul.edu.br/static/event/style-certificate.css'
#     }

#     # locale.setlocale(locale.LC_TIME, 'pt_PT.utf8')
#     current_date = datetime.date.today()
#     formatted_date = current_date.strftime('%d/%m/%Y')

#     context = {'name': name, 'event': event.name, 'date': formatted_date} 

#     temp_dir = tempfile.mkdtemp()
#     output_pdf = os.path.join(temp_dir, 'certificate.pdf')

#     template_loader = jinja2.FileSystemLoader('.')
#     template_env = jinja2.Environment(loader=template_loader)
#     html_template = 'templates/events/certificate.html'
#     template = template_env.get_template(html_template)
#     output_text = template.render(context)

#     config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
#     pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)

#     with open(output_pdf, 'rb') as pdf_file:
#         pdf_content = pdf_file.read()

#     os.remove(output_pdf)
#     os.rmdir(temp_dir)

#     return pdf_content

# def get_certificate(request, enrollment_id):
#     enrollment = get_object_or_404(EnrollmentType2, id=enrollment_id)

#     certificate_content = generate_certificate(enrollment.full_name, enrollment.event)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="certificate_{enrollment.user.username}.pdf"'
#     response.write(certificate_content)

#     return response

# def delete_enrollment(request, enrollment_id):
#     enrollment = Enrollment.objects.get(id=enrollment_id)
#     if request.user == enrollment.user:
#         enrollment.delete()
#         return redirect('users:profile')
#     else:
#         return redirect('users:profile')

# def delete_enrollment_type2(request, enrollment_id):
#     enrollment = EnrollmentType2.objects.get(id=enrollment_id)
#     if request.user == enrollment.user:
#         enrollment.delete()
#         return redirect('users:profile')
#     else:
#         return redirect('users:profile')
    
# def delete_enrollment_type3(request, enrollment_id):
#     enrollment = enrollment3PasseioIfsulForm.objects.get(id=enrollment_id)
#     if request.user == enrollment.user:
#         enrollment.delete()
#         return redirect('users:profile')
#     else:
#         return redirect('users:profile')
    
# def delete_enrollment_type4(request, enrollment_id):
    # enrollment = enrollment4PasseioIfsulForm.objects.get(id=enrollment_id)
    # if request.user == enrollment.user:
    #     enrollment.delete()
    #     return redirect('users:profile')
    # else:
    #     return redirect('users:profile')