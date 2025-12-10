import pytest
from integrations.strava.client import StravaClient
from integrations.strava.exceptions import StravaRouteNotFoundError

class MockResponse:
    def __init__(self, ok=True, status_code=200, json_data=None):
        self.ok = ok
        self.status_code = status_code
        self._json = json_data or {}

    def raise_for_status(self):
        if not self.ok:
            raise Exception("HTTP Error")

    def json(self):
        return self._json


def test_get_route_details_success(monkeypatch):
    def mock_post(url, data):
        return MockResponse(json_data={
            "access_token": "fake-token",
            "expires_at": 9999999999
        })

    def mock_get(url, headers=None, params=None):
        return MockResponse(json_data={
            "map": {"summary_polyline": "abcd123"},
            "distance": 10000
        })

    monkeypatch.setattr("integrations.strava.client.requests.post", mock_post)
    monkeypatch.setattr("integrations.strava.client.requests.get", mock_get)


    client = StravaClient()
    data = client.get_route_details("1234")
    
    assert data["polyline"] == "abcd123"
    assert data["distance"] == 10.0


def test_get_route_details_not_found(monkeypatch):
    def mock_post(url, data):
        return MockResponse(json_data={
            "access_token": "fake-token",
            "expires_at": 9999999999
        })

    def mock_get(url, headers, params=None):
        return MockResponse(ok=False, status_code=404)

    monkeypatch.setattr("integrations.strava.client.requests.post", mock_post)
    monkeypatch.setattr("integrations.strava.client.requests.get", mock_get)

    client = StravaClient()

    with pytest.raises(StravaRouteNotFoundError):
        client.get_route_details("#############")
