# app
from functools import wraps

from flask import (
    Flask,
    jsonify,

)

from model import (
    USERS,
    PARCELS
)
from .errors import *


def create_app(config=None):
    app = Flask(__name__)

    @app.route('/api/v1/parcels')
    def get_parcels():
        """Fetch all parcel delivery orders"""
        return jsonify({'parcels': PARCELS}), 200

    @app.route('/api/v1/parcels/<parcelId>')
    def get_a_parcel(parcelId):
        """Fetch a specific parcel delivery order"""
        # cast parcelId to int
        try:
            parcelId = int(parcelId)
        # parcelId is not int
        except (ValueError):
            return jsonify(Not_found), 404

        parcel = {}

        for Order in PARCELS:
            # parcel id exists
            if Order['id'] == int(parcelId):
                parcel['id'] = Order['id']
                parcel['Item'] = Order['Item']
                parcel['PickUpAddress'] = Order['pickUp']
                parcel['DestinationAddress'] = Order['destination']
                parcel['ownerId'] = Order['ownerId']
                parcel['Status'] = Order['status']
                return jsonify({'Parcel': parcel}), 200
        # parcelId is of type int but does not exist in parcels
        return jsonify(Not_found), 404

    @app.route('/api/v1/users/<userId>/parcels')
    def get_a_parcel_by_userId(userId):
        """Fetch all parcel delivery
        orders by a specific user """

        try:
            userId = int(userId)

        # id is not of type Number
        except (TypeError, ValueError):
            return jsonify(Bad_request), 400

        # Is User valid
        user_exists = False
        for user in USERS:
            if user['userId'] == userId:
                user_exists = True

        if not user_exists:
            return jsonify(Bad_request), 400

        # Only look up parcels for a valid user
        user_parcels = []
        for parcel in PARCELS:
            if parcel['ownerId'] == userId:
                #  user_parcels['ownerId'] = {
                #      ''
                #  }
                user_parcels.append(parcel)

            # valid user has no parcels
        if not user_parcels:
            return jsonify(Not_found), 404
        # valid user has parcels
        return jsonify({'parcels': user_parcels}), 200

    def cancel_a_delivery_order():
        """Cancel a specific parcel delivery order"""
        pass

    def add_a_parcel_order():
        """Create a parcel delivery order"""
        pass

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
