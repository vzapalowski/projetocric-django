import pytest
from core.forms.route import RouteForm
from integrations.strava.client import StravaClient
from core.models import Route

@pytest.mark.django_db
def test_route_creation(monkeypatch):
    class MockClient:
        def get_route_details(self, route_id):
            return {
                "polyline": "poly123",
                "distance": 12345
            }

    monkeypatch.setattr("core.forms.route.StravaClient", MockClient)

    form = RouteForm(data={
        "external_strava_id": "3024727868187306952",
        "name": "Rota Teste",
        "color": "#FF0000",
        "active": True,
        "is_event_route": False,
    })

    assert form.is_valid()
    route = form.save()
    
    assert route.polyline == "poly123"
    assert route.distance == "12345"
    assert Route.objects.count() == 1
