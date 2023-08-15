from django.db import models
from django.contrib.auth.models import User
from event.models.anchor_point import AnchorPoint
from event.models.route_path import RoutePath


class Event(models.Model):
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
    )

    name = models.CharField(max_length=50, verbose_name='Nome do Evento')
    description = models.CharField(max_length=500, verbose_name="Descrição do evento", null=True)
    lat = models.CharField(max_length=20, null=True, blank=True, default='-29.95', verbose_name='Latitute de Mapa')
    lng = models.CharField(max_length=20, null=True, blank=True, default='-51.64', verbose_name='Longitude do Mapa')
    location = models.CharField(max_length=40, null=True, blank=True, verbose_name='Localidade')
    date = models.DateField(verbose_name='Data do evento', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em andamento', verbose_name='Situação')
    routes_data = models.ManyToManyField(RoutePath, blank=True, null=True, verbose_name='Rotas do Evento')
    points = models.ManyToManyField(AnchorPoint, blank=True, null=True, verbose_name='Pontos do Evento')
    warnings = models.ManyToManyField('event.Warning', blank=True, null=True, verbose_name='Avisos')
    users = models.ManyToManyField(User, related_name='events', blank=True)

    def __str__(self) -> str:
        return self.name