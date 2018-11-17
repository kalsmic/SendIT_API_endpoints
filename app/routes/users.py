# users.py
"""File contains routes for user end point"""

from flask import (
    Blueprint,
    jsonify
)

from app.models.parcel import parcelOrders
from app.models.user import (
    user_id_table
)
from app.responses import (
    Not_found,
    Bad_request
)

users_bp = Blueprint('users_bp', __name__, url_prefix='/api/v1/users')


@users_bp.route('/<userId>/parcels', methods=['GET'])
def get_a_parcel_by_userId(userId):
    """Fetch all parcel delivery
    orders by a specific user """

    # cast parcelId to int
    try:

        userId = int(userId)

    except ValueError:
        # userId is not a number
        # Therefore cannot be cast to an integer

        return jsonify(Bad_request), 400

    # Avoids returning the last userId when userId of zero is given
    """checks if userId exists"""
    if userId not in user_id_table.keys():
        return jsonify(Bad_request), 400

    # Only look up parcels for a valid user
    user_parcels = []
    for parcel in parcelOrders:
        if parcel.ownerId == userId:
            user_parcels.append(parcel.parcel_details())

        # valid user has no parcels
    if not user_parcels:
        return jsonify(Not_found), 404
    # valid user has parcels
    return jsonify({'parcels': user_parcels}), 200
