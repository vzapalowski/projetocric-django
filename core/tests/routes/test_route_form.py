import pytest
from core.forms.route import RouteForm
from integrations.strava.exceptions import StravaRouteNotFoundError

pytestmark = pytest.mark.django_db

@pytest.fixture
def mock_client(monkeypatch):

    class MockClient:
        def get_route_details(self, route_id):
            return {
                "polyline": "abc123",
                "distance": 15000
            }

    monkeypatch.setattr(
        "core.forms.route.StravaClient",
        MockClient
    )


def test_route_form_valid(mock_client):
    form = RouteForm(data={
        "external_strava_id": "3024727868187306952",
        "name": "Rota Teste",
        "color": "#FF0000",
        "active": True,
        "is_event_route": False,
    })

    assert form.is_valid()
    assert form.cleaned_data["polyline"] == "abc123"
    assert form.cleaned_data["distance"] == 15000


def test_route_form_not_found(monkeypatch):
    class MockClientFail:
        def get_route_details(self, route_id):
            raise StravaRouteNotFoundError("Rota não existe")

    monkeypatch.setattr(
        "core.forms.route.StravaClient",
        MockClientFail
    )

    form = RouteForm(data={
        "external_strava_id": "123456",
        "name": "Rota Teste",
        "color": "#FF0000",
        "active": True,
        "is_event_route": False,
    })

    assert not form.is_valid()
    assert "Rota não existe" in str(form.errors)
