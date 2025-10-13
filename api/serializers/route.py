from rest_framework import serializers

from core.models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name', 'color', 'id_route', 'polyline')