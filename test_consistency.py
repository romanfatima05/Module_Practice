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


#........................................................two API responses contain the same data.

def test_user_data_matches(api_session, base_url):
    all_response = api_session.get(f"{base_url}/users")
    single_response = api_session.get(f"{base_url}/users/1")

    all_users = all_response.json()
    single_user = single_response.json()

    user_from_list = all_users[0]

    assert user_from_list["name"] == single_user["name"]
#........................................verify id
def test_user_id_match(api_session,base_url):
    all_response=api_session.get(f"{base_url}/users")
    single_response=api_session.get(f"{base_url}/users/1")
    all_user=all_response.json()
    single_user=single_response.json()
    user_from_list=all_user[0]
    assert user_from_list["id"]==single_user["id"]
    assert single_user["id"]==1
#........................................email verify
def test_user_email_match(api_session,base_url):
    all_response=api_session.get(f"{base_url}/users")
    single_response=api_session.get(f"{base_url}/users/1")
    all_user=all_response.json()
    single_user=single_response.json()
    user_from_list=all_user[0]
    assert user_from_list["email"]==single_user["email"]
    assert single_user["id"]==1

#.............................................:test_invalid_structure
def test_invalid_structure(api_session,base_url):
    response=api_session.get(f"{base_url}/users")
    users=response.json()
    assert isinstance(users,list)
    assert len(users)>0

#..............................................nested json date validation

def test_user_address_structure(api_session, base_url):
    response = api_session.get(f"{base_url}/users/1")
    user = response.json()

    assert "address" in user
    assert isinstance(user["address"], dict)
    assert "city" in user["address"]
    assert isinstance(user["address"]["city"], str)
#..................................................
from jsonschema import validate
def test_validate_schema(api_session,base_url):
    response=api_session.get(f"{base_url}/users/1")
    users=response.json()
    schema={
        "type":"object",
        "properties":{
            "name":{
                "type":"string"
            },
            "address":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string"
                    }
                },
                    "required":["city"]
            }
        },
            "required":["name","address"]
        
    }
    validate(instance=users,schema=schema)

#.....................................................validation error
import pytest
from jsonschema import validate, ValidationError
def test_invalid_nested_schema():
    users = {
        "name":345,
        "address": {
            "city": "123"
        }
    }
    schema={
            "type":"object",
            "properties":{
                "name":{
                    "type":"string"
                },
                "address":{
                    "type":"object",
                    "properties":{
                        "city":{
                            "type":"string"
                        }
                    },
                        "required":["city"]
                }
            },
                "required":["name","address"]
            
        }
    with pytest.raises(ValidationError):
        validate(instance=users,schema=schema)

#.................................................addition properties

import pytest
from jsonschema import validate, ValidationError
def test_invalid_additional_schema():
    users = {
        "name":"Ali",
        "address": {
            "city": "123",
            "country": "Pakistan"
        }
    }
    schema={
            "type":"object",
            "properties":{
                "name":{
                    "type":"string"
                },
                "address":{
                    "type":"object",
                    "properties":{
                        "city":{
                            "type":"string",
                        
                    }     
                        
                    },
                        "additionalProperties": False,
                        "required":["city"]
                }
            },
                "required":["name","address"]
            
        }
    with pytest.raises(ValidationError):
        validate(instance=users,schema=schema)



#...........................................
import pytest
from jsonschema import validate, ValidationError
def test_invalid_missing_schema():
    users = {
        "name":"Ali",
        "address": {
            #"city": "123",
            "country": "Pakistan"
        }
    }
    schema={
            "type":"object",
            "properties":{
                "name":{
                    "type":"string"
                },
                "address":{
                    "type":"object",
                    "properties":{
                        "country":{
                            "type":"string",
                        
                    }     
                        
                    },
                        "additionalProperties": False,
                        "required":["city"]
                }
            },
                "required":["name","address"]
            
        }
    with pytest.raises(ValidationError):
        validate(instance=users,schema=schema)
