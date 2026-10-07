import requests
def test_user2(url,api_session):
    response = requests.get(f"{url}/2")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 2
    assert "name" in data