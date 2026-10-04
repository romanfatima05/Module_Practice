import pytest
import requests


@pytest.fixture()
def api_client():
    

    client = requests.Session()

    yield client

    
    client.close()

