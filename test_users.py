import requests
def test_user_id():
    assert 1 == 1

def test_user_name():
    assert "Roman" == "Roman"
def test_user_api(api_session, base_url):
    response = api_session.get(f"{base_url}/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
def test_second_user(api_session, base_url):
    response = api_session.get(f"{base_url}/users/2")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 2
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
def test_user_not_found(api_session, base_url):
    response = api_session.get(f"{base_url}/users/999")

    assert response.status_code == 404
    print(response.text)
    data = response.json()
    assert data == {}