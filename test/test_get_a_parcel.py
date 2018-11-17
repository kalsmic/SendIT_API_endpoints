# test_get__a_parcel.py

"""Test Module for GET a specific parcel endpoint"""
from flask import json

from app.models.parcel import parcelOrders
from app.responses import (
    Bad_request
)


def test_get_a_parcel_with_invalid_parcel_id(client):
    """When an invalid parcel Id is provided"""


    with client.get('/api/v1/parcels/0') as parcelId_out_of_bounds:
        """Id is a number and does not exist in the parcels
           Then system returns the specific parcel and a status code of 400"""
        assert parcelId_out_of_bounds.status_code == 400
        assert json.loads(parcelId_out_of_bounds.data) == Bad_request

    with client.get('/api/v1/parcels/7uf') as parcelId_not_an_integer:
        """parcelId is not a number
                   Then system returns the specific parcel and a status code of 400"""
        assert parcelId_not_an_integer.status_code == 400
        assert json.loads(parcelId_not_an_integer.data) == Bad_request


def test_get_a_parcel_with_parcelId_which_exists_and_is_valid(client):
    """Given a valid parcel Id
        Then system returns the specific parcel and a status code of 200"""
    response = client.get('/api/v1/parcels/1')
    assert response.status_code == 200

    data = json.loads(response.data.decode())

    assert data['parcel'] == parcelOrders[0].parcel_details()
