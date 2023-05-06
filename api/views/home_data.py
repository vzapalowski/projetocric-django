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
                    route_data = {
                        'id': route.id,
                        'name': route.name,
                        'id_route': route.id_route,
                        'polyline': route.polyline,
                    }
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
