from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from .models import Route
from .models import Api

api = Api()
route = Route()

@receiver(post_save, sender=Route)
def my_function(sender, instance, created, **kwargs):
    if created:
        last_insert = Route.objects.latest('id')
        obj_route = route.get_route(last_insert.id_route)
        try:
            polilyne = api.getRoute(last_insert.id_route)
            obj_route.polilyne = polilyne
            obj_route.save()
        except KeyError:
            obj_route.polilyne = None
            obj_route.save()