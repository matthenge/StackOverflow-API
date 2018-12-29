"""Question views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.question_models import QuestionModels
from app.api.v1.utils.validation import verify_id
from app.api.v1.utils.authentication import login_required

questionv1 = Blueprint('questionv1', __name__, url_prefix='/api/v1')
questions = QuestionModels()


@questionv1.route('/questions', methods=['POST'])
@login_required
def ask_question(username):
    """Create question"""
    try:
        data = request.get_json()
        user_id = data['user_id']
        title = data['title']
        body = data['body']
        tags = data['tags']
        answer = data['answer']
    except KeyError:
        return make_response(jsonify({
            "Error": "Please make sure all the fields are present"
        }), 401)
    qdata = questions.add_question(user_id, title, body, tags, answer)
    if qdata == "empty":
        return make_response(jsonify({
                "Error": "All fields are required"
            }), 401)
    return make_response(jsonify({
            "message": "Question Posted Successfully"
        }), 201)


@questionv1.route('/questions', methods=['GET'])
@login_required
def retrieve_questions(username):
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
            "All Questions": all_questions
        }), 200)


@questionv1.route('/questions/<questionId>', methods=['GET'])
@login_required
def retrieve_one_question(questionId, username):
    """Return one question"""
    verify = verify_id(questionId)
    if verify is False:
            return make_response(jsonify({
                "Error": "Please enter a valid question ID"
            }), 400)
    one_question = questions.get_one_question(questionId)
    if one_question:
        return make_response(jsonify({
                "Question": one_question
            }), 200)
    elif not one_question:
        return make_response(jsonify({
                "Error": "Question does not exist or deleted"
            }), 400)


@questionv1.route('/questions/<questionId>', methods=['DELETE'])
@login_required
def delete_question(questionId, username):
    """Delete a question"""
    verify = verify_id(questionId)
    if verify is False:
            return make_response(jsonify({
                "Error": "Please enter a valid question ID"
            }), 400)
    delete_question = questions.delete_one_question(questionId)
    if delete_question is False:
        return make_response(jsonify({
                "Error": "Question does not exist or already deleted"
            }), 400)
    else:
        return make_response(jsonify({
                "Message": "Question Deleted"
            }), 200)
