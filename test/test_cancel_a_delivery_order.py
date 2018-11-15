# from app import PARCELS
# from app.http_responses import (
#     Bad_request,
#     Not_found,
#     Not_modified
# )
#
# from flask import json
#
#
# def test_cancel_a_parcel_delivery_already_marked_as_delivered(client):
#     """ API Consumer cancels a parceld delivery order
#     whose status is already delivered or cancelled
#     An HTTP status code of 304 is rerturned """
#
#     with client.get('/api/v1/parcels/3/cancel') as marked_as_delivered:
#         marked_as_delivered.status_code == 304
#
#     with client.get('/api/v1/parcels/4/cancel') as already_cancelled:
#         already_cancelled.status_code == 304
#
#
# def test_cancel_a_parcel_delivery_already(client):
#     """Given an API consumer
#     When I submit a PUT to  /api/v1/parcels/<parcelId>
#     And the parcel delivery order is yet to be marked as delivered
#     Then the asset is status  updated
#     And the system returns An HTTP status code of 204 """
#
#     in_transit = client.get('/api/v1/parcels/1/cancel')
#     in_transit.status_code == 204
