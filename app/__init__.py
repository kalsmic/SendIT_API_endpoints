# app
from flask import Flask

from app.routes.parcels import parcels_bp
from app.routes.users import users_bp
from config import Config


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return "SendIT is a courier service that helps users\
         deliver parcels to different destinations"

    app.register_blueprint(parcels_bp)
    app.register_blueprint(users_bp)

    return app

app = create_app()


if __name__ == "__main__":
    app.run()
