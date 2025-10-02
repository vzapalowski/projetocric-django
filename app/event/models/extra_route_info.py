from django.db import models
from event.models import Event


class ExtraRouteInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    field_one = models.CharField(max_length=100, verbose_name='Campo 1', null=True, blank=True)
    field_two = models.CharField(max_length=100, verbose_name='Campo 2', null=True, blank=True)
    field_three = models.CharField(max_length=100, verbose_name='Campo 3', null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='extra_info')

    def __str__(self):
        return self.title