"""Question models"""
import datetime
from app.api.v1.utils.manage import fetch_one

questions = []


class QuestionModels:
    """Question models class"""
    def __init__(self):
        """Initialize the question models class"""
        pass

    def add_question(self, user_id, title, body, tags, answer):
        """Create new question"""
        question_data = {
            'questionId': len(questions) + 1,
            'user_id': user_id,
            'time': datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
            'title': title,
            'body': body,
            'tags': tags,
            'answer': answer
        }
        question_details = questions.append(question_data)
        return question_details

    def get_all_questions(self):
        """Return all questions"""
        return questions

    def get_one_question(self, questionId):
        """Return specific question"""
        return fetch_one(questions, questionId)

    def delete_one_question(self, questionId):
        """Delete a specific question"""
        question = fetch_one(questions, questionId)
        if question:
            return questions.remove(question)
        elif not question:
            return False
