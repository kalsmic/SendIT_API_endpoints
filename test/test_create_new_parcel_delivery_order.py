from app import PARCELS
from app.http_responses import (
    Bad_request,
    Not_found,
    Not_modified
)

from flask import json

missing_data = {
    "pickUp": "",
    "destination": "d",
    "Item": "fe",
    "ownerId": 1
}
complete_data = {
    "pickUp": "Jinja",
    "destination": "Mukono",
    "Item": "Text Books",
    "ownerId": 1
}
missing_data_response = {
    "message": "pickUp cannot be empty"
}
complete_data_response = {
    "newOrder": {
        "Item": "Text Books",
        "destination": "Mukono",
        "id": 5,
        "ownerId": 1,
        "pickUp": "Jinja",
        "status": "Pending"
    }
}


def test_create_a_parcel_delivery(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    with client.post('/api/v1/parcels', data=json.dumps(missing_data), headers=headers) as \
            create_order_with_missing_data:
        assert create_order_with_missing_data.content_type == mimetype
        assert create_order_with_missing_data.status_code == 400
        data = json.loads(create_order_with_missing_data.data.decode())
        assert data == missing_data_response

    with client.post('/api/v1/parcels', data=json.dumps(complete_data), headers=headers) as \
            create_order_with_complete_data:
        assert create_order_with_complete_data.content_type == mimetype
        assert create_order_with_complete_data.status_code == 201
        data = json.loads(create_order_with_complete_data.data.decode())
        assert data == complete_data_response
