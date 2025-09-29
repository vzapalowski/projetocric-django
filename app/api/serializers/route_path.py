from rest_framework import serializers

from event.models.route_path import RoutePath
from .route import RouteSerializer

class RoutePathSerializer(serializers.ModelSerializer):
    route = RouteSerializer()
    class Meta:
        model = RoutePath
        fields = ('id', 'name', 'route', 'time', 'departure_location', 'active')
