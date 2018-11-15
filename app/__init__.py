# app

from flask import (
    Flask,
    Blueprint
)

from dummy_data import (
    USERS,
    PARCELS
)
from .http_responses import *
from .models.parcel import parcel
from .models.user import user




def create_app(config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "SendIT is a courier service that helps users\
         deliver parcels to different destinations"

    app.register_blueprint(parcel)
    app.register_blueprint(user)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
