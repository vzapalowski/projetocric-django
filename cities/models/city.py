from django.db import models

from core.models.route import Route

class City(models.Model):
    PATH_IMAGES_CITIES_BANNER = 'cities/images/banner_photos/%Y/%m/%d'
    name = models.CharField(max_length=255, verbose_name='Nome')
    banner_image = models.ImageField(upload_to=PATH_IMAGES_CITIES_BANNER, verbose_name="Imagem do Banner")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default="-29.958491", verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default="-51.629398", verbose_name="Longitude")
    active = models.BooleanField(default=False, verbose_name='Acessível')
    visible = models.BooleanField(default=False, verbose_name='Visível')
    zoom = models.IntegerField(default=14, verbose_name='Zoom')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    route = models.ManyToManyField(Route, blank=True, verbose_name='Rotas')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'