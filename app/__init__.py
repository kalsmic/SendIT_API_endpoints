# app

from flask import (
    Flask,
    jsonify,
    Response,
    abort
)

from model import (
    USERS,
    PARCELS
)


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
            return jsonify({'Error': 'Not Found'}), 404

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
        return jsonify({'Error': 'Not Found'}), 404

    def get_a_parcel_by_userId():
        """Fetch all parcel delivery
         orders by a specific user """

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
