# celeryconfig.py

from kombu import Exchange, Queue
from hashicorp_poc import get_config_details

# Celery configuration
config_details = get_config_details()
password = config_details['password']
host = config_details['host']
port = config_details['port']

# Define task queues
task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('high_priority', Exchange('high_priority'), routing_key='high_priority'),
    Queue('low_priority', Exchange('low_priority'), routing_key='low_priority'),
)

# Define task routes
task_routes = {
    'task_procedure.tasks.process_data_from_source_high_priority': {'queue': 'high_priority'},
    'task_procedure.tasks.process_data_from_source_low_priority': {'queue': 'low_priority'},
    'task_procedure.tasks.process_data_from_source_default': {'queue': 'default'},
}

broker_url = f'redis://:{password}@{host}:{port}/0'
result_backend = f'redis://:{password}@{host}:{port}/0'

# Additional Celery configuration
task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'
task_acks_late = True
worker_concurrency = 4