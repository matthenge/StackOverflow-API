"""Resource for shared functions"""


def fetch_one(questions, questionId):
    """Fetch specific item"""
    for question in questions:
            if int(questionId) == question['questionId']:
                return question
