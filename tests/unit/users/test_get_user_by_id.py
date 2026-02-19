from tests.unit.helpers.schema_validators import validate_user_schema


def test_get_user_by_id(users_client):
    user_id = 1

    response = users_client.get_user(user_id)

    assert response.status_code == 200

    data = response.json()
    validate_user_schema(data)
    