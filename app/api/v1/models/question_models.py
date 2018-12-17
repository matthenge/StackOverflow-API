"""Question models"""
import datetime

questions = []

class QuestionModels:
    """Question models class"""
    def __init__(self):
        """Initialize the question models class"""
        self.db = questions

    def add_question(self, user_id, title, body, tags, answer):
        """Create new question"""
        question_data = {
            'question_id' : len(questions) + 1,
            'user_id' : user_id,
            'time': datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
            'title' : title,
            'body' : body,
            'tags' : tags,
            'answer' : answer      
        }
        question_details = self.db.append(question_data)
        return question_details
