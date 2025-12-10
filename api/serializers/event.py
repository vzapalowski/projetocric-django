from rest_framework import serializers

from event.models import Event
from api.serializers.anchorpoint import AnchorpointSerializer
from api.serializers.event_route import EventRouteSerializer

class EventSerializer(serializers.ModelSerializer):
    anchorpoint = AnchorpointSerializer(many=True)
    coordinates = serializers.SerializerMethodField()
    routes = EventRouteSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'name', 
            'description',
            'date',
            'secondary_date',
            'status',
            'banner_image', 
            'zoom', 
            'anchorpoint',
            'routes',
            'coordinates',
        )

    def get_coordinates(self, obj):
        return {
            'lat': obj.latitude, 
            'lng': obj.longitude
        }