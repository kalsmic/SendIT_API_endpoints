# test factory
from flask import jsonify, json
from app import create_app


def test_get_parcels(client):
    with client.get('/api/v1/parcels') as response:
        assert response.status_code == 200
        data = json.loads(response.data.decode())
        assert isinstance(data, dict)

        # Parcels are list of dictionaries
        assert isinstance(data['parcels'], list)

        # A single parcel is of Type dictionary
        assert isinstance(data['parcels'][0], dict)

        assert data['parcels'][0] == {
            'id': 1,
            'title': 'Laptop',
            'pickUp': 'kampala',
            'destination': 'Moroto',
            'status': 'Pending',
            'ownerid': 1
        }
        assert data['parcels'][1] != {
            'id': 1,
            'title': 'Laptop',
            'pickUp': 'kampala',
            'destination': 'Moroto',
            'status': 'Pending',
            'ownerid': 1
        }

        assert data['parcels'][1] == {
            'id': 2,
            'title': 'Office Cabin',
            'pickUp': 'Kole',
            'destination': 'Otuke',
            'status': 'In Transit',
            'ownerid': 2
        }

        assert data['parcels'][0] != {
            'id': 2,
            'title': 'Office Cabin',
            'pickUp': 'Kole',
            'destination': 'Otuke',
            'status': 'In Transit',
            'ownerid': 2
        }
