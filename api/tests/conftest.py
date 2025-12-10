import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_headers(api_client):
    session = api_client.session
    session["auth_token"] = "test_auth_token"
    session.save()
    return {"HTTP_X_AUTH_TOKEN": "test_auth_token"}
