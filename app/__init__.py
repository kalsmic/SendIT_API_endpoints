# app
import os
from flask import Flask


from .dummy_data import (
    USERS,
    PARCELS
)

from app.models.parcel.get_parcels import getParcels
from app.models.parcel.parcel import PARCEL

from .http_responses import *
from .models.user import user


PARCELS.extend ([
    # PARCEL(id, 'item' 'pickUp', 'destination', 'status', ownerId),
    PARCEL('item' ,'pickUp', 'destination', 'status', 'owner1'),
    PARCEL('Laptop', 'Kampala', 'Moroto', 'pending', 'owner2'),
    PARCEL('Office Cabin', 'Kole', 'Otuke', 'In Transit','owner3'),
    PARCEL('HNIS FORMS', 'Yumbe', 'Koboko', 'Delivered', 'owner4'),
    PARCEL('HNIS FORMS' ,'Yumbe', 'Koboko', 'Delivered', 'owner5'),
    PARCEL('APPRAISAL FORMS' ,'Mwanza', 'Bukoba', 'Cancelled', 'owner6')
])

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    @app.route('/')
    def index():
        return "SendIT is a courier service that helps users\
         deliver parcels to different destinations"

    app.register_blueprint(getParcels)
    # app.register_blueprint(parcel)
    # app.register_blueprint(user)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
    print(os.environ['APP_SETTINGS'])
