# test factory
from flask import json
from app import PARCELS


def test_get_helloworld(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"SendIT is a courier service that\
         helps users deliver parcels to different destinations"
    assert response.status_code != 201


def test_get_parcels(client):
    with client.get('/api/v1/parcels') as response:
        assert response.status_code == 200
        data = json.loads(response.data.decode())
        assert isinstance(data, dict)

        # Parcels are list of dictionaries
        assert isinstance(data['parcels'], list)

        # A single parcel is of Type dictionary
        assert isinstance(data['parcels'][0], dict)

        assert data['parcels'][0] == PARCELS[0]
        assert data['parcels'][1] != PARCELS[0]

        assert data['parcels'][1] == PARCELS[1]

        assert data['parcels'][0] != PARCELS[1]
