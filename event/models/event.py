from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from event.models import Warning
from event.models.event_route import EventRoute
from event.models.event_form import EventForm
from core.models.anchorpoint import Anchorpoint

class Event(models.Model):
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
    )


    name = models.CharField(max_length=255, verbose_name='Nome do Evento')
    description = models.TextField(max_length=1000, verbose_name="Descrição do evento", null=True)
    date = models.DateField(blank=True, null=True, verbose_name='Data do evento')
    
    secondary_date = models.DateField(blank=True, null=True, verbose_name='Data secundária do evento')
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='Latitute')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='Longitude')
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name='Localidade')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em andamento', verbose_name='Situação')
    banner_image = models.ImageField(upload_to='events/images/%Y/%m/%d', null=True, blank=True, verbose_name='Banner do evento')
    zoom = models.IntegerField(default=13, verbose_name='Zoom')
    pdf_file = models.FileField(upload_to='events/pdfs/%Y/%m/%d', null=True, blank=True, verbose_name='Termo de inscrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    warning = models.ManyToManyField(Warning, blank=True, verbose_name='Avisos')
    participants = models.ManyToManyField(User, related_name='events', blank=True)
    anchorpoint = models.ManyToManyField(Anchorpoint, blank=True, verbose_name='Pontos do Evento')

    form = models.ForeignKey(EventForm, on_delete=models.SET_NULL, null=True, blank=True,  related_name='event_forms', verbose_name='Formulário de inscrição')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'event'