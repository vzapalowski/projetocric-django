from django.db import models
from core.validators import validate_file_extension_category

# class Category(models.Model):
#     PATH_IMAGES_CATEGORIES = 'cities/categories/photos/%Y/%m/%d'
#     image = models.FileField(upload_to=PATH_IMAGES_CATEGORIES, validators=[validate_file_extension_category])

    
class AnchorpointCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    icon_path = models.FileField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'anchorpoint_category'