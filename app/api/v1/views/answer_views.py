"""Answer views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.answer_models import AnswerModels
from app.api.v1.utils.authentication import login_required
from app.api.v1.utils.validation import verify_id

answerv1 = Blueprint('v1', __name__, url_prefix='/api/v1')
answers = AnswerModels()


@answerv1.route('/questions/answers', methods=['POST'])
@login_required
def post_answer(current_user):
    """Post an answer"""
    try:
        data = request.get_json()
        username = data['username']
        questionId = data['questionId']
        question = data['question']
        answer = data['answer']
    except KeyError:
        return make_response(jsonify({
            "Error": "Please make sure all the fields are present"
        }), 401)

    ans_data = answers.post_answer(username, questionId, question, answer)
    if ans_data == "empty":
        return make_response(jsonify({
                "Error": "All fields are required"
            }), 401)
    return make_response(jsonify({
            "message": "Answer Posted Successfully"
        }), 201)


@answerv1.route('/questions/answers', methods=['GET'])
@login_required
def retrieve_answers(current_user):
    """Return all answers"""
    all_answers = answers.get_all_answers()
    return make_response(jsonify({
            "All Answers": all_answers
        }), 200)


@answerv1.route('/questions/answers/<username>', methods=['GET'])
@login_required
def user_questions(username, current_user):
    """Return user answers"""
    user_ans = answers.get_user_answers(username)
    if user_ans == "empty":
            return make_response(jsonify({
                "Error": "No answers posted by user"
            }), 400)
    return make_response(jsonify({
                "Answers": user_ans
            }), 200)


@answerv1.route('/questions/<answerId>', methods=['DELETE'])
@login_required
def delete_question(answerId, current_user):
    """Delete a question"""
    verify = verify_id(answerId)
    if verify is False:
            return make_response(jsonify({
                "Error": "Please enter a valid answer ID"
            }), 400)
    delete_answer = answers.delete_one_answer(answerId)
    if delete_answer is False:
        return make_response(jsonify({
                "Error": "Answer does not exist or already deleted"
            }), 400)
    else:
        return make_response(jsonify({
                "Message": "Answer Deleted"
            }), 200)
