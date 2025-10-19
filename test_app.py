import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route_status(client):
    """Home route should return status code 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_home_route_content(client):
    """Home route should contain specific content"""
    response = client.get("/")
    assert "Health+ The AI Symptom Checker" in response.data.decode()
