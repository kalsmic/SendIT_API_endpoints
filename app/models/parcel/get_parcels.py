# get_parcels.py
"""This module fetches all parcel delivery orders"""

from flask import (
    jsonify,
    Blueprint
)

from .parcel import PARCELS

getParcels = Blueprint('getParcels', __name__, url_prefix='/api/v1')


@getParcels.route('/parcels', methods=['GET'])
def get_all_parcels():
    """Fetch all parcel delivery orders"""

    parcelOrders = []
    # traverse through the parcels
    for parcel in PARCELS:
        # get details for each parcel
        parcelOrders.append(parcel.parcel_details())

    return jsonify({'parcels': parcelOrders}), 200
