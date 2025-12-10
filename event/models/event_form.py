from django.db import models


class EventForm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'event_form'
        verbose_name = 'Formulário de Evento'
        verbose_name_plural = 'Formulários de Eventos'