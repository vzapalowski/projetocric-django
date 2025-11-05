from django.db import models
from django.utils import timezone
from event.models.event import Event

class Warning(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(max_length=500, verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,  related_name='event_warning', verbose_name='Evento')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'event_warning'