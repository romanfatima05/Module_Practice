def login(api_client, username, password):

    payload = {
        "username": username,
        "password": password
    }

    return api_client.post(
        "https://httpbin.org/post",
        json=payload
    )