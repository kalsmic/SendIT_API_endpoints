# test factory
"""File contains test for checking whether app runs well"""


def test_index(client):
    """Tests the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"SendIT is a courier service that helps users\
         deliver parcels to different destinations"
