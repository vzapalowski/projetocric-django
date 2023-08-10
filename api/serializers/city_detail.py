from rest_framework import serializers

from cities.models import City
from api.serializers import RouteSerializer
from api.serializers.anchor_point import AnchorPointSerializer

class CityDetailSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    points = AnchorPointSerializer(many=True)

    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ('id', 'name', 'banner_image', 'coordinates', 'zoom', 'routes', 'points')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}