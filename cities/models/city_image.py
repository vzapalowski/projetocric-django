from django.db import models
from cities.models import City


class CityImage(models.Model):
    PATH_IMAGES_CITY = 'cities/images/%Y/%m/%d'
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=PATH_IMAGES_CITY)
    tittle = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=400)

    def __str__(self):
        return self.image.name
    