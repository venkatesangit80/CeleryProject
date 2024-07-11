Design Documentation for Celery-Redis Based Task Processing Platform

Overview

This document outlines the design and architecture of a task processing platform powered by Celery and Redis. The platform is designed to execute tasks dynamically by taking module content as a string and method name as parameters. Configuration and sensitive information are securely managed using Vault. Results are temporarily stored in Redis, enabling chaining multiple workflows as required.

System Architecture

	1.	Celery Task Queue
	•	Purpose: Distribute tasks across multiple workers for parallel execution.
	•	Components:
	•	Workers: Processes that execute tasks.
	•	Brokers: Redis acts as the broker to queue the tasks.
	2.	Redis
	•	Purpose: Acts as the message broker and result backend.
	•	Configuration:
	•	Data stored with a key format of function_name_time_value.
	•	Data TTL (Time to Live) set to 5 minutes for consumption.
	3.	Vault
	•	Purpose: Securely stores and manages configuration and sensitive information.
	•	Usage: Provides necessary configuration details and credentials to the platform.
	4.	API Layer
	•	Purpose: Interface for retrieving task results from Redis.
	•	Endpoints:
	•	/get-result: Fetches the result from Redis using the specified key.
	5.	Flower
	•	Purpose: Real-time monitoring and administration tool for Celery.
	•	Features:
	•	Monitoring task progress and history.
	•	Managing worker status and performance.
	•	Viewing task events and logs.

Workflow

	1.	Task Submission
	•	The consumer submits a task containing module content (in string format) and the method name.
	•	Sensitive information and configuration details are fetched from Vault.
	•	The task is enqueued into Celery with the required parameters.
	2.	Task Execution
	•	Celery workers fetch tasks from the Redis broker.
	•	Workers dynamically execute the method specified in the task.
	•	The method’s output is stored in Redis with the key function_name_time_value.
	3.	Result Storage
	•	Results are stored in Redis with a TTL of 5 minutes.
	•	Key format ensures uniqueness and easy retrieval.
	4.	Result Retrieval
	•	Consumers can retrieve results via an API call.
	•	The API layer interfaces with Redis to fetch and return the results based on the key.
	5.	Monitoring with Flower
	•	Flower is used to monitor the health and performance of Celery tasks and workers in real-time.
	•	It provides a web-based interface to manage and inspect tasks, track progress, and diagnose issues.

Configuration and Deployment

	1.	Celery Configuration
	•	BROKER_URL and RESULT_BACKEND set to Redis.
	•	task_serializer, result_serializer, and accept_content configured for optimal performance.
	2.	Redis Configuration
	•	Configured to handle both task queuing and result storage.
	•	Ensures data persistence and eviction policies are set appropriately.
	3.	Vault Configuration
	•	Policies and access controls defined to secure sensitive information.
	•	Dynamic secrets and leasing managed for configuration data.
	4.	API Server
	•	Flask or FastAPI can be used to implement the API layer.
	•	API endpoints defined to interact with Redis for result retrieval.
	5.	Flower Configuration
	•	Flower can be set up and configured to monitor the Celery workers.
	•	Accessible via a web interface for real-time monitoring.

Security Considerations

	1.	Vault
	•	Ensure secure access to Vault with role-based access control (RBAC).
	•	Regularly rotate secrets and use short-lived tokens.
	2.	Redis
	•	Use secure connections (TLS) to communicate with Redis.
	•	Implement authentication mechanisms to prevent unauthorized access.
	3.	API
	•	Implement authentication and authorization for API access.
	•	Rate limiting to prevent abuse.

Monitoring and Logging

	1.	Celery
	•	Monitor task execution and worker health using Flower.
	•	Log task submissions, executions, and failures.
	2.	Redis
	•	Monitor key expiration and storage metrics.
	•	Log access and error events.
	3.	Vault
	•	Monitor access patterns and audit logs.
	•	Ensure compliance with security policies.
	4.	API Layer
	•	Monitor API usage and performance metrics.
	•	Log request and response data for troubleshooting.
	5.	Flower
	•	Use Flower’s web interface for real-time monitoring of tasks and workers.
	•	Track task progress, view history, and manage worker statuses.

Extensibility

	1.	Workflow Chaining
	•	Consumers can chain multiple tasks by defining workflows.
	•	Each task’s result can be used as input for subsequent tasks.
	2.	Modular Design
	•	Platform designed to be extended with new tasks and methods.
	•	Easy integration with other services and workflows.

Conclusion

This design provides a robust and scalable platform for dynamic task execution with Celery and Redis, ensuring secure management of sensitive information through Vault. The inclusion of Flower for real-time monitoring enhances the platform’s observability and management capabilities, supporting flexible workflow chaining and making it adaptable to various use cases.

Feel free to reach out for any additional details or specific queries regarding this design.