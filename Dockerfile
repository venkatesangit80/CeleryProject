FROM python:3.9-slim
LABEL authors="venkatesansubramanian"

ENTRYPOINT ["top", "-b"]

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV hcp_id=
ENV hcp_value=

CMD ["celery", "-A", "task_producer.tasks", "worker", "--loglevel=info", "-n", "worker1", "--concurrency=4"]