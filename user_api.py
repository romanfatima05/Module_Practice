def get_user(api_client, user_id):
    return api_client.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )


def create_user(api_client, payload):
    return api_client.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )

def update_user(api_client,user_id,payload):
    return api_client .put(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=payload
    )
def delete_user(api_client, user_id):
    return api_client.delete(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
def update_user2(api_client,user_id,payload):
    return api_client .patch(
        f"https://jsonplaceholder.typicode.com/users/1",
        json=payload
    )