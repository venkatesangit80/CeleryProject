from time import sleep
from celery import shared_task

def add(x, y):
    sleep(20)  # Simulate a long computation
    return x + y