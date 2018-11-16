# Cancel_parcel.py
"""This module implements add a  parcel delivery order"""

from flask import (
    jsonify,
    Blueprint,
    request,
    json
)

from .parcel import PARCEL, PARCELS, get_parcel_by_id

addParcel = Blueprint('addParcel', __name__, url_prefix='/api/v1')


@addParcel.route('/parcels', methods=['POST'])
def add_a_parcel_order():
    """Create a parcel delivery order
    Expects parameters:
        Item: type string
        pickUp: type string
        destination: type string
        ownerId: type int
    Returns:
        400 HTTP error code if a parameter i not provided
        201 HTTP error code  if Order is created Successfully

    """

    data = request.data
    parcelDict = json.loads(data)

    for key, value in parcelDict.items():
        # empty fields
        if not value:
            return jsonify({'message': "{} cannot be empty".format(key)}), 400
    # add new parcel order
    newParcel = PARCEL(parcelDict['Item'], parcelDict['pickUp'], parcelDict['destination'], 'Pending',
                       parcelDict['ownerId'])
    PARCELS.append(newParcel)
    # return new parcel with parcel it attached to it
    return jsonify({'parcel': get_parcel_by_id(len(PARCELS))}), 201
