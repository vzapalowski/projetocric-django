from rest_framework import serializers

from event.models import Event
from api.serializers import RouteSerializer

class EventSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'description', 'coordinates', 'routes')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}