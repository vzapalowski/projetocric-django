from rest_framework import serializers

from event.models import Event
from api.serializers.route_path import RoutePathSerializer
from api.serializers.anchor_points_event import AnchorPointEventSerializer

class EventSerializer(serializers.ModelSerializer):
    routes_data = RoutePathSerializer(many=True, read_only=True)
    points = AnchorPointEventSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id','name', 'description', 'coordinates', 'zoom', 'routes_data', 'points')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}