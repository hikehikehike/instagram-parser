import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope='module')
def client():
    with TestClient(app) as client:
        yield client


def test_parse_posts(client):
    response = client.get('/parse_posts')
    response2 = client.get('/')

    assert response.status_code == 200, 'Expected status code 200'

    posts = response.json()['posts']
    posts2 = response2.json()['posts']

    assert len(posts2) == 10, f'{len(posts2)} Expected 10 posts, but got {len(posts2)}'
    assert len(posts) == 10, f'{len(posts)} Expected 10 posts, but got {len(posts)}'
