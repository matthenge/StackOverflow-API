from flask import Flask, Blueprint
from .api.v1.views.user_views import userv1 as v1
from .api.v1.views.question_views import questionv1 as v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix='/api/v1/')
    app.url_map.strict_slashes = False

    return app
