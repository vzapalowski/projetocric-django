import pytest
from cities.models import City
from core.models import Route

@pytest.mark.django_db
def test_city_detail(api_client, auth_headers):
    city = City.objects.create(
        name="Teste",
        visible=True,
        banner_image="img.jpg"
    )

    route = Route.objects.create(
        name="Rota 1",
        external_strava_id="123456",
        color="#FF0000"
    )

    city.route.add(route)

    response = api_client.get(f"/api/cities/{city.id}/", **auth_headers)

    assert response.status_code == 200
    assert response.data["name"] == "Teste"
    assert len(response.data["routes"]) == 1
    assert response.data["routes"][0]["name"] == "Rota 1"
