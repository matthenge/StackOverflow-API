"""User views"""
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.user_models import UserModels 

userv1 = Blueprint('v1', __name__, url_prefix='/api/v1')
users = UserModels()

@userv1.route('/auth/signup', methods=['POST'])
def signup():
    """Register user"""
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    users.add_user(username, email, password)
    return make_response(jsonify({
            "message": "successful registration"
        }), 201)
