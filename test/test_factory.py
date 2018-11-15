# # test factory
# from flask import json,url_for
# from app import PARCELS


# def test_get_helloworld(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.data == b"SendIT is a courier service that helps users\
#          deliver parcels to different destinations"
#     assert response.status_code != 201

# def test_get_parcels(client):
#     with client.get(url_for('parcels')) as response:
#         assert response.status_code == 200
