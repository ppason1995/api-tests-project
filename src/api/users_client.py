from src.api.base_session import BaseSession

class UsersClient:
    """
    Client responsible for /users endpoints.
    """

    def __init__(self, session: BaseSession):
        self.session = session

    def get_users(self):
        """Get list of users."""
        return self.session.get("/users")
    
    def get_user(self, user_id: int):
        """Get single user by id."""
        return self.session.get(f"/users/{user_id}")
