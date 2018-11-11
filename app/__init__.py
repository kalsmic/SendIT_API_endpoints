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

        pass

    def get_a_parcel():
        """Fetch a specific parcel delivery order"""
        pass

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
