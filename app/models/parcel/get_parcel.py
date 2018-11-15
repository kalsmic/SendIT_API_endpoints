# get_parcel.py
"""This module fetches a specific parcel delivery orders"""

from flask import (
    jsonify,
    Blueprint
)

from app.http_responses import (
    Bad_request,
    Not_found
)
from .parcel import get_parcel_by_id

getParcel = Blueprint('getParcel', __name__, url_prefix='/api/v1')


@getParcel.route('/parcels/<parcelId>', methods=['GET'])
def get_all_parcel(parcelId):
    """Parameter: int parcelId
    :returns:
        404 If parcelId is not an integer,
        400 If parcelId does not exist
        200 if parcelId exists"""

    # cast parcelId to int
    try:
        parcelId = int(parcelId)
    #     if parcel id is not an integer
    except ValueError:
        return jsonify(Bad_request), 400

    try:
        # return parcel order if parcelId exists
        return jsonify({'parcel': get_parcel_by_id(parcelId)}), 200

    # parcelId does not exist
    except KeyError:
        return jsonify(Not_found), 404
