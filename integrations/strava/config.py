from django.conf import settings

class StravaConfig:
    def __init__(self, client_id, client_secret, refresh_token, auth_url='https://www.strava.com/oauth/token', api_base_url='https://www.strava.com/api/v3'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.auth_url = auth_url
        self.api_base_url = api_base_url

    @classmethod
    def from_settings(cls):
        return cls(
            getattr(settings, 'STRAVA_CLIENT_ID', ''),
            getattr(settings, 'STRAVA_CLIENT_SECRET', ''),
            getattr(settings, 'STRAVA_REFRESH_TOKEN', '')
        )