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

        cleaned["polyline"] = polyline
        cleaned["distance"] = data.get("distance")

        self._strava_details = data

        return cleaned
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if hasattr(self, "_strava_details"):
            instance.polyline = self._strava_details.get("polyline")
            instance.distance = str(self._strava_details.get("distance"))

        if commit:
            instance.save()

        return instance
