from django.db import models
from .event import Event


class EnrollmentType2(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.CharField(max_length=30, verbose_name='Email para contato')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')
    term_file = models.FileField(upload_to='events/enrollments/%Y/%m/%d', verbose_name='Termo de inscrição')

    def __str__(self):
        return self.full_name
    