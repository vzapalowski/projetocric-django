from django.db import models
from cities.models import City

class CityImage(models.Model):
    PATH_IMAGES_CITY = 'cities/images/%Y/%m/%d'
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='images')
    image_path = models.ImageField(upload_to=PATH_IMAGES_CITY)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image_path.name if self.image_path else "Sem imagem"

    class Meta:
        db_table = 'city_image'