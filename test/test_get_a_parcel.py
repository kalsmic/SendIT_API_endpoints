# test_get__a_parcel.py

"""Test Module for GET a specific parcel endpoint"""
from flask import json

from app.http_responses import (
    Not_found,
    Bad_request
)
from app.models.parcel.parcel import get_parcel_by_id


def test_get_a_parcel_with_invalid_parcel_id(client):

    with client.get('/api/v1/parcels/90') as parcelId_out_of_bounds:
        assert parcelId_out_of_bounds.status_code == 404
        assert json.loads(parcelId_out_of_bounds.data) == Not_found

    with client.get('/api/v1/parcels/7uf') as parcelId_not_an_integer:
        assert parcelId_not_an_integer.status_code == 400
        assert json.loads(parcelId_not_an_integer.data) == Bad_request


def test_get_a_parcel_with_parcelId_which_exists_and_is_valid(client):
    response = client.get('/api/v1/parcels/1')
    assert response.status_code == 200
    data = json.loads(response.data.decode())

    assert data['parcel'] == get_parcel_by_id(1)
