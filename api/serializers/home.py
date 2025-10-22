from rest_framework import serializers

from api.serializers import RouteSerializer
from api.serializers.anchorpoint import AnchorpointSerializer
from home.models import Home

class HomeSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    points = AnchorpointSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = (
            'id', 
            'name', 
            'coordinates', 
            'zoom', 
            'routes', 
            'points'
        )

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}