import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app

client = TestClient(app)

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    response = client.post("/items/", json={"id": "1", "name": "Item 1"})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"id": "1", "name": "Item 1"}

def test_create_item_invalid():
    response = client.post("/items/", json={"id": "1"})
    assert response.status_code == 422

def test_get_items_filled():
    response = client.get("/items/")
    assert response.status_code == 200
    print("reponse = ", response.json())
    assert response.json() == [{'id': '1', 'name': 'Item 1'}]

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": "1", "name": "Item 1"}

def test_delete_item_not_found():
    response = client.delete("/items/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
