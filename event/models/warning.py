from django.db import models
from django.utils import timezone

class Warning(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(max_length=500, verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'warning'