#....................................................wrong data type
from jsonschema import validate,ValidationError
def test_wrong_data():
    users={
        "name":123,
        "address":{
            "city":123
        }

    }
    schema={
        "type":"object",
        "properties":{
            "name":{
                "type":"string"
            },
            "address":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string"
                    }
                },
                "required":["city"]
                }
        },
        "required":["name","address"]
    }
    with pytest.raises(ValidationError):
        validate(instance=users,schema=schema)

#...................................................................draft7validator
from jsonschema import Draft7Validator
def test_all_errors():
    users={
        "name":1234,
        "address":{
          "city":1234
        }
    }
    schema={
        "type":"object",
        "properties":{
            "name":{
                "type":"string"
            },
            "address":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string"
                    }
                },
                "required":["city"]
            }
        },
        "required":["name","address"]

    }
    validator=Draft7Validator(schema)
    errors=list(validator.iter_errors(users))
    #assert len(errors)==2
    for error in errors:
        print("\n--- Validation Error ---")
        print("Field:", list(error.path))
        print(error.message)
        print("Failed rule:", error.validator)
        print("Expected:", error.validator_value)
    assert len(errors)==2

#.................................................................
from jsonschema import Draft7Validator

def test_collct_error():

    users = {
        "address": {
            "city": "Bahawalpur",
            "country": "Pakistan"
        },
        "age": 22
    }

    schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "address": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string"
                    }
                },
                "required": ["city"],
                "additionalProperties": False
            }
        },
        "required": ["name", "address"],
        "additionalProperties": False
    }

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(users))

    for error in errors:
        print("\n--- Validation Error ---")
        print("Field:", list(error.path))
        print("Message:", error.message)
        print("Failed rule:", error.validator)
        print("Expected:", error.validator_value)

    assert len(errors) == 3

#...........................................validate multiple user records together
def test_multiple_records():
    users=[
        {"id":1,"name":"Ali","email":"sara@gmail.com"},
        {"id":"2","name":123,"email":"sar@gmail.com"},
        {"id":3,"name":"Al","email":"saa@gmail.com"}
    ]
    schema={
        "type":"array",
        "items": {
        "type": "object",
        "properties":{
            "id":{"type":"integer"},
            "name":{
                "type":"string"
            },
             "email":{
                 "type":"string"
            }
        },
        "required":["id","name","email"]
        }
    }
    validator=Draft7Validator(schema)
    errors=list(validator.iter_errors(users))
    for error in errors:
       
        print("field",list(error.path))
        print("failed",error.message)
        assert len(errors)==2
#...........................................email validator(format)

def test_multiple1_records():
    users=[
        {"id":1,"name":"Ali","email":"sara@gmail.com"},
        {"id":"2","name":123,"email":"sar@gmail.com"},
        {"id":3,"name":"Al","email":"sa"}
    ]
    schema={
        "type":"array",
        "items": {
        "type": "object",
        "properties":{
            "id":{"type":"integer"},
            "name":{
                "type":"string"
            },
             "email":{
                 "type":"string",
                 "format":"email"
            }
        },
        "required":["id","name","email"]
        }
    }
    validator=Draft7Validator(schema,format_checker=Draft7Validator.FORMAT_CHECKER)
    errors=list(validator.iter_errors(users))
    for error in errors:
       
        print("field",list(error.path))
        print("failed",error.message)
        assert len(errors)==3
#.................................missing email
def test_multiple2_records():
    users=[
        {"id":1,"name":"Ali","email":"sara@gmail.com"},
        {"id":"2","name":123,"email":"sar@gmail.com"},
        {"id":3,"name":"Al"}
    ]
    schema={
        "type":"array",
        "items": {
        "type": "object",
        "properties":{
            "id":{"type":"integer"},
            "name":{
                "type":"string"
            },
             "email":{
                 "type":"string",
                 "format":"email"
            }
        },
        "required":["id","name","email"]
        }
    }
    validator=Draft7Validator(schema,format_checker=Draft7Validator.FORMAT_CHECKER)
    errors=list(validator.iter_errors(users))
    for error in errors:
       
        print("field",list(error.path))
        print("failed",error.message)
        assert len(errors)==3

