from tests.unit.helpers.schema_validators import validate_users_list_schema

def test_get_users(users_client):
    # Verify that users endpoint returns non-empty list
    users = users_client.get_users()
    assert isinstance(users, list)
    assert len(users) > 0

    validate_users_list_schema(users)

