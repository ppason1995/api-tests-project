def validate_user_schema(user: dict):
    """
    Validate schema of single user object.
    """

    required_keys = {"id", "name", "email"}

    #required keys exist
    assert set(user.keys()) >= required_keys

    #type validation
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)

def validate_users_list_schema(users: list):
    assert isinstance(users, list)
    assert len(users) > 0

    for user in users:
        validate_user_schema(user)