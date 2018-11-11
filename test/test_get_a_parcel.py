from flask import request, url_for, json
from app import PARCELS

Not_found = {"Error": "Not Found"}


def test_get_a_parcel_with_invalid_parcel_id(client):
    """Given an API Consumer
    When I submit a GET request to /parcels/<parcelId> endpoint
    And parcelId that does not exist in the parcel orders
    Then the system returns an HTTP status code of 404
    And a JSON representation of the error 'Not Found' """

    with client.get('/api/v1/parcels/7') as parcelId_out_of_bounds:
        assert parcelId_out_of_bounds.status_code == 404
        assert json.loads(parcelId_out_of_bounds.data) == Not_found

    with client.get('/api/v1/parcels/7uf') as parcelId_not_an_integer:
        assert parcelId_not_an_integer.status_code == 404
        assert json.loads(parcelId_not_an_integer.data) == Not_found


def test_get_a_parcel(client):
    # """Given an API Consumer
    # When I submit a GET request to /parcels/<parcelId> endpoint
    # And I have a valid parcel Id
    # Then the system should return
    # An HTTP status code of 200
    # A JSON representation of the parcel delivery order
    # that matches the parcelId """

    response = client.get('/api/v1/parcels/1')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['Parcel'] == {
        "DestinationAddress": "Moroto",
        "Item": "Laptop",
        "PickUpAddress": "kampala",
        "Status": "Pending",
        "id": 1,
        "ownerId": 1
    }
    assert data['Parcel'] != {
        "DestinationAddress": "Otuke",
        "Item": "Office Cabin",
        "PickUpAddress": "Kole",
        "Status": "In Transit",
        "id": 2,
        "ownerId": 2
    }
