"""User views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.user_models import UserModels

userv1 = Blueprint('userv1', __name__, url_prefix='/api/v1')
users = UserModels()


@userv1.route('/auth/signup', methods=['POST'])
def signup():
    """Register user"""
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    users.add_user(username, email, password, confirm_password)
    return make_response(jsonify({
            "message": "successful registration"
        }), 201)


@userv1.route('/auth/login', methods=['POST'])
def login():
    """Login a registered user"""
    data = request.get_json()
    username = data['username']
    password = data['password']

    one_user = users.login_by_username(username, password)
    if one_user is False:
        return make_response(jsonify({
            "Error": "User not found: Please register"
        }), 401)
    elif one_user == "Password Error":
        return make_response(jsonify({
            "Error": "Password Incorrect"
        }), 401)
    elif one_user:
        return make_response(jsonify({
            "Message": "Logged in Successfully"
        }), 201)
