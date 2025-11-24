from cities.models import City
from core.models import Anchorpoint
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.anchorpoint import AnchorpointSerializer
from api.permissions import HasApiAuthToken

class HomeData(APIView):
    permission_classes = [HasApiAuthToken]
    
    def get(self, request):
        cities_list = City.objects.filter(visible=True)
        routes = []
        anchorpoints = Anchorpoint.objects.filter(is_event_anchorpoint=False)
            
        for city in cities_list:
            city_routes = city.route.filter(is_event_route=False)
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
            'latitude': -29.9949289,
            'longitude': -51.8243548,
            'zoom': 10,
            'points': AnchorpointSerializer(anchorpoints, many=True).data,
            'routes': routes
        }
        return Response(data)