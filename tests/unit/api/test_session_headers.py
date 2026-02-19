from src.api.session import ApiSession

def test_session_builds_auth_header():
    session = ApiSession(token="TEST_TOKEN")

    headers = session._headers()

    assert headers == {
        "Authorization": "Bearer TEST_TOKEN"
    }