class StravaAPIException(Exception):
    """Exception base for Strava Api error"""
    pass

class StravaAuthenticationError(StravaAPIException):
    """Authentication errors in Strava Api"""
    pass

class StravaRouteNotFoundError(StravaAPIException):
    """Not found route error in Strava Api"""
    
    def __init__(self, route_id: str):
        self.route_id = route_id
        super().__init__(f"Rota {route_id} não encontrada na API do Strava")
        
class StravaPolylineNotFoundError(StravaAPIException):
    """Not found polyline error in Strava Api"""
    
    def __init__(self, route_id: str):
        self.route_id = route_id
        super().__init__(f"Polyline não encontrada na rota {route_id} da API do Strava")

class StravaAPIConnectionError(StravaAPIException):
    """Connection error in Strava Api"""
    pass