import unittest
from unittest.mock import patch, MagicMock
from tasks import get_configuration, get_weather
from celery import Celery

# Ensure Celery runs tasks locally during testing (eager mode)
app = Celery()
app.conf.update(
    task_always_eager=True,  # Run tasks synchronously
    task_eager_propagates=True,  # Raise exceptions if they occur
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)

class TestTasks(unittest.TestCase):

    @patch('tasks.get_config_details')
    def test_get_configuration(self, mock_get_config_details):
        # Mock the return value of get_config_details
        mock_get_config_details.return_value = {
            'password': 'fake_password',
            'host': 'localhost',
            'port': 6379,
            'weatherkey': 'fake_weather_key'
        }
        # Test get_configuration logic
        password, host, port, config_details = get_configuration()
        self.assertEqual(password, 'fake_password')
        self.assertEqual(host, 'localhost')
        self.assertEqual(port, 6379)
        self.assertEqual(config_details['weatherkey'], 'fake_weather_key')

    @patch('tasks.requests.get')
    @patch('tasks.redis.Redis')
    @patch('tasks.get_configuration')
    def test_get_weather(self, mock_get_configuration, mock_redis, mock_requests):
        # Mock configuration details
        mock_get_configuration.return_value = ('fake_password', 'localhost', 6379, {'weatherkey': 'fake_weather_key'})

        # Mock Redis
        mock_redis_instance = mock_redis.return_value
        mock_redis_instance.set = MagicMock()

        # Mock API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'cod': 200,
            'main': {'temp': 300.15},
            'weather': [{'description': 'clear sky'}]
        }
        mock_requests.return_value = mock_response

        # Call the task and verify the response
        result = get_weather('London')
        self.assertIn('temperature', result)
        self.assertIn('description', result)
        self.assertIn('city', result)


if __name__ == '__main__':
    unittest.main()