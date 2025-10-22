from rest_framework import serializers
from cities.models import City
from api.serializers import RouteSerializer
from api.serializers.anchorpoint import AnchorpointSerializer

class CitySerializer(serializers.ModelSerializer):
    route = RouteSerializer(many=True, read_only=True)
    # REMOVA ou CORRIJA a linha abaixo - anchorpoint não existe no modelo
    anchorpoint = AnchorpointSerializer(many=True)
    
    coordinates = serializers.SerializerMethodField()
    
    class Meta:
        model = City
        fields = (
            'id', 
            'name', 
            'banner_image', 
            'coordinates', 
            'zoom', 
            'active',
            'visible',
            'route',
            'anchorpoints' 
        )

    def get_coordinates(self, obj):
        return {'lat': obj.latitude, 'lng': obj.longitude}