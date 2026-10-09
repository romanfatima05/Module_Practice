

import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_session(base_url):
    session = requests.Session()

    session.headers.update({
        "Accept": "application/json"
    })

    yield session

    session.close()

   
#@pytest.fixture(autouse=True)
#def setup(scope="session"):
    #print("Automatic fixture running")
  #  yield 
#    print("teardown")