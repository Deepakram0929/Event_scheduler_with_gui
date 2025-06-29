import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_events(client):
    response = client.get('/events')
    assert response.status_code == 200

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Test Meeting",
        "description": "Test Description",
        "start_time": "2025-06-30 09:00",
        "end_time": "2025-06-30 10:00"
    })
    assert response.status_code == 201
    assert b'Event created successfully' in response.data
