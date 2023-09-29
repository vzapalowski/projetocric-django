from django.db import models
from event.models.how_knew import HowKnew
from event.models.route_path import RoutePath
from event.models.event import Event
from django.contrib.auth.models import User


class Bond(models.Model):
    name = models.CharField(max_length=100, verbose_name='Vínculo')

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.CharField(max_length=70, verbose_name='Email para contato')
    social_network = models.CharField(max_length=30, verbose_name='Instagram', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    bond_choice = models.ForeignKey(Bond, on_delete=models.CASCADE, verbose_name='Vínculo')
    rg = models.CharField(max_length=10, verbose_name='RG')
    how_knew = models.ForeignKey(HowKnew, on_delete=models.CASCADE, verbose_name='Como soube do evento?')
    route_path = models.ForeignKey(RoutePath, on_delete=models.CASCADE, verbose_name='Nome do Trajeto')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')

    def __str__(self):
        return self.full_name
    