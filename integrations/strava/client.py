from datetime import datetime
import requests

from .config import StravaConfig
from .exceptions import (
    StravaAuthenticationError,
    StravaRouteNotFoundError,
    StravaAPIConnectionError
)

class StravaClient:
    def __init__(self, config=None):
        # self.config = config or StravaConfig.from_settings()
        # This is for tests, i'am gonna change this after development
        self.config = config or StravaConfig.from_test()
        self._access_token = None
        self._expires_at = None

    def _token_valid(self):
        return self._access_token and self._expires_at and datetime.now() < self._expires_at

    def _get_access_token(self):
        if self._token_valid():
            return self._access_token

        try:
            resp = requests.post(self.config.auth_url, data={
                'client_id': self.config.client_id,
                'client_secret': self.config.client_secret,
                'refresh_token': self.config.refresh_token,
                'grant_type': 'refresh_token'
            })
            resp.raise_for_status()
            data = resp.json()

            self._access_token = data.get('access_token')
            exp = data.get('expires_at')

            if not self._access_token:
                raise StravaAuthenticationError("Token inválido")

            self._expires_at = datetime.fromtimestamp(exp)
            return self._access_token
        except Exception as e:
            raise StravaAuthenticationError("Não foi possível renovar o token.")

    def _request(self, endpoint, params=None):
        try:
            resp = requests.get(
                self.config.api_base_url + endpoint,
                headers={'Authorization': f'Bearer {self._get_access_token()}'},
                params=params
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise StravaAPIConnectionError("Erro ao conectar com a Api do Strava")

    def get_route(self, route_id):
        try:
            data = self._request(f"/routes/{route_id}")
            return data
        except Exception:
            raise StravaRouteNotFoundError(f"Rota {route_id} não encontrada")

    def get_route_polyline(self, route_id):
        data = self.get_route(route_id)
        polyline = data.get('map', {}).get('summary_polyline')
        if not polyline:
            raise StravaRouteNotFoundError("Polyline não disponível")
        return polyline

    def get_route_distance(self, route_id):
        data = self.get_route(route_id)
        dist = data.get('distance')
        if dist is not None:
            return float(dist)
        return None