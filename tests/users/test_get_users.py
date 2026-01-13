from tests.helpers.schema_validators import validate_users_list_schema

def test_get_users(users_client):
    # Verify that users endpoint returns non-empty list
    response = users_client.get_users()
    assert response.status_code == 200

    data = response.json()
    validate_users_list_schema(data)

