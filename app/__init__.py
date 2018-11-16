# app
import os
from flask import Flask


# from .dummy_data import (
#     USERS,
#     # PARCELS
# )

from app.models.parcel.get_parcels import getParcels
from app.models.parcel.get_parcel import getParcel
from app.models.parcel.cancel_parcel import cancelParcel
from app.models.parcel.add_parcel import addParcel
from app.models.user import user


from app.models.parcel.parcel import PARCEL
from app.models.user import user

from .http_responses import *
from .models.user import user



def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    @app.route('/')
    def index():
        return "SendIT is a courier service that helps users\
         deliver parcels to different destinations"

    app.register_blueprint(getParcels)
    app.register_blueprint(addParcel)
    app.register_blueprint(getParcel)
    app.register_blueprint(cancelParcel)
    # app.register_blueprint(parcel)
    app.register_blueprint(user)

    return app


app = create_app()


if __name__ == "__main__":
    # app = create_app()
    app.run()
    print(os.environ['APP_SETTINGS'])
