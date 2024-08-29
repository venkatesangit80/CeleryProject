FROM python:3.9-slim
LABEL authors="venkatesansubramanian"

ENTRYPOINT ["top", "-b"]

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV hcp_client_id=o4LHqADty1XZVANtTaHLxcxjCQrlha9Y
ENV hcp_secret=XqRJDnfJz2cpEK6lbveYwiNhYKWQgZ_tVyT4yuDFikNAUMHMoQcz11bkHgqYKB99

CMD ["celery", "-A", "task_producer.tasks", "worker", "--loglevel=info", "-n", "worker1", "--concurrency=4"]