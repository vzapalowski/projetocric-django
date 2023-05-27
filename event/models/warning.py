from django.db import models
from django.utils import timezone

class Warning(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.CharField(max_length=500, verbose_name='Conteúdo')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')

    def __str__(self):
        return self.title