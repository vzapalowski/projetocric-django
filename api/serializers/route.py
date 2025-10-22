from rest_framework import serializers

from core.models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'id', 
            'name', 
            'polyline',
            'distance',
            'color', 
            'external_strava_id', 
        )