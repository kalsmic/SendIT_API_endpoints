# app

from flask import (
    Flask,
    jsonify,
    Response
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

        # parcelId is not an interger
        if not isinstance(parcelId, int):
            return jsonify({'Error': 'Not found'}), 404

        try:
            for Order in PARCELS:
                # parcel id exists
                if Order['id'] == parcelId:
                    return jsonify(
                        'parcel', {
                            'Title': Order['title'],
                            'PickUpAddress': Order['pickUp'],
                            'DestinationAddress': Order['destination'],
                            'Status': Order['status']
                        }
                    ), 200
            # parcel id doesn't exist
            return jsonify({'Error': 'Not found'}), 404

        except IndexError:
            return jsonify({'Error': 'Not found'}), 404

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
