def test_create_user_with_missing_email(users_client):
    payload = {
        "name" : "Invalid user"
        # missing email
    }

    response = users_client.create_user(payload)

    assert response.status_code in (200, 201)

    data = response.json()

    # API accepted request, but response should not match full user schema
    assert "email" not in data or data["email"] is None