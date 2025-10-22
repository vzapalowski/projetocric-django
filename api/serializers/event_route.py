from rest_framework import serializers

from event.models.event_route import EventRoute
from .route import RouteSerializer

class EventRouteSerializer(serializers.ModelSerializer):
    route = RouteSerializer()

    class Meta:
        model = EventRoute
        fields = (
            'id', 
            'route', 
            'name', 
            'time', 
            'departure_location', 
            'concentration',
            'active'
        )
