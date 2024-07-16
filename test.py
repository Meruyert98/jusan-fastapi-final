from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_reverse():
    headers = {"string": "hello"}
    response = client.post("/reverse", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_add_to_list():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_get_list():
    client.put("/list", json={"element": "Apple"})  # Ensure list is not empty
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_calculator():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculator_invalid_format():
    response = client.post("/calculator", json={"expr": "1+1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "invalid"}

def test_calculator_zero_division():
    response = client.post("/calculator", json={"expr": "1,/,0"})
    assert response.status_code == 403
    assert response.json() == {"detail": "zerodiv"}