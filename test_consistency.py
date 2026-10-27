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

#.................................................................................................

def test_unique_email_users(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    users=response.json()
    for i in range(len(users)):
         for j in range(i+1,len(users)):
            
            assert users[i]["email"] != users[j]["email"]

#....................................................................................................

#check there is duplication of email give invalid or fail
def test_duplicate_email_detection():
    emails = ["ali@example.com", "sara@example.com", "ali@example.com"]

    for i in range(len(emails)):
        for j in range(i + 1, len(emails)):
            assert emails[i] != emails[j]
#...............................................................................................

def test_user_count_consistency(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    user_count = len(users)
    successful_count = 0

    for user in users:
        user_id=user["id"]
        detail_response=api_session.get(f"{base_url}/users/{user_id}")
        
        assert detail_response.status_code==200
        successful_count+=1
    
    assert successful_count==user_count

#...................................................................................

def test_id_consistency(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200
    users=response.json()
    for i in range(len(users)):
        for j in range(i+1,len(users)):
            assert users[i]["id"]!=users[j]["id"]

        
#.....................................................................................
def test_users_response_time(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    assert response.status_code==200


    assert response.elapsed.total_seconds()<2
#...........................................................................................

def test_patch_user_name(api_session, base_url):
    user_id = 1

    updated_data = {
        "name": "Roman Updated"
    }

    response = api_session.patch(
        f"{base_url}/users/{user_id}",
        json=updated_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["name"] == updated_data["name"]

#....................................................

def test_patch_invalid_user_id(api_session, base_url):
    response = api_session.patch(
        f"{base_url}/users/9999",
        json={"name": "Roman Updated","id":"9999"}
    )

    assert response.status_code == 200
    data=response.json()
    assert "id" in data
    assert str(data["id"]) == "9999"
    assert data["name"] == "Roman Updated"
    print(data)

#...............................................................

def test_invalid_user_update(api_session,base_url):
    user_id=1
    original_response=api_session.get(f"{base_url}/users/{user_id}")
    assert original_response.status_code == 200

    original_data = original_response.json()
    original_email = original_data["email"]
    response=api_session.patch(f"{base_url}/users/{user_id}",
    json={"name":"Roman update"}
    )
    assert response.status_code==200
    data=response.json()
    assert data["name"]=="Roman update"
    assert data["email"]==original_email

#......................................................................
def test_email_user_type(api_session,base_url) :
    response=api_session.get(f"{base_url}/users/1") 
    assert response.status_code==200
    data=response.json()
    assert isinstance(data["email"],str)

#.................................................................API response-time thresholds

import time
def test_response_user_time(api_session,base_url):
    start=time.perf_counter()
    response=api_session.get(f"{base_url}/users")
    elapsed=time.perf_counter() - start
    assert response.status_code==200
    assert elapsed<2.0, f"API took {elapsed:.2f} seconds"


