import pytest
from cities.models import City

@pytest.mark.django_db
def test_city_list_returns_only_visible(api_client, auth_headers):
    City.objects.create(name="City Visible", visible=True, banner_image="x.jpg")
    City.objects.create(name="City Visible 2", visible=True, banner_image="x.jpg")
    City.objects.create(name="City Hidden", visible=False, banner_image="x.jpg")

    response = api_client.get("/api/cities/", **auth_headers)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == "City Visible"
