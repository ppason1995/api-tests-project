import pytest

def test_get_users(users_client):
    # Verify that users endpoint returns non-empty list
    response = users_client.get_users()

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0