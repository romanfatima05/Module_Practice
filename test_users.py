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
import pytest
@pytest.mark.parametrize("user_id",[2,5,7])
def test_multiple_users(api_session,base_url,user_id):
    response=api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code==200
    data=response.json()
    assert data["id"]==user_id

@pytest.mark.parametrize("user_id",[42,65,74])
def test_notfound_users(api_session,base_url,user_id):
    response=api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code==404
    data=response.json()
    #assert data["id"]==user_id


@pytest.mark.parametrize(
    "user_id,expected_status",
    [
    (1,200),
    (2,200),
    (999,404)
]
)
def test_multi_users(api_session,base_url,user_id,expected_status):
    response=api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code== expected_status
    data = response.json()

    if expected_status == 200:
        assert data["id"] == user_id
    else:
        assert data == {}

