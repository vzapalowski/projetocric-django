import pytest
from event.models import Event

@pytest.mark.django_db
def test_event_list(api_client, auth_headers):
    Event.objects.create(
        name="Evento Teste",
        description="Desc",
        date="2025-01-01",
        banner_image="a.jpg"
    )

    response = api_client.get("/api/event_list/", **auth_headers)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Evento Teste"
