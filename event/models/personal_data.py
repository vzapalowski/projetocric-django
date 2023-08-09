from django.db import models
from django.contrib.auth.models import User
from event.models.enrollment import Bond


class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    social_network = models.CharField(max_length=30, verbose_name='Instagram', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=10, verbose_name='RG')
    bond_choice = models.ForeignKey(Bond, on_delete=models.CASCADE, verbose_name='Vínculo')

    def __str__(self):
        return self.full_name
