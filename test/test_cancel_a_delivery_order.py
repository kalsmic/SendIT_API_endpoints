
# test_cancel_a_parcel.py

"""Test Module for GET a specific parcel endpoint"""
from flask import json

from app.http_responses import (
    Bad_request,
Not_modified

)

def test_get_cancel_a_parcel_with_invalid_parcel_id(client):
    # parcelId is an integer but does not exixt
    with client.put('/api/v1/parcels/78/cancel') as parcelId_out_of_bounds:
        assert parcelId_out_of_bounds.status_code == 400
        assert json.loads(parcelId_out_of_bounds.data) == Bad_request

    # parcelId is not off type integer
    with client.put('/api/v1/parcels/7uf/cancel') as parcelId_not_an_integer:
        assert parcelId_not_an_integer.status_code == 400
        assert json.loads(parcelId_not_an_integer.data) == Bad_request



def test_cancel_a_parcel_delivery_order_with_valid_parcelId(client):

     # Pending
    with client.put('/api/v1/parcels/1/cancel') as status_pending:
        assert status_pending.status_code == 204



#     # In transit
    with client.put('/api/v1/parcels/2/cancel') as status_in_transit:
        assert status_in_transit.status_code == 304
        # assert json.loads(status_in_transit.data) == Not_modified
# #
#
#      # Delivered
    with client.put('/api/v1/parcels/3/cancel') as status_delivered:
        assert status_delivered.status_code == 304

