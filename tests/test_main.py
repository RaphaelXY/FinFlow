from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "password": "123456"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_transaction():
    response = client.post("/transactions/", json={
        "amount": 150.0,
        "type": "income",
        "description": "freelance"
    })
    assert response.status_code == 200
    assert response.json()["amount"] == 150.0