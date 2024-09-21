from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models.api_strava import Api

from .models import Route, City, Category, Segment
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
def insert_distance(sender, instance, **kargs):
    api = Api()
    try:
        distance = api.get_distance(instance.id_route)
        instance.distance = f'{distance / 1000:.2f}'
    except KeyError:
        instance.distance = None
        
@receiver(post_save, sender=Route)
def insert_segments(sender, instance, created, **kwargs):
    api = Api()
    try:
        # # Obtém os segmentos da rota
        segments = api.get_segments(instance.id_route)
        
        # # Insere ou atualiza os segmentos da rota
        for seg in segments:
            segment  = api.get_segment(seg['id'])
            Segment.objects.update_or_create(
                id=segment['id'], 
                name=segment['name'],
                city = segment['city'] if segment['city'] is not None else 'Não Informada',
                state = segment['state'] if segment['state'] is not None else 'Não Informado',
                country = segment['country'] if segment['country'] is not None else 'Não Informado',
                distance = f"{segment['distance'] / 1000:.2f}" if segment['distance'] is not None else 'Não Informada',
                total_elevation_gain = segment['total_elevation_gain'] if segment['total_elevation_gain'] is not None else 'Não Informado',
                average_grade = segment['average_grade'] if segment['average_grade'] is not None else 'Não Informada',
                elevation_low = segment['elevation_low'] if segment['elevation_low'] is not None else 'Não Informada',
                elevation_high = segment['elevation_high'] if segment['elevation_high'] is not None else 'Não Informada',
                polyline = segment['map']['polyline'] if segment['map']['polyline'] is not None else 'Não Informada',
                effort_count = segment['effort_count'] if segment['effort_count'] is not None else 'Não Informadas',
                athlete_count = segment['athlete_count'] if segment['athlete_count'] is not None else 'Não Informada',
                route=instance  
            )

    except KeyError:
        instance.segments = None


@receiver(pre_save, sender=City)
def change_name_banner_image(sender, instance, **kwargs):
    if instance.banner_image:   
       instance.banner_image.name = replace(instance.banner_image.name)

@receiver(pre_save, sender=Category)
def change_name_category_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.name = replace(instance.image.name)

