# user.py
""" Module contains endpoints for getting a parcel order for a given user"""

from flask import (
    Flask,
    jsonify,
    request,
    json,
    Blueprint
)

from app.dummy_data import (
    PARCELS,
    USERS
)
from app.http_responses import (
    Not_found,
    Bad_request
)

user = Blueprint('user',__name__,url_prefix='/api/v1/users')

@user.route('/<userId>/parcels', methods=['GET'])
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

            user_parcels.append(parcel)

        # valid user has no parcels
    if not user_parcels:
        return jsonify(Not_found), 404
    # valid user has parcels
    return jsonify({'parcels': user_parcels}), 200

    
