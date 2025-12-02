import pytest
import json
from app import app, load_drugs

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

def test_about_route(client):
    """About route should return status code 200"""
    response = client.get("/about")
    assert response.status_code == 200

def test_drugs_route_no_query(client):
    """Drugs route without query should return status code 200"""
    response = client.get("/drugs")
    assert response.status_code == 200

def test_drugs_route_with_query(client):
    """Drugs route with query should handle case-insensitive search"""
    response = client.get("/drugs?query=paracetamol")
    assert response.status_code == 200

def test_chat_route(client):
    """Chat route should return status code 200"""
    response = client.get("/chat")
    assert response.status_code == 200

def test_chat_api_invalid_request(client):
    """Chat API should handle invalid requests"""
    response = client.post("/api/chat", data="invalid")
    assert response.status_code == 400
    
def test_chat_api_empty_message(client):
    """Chat API should handle empty messages"""
    response = client.post("/api/chat", 
                         json={"message": ""},
                         content_type='application/json')
    assert response.status_code == 400

def test_chat_api_valid_message(client):
    """Chat API should handle valid messages"""
    response = client.post("/api/chat", 
                         json={"message": "Hello"},
                         content_type='application/json')
    assert response.status_code == 200
    assert "reply" in json.loads(response.data)

def test_load_drugs_empty_file(tmp_path):
    """load_drugs should handle empty file"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("")
    app.config["DRUGS_FILE"] = str(empty_file)
    assert load_drugs() == []

def test_load_drugs_invalid_json(tmp_path):
    """load_drugs should handle invalid JSON"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("invalid json")
    app.config["DRUGS_FILE"] = str(invalid_file)
    assert load_drugs() == []
