# test_get_parcels.py

"""Test Module for GET parcels endpoint"""
from flask import json

from app.models.parcel import parcelOrders


def test_get_parcels(client):
    with client.get('/api/v1/parcels') as response:
        assert response.status_code == 200
        data = json.loads(response.data.decode())
        assert isinstance(data, dict)

        # Parcels are list of dictionaries
        assert isinstance(data['parcels'], list)

        # A single parcel is of Type dictionary
        assert isinstance(data['parcels'][0], dict)

        # Check if parcels the parcels returned match

        assert data['parcels'][0] == parcelOrders[0].parcel_details()
        assert data['parcels'][0] != parcelOrders[1].parcel_details()

        # Check if the number of parcels returned matched the number of parcels available
        assert len(data['parcels']) == len(parcelOrders)
