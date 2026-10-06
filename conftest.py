import pytest
import requests


@pytest.fixture()
def api():
    return "https://jsonplaceholder.typicode.com"
@pytest.fixture()
def url(api):
    return f"{api}/users"
@pytest.fixture()
def api_session(url):
    session = requests.Session()
    session.headers.update({
        "accept":"application/json"
    })


    yield session

   
