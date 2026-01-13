def test_get_user_not_found(users_client):
    user_id = 9999

    response = users_client.get_user(user_id)

    assert response.status_code == 404

    data = response.json()
    assert data == {}