def validate_user(user):

    assert "id" in user
    assert "name" in user

    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)