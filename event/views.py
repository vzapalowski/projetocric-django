from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from django.http import FileResponse
from django.shortcuts import get_object_or_404

from event.models import Event
from event.models import EnrollmentForm, EnrollmentFormType2
from event.models.enrollment import Bond
from event.models.how_knew import HowKnew
from event.models.route_path import RoutePath
from event.credentials import *


class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['pk'])
        
        context['event'] = event
        context['form'] = lambda: EnrollmentForm(self.request.POST) if self.request.method == 'POST' else EnrollmentForm()
        context['form_2'] = lambda: EnrollmentFormType2(self.request.POST) if self.request.method == 'POST' else EnrollmentFormType2()
        context['bond'] = Bond.objects.all()
        context['howKnew'] = HowKnew.objects.all()
        context['routePath'] = RoutePath.objects.all()
        context['events'] = Event.objects.all()

        return context

def enrollment(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            sendEmail("John Doe")
            form.save()
            messages.success(request, 'Cadastro feito com Sucesso!')

        else:
            error_message = "\n".join(
                f"{str(form.fields[field_name].label)}: {error}"
                for field_name, error_list in form.errors.items()
                for error in error_list
            )
            messages.error(request, error_message)
    else:
        form = EnrollmentForm()
    
    context = {
        'event': event,
        'form': form,
        'bond': Bond.objects.all(),
        'howKnew': HowKnew.objects.all(),
        'routePath': RoutePath.objects.all()
    }
    
    return render(request, 'events/index.html', context)

def enrollment2(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EnrollmentFormType2(request.POST, request.FILES)
        if form.is_valid():
            # sendEmail("John Doe")
            form.save()
            messages.success(request, 'Cadastro feito com Sucesso!')

        else:
            error_message = "\n".join(
                f"{str(form.fields[field_name].label)}: {error}"
                for field_name, error_list in form.errors.items()
                for error in error_list
            )
            messages.error(request, error_message)
    else:
        form = EnrollmentFormType2()
    
    context = {
        'event': event,
        'form_2': form
    }
    
    return render(request, 'events/index.html', context)


def download_pdf(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.pdf_file:
        pdf_path = event.pdf_file.path
        response = FileResponse(open(pdf_path, 'rb'))
        return response
    else:
        return render(request, 'pdf_not_found.html', {'event': event})
    
def sendEmail(name):
    email_sender = EMAIL
    email_password = PASSWORD
    email_reveiver = 'marcelooliveira.ch070@academico.ifsul.edu.br'

    subject = 'Confirmação de Inscrição no Evento [Nome do Evento]'

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('/event/templates/events/email/mail.html')

    template_params = {'name': name, 'last_name': 'Doe', 'from': 'IFSul'}

    html_body = template.render(**template_params)

    em = MIMEMultipart("alternative")
    em['From'] = email_sender
    em['To'] = email_reveiver
    em['Cc'] = email_sender
    em['Bcc'] = email_sender
    em['Subject'] = subject


    body = MIMEText(html_body, 'html')
    em.attach(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reveiver, em.as_string())

