# app
from flask import (
    Flask,
    jsonify,
    Response
)


def create_app(config=None):
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return "Test run to configure Travis CI"

    return app
