from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_audio():
    # Valid input: Testing the /generate-audio/ endpoint with sample story text
    response = client.post("/generate-audio/", json={"text": "Once upon a time in a faraway land..."})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "file_path" in response.json()


def test_invalid_input():
    # Invalid input: Testing the /generate-audio/ endpoint with missing text
    response = client.post("/generate-audio/", json={})
    assert response.status_code == 422  # Unprocessable Entity (validation error)
