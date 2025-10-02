from django.db import models
from cities.models import City


class CityManager(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    