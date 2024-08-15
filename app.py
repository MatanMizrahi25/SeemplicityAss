from flask import Flask, request, jsonify
from celery.result import AsyncResult
from celery_config import make_celery

# Initialize the Flask app
app = Flask(__name__)

# Configuration for Celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

# Initialize Celery
celery = make_celery(app)

# Define a sample task (sum two numbers)
@celery.task(name='tasks.sum_task')
def sum_task(a, b):
    return a + b


@app.route('/')
def index():
    return "Task Runner Service is up and running!"


@app.route('/run_task', methods=['POST'])
def run_task():
    data = request.get_json()
    print("Received data:", data)  # For debugging
    if not data or 'task_name' not in data or 'task_params' not in data:
        return jsonify({"error": "Invalid input"}), 400

    task_name = data['task_name']
    task_params = data['task_params']

    if task_name == "sum":
        task = sum_task.apply_async(args=task_params)
    else:
        return jsonify({"error": "Unknown task name"}), 400

    return jsonify({'task_id': task.id})


@app.route('/task_output/<task_id>', methods=['GET'])
def get_task_output(task_id):
    task = AsyncResult(task_id)
    if task.ready():
        result = task.result
        return jsonify({'task_id': task_id, 'result': result})
    else:
        return jsonify({'task_id': task_id, 'result': 'Task not ready'}), 202

if __name__ == '__main__':
    app.run(debug=True)