#.......................................aditional
def test_multiple3_records():
    users=[
        {"id":1,"name":"Ali","email":"sara@gmail.com","age":21},
        {"id":"2","name":123,"email":"sar@gmail.com"},
        {"id":3,"name":"Al"}
    ]
    schema={
        "type":"array",
        "items": {
        "type": "object",
        "properties":{
            "id":{"type":"integer"},
            "name":{
                "type":"string"
            },
             "email":{
                 "type":"string",
                 "format":"email"
            }
        },
        "required":["id","name","email"],
        "additionalProperties":False
        }
    }
    validator=Draft7Validator(schema,format_checker=Draft7Validator.FORMAT_CHECKER)
    errors=list(validator.iter_errors(users))
    for error in errors:
       
        print("field",list(error.path))
        print("failed",error.message)
        assert len(errors)==4
#......................................nested
from jsonschema import Draft7Validator

def test_nested_user():

    user = {
        "id": 1,
        "name": "Roman",
        "address": {
            "city": 123,
           
        }
    }

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "address": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "zipcode": {"type": "string"}
                },
                "required": ["city", "zipcode"]
            }
        },
        "required": ["id", "name", "address"]
    }

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(user))

    for error in errors:
        print("Field:", list(error.path))
        print("Error:", error.message)

    assert len(errors) == 2
#.........................................
def test_nested_multiple_users():

    users = [
        {
            "id": 1,
            "name": "Ali",
            "address": {
                "city": "Bahawalpur",
                "zipcode": "63100"
            }
        },
        {
            "id": 2,
            "name": 123,
            "address": {
                "city": 456,
                "zipcode": "63000"
            }
        }
    ]

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "address": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "zipcode": {"type": "string"}
                    },
                    "required": ["city", "zipcode"],
                    "additionalProperties": False
                }
            },
            "required": ["id", "name", "address"],
            "additionalProperties": False
        }
    }

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(users))

    for error in errors:
        print("Field:", list(error.path))
        print("Error:", error.message)

    assert len(errors) == 2

#.....................................deep nested json object
def test_deep_nested():
    users={
        "name":"Ali",
        "age":"123",
        "address":{
            "city":"bwp",
            "zipcode":"12345",
            "geo":{
                "lat":12356,
                "lng":"12800"
            }
                
        }
    }
    schema={
        "type":"object",
        "properties":{
            "name":{
                "type":"string"
            },
            "age":{
                "type":"integer"
            },
            "address":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string"
                    },
                    "zipcode":{
                        "type":"string"
                    },
                    "geo":{
                        "type":"object",
                        "properties":{
                            "lat":{
                                "type":"string"

                            },
                            "lng":{
                                 "type":"string"
                            }
                        },
                        "required":["lng","lat"]
                    }
                },
                "required":["city","zipcode","geo"],
                "additionalProperties":False
              
            }
        },
        "required":["name","age","address"],
        "additionalProperties":False

    }
    validator=Draft7Validator(schema)
    errors=list(validator.iter_errors(users))
    for error in errors:
        print("failed",error.message)
        print("field",list(error.path))
        print("validate",error.validator)
        print("value",error.validator_value)
        assert len(errors)==2

#.........................................min,max items
def test_min_max_items():

    users = ["Ali","sara","ahmad","sara","ahmad"]

    schema = {
        "type": "array",
        "items": {"type": "string"},
        "minItems": 2,
        "maxItems": 4
    }

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(users))

    for error in errors:
        print("Error:", error.message)
        print("Rule:", error.validator)

    assert len(errors) == 1

#...........................unique item
def test_unique_items():

    users = ["Ali","sara","ahmad"]

    schema = {
        "type": "array",
        "items": {"type": "string"},
        "minItems": 2,
        "maxItems": 4,
    
        "uniqueItems":True
    }
    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(users))

    for error in errors:
        print("Error:", error.message)
        print("Rule:", error.validator)

    assert len(errors) == 0