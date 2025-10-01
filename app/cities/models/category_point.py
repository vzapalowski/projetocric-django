from django.db import models
from cities.validators import validate_file_extension_category

class Category(models.Model):
    PATH_IMAGES_CATEGORIES = 'cities/categories/photos/%Y/%m/%d'
    name = models.CharField(max_length=50, verbose_name='Nome')
    image = models.FileField(upload_to=PATH_IMAGES_CATEGORIES, validators=[validate_file_extension_category])

    def __str__(self):
        return self.name
    