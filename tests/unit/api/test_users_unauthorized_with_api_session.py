import pytest
from src.api.session import ApiSession
from src.api.users_client import UsersClient

def test_get_users_unauthorized(monkeypatch):
    def fake_get(url, headers=None):
        class FakeResponse:
            status_code = 401

            def json(self):
                return {}
            
        return FakeResponse()
    
    monkeypatch.setattr("requests.get", fake_get)

    session = ApiSession(token="TEST_TOKEN")
    client = UsersClient(session=session)

    with pytest.raises(RuntimeError, match="Unauthorized"):
        client.get_users()