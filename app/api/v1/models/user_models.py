"""User models"""
users = []

class UserModels:
    """User models class"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = users

    def add_user(self, username, email, password):
        """Adding new users"""
        user_data = {
            'user_id' : len(users) + 1,
            'username' : username,
            'email' : email,
            'password' : password      
        }
        user_details = self.db.append(user_data)
        return user_details
