from django.db import models
from core.models import Route

class EventRoute(models.Model):
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, related_name='event_routes')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Nome do caminho')
    time = models.CharField(max_length=100, verbose_name='Horário de Saída')
    departure_location = models.CharField(max_length=255, verbose_name='Local de Partida')
    concentration = models.CharField(max_length=255, default='----', verbose_name='Horário de concentração')
    active = models.BooleanField(default=False, verbose_name='Estado da Rota')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'event_route'
        unique_together = (('event', 'route'),)