from tests.helpers.schema_validators import validate_user_schema

def test_get_users_with_id_params(users_client):
    params = {
        "id" : 1
    }

    response = users_client.get_users_with_params(params)
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

    validate_user_schema(data[0])
    assert data[0]["id"] == 1

def test_get_users_with_non_existing_id(users_client):
    params = {
        "id" : 9999
    }

    response = users_client.get_users_with_params(params)
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert data == []