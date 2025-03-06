# tests/test_app.py
import pytest
from app import app  # Assuming your Flask app is in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI Chat Interface" in response.data  # Adjust based on your app's output

def test_model(client):
    response = client.post('/chat', json={'message': 'Hi'})
    assert response.status_code == 200
    assert 'response' in response.json  # Adjust based on your API's response format
