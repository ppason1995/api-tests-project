import pytest
from src.api.base_session import BaseSession
from src.api.users_client import UsersClient

@pytest.fixture
def base_session():
    """
    Base HTTP session configured with test API base URL.
    Shared across API clients.
    """
    return BaseSession("https://jsonplaceholder.typicode.com")

@pytest.fixture
def users_client(base_session):
    """
    Users API client using shared BaseSession.
    """
    return UsersClient(base_session)