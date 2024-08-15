import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_run_task(client):
    rv = client.post('/run_task', json={'task_name': 'sum', 'task_params': [1, 2]})
    assert rv.status_code == 200
    response_data = rv.get_json()
    assert 'task_id' in response_data

def test_get_task_result(client):
    rv = client.post('/run_task', json={'task_name': 'sum', 'task_params': [1, 2]})
    task_id = rv.get_json().get('task_id')
    rv = client.get(f'/get_task_output/{task_id}')
    assert rv.status_code == 200
    response_data = rv.get_json()
    assert response_data.get('result') == 3
