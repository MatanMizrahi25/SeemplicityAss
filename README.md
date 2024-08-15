# SeemplicityAss

## Overview

SeemplicityAss is a Python Flask application designed for task management and data collection, featuring integration with GPT.
It employs a scalable architecture using a manager-worker design pattern and task queuing to efficiently handle complex and long-running tasks.

## Features

- Task management with status querying
- Scalable architecture for handling long and complex tasks
- Integration with GPT for information querying
- Data collection from GitLab repositories
- Extensible for adding new tasks

## Installation

### Prerequisites

- Python 3.12
- Docker and Docker Compose

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/SeemplicityAss.git
    cd SeemplicityAss
    ```

2. Create and activate a virtual environment:
    ```sh
    python3.12 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Local Setup

1. Start Redis server:
    ```sh
    redis-server
    ```

2. Start Celery worker:
    ```sh
    celery -A tasks worker --loglevel=info
    ```

3. Run the Flask application:
    ```sh
    flask run
    ```

### Docker Setup

1. Build Docker images:
    ```sh
    docker-compose build
    ```

2. Start the services:
    ```sh
    docker-compose up
    ```

### Endpoints

- Add Task: `POST /tasks`
- Query Task Status: `GET /tasks/<task_id>`
- Query GPT: `POST /tasks/query_gpt`
- GitLab Data Collection: `POST /tasks/gitlab_collect`

## Testing

1. Ensure the application is running.
2. Run tests using pytest:
    ```sh
    pytest
    ```



# SeemplicityAss
