from django.db import models
from django.contrib.auth.models import User
from event.models.anchor_point import AnchorPoint
from event.models.route_path import RoutePath


class Event(models.Model):
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
    )

    FORM_TYPE_CHOICES = (
        ('Type-1', 'Type-1'),
        ('Type-2', 'Type-2'),
    )

    name = models.CharField(max_length=50, verbose_name='Nome do Evento')
    description = models.CharField(max_length=800, verbose_name="Descrição do evento", null=True)
    lat = models.CharField(max_length=20, null=True, blank=True, default='-29.95', verbose_name='Latitute de Mapa')
    lng = models.CharField(max_length=20, null=True, blank=True, default='-51.64', verbose_name='Longitude do Mapa')
    zoom = models.IntegerField(default=13, verbose_name='Zoom')
    location = models.CharField(max_length=40, null=True, blank=True, verbose_name='Localidade')
    banner_image = models.ImageField(upload_to='events/images/%Y/%m/%d', null=True, blank=True, verbose_name='Banner do evento')
    date = models.DateField(verbose_name='Data do evento', null=True, blank=True)
    secondary_date = models.DateField(verbose_name='Data secundária do evento', null=True, blank=True)
    form_type = models.CharField(max_length=30, choices=FORM_TYPE_CHOICES, default='Type-1', verbose_name='Tipo de formulário')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em andamento', verbose_name='Situação')
    routes_data = models.ManyToManyField(RoutePath, blank=True, null=True, verbose_name='Rotas do Evento')
    points = models.ManyToManyField(AnchorPoint, blank=True, null=True, verbose_name='Pontos do Evento')
    warnings = models.ManyToManyField('event.Warning', blank=True, null=True, verbose_name='Avisos')
    users = models.ManyToManyField(User, related_name='events', blank=True)
    pdf_file = models.FileField(upload_to='events/pdfs/%Y/%m/%d', null=True, blank=True, verbose_name='Termo de inscrição')

    def __str__(self) -> str:
        return self.name
    