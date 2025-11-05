from rest_framework import serializers
from cities.models import City
from api.serializers import RouteSerializer
from api.serializers import AnchorpointSerializer

class CityDetailSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(source='route.all', many=True, read_only=True)
    points = AnchorpointSerializer(source='anchorpoints', many=True, read_only=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ('id', 'name', 'banner_image', 'coordinates', 'zoom', 'routes', 'points')

    def get_coordinates(self, obj):
        try:
            return {
                'lat': float(obj.latitude) if obj.latitude else None,
                'lng': float(obj.longitude) if obj.longitude else None
            }
        except (TypeError, ValueError):
            return {'lat': None, 'lng': None}