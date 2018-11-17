# test/test_cancel_a_delivery_order.py

"""Test Module for cancel  a specific parcel delivery order endpoint"""
from flask import json

from app.responses import (
    Bad_request

)


def test_get_cancel_a_parcel_with_invalid_parcel_id(client):
    # parcelId is an integer but does not exixt
    with client.put('/api/v1/parcels/78/cancel') as parcelId_out_of_bounds:
        """When id  is of type int but does not exist in the parcels
        Then system returns an HTTP Error code of 400"""
        assert parcelId_out_of_bounds.status_code == 400
        assert json.loads(parcelId_out_of_bounds.data) == Bad_request

    # parcelId is not off type integer
    with client.put('/api/v1/parcels/7uf/cancel') as parcelId_not_an_integer:
        """When an id that is not of type int is provided
        Then system returns an HTTP Error code of 400"""
        assert parcelId_not_an_integer.status_code == 400
        assert json.loads(parcelId_not_an_integer.data) == Bad_request


def test_cancel_a_parcel_delivery_order_with_valid_parcelId(client):
    """Tests diffent Scenarios when Id is valid against the parcel's status"""
    # Pending
    with client.put('/api/v1/parcels/1/cancel') as status_pending:
        """When parcel has a status of pending
        Then asset is modified
        And System returns its details are returned
         """
        assert status_pending.status_code == 200
        assert json.loads(status_pending.data.decode()) == {
            "parcel": {
                "Item": "item",
                "destination": "Destination Address",
                "id": 1,
                "ownerId": "user1",
                "pickUp": "pickUp Address",
                "status": "Cancelled"
            }
        }

    #         In transit
    with client.put('/api/v1/parcels/3/cancel') as status_in_transit:
        """When parcel has a status of In Transit
        Then asset is not modified"""
        assert status_in_transit.status_code == 304

    #          Delivered
    with client.put('/api/v1/parcels/4/cancel') as status_delivered:
        """When parcel has a status of Delivered
             Then asset is not modified"""
        assert status_delivered.status_code == 304
