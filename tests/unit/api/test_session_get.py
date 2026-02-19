from src.api.session import ApiSession

def test_session_get_sends_headers(monkeypatch):
    def fake_get(url, headers=None):
        assert url == "http://example.com"
        assert headers == {
            "Authorization": "Bearer TEST_TOKEN"
        }

        class FakeResponse:
            status_code = 200
            text = ""

            def json(self):
                return {"ok": True}
            
        return FakeResponse()
    
    monkeypatch.setattr("src.api.session.requests.get", fake_get)

    session = ApiSession(token="TEST_TOKEN")
    response = session.get("http://example.com")

    assert response.json() == {"ok": True}