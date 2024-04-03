# Celery POC Project

Celery Project is a POC project to demonstrate how to use Celery with Python Script to create a simple task queue. Redis is used as the message broker and the result backend.

## Installation 

To install the necessary dependencies, run the following command:
    
```bash
pip install -r requirements.txt
```


### Prerequisites

What things you need to install the software and how to install them
- 
- Python 3.8 or higher
- Redis
- Celery

### Example

To run the example, first start the redis server:
```bash
redis-server
```

Then, start the Celery worker:
```bash
celery -A tasks worker --loglevel=info
```

Finally, run the example script:
```bash
python task_executor.py
```
