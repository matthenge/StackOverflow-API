"""Answer views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.answer_models import AnswerModels
from app.api.v1.utils.authentication import login_required

answerv1 = Blueprint('v1', __name__, url_prefix='/api/v1')
answers = AnswerModels()


@answerv1.route('/questions/answers', methods=['POST'])
@login_required
def post_answer(username):
    """Post an answer"""
    try:
        data = request.get_json()
        questionId = data['questionId']
        question = data['question']
        answer = data['answer']
    except KeyError:
        return make_response(jsonify({
            "Error": "Please make sure all the fields are present"
        }), 401)

    ans_data = answers.post_answer(questionId, question, answer)
    if ans_data == "empty":
        return make_response(jsonify({
                "Error": "All fields are required"
            }), 401)
    return make_response(jsonify({
            "message": "Answer Posted Successfully"
        }), 201)
