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
app = Celery('task_producer.tasks')
app.config_from_object('celeryconfig')

#Create a generic celery task to read the string method using exec and execute the method and return the result
def process_data(script_code, function_name, *args, **kwargs):
    redis_client = redis.Redis(host=host, port=port, password=password, db=0)
    local_dict = {}
    exec(script_code, globals(), local_dict)
    func = local_dict.get(function_name)
    if func is None:
        raise ValueError(f"Function {function_name} not found in the script")
    result = func(*args, **kwargs, config_details=config_details)
    redis_key = f"{function_name}_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    redis_client.set(redis_key, result)
    redis_client.expire(redis_key, 3600)
    print(f"Result for {function_name} is {result}")
    return result

@app.task(bind=True, name='process_data_from_source_high_priority', max_retries=3, acks_late=True)
def process_data_from_source_high_priority(self, script_code, function_name, *args, **kwargs):
    try:
        result = process_data(script_code, function_name, *args, **kwargs)
        return result
    except ValueError as ve:
        print(f"ValueError in {function_name} is {ve}")
        raise ve
    except Exception as e:
        print(f"Exception in {function_name} is {e}")
        self.retry(countdown=60, exc=e)

@app.task(bind=True, name='process_data_from_source_low_priority', max_retries=3, acks_late=True)
def process_data_from_source_low_priority(self, script_code, function_name, *args, **kwargs):
    try:
        result = process_data(script_code, function_name, *args, **kwargs)
        return result
    except ValueError as ve:
        print(f"ValueError in {function_name} is {ve}")
        raise ve
    except Exception as e:
        print(f"Exception in {function_name} is {e}")
        self.retry(countdown=60, exc=e)

@app.task(bind=True, name='process_data_from_source_normal', max_retries=3, acks_late=True)
def process_data_from_source_normal(self, script_code, function_name, *args, **kwargs):
    try:
        result = process_data(script_code, function_name, *args, **kwargs)
        return result
    except ValueError as ve:
        print(f"ValueError in {function_name} is {ve}")
        raise ve
    except Exception as e:
        print(f"Exception in {function_name} is {e}")
        self.retry(countdown=60, exc=e)

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
