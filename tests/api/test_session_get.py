from src.api.session import ApiSession

def test_session_get_sends_headers(monkeypatch):
    def fake_get(url, headers=None):
        assert url == "http://example.com"
        assert headers == {
            "Authorization": "Bearer TEST_TOKEN"
        }

        class FakeResponse:
            def json(self):
                return {"ok": True}
            
        return FakeResponse()
    
    monkeypatch.setattr("requests.get", fake_get)

    session = ApiSession(token="TEST_TOKEN")
    response = session.get("http://example.com")

    assert response.json() == {"ok": True}