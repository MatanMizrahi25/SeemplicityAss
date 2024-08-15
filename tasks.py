from celery import Celery
import redis

app = Celery('tasks', broker='redis://localhost:6379/0')
result_store = redis.StrictRedis(host='localhost', port=6379, db=1)

@app.task
def run_task(task_id, task_name, task_params):
    if task_name == "sum":
        result = sum(task_params)
    elif task_name == "query_gpt":
        result = query_gpt(task_params)
    elif task_name == "custom_task":
        result = custom_task(task_params)
    else:
        result = "Unknown task"
    result_store.set(task_id, result)

def get_task_result(task_id):
    return result_store.get(task_id).decode("utf-8")

def query_gpt(params):
    return "GPT-3 response"
    ##pass

def custom_task(params):
    return "Custom task result"
    ##pass
