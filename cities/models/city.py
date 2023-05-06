from django.db import models

from cities.models.route import Route
from cities.models.anchor_point import AnchorPoint

class City(models.Model):
    PATH_IMAGES_CITIES_BANNER = 'cities/images/banner_photos/%Y/%m/%d'
    name = models.CharField(max_length=100, verbose_name='Nome')
    lat = models.CharField(max_length=50, default='-29.95', verbose_name="Latitude")
    lng = models.CharField(max_length=50, default='-51.64', verbose_name="Longitude")
    banner_image = models.ImageField(upload_to=PATH_IMAGES_CITIES_BANNER, verbose_name="Imagem do Banner")
    routes = models.ManyToManyField(Route, blank=True, null=True, verbose_name='Rotas')
    points = models.ManyToManyField(AnchorPoint, blank=True, null=True, verbose_name='Pontos de apoio')
    visible = models.BooleanField(default=False, verbose_name='Visível')

    def __str__(self):
        return self.name
