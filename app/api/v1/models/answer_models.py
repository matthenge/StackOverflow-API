"""Answers Model"""
import datetime


answers = []


class AnswerModels:
    """Main Answers Class"""
    def __init__(self):
        """Initialize the answer model class"""
        pass

    def post_answer(self, questionId, question, answer):
        """Post answer method"""
        answer_data = {
            'answerId': len(answers) + 1,
            'time': datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
            'questionId': questionId,
            'question': question,
            'answer': answer
        }
        return answers.append(answer_data)
