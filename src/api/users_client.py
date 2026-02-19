from src.api.base_session import BaseSession

class UsersClient:
    """
    Client responsible for /users endpoints.
    """

    def __init__(self, session: BaseSession):
        self.session = session

    def get_users(self):
        """Get list of users."""
        response =  self.session.get("/users")
        return response.json()
    
    def get_user(self, user_id: int):
        """Get single user by id."""
        return self.session.get(f"/users/{user_id}")
    
    def create_user(self, payload: dict):
        """Create new user."""
        return self.session.post("/users", json=payload)
    
    def update_user(self, user_id: int, payload: dict):
        """Update existing user."""
        return self.session.patch(f"/users/{user_id}", json=payload)
    
    def delete_user(self, user_id: int):
        """Delete user by id."""
        return self.session.delete(f"/users/{user_id}")
    
    def get_users_with_params(self, params: dict):
        """Get users with query parameters."""
        return self.session.get("/users", params=params)