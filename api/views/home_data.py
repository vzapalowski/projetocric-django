from rest_framework import generics
from api.serializers import HomeSerializer
from home.models import Home
from cities.models import City


class HomeData(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        homes = super().get_queryset()
        query_cities = City.objects.filter(visible=True)
        for home in homes:
            routes = []
            points = []
            for city in query_cities:
                city_routes = city.routes.all()
                city_points = city.points.all()
                for route in city_routes:
                    visible_segments = route.segments.filter(visible=True)
                    route_data = {
                        'id': route.id,
                        'name': route.name,
                        'color': route.color,
                        'id_route': route.id_route,
                        'polyline': route.polyline,
                        'segments': [
                            {
                                'id': segment.id, 
                                'name': segment.name, 
                                'visible': segment.visible,
                                'city': segment.city,
                                'state': segment.state,
                                'country': segment.country,
                                'distance': segment.distance,
                                'total_elevation_gain': segment.total_elevation_gain,
                                'average_grade': segment.average_grade,
                                'elevation_low': segment.elevation_low,
                                'elevation_high': segment.elevation_high,
                                'effort_count': segment.effort_count,
                                'athlete_count': segment.athlete_count,
                                'polyline': segment.polyline
                            } for segment in visible_segments]
                    }
                    if route_data not in routes:
                        routes.append(route_data)
                        
                for point in city_points:
                    point_data = {
                    'id': point.id,
                    'name': point.name,
                    'image': point.image,
                    'business_hours': point.business_hours,
                    'lat': point.lat,
                    'lng': point.lng,
                    'category': point.category,
                    'phone': point.phone,
                    'address': point.address
                    }
                    points.append(point_data)
            home.routes = routes
            home.points = points
        return homes
