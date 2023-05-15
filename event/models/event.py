from django.db import models

from cities.models import Route
from event.models.anchor_point import AnchorPoint

from event.models.route_path import RoutePath

class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do Evento')
    description = models.CharField(max_length=500, verbose_name="Descrição do evento", null=True)
    lat = models.CharField(max_length=20, null=True, blank=True, default='-29.95', verbose_name='Latitute de Mapa')
    lng = models.CharField(max_length=20, null=True, blank=True, default='-51.64', verbose_name='Longitude do Mapa')
    routes_data = models.ManyToManyField(RoutePath, blank=True, null=True, verbose_name='Rotas do Evento')
    points = models.ManyToManyField(AnchorPoint, blank=True, null=True, verbose_name='Pontos do Evento')

    def __str__(self) -> str:
        return self.description