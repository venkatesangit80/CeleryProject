import os
from celery import Celery
from time import sleep
import redis
from datetime import datetime
from hashicorp_poc import get_config_details

# Celery configuration
config_details = get_config_details()
password = config_details['password']
host = config_details['host']
port = config_details['port']
app = Celery('task_producer',
             broker=f'redis://:{password}@{host}:{port}/0',
             backend=f'redis://:{password}@{host}:{port}/0')

#Create a generic celery task to read the string method using exec and execute the method and return the result
@app.task(name='process_data_from_source')
def process_data_from_source(script_code, function_name, *args, **kwargs):
    redis_client = redis.Redis(host=host, port=port, password=password, db=0)
    local_dict = {}
    exec(script_code, globals(), local_dict)
    func = local_dict.get(function_name)
    if func:
        result = func(*args, **kwargs, config_details=config_details)
        redis_key = f"{function_name}_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        redis_client.set(redis_key, result)
        redis_client.expire(redis_key, 3600)
        print(f"Result for {function_name} is {result}")
        return result
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
