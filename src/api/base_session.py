import requests

class BaseSession:
    """
    Base HTTP session used by API clients.
    Responsible for building full URLs and sending HTTP requests.
    """

    def __init__(self, base_url):
        # Remove trailing slash to avoid double slashes in endpoints
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        """Send GET request to given API endpoint."""
        return self.session.get(
            self.base_url + endpoint, params=params)
    
    def post(self, endpoint, json=None):
        """Send POST request to given API endpoint."""
        return self.session.post(
            self.base_url + endpoint, json=json)
    
    def patch(self, endpoint, json=None):
        """Send PATCH request to given API endpoint."""
        return self.session.patch(
            self.base_url + endpoint, json=json)
    
    def delete(self, endpoint):
        """Send DELETE request to given API endpoint."""
        return self.session.delete(
            self.base_url + endpoint)
    
