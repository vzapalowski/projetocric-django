from cities.models.api_strava import Api

class StravaService:
    @staticmethod
    def fetch_and_set_polyline(route):
        api = Api()
        try:
            if not route.external_strava_id:
                raise Exception("ID do Strava não foi informado")
            
            polyline = api.get_route(route.external_strava_id)    
            route.polyline = polyline
            
            return route
        except KeyError as e:
            route.polyline = None
            raise Exception(f"Rota {route.external_strava_id} não encontrada na API do Strava")