# parcel.py
""" Module contains endpoints for getting , creating and updating a parcel delivery order"""

from flask import (
    jsonify,
    request,
    json,
    Blueprint
)

from app.dummy_data import PARCELS

from app.http_responses import (
    Not_found,
    Not_modified
)

parcel = Blueprint('parcel',__name__,url_prefix='/api/v1')


@parcel.route('/parcels', methods=['GET'])
def get_parcels():
    """Fetch all parcel delivery orders"""
    return jsonify({'parcels': PARCELS}), 200


@parcel.route('/parcels/<parcelId>', methods=['GET'])
def get_a_parcel(parcelId):
    """Fetch a specific parcel delivery order
    Expects a parameter of type int
    Returns: 404 Error if parcelId not found
    Otherwise returns the parcel and HTTP code 200"""
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
            
            # Parcel is, return parcel
            return jsonify({'parcel': parcel}), 200
    # parcelId is of type int but does not exist in parcels
    return jsonify(Not_found), 404


@parcel.route('/parcels/<parcelId>/cancel', methods=['PUT'])
def cancel_a_delivery_order(parcelId):
    """Cancel a specific parcel delivery order
    Expects parcelId as parameter and of type int
    Returns: 400 if parcelId is invalid,
    Returns: 204 if parcel's successfully cancelled
    Returns : 304 if parcel is Already cancelled or Delivered
    """
    try:
        parcelId = int(parcelId)

    # id is not of type Number
    except (TypeError, ValueError):
        return jsonify(Bad_request), 400

    modifiable = ('Delivered', 'Cancelled')

    for parcel in PARCELS:
            # Cancel order
        if parcel['id'] == parcelId and parcel['status'] not in modifiable:
            parcel['status'] = 'Cancelled'
            return jsonify({'parcels': parcel}), 204

    return jsonify(Not_modified), 304


@parcel.route('/parcels', methods=['POST'])
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

    for key,value in parcelDict.items():
        # empty fields
        if not value:
            return jsonify({'message':"{} cannot be empty".format(key)}),400
    # add new parcel order
    PARCELS.append(
    {
        'id': int( PARCELS[-1]['id']+1),
        'Item': parcelDict['Item'],
        'pickUp': parcelDict['pickUp'],
        'destination': parcelDict['destination'],
        'status': 'Pending',
        'ownerId': parcelDict['ownerId']
    }
    )
    # return the contents of the new order
    return jsonify({'newOrder': PARCELS[-1]}),201








