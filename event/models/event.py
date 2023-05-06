from django.db import models

from cities.models import Route

class Event(models.Model):
    description = models.CharField(max_length=500, verbose_name="Descrição do evento", null=True)
    lat = models.CharField(max_length=20, null=True, blank=True, default='-29.95', verbose_name='Latitute de Mapa')
    lng = models.CharField(max_length=20, null=True, blank=True, default='-51.64', verbose_name='Longitude do Mapa')
    routes = models.ManyToManyField(Route, blank=True, null=True, verbose_name="Rotas do Evento")

    def __str__(self) -> str:
        return self.description