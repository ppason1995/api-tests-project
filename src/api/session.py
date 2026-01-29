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
        response = requests.get(
            url,
            headers=self._headers()
            )
        
        if response.status_code == 401:
            raise RuntimeError("Unauthorized")
        
        return response