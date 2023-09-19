from django.db import models
from event.models.how_knew import HowKnew
from event.models.route_path import RoutePath
from django.contrib.auth.models import User

    
class EnrollmentField(models.Model):
    name = models.CharField(max_length=25,verbose_name='Nome')
    type = models.CharField(max_length=25,verbose_name='Tipo',null=True)

    def __str__(self):
        return self.name
    