def test_get_user_by_id(users_client):
    user_id = 1

    response = users_client.get_user(user_id)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data
