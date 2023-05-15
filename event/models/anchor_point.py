from django.db import models

from cities.validators import validate_file_extension_category

class AnchorPoint(models.Model):
    PATH_ICONS_ANCHOR_POINT = 'events/icons/%Y/%m/%d'
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.CharField(max_length=100, verbose_name='Descrição do ponto')
    iconUrl = models.FileField(upload_to=PATH_ICONS_ANCHOR_POINT, validators=[validate_file_extension_category])
    lat = models.CharField(max_length=20, verbose_name='Latitude do Ponto')
    lng = models.CharField(max_length=20, verbose_name='Longitude do Ponto')
    active = models.BooleanField(default=False, verbose_name='Estado do Ponto')

    def __str__(self):
        return self.title
