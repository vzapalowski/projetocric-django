from django.db import models
from colorfield.fields import ColorField

class Route(models.Model):
    external_strava_id = models.CharField(unique=True, max_length=50, blank=True, null=True, verbose_name='Id Strava da rota')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome')
    polyline = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Marcação')
    color = models.ColorField(default="#FF0000", verbose_name="Cor da rota")
    distance = models.CharField(max_length=500, blank=True, null=True, verbose_name='Distância')
    active = models.BooleanField(default=False, verbose_name='Ativa')

    def __str__(self) -> str:
        return self.name

    def get_routes(self):
        return Route.objects.all()
    
    def get_route(self, externalStravaId):
        return Route.objects.get(external_strava_id=externalStravaId)

    class Meta:
        db_table = 'route'