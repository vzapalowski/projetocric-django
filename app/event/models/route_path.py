from django.db import models

from cities.models import Route

class RoutePath(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do caminho')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    concentration = models.CharField(max_length=100, default='----', verbose_name='Horário de concentração')
    time = models.CharField(max_length=100, verbose_name='Horário de Sáida')
    departure_location = models.CharField(max_length=100, verbose_name='Local de Partida')
    active = models.BooleanField(default=False, verbose_name='Estado da Rota')

    def __str__(self):
        return self.name