from django.db import models


class Address(models.Model):
    street_name = models.CharField(max_length=100, verbose_name='Nome da rua')
    number = models.PositiveSmallIntegerField(verbose_name='Número do comércio')
    neighborhood = models.CharField(max_length=100, verbose_name='Bairro')
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE, verbose_name='Cidade')

    def __str__(self):
        return self.street_name
    