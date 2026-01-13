from tests.helpers.schema_validators import validate_user_schema

def test_create_user(users_client):
    payload={
        "name" : "Test User",
        "email" : "test.user@example.com"
    }

    response = users_client.create_user(payload)

    assert response.status_code in (200, 201)

    data = response.json()
    validate_user_schema(data)

    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]