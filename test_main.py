from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World!'}

def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status' : 'healthy'}

def test_addition():
    response = client.get('/add/5/2')
    assert response.status_code == 200
    assert response.json() == {'result' : 7}