from django.db import models
from colorfield.fields import ColorField
        
class Route(models.Model):
    external_strava_id = models.CharField("ID Strava", max_length=50, unique=True)
    name = models.CharField("Nome", max_length=255, unique=True)
    color = ColorField("Cor da rota", default="#FF0000")

    polyline = models.TextField("Polyline", blank=True, null=True, editable=False)
    distance = models.CharField("Distância(Km)", max_length=100, blank=True, null=True, editable=False)

    active = models.BooleanField("Ativa", default=False)
    is_event_route = models.BooleanField("Rota de evento", default=False)

    def __str__(self):
        return self.name
    
    def get_routes(self):
        return Route.objects.all()
    
    def get_route(self, externalStravaId):
        return Route.objects.get(external_strava_id=externalStravaId)

    class Meta:
        db_table = 'route'
        ordering = ['name']