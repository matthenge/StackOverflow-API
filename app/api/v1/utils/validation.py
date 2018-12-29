"""User input validation"""
import re
from app.api.v1.utils.manage import find_username, find_email


def email_validation(email):
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if email and re.match(regex, email):
        return True
    else:
        return False


def details_validation(username, email, password, confirm_password):
    if not username:
        return None
    elif not email:
        return None
    elif not password:
        return None
    elif not confirm_password:
        return None
    else:
        return True


def question_validation(user_id, title, body, tags, answer):
    if not user_id:
        return None
    elif not title:
        return None
    elif not body:
        return None
    elif not tags:
        return None
    elif not tags:
        return None
    else:
        return True


def answer_validation(questionId, question, answer):
    if not questionId:
        return None
    elif not question:
        return None
    elif not answer:
        return None
    else:
        return True


def verify_user(users, username, email):
    user = find_username(users, username)
    if user:
        return "username"
    mail = find_email(users, email)
    if mail:
        return "email"


def verify_id(questionId):
    try:
        int(questionId)
    except ValueError:
        return False