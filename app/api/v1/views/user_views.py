"""User views"""
from flask import make_response, jsonify, request, Blueprint, current_app
from app.api.v1.models.user_models import UserModels
from app.api.v1.utils.authentication import login_required
import jwt
import datetime

userv1 = Blueprint('userv1', __name__, url_prefix='/api/v1')
users = UserModels()


@userv1.route('/auth/signup', methods=['POST'])
def signup():
    """Register user"""
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
    except KeyError:
        return make_response(jsonify({
            "Error": "Please make sure all the fields are present"
        }), 401)

    user = users.add_user(username, email, password, confirm_password)
    if user == "invalid":
        return make_response(jsonify({
                "Error": "Please enter a correct email address"
            }), 401)
    if user == "empty":
        return make_response(jsonify({
                "Error": "All fields are required"
            }), 401)
    if user == "username exists":
        return make_response(jsonify({
            "Error": "The username already exists. Please choose another one"
            }), 401)
    if user == "email exists":
        return make_response(jsonify({
                "Error": "The email already exists. Please login"
            }), 401)
    if user == "unmatched":
        return make_response(jsonify({
                "Error": "Passwords do not match"
            }), 401)
    return make_response(jsonify({
            "message": "successful registration"
        }), 201)


@userv1.route('/auth/login', methods=['POST'])
def login():
    """Login a registered user"""
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
    except KeyError:
        return make_response(jsonify({
            "Error": "Please make sure all the fields are present"
        }), 401)
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
        try:
            expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            details = {'username': username, 'exp': expiry}
            token = jwt.encode(details, current_app.config['SECRET_KEY'],
                               algorithm='HS256')
            return make_response(jsonify({
                "Token": token.decode('UTF-8'),
                "Message": "Logged in as {}".format(username)
                }), 200)
        except Exception as error:
            return str(error)


@userv1.route('/auth/users', methods=['GET'])
@login_required
def user_accounts(username):
    accounts = users.all_users()
    return make_response(jsonify({
            "Message": accounts
        }), 201)
