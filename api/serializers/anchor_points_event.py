from rest_framework import serializers

from core.models.anchorpoint import Anchorpoint

class AnchorPointEventSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    class Meta:
        model = Anchorpoint
        fields = ('title', 'iconUrl', 'coordinates')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}
