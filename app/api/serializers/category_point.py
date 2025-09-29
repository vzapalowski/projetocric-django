from rest_framework import serializers

from cities.models import Category

class CategoryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = ('name', 'image')
