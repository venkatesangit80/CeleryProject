import os
from celery import Celery
from time import sleep

# Celery configuration
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')
app = Celery('task_producer',
             broker=f'redis://:{password}@{host}:{port}/0',
             backend=f'redis://:{password}@{host}:{port}/0')

#Create a generic celery task to read the string method using exec and execute the method and return the result
@app.task(name='process_data_from_source')
def process_data_from_source(script_code, function_name, *args, **kwargs):
    local_dict = {}
    exec(script_code, globals(), local_dict)
    func = local_dict.get(function_name)
    if func:
        return func(*args, **kwargs)
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
