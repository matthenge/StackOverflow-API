"""Answers Model"""
import datetime
from app.api.v1.utils.validation import answer_validation
from app.api.v1.utils.manage import fetch_one, get_all_by


answers = []


class AnswerModels:
    """Main Answers Class"""
    def __init__(self):
        """Initialize the answer model class"""
        pass

    def post_answer(self, username, questionId, question, answer):
        """Post answer method"""
        answer_data = {
            'answerId': len(answers) + 1,
            'time': datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
            'username': username,
            'questionId': questionId,
            'question': question,
            'answer': answer
        }
        field = answer_validation(username, questionId, question, answer)
        if field is None:
            return "empty"
        return answers.append(answer_data)

    def get_all_answers(self):
        """Return all answers"""
        return answers

    def get_one_answer(self, answerId):
        """Return specific answer"""
        return fetch_one(answers, answerId)

    def get_user_answers(self, username):
        """Return user answers"""
        user_answers = get_all_by(answers, username)
        if not user_answers:
            return "empty"
        return user_answers

    def delete_one_answer(self, answerId):
        """Delete a specific answer"""
        answer = fetch_one(answers, answerId)
        if answer:
            return answers.remove(answer)
        elif not answer:
            return False
