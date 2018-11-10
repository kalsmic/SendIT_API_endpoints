# test factory
from app import create_app


def test_get_helloworld(client):
    response = client.get('/')
    assert response.status_code == 200
