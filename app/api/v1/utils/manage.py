"""Resource for shared functions"""


def fetch_one(questions, questionId):
    """Fetch specific item"""
    for question in questions:
            if int(questionId) == question['questionId']:
                return question


def find_username(users, username):
    """Find the username in the database"""
    for user in users:
        if username == user['username']:
            return user
