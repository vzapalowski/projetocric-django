from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models.api_strava import Api
from core.models import Route, AnchorpointCategory as Category
from .models import City
from projetocric.utilities import replace

@receiver(pre_save, sender=Route)
def insert_polyline(sender, instance, **kwargs):
    api = Api()
    try:
        polyline = api.get_route(instance.id_route)
        instance.polyline = polyline
    except KeyError:
        instance.polyline = None
        
@receiver(pre_save, sender=Route)
def insert_distance(sender, instance, **kwards):
    api = Api()
    try:
        distance = api.get_distance(instance.id_route)
        instance.distance = f'{distance/1000:.2f}'
    except KeyError:
        instance.distance = None

@receiver(pre_save, sender=City)
def change_name_banner_image(sender, instance, **kwargs):
    if instance.banner_image:   
       instance.banner_image.name = replace(instance.banner_image.name)

@receiver(pre_save, sender=Category)
def change_name_category_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.name = replace(instance.image.name)

