import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_url(base_url):
    return f"{base_url}/users"


def test_user(api_url):
    response = requests.get(f"{api_url}/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data