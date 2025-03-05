# tests/test_app.py
import pytest
import sys
import os
# Add the app directory to the Python path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from app import app  # Assuming your Flask app is in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data  # Adjust based on your app's output

def test_model(client):
    response = client.post('/chat', json={'message': 'Hi'})
    assert response.status_code == 200
    assert 'response' in response.json  # Adjust based on your API's response format
