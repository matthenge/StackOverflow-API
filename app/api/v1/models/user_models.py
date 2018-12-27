"""User models"""
from app.api.v1.utils.manage import find_username, hash_password
from app.api.v1.utils.manage import check_hash_password
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
        user_data['password'] = hash_password(password, username)
        user_details = users.append(user_data)
        return user_details

    def login_by_username(self, username, password):
        """Login a user by username"""
        hashed = hash_password(password, username)
        user = find_username(users, username)
        if user and check_hash_password(hashed, user['password']) is True:
            return user
        elif user and check_hash_password(hashed, user['password']) is False:
            return "Password Error"
        elif not user:
            return False
