# test factory
from app import create_app


def test_get_helloworld(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Test run to configure Travis CI"
    assert response.status_code != 201
