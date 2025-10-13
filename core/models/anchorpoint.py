from django.db import models
from core.models.AnchorpointCategory import AnchorpointCategory

# class AnchorPoint(models.Model):
#     PATH_IMAGES_ANCHOR_POINTS = 'cities/anchor_points/photos/%Y/%m/%d'
#     image = models.ImageField(upload_to=PATH_IMAGES_ANCHOR_POINTS, verbose_name='Imagem do ponto de apoio')
    
class Anchorpoint(models.Model):
    anchorpoint_category = models.ForeignKey(AnchorpointCategory, on_delete=models.CASCADE, verbose_name='Tipo do ponto de apoio')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='Latitude')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='Longitude')
    business_hours = models.CharField(max_length=120, blank=True, null=True, verbose_name='Horário de funcionamento')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Telefone')
    image = models.CharField(max_length=255, blank=True, null=True, verbose_name='Imagem do ponto de apoio')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Endereço')
    is_event_anchorpoint = models.BooleanField(default=False, verbose_name='É um ponto de apoio de evento?')
    active = models.BooleanField(default=False, verbose_name="Ativo")

    def __str__(self) -> str:
        return self.name
    
    def get_anchor_points(self):
        return AnchorPoint.objects.all()

    class Meta:
        db_table = 'anchorpoint'