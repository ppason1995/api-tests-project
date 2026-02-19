from tests.unit.helpers.schema_validators import validate_user_schema

def test_update_user_success(users_client):
    user_id = 1
    payload = {
        "name" : "Updated User name"
    }

    response = users_client.update_user(user_id, payload)
    assert response.status_code == 200

    data = response.json()

    # API returns merged object
    assert data["name"] == payload["name"]

def test_update_user_not_found(users_client):
    user_id = 9999
    payload = {
        "name" : "Ghost User"
    }

    response = users_client.update_user(user_id, payload)
    
    # jsonplaceholder still returns 200
    assert response.status_code == 200

    data = response.json()

    # response does not contain valid user id
    assert data.get("id") != user_id
