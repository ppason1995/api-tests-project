def test_delete_user_success(users_client):
    user_id = 1

    response = users_client.delete_user(user_id)

    assert response.status_code in (200, 204)

def test_delete_user_not_found(users_client):
    user_id = 9999

    response = users_client.delete_user(user_id)

    # jsonplaceholder still responds with success
    assert response.status_code in (200, 204)