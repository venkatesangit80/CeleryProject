Guide to Maintain the Platform

This guide outlines how to use Flower to monitor the performance of tasks and workers, identify crashed Celery workers, and restart them in a PCF environment.

1. Using Flower to Monitor Tasks and Workers

Flower provides a web-based tool for monitoring and administrating Celery clusters.

	1.	Access Flower Dashboard:
	•	Navigate to the Flower web interface using the provided URL and login using your PingFed authentication.
	2.	Dashboard Overview:
	•	The main dashboard shows an overview of active workers, task history, and real-time task progress.
	3.	Monitoring Tasks:
	•	Navigate to the “Tasks” tab to view detailed information about tasks, including status, arguments, results, start time, and runtime.
	•	Use filters to find specific tasks by state (e.g., STARTED, SUCCESS, FAILURE).
	4.	Monitoring Workers:
	•	Go to the “Workers” tab to see the list of active workers.
	•	View the state of each worker (e.g., ONLINE, OFFLINE), the number of tasks processed, and the worker’s last heartbeat.

2. Identifying a Crashed Celery Worker

	1.	Worker Status:
	•	In the “Workers” tab, look for workers with the status “OFFLINE” or those that haven’t sent a heartbeat for a significant period.
	2.	Logs and Alerts:
	•	Check logs for error messages or alerts that indicate a worker has crashed.
	•	Use Flower’s real-time monitoring to spot anomalies in task execution times and worker availability.
	3.	Metrics Monitoring:
	•	Use the Metric Retriever (FastAPI) to fetch performance metrics and identify irregularities that may indicate a worker crash.

3. Restarting a Crashed Celery Worker in PCF

	1.	Access PCF CLI:
	•	Open your terminal and log in to PCF using the cf login command with your credentials.
	2.	List Applications:
	•	Run cf apps to list all deployed applications and locate the Celery worker application.
	3.	Restart Worker:
	•	Use the command cf restart <worker-app-name> to restart the specific Celery worker application.
	•	Replace <worker-app-name> with the actual name of your Celery worker application.
	4.	Verify Restart:
	•	Monitor the application logs with cf logs <worker-app-name> --recent to ensure the worker restarts correctly and begins processing tasks.
	•	Check the Flower dashboard to confirm the worker is back online and functioning properly.

Best Practices

	•	Regular Monitoring: Regularly check the Flower dashboard and PCF logs to catch issues early.
	•	Alerts: Set up alerts in Flower or an external monitoring tool to notify you of worker crashes or task failures.
	•	Scaling: Ensure you have sufficient worker instances running in PCF to handle peak loads and avoid overloading individual workers.
	•	Configuration Management: Use HashiCorp Vault for dynamic configuration management to update settings without needing to restart workers.

By following this guide, you can efficiently monitor, identify, and resolve issues with your Celery workers, ensuring smooth and reliable operation of your platform.