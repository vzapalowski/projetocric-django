from rest_framework import serializers

from event.models.anchor_point import AnchorPoint

class AnchorPointEventSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    class Meta:
        model = AnchorPoint
        fields = ('title', 'iconUrl', 'coordinates')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}
