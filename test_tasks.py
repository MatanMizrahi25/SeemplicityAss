# test_tasks.py

import pytest
from celery.result import AsyncResult
from tasks import run_task, get_task_result

@pytest.fixture
def celery_app():
    from tasks import app
    app.conf.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )
    return app

@pytest.fixture
def celery_worker(celery_app, celery_worker):
    return celery_worker

def test_run_sum_task(celery_worker):
    task = run_task.apply_async(args=['sum', [1, 2]])
    result = AsyncResult(task.id)
    assert result.get(timeout=10) == 3

def test_query_gpt_task(celery_worker):
    task = run_task.apply_async(args=['query_gpt', ['example']])
    result = AsyncResult(task.id)
    assert result.get(timeout=10) == 'GPT-3 response'

def test_custom_task(celery_worker):
    task = run_task.apply_async(args=['custom_task', ['param']])
    result = AsyncResult(task.id)
    assert result.get(timeout=10) == 'Custom task result'
