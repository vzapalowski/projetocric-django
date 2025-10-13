from rest_framework import serializers

from core.models import Anchorpoint
from api.serializers.anchorpoint_category import AnchorpointCategorySerializer

class AnchorPointSerializer(serializers.ModelSerializer):
    category = AnchorpointCategorySerializer(many=False)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Anchorpoint
        fields = ('id', 'name', 'image', 'business_hours', 'coordinates', 'category', 'phone', 'address')

    def get_coordinates(self, obj):
        try:
            #FOR DICT
            return {'lat': obj['lat'], 'lng': obj['lng']}
        except TypeError:
            #FOR INSTANCE OF ANCHORPOINT
            return {'lat': obj.lat, 'lng': obj.lng}
        