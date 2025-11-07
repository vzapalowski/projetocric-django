from django import forms
from ..models import Route
from integrations.strava.client import StravaClient
from integrations.strava.exceptions import StravaRouteNotFoundError

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()
        # Getting field from form
        route_id = cleaned.get("external_strava_id")

        if not route_id:
            return cleaned

        client = StravaClient()

        try:
            data = client.get_route_details(route_id)
        except StravaRouteNotFoundError as e:
            raise forms.ValidationError(f"{e}")
        except Exception as e:
            raise forms.ValidationError(f"Erro inesperado: {e}")

        polyline = data.get("polyline")
        if not polyline:
            raise forms.ValidationError("A rota existe no Strava, mas não foi possível encontrar polyline")

        # atribui no cleaned_data
        cleaned["polyline"] = polyline
        cleaned["distance"] = data.get("distance")

        # guarda para usar no save_model
        self._strava_details = data

        return cleaned
