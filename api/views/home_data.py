from rest_framework import generics
from api.serializers import HomeSerializer
from home.models import Home
from cities.models import City
from core.models import Anchorpoint
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.anchorpoint import AnchorpointSerializer

class HomeData(APIView):

    def get(self, request):
        query_cities = City.objects.filter(visible=True)
        
        routes = []
            
        # Buscar todos os anchorpoints das cidades visíveis de uma vez
        anchorpoints = Anchorpoint.objects.filter(city__in=query_cities)
            
        for city in query_cities:
            city_routes = city.route.all()
                
            for route in city_routes:
                route_data = {
                    'id': route.id,
                    'name': route.name,
                    'color': route.color,
                    'external_strava_id': route.external_strava_id,
                    'polyline': route.polyline,
                }
                if route_data not in routes:
                    routes.append(route_data)
            
            
        data = {
            'points': AnchorpointSerializer(anchorpoints, many=True).data,
            'routes': routes
        }

        return Response(data)