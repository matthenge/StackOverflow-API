"""Answer views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.answer_models import AnswerModels

answerv1 = Blueprint('v1', __name__, url_prefix='/api/v1')
answers = AnswerModels()


@answerv1.route('/questions/answers', methods=['POST'])
def post_answer():
    """Post an answer"""
    data = request.get_json()
    questionId = data['questionId']
    question = data['question']
    answer = data['answer']

    answers.post_answer(questionId, question, answer)
    return make_response(jsonify({
            "message": "Answer Posted Successfully"
        }), 201)
