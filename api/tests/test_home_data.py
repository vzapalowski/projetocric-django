import pytest
from cities.models import City
from core.models import Route, Anchorpoint, AnchorpointCategory

@pytest.mark.django_db
def test_home_data(api_client, auth_headers):
    category = AnchorpointCategory.objects.create(
        name="Teste",
        icon_name="teste"
    )

    city = City.objects.create(
        name="CityTeste",
        visible=True,
        banner_image="img.jpg"
    )

    route = Route.objects.create(
        external_strava_id="abc1234",
        name="Rota Teste",
        color="#00FF00",
        polyline="abc123",
        distance="100"
    )

    city.route.add(route)

    Anchorpoint.objects.create(
        name="Ponto 1",
        city=city,
        latitude=-29.1,
        longitude=-51.2,
        anchorpoint_category=category,
        image="img.jpg"
    )

    response = api_client.get("/api/home_cities/", **auth_headers)

    assert response.status_code == 200
    assert "routes" in response.data
    assert "points" in response.data

    assert len(response.data["routes"]) == 1
    assert len(response.data["points"]) == 1
