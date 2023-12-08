from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json == "Welcome to the grocery database service!"

def test_get_coffee_info():
    resp = client.get("/coffee")
    assert resp.status_code == 200

def test_get_count():
    resp = client.get("/product_count")
    assert resp.status_code == 200