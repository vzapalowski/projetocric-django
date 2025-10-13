from rest_framework import serializers

from core.models import AnchorpointCategory

class AnchorpointCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  AnchorpointCategory
        fields = ('name', 'image')
