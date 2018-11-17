# # test_get__parcels__by_userId.py

"""Test Module for GET parcels for a specific user endpoint"""

from flask import json

from app.models.parcel import parcelOrders
from app.responses import (
    Bad_request,
    Not_found
)


def test_get_parcels_for_a_user_with_invalid_user_id(client):
    # """ Given an API Consumer
    # When I submit a GET request to /users/<userId>/parcels
    # And no parcel orders exist for the given user id
    # Then the system returns an HTTP status code of 404
    # And a JSON representation of the error 'Not found' """

    with client.get('/api/v1/users/er9/parcels') as userId_Type_Error:
        assert userId_Type_Error.status_code == 400
        assert json.loads(userId_Type_Error.data) == Bad_request

    with client.get('/api/v1/users/9/parcels') as userId_does_not_exist:
        assert userId_does_not_exist.status_code == 400
        assert json.loads(userId_does_not_exist.data) == Bad_request


def test_get_parcels_for_a_valid_user_who_has_no_orders(client):
    """When no orders exist for the specified userId"""
    response = client.get('/api/v1/users/3/parcels')
    assert response.status_code == 404
    assert json.loads(response.data) == Not_found


def test_get_parcels_for_a_valid_user_who_has_atleast_one_order(client):
    """ When userId is valid
        Then System should return the parcels with specified userId"""
    response = client.get('/api/v1/users/1/parcels')
    assert response.status_code == 200
    assert json.loads(response.data) =={'parcels':[
        parcel.parcel_details() for parcel in parcelOrders if parcel.ownerId == 1]}

    assert json.loads(response.data) != {'parcels': [
        parcel.parcel_details() for parcel in parcelOrders if parcel.ownerId == 2]}