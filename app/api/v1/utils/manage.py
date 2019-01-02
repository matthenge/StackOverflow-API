"""Resource for shared functions"""
import hashlib


def fetch_one(questions, questionId):
    """Fetch specific item"""
    for question in questions:
            if int(questionId) == question['questionId']:
                return question


def get_all_by(db, username):
    """Fetch all by one user"""
    user_items = []
    for item in db:
        if item['username'] == username:
            user_items.append(item)
    return user_items


def find_username(users, username):
    """Find the username in the database"""
    for user in users:
        if username == user['username']:
            return user


def find_email(users, email):
    """Find the email in the database"""
    for user in users:
        if email == user['email']:
            return user


def hash_password(password, username):
    """Hash user passwords"""
    salt = password + username
    hashed = hashlib.md5(str.encode(salt)).hexdigest()
    return hashed


def check_hash_password(password, hashed):
    """Check hashed passwords are same"""
    if password == hashed:
        return True
    else:
        return False
