def test_user_name(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    for user in users:
        user_id=user["id"]
        list_name = user["name"]
        detail_response = api_session.get(
            f"{base_url}/users/{user_id}"
        )
        assert detail_response.status_code == 200

        detail_data = detail_response.json()

        assert detail_data["id"] == user_id
        assert detail_data["name"] == list_name
#..........................................................................
def test_user_id(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    for user in users:
        user_id=user["id"]
        detail_response=api_session.get(f"{base_url}/users/{user_id}")
        assert detail_response.status_code==200
        detail_data=detail_response.json()
        assert detail_data["id"]==user_id

#..............................................................................................
def test_user_email(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    for user in users:
        user_id=user["id"]
        user_email=user["email"]
        detail_response=api_session.get(f"{base_url}/users/{user_id}")
        detail_data=detail_response.json()
        assert detail_data["id"] == user_id
        assert detail_data["email"]==user_email
#........................................................................................

import pytest
@pytest.mark.parametrize(
    "field",
    ["id","email","name"]
)
def test_multiple_users(api_session,base_url,field):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    for user in users:
        user_id = user["id"]
        detail_response=api_session.get(f"{base_url}/users/{user_id}")
        assert detail_response.status_code==200
        
        detail_data=detail_response.json()
        assert detail_data[field]==user[field]


