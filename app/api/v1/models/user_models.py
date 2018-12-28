"""User models"""
from app.api.v1.utils.manage import find_username, hash_password
from app.api.v1.utils.manage import check_hash_password, find_email
from app.api.v1.utils.validation import email_validation, details_validation
from app.api.v1.utils.validation import verify_user
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
        data = details_validation(username, email, password, confirm_password)
        if data is None:
            return "empty"
        valid_email = email_validation(email)
        if valid_email is False:
            return "invalid"
        verify = verify_user(users, username, email)
        if verify == "username":
            return "username exists"
        elif verify == "email":
            return "email exists"
        user_data['password'] = hash_password(password, username)
        hashed = hash_password(confirm_password, username)
        if check_hash_password(hashed, user_data['password']) is False:
            return "unmatched"
        user_data['confirm_password'] = hash_password(confirm_password,
                                                      username)
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

    def all_users(self):
        return users
