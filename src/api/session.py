import requests

class ApiSession:
    def __init__(self, token: str | None = None):
        self.token = token

    def _headers(self):
        if not self.token:
            return {}
        return {
            "Authorization": f"Bearer {self.token}"
        }
    
    def get(self, url: str):
        return requests.get(
            url, headers=self._headers()
            )
    