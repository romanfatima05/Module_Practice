import requests
def test_user(url,api_session):
    response = requests.get(f"{url}/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data