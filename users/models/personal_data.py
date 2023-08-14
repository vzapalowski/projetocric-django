from django.db import models
from django.contrib.auth.models import User
from event.models.enrollment import Bond


class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_network = models.CharField(max_length=30, verbose_name='Instagram', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Data de Nascimento', null=True)
    rg = models.CharField(max_length=10, verbose_name='RG', null=True)
    bond_choice = models.ForeignKey(Bond, on_delete=models.CASCADE, verbose_name='Vínculo', null=True)

    def __str__(self):
        return self.user.email
