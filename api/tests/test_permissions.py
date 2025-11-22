from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_no_token_returns_403(api_client):
    response = api_client.get("/api/cities/")
    assert response.status_code == 403
    assert "credenciais" in response.data["detail"]

@pytest.mark.django_db
def test_invalid_token_returns_403(api_client):
    session = api_client.session
    session["auth_token"] = "abc12345"
    session.save()

    response = api_client.get("/api/cities/", HTTP_X_AUTH_TOKEN="12345")
    
    assert response.status_code == 403

@pytest.mark.django_db
def test_valid_token_allows_access(api_client, auth_headers):
    response = api_client.get("/api/cities/", **auth_headers)
    assert response.status_code in [200, 204]
