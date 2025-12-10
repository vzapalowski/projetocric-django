from rest_framework import serializers

from core.models import Anchorpoint
from api.serializers.anchorpoint_category import AnchorpointCategorySerializer

class AnchorpointSerializer(serializers.ModelSerializer):
    anchorpoint_category = AnchorpointCategorySerializer(many=False)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Anchorpoint
        fields = (
            'id', 
            'name', 
            'coordinates', 
            'business_hours', 
            'phone', 
            'image', 
            'address',
            'anchorpoint_category', 
        )

    def get_coordinates(self, obj):
        if isinstance(obj, dict):
            return {'lat': obj.get('lat'), 'lng': obj.get('lng')}
        else:
            return {'lat': obj.latitude, 'lng': obj.longitude}