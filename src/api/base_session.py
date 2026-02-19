import requests
from .exceptions import (
    ApiError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    ServerError,
)

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
    
    def _handle_response(self, response):
        if 200 <= response.status_code < 300:
            return response
        
        if response.status_code == 400:
            raise BadRequestError(response.text)
        
        if response.status_code == 401:
            raise UnauthorizedError(response.text)
        
        if response.status_code == 403:
            raise ForbiddenError(response.text)
        
        if response.status_code == 404:
            raise NotFoundError(response.text)
        
        if 500 <= response.status_code < 600:
            raise ServerError(response.text)
        
        raise ApiError(f"Unexpected status code: {response.status_code}")
    
