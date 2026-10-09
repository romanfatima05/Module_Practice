def test_post(api_session, base_url):
    response = api_session.get(f"{base_url}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)