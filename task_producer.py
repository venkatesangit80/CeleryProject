import os
from celery import Celery
from time import sleep

# Celery configuration
app = Celery('task_producer', broker='redis://localhost:6379', backend='redis://localhost:6379')
#app = Celery('task_producer')
#app.config_from_object('celeryconfig')


# Is celeryconfig a python file? If so, what is the content of the file?
# The content of the file is:
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True
# task_track_started = True
# task_time_limit = 300
# task_soft_time_limit = 60
# task_acks_late = True
# task_reject_on_worker_lost = True
# task_ignore_result = False
# task_store_errors_even_if_ignored = True
# task_publish_retry = True
# task_publish_retry_policy = {
#     'max_retries': 3,
#     'interval_start': 0,
#     'interval_step': 0.2,
#     'interval_max': 0.2,
# }
# task_default_queue = 'default'
# task_default_exchange = 'default'
# task_default_routing_key = 'default'
# task_default_exchange_type = 'direct'
# task_default_delivery_mode = 2
# task_default_priority = 0
# task_default_rate_limit = None
# task_default_acks_late = None
# task_default_time_limit = None
# task_default_soft_time_limit = None

@app.task(name='addition')
def add(x, y):
    print("Execution Started")
    sleep(20)  # Simulate a long computation
    return x + y

@app.task(name='subtraction')
def subtract(x, y):
    print("Execution Started")
    sleep(20)
    return x - y

@app.task(name='multiplication')
def multiply(x, y):
    print("Execution Started")
    sleep(20)
    return x * y

@app.task(name='division')
def divide(x, y):
    print("Execution Started")
    sleep(20)
    return x / y