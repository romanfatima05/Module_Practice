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

#check ther is diuplication of email give invalid or fail
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



   

