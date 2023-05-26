from django.db import models
from event.models import Event

class Warning(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.CharField(max_length=500, verbose_name='Conteúdo')

    def __str__(self):
        return self.title