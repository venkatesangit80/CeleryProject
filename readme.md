1. Celery Broker which is Enterprise Redis

The Celery Broker, powered by Enterprise Redis, serves as the message queue that enables the communication between different components of the platform. Redis, known for its speed and reliability, efficiently manages the distribution of tasks to Celery workers. In this setup, Redis ensures that tasks are queued, processed, and handled in a highly performant manner, supporting the platform’s scalability and robustness.

2. Celery Worker deployed in PCF

Celery Workers, deployed in Pivotal Cloud Foundry (PCF), execute the tasks assigned by the Celery Broker. PCF provides a scalable and managed environment for deploying and running these workers, ensuring they can handle varying workloads efficiently. The deployment in PCF allows for seamless scaling, fault tolerance, and easier management of the Celery workers, ensuring consistent task processing capabilities.

3. Celery Worker gets task as script as parameter, function name, and parameter for the task as another parameter. Return JSON value.

Each Celery Worker receives tasks in the form of a script, a function name, and corresponding parameters. The worker executes the given function with the provided parameters and returns the output as a JSON value. This dynamic task execution model allows for flexibility in processing various types of tasks, ensuring that different functions can be executed without modifying the worker codebase.

4. Save the JSON to Enterprise Redis as temp value and key as function name with unique value as key.

The JSON output from the Celery Worker is temporarily stored in Enterprise Redis. The key for this stored value is a combination of the function name and a unique identifier, ensuring each result can be uniquely accessed. This temporary storage mechanism in Redis allows for quick and efficient retrieval of task results, supporting real-time data access needs.

5. Metric retriever is a FastAPI that gets all the value list for the given function name.

The Metric Retriever, built using FastAPI, provides an interface to fetch all the values associated with a given function name from Redis. FastAPI, known for its speed and ease of use, ensures that the retrieval of these metrics is fast and efficient. This component is crucial for aggregating and presenting the processed data, enabling users to access the results of their tasks in a structured and timely manner.

6. Flower monitor deployed in PCF with PingFed authentication

The Flower Monitor, deployed in PCF, provides real-time monitoring of Celery workers and tasks. It uses PingFederate (PingFed) for authentication, ensuring secure access to the monitoring dashboard. This setup allows operators to track the performance and status of tasks, manage worker nodes, and troubleshoot issues in a secure and controlled environment.