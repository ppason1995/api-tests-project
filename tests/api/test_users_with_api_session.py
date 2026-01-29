from src.api.session import ApiSession
from src.api.users_client import UsersClient

def test_get_users_with_api_sessions(monkeypatch):
    # fake requests.get
    def fake_get(url, headers=None):
        assert url.endswith("/users")
        assert headers == {
            "Authorization": "Bearer TEST_TOKEN"
        }

        class FakeResponse:
            def json(self):
                return [{"id": 1, "name": "Alice"}]
    
        return FakeResponse()
    
    monkeypatch.setattr("requests.get", fake_get)

    session = ApiSession(token="TEST_TOKEN")
    client = UsersClient(session=session)

    users = client.get_users()

    assert users == [{"id": 1, "name": "Alice"}]
