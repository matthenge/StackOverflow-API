"""Question views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.question_models import QuestionModels 

questionv1 = Blueprint('v1', __name__, url_prefix='/api/v1')
questions = QuestionModels()

@questionv1.route('/questions', methods=['POST'])
def ask_question():
    """Create question"""
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    body = data['body']
    tags = data['tags']
    answer = data['answer']

    questions.add_question(user_id, title, body, tags, answer)
    return make_response(jsonify({
            "message": "Question Posted Successfully"
        }), 201)
