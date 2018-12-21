"""User models"""
from app.api.v1.utils.manage import find_username, find_password
users = []


class UserModels:
    """User models class"""
    def __init__(self):
        """Initialize the user model class"""
        pass

    def add_user(self, username, email, password, confirm_password):
        """Adding new users"""
        user_data = {
            'user_id': len(users) + 1,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }
        user_details = users.append(user_data)
        return user_details

    def find_by_username(self, username):
        """Find a user by username"""
        return find_username(users, username)

    def check_password(self, password):
        """Check if password matches"""
        return find_password(users, password)
