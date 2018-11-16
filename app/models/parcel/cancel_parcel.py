# Cancel_parcel.py
"""This module implements Cancel a specific parcel delivery order"""

from flask import (
    jsonify,
    Blueprint
)

from app.http_responses import (
    Bad_request,
    Not_modified,
    Not_Allowed
)
from .parcel import get_parcel_by_id, parcel_table, get_parcel_reference

cancelParcel = Blueprint('cancelParcel', __name__, url_prefix='/api/v1')


@cancelParcel.route('/parcels/<parcelId>/cancel', methods=['PUT'])
def cancel_a_delivery_order(parcelId):
    """Parameter: integer parcelId
       Returns: 400 if parcelId is not  of type int
       Returns: 204 if parcel's successfully cancelled
       Returns : 304 if parcel is Already cancelled or Delivered
    """
    # cast parcelId to int
    try:
        parcelId = int(parcelId)
    #     if parcel id is not an integer
    except ValueError:
        return jsonify(Bad_request), 400

    # Check if parcel id exists in the parcel's table
    if parcelId in parcel_table().keys():

        # Check if parcel is not cancelled or delivered
        if get_parcel_reference(parcelId).cancel_parcel_Order():
            return jsonify({'parcels': get_parcel_by_id(parcelId)}), 204

        # Either parcel is already Cancelled or Delivered
        return jsonify(Not_modified), 304
    # parcelId does not exist
    return jsonify(Bad_request), 400
