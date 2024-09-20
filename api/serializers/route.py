from rest_framework import serializers

from cities.models import Route, Segment

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ['id', 'name', 'visible', 'city', 'state', 'country', 'distance', 'total_elevation_gain', 'average_grade', 'elevation_low', 'elevation_high', 'effort_count', 'athlete_count', 'polyline']

class RouteSerializer(serializers.ModelSerializer):
    segments = SegmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Route
        fields = ('id', 'name', 'color', 'id_route', 'polyline', 'segments')