from tests.helpers.schema_validators import validate_user_schema

def test_create_user_success(users_client):
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

def test_create_user_missing_email(users_client):
    payload = {
        "name" : "Test User"
    }

    response = users_client.create_user(payload)
    assert response.status_code in (200, 201)

    data = response.json()

    # response does not fulfill full user contract
    assert "email" not in data

def test_create_user_with_empty_payload(users_client):
    response = users_client.create_user({})
    assert response.status_code in (200, 201)

    data = response.json()

    assert "name" not in data
    assert "email" not in data