from django.db import models
from colorfield.fields import ColorField


class Route(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nome')
    color = ColorField(default="#FF0000", verbose_name="Cor da rota")
    id_route = models.CharField(max_length=50, unique=True, verbose_name='Id da rota')
    polyline = models.CharField(max_length=5000,blank=True, null=True, verbose_name='Marcação')
    distance = models.CharField(max_length=500, blank=True, null=True, verbose_name='Distância')
    active = models.BooleanField(default=False, verbose_name='Ativa')

    def __str__(self) -> str:
        return self.name

    def get_routes(self):
        data = Route.objects.all()
        return data
    
    def get_route(self, idRoute):
        return Route.objects.get(id_route=idRoute)