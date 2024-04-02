from .task_producer import app as celery_app
__all__ = ('celery_app',)

# Start celery app
# celery -A task_producer worker --loglevel=info
# celery -A task_producer beat --loglevel=info

# Start flower
# celery -A task_producer flower --loglevel=info
# http://localhost:5555
# http://localhost:5555/dashboard
# http://localhost:5555/api/task/info
# http://localhost:5555/api/task/events
# http://localhost:5555/api/task/async-apply
# http://localhost:5555/api/task/async-apply/1
# http://localhost:5555/api/task/async-apply/1/result
# http://localhost:5555/api/task/async-apply/1/traceback
# http://localhost:5555/api/task/async-apply/1/retval
# http://localhost:5555/api/task/async-apply/1/ack
# http://localhost:5555/api/task/async-apply/1/nack
# http://localhost:5555/api/task/async-apply/1/reject
# http://localhost:5555/api/task/async-apply/1/revoke
# http://localhost:5555/api/task/async-apply/1/terminate
# http://localhost:5555/api/task/async-apply/1/kill
# http://localhost:5555/api/task/async-apply/1/timeout
# http://localhost:5555/api/task/async-apply/1/pending
# http://localhost:5555/api/task/async-apply/1/running
# http://localhost:5555/api/task/async-apply/1/failed
# http://localhost:5555/api/task/async-apply/1/succeeded
# http://localhost:5555/api/task/async-apply/1/revoked
# http://localhost:5555/api/task/async-apply/1/retried
# http://localhost:5555/api/task/async-apply/1/eta
# http://localhost:5555/api/task/async-apply/1/retry
# http://localhost:5555/api/task/async-apply/1/args
# http://localhost:5555/api/task/async-apply/1/kwargs
# http://localhost:5555/api/task/async-apply/1/result
# http://localhost:5555/api/task/async-apply/1/result/task_id
# http://localhost:5555/api/task/async-apply/1/result/task_name
# http://localhost:5555/api/task/async-apply/1/result/task_args
# http://localhost:5555/api/task/async-apply/1/result/task_kwargs
# http://localhost:5555/api/task/async-apply/1/result/task_result
# http://localhost:5555/api/task/async-apply/1/result/task_status
# http://localhost:5555/api/task/async-apply/1/result/task_timestamp
# http://localhost:5555/api/task/async-apply/1/result/task_runtime
# http://localhost:5555/api/task/async-apply/1/result/task_traceback
# http://localhost:5555/api/task/async-apply/1/result/task_exception
# http://localhost:5555/api/task/async-apply/1/result/task_worker
# http://localhost:5555/api/task/async-apply/1/result/task_retries
# http://localhost:5555/api/task/async-apply/1/result/task_retries_max
# http://localhost:5555/api/task/async-apply/1/result/task_retries_current
# http://localhost:5555/api/task/async-apply/1/result/task_retries_remaining
# http://localhost:5555/api/task/async-apply/1/result/task_retries_delta
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_current
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_max
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_delta
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_step
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_start
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_end
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_remaining
# http://localhost:5555/api/task/async-apply/1/result/task_retries_interval_elapsed


# Start celery app with beat
# celery -A task_producer worker --loglevel=info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile=celerybeat.pid --logfile=celerybeat.log --detach --uid=1000 --gid=1000 --umask=0022 --workdir=/home/developer/PycharmProjects/CeleryProject --pidfile=celerybeat.pid --logfile=celerybeat.log



# Start celery app with beat and flower
# celery -A task_producer worker --loglevel=info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile=celerybeat.pid --logfile=celerybeat.log --detach --uid=1000 --gid=1000 --umask=0022 --workdir=/home/developer/PycharmProjects/CeleryProject --pidfile=celerybeat.pid --logfile=celerybeat.log
# celery -A task_producer flower --loglevel=info --detach --uid=1000 --gid=1000 --umask=0022 --workdir=/home/developer/PycharmProjects/CeleryProject --pidfile=flower.pid --logfile=flower.log

# Setup Auto-Reload
# pip install watchdog
# celery -A task_producer worker --loglevel=info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile=celerybeat.pid --logfile=celerybeat.log --detach --uid=1000 --gid=1000 --umask=0022 --workdir=/home/developer/PycharmProjects/CeleryProject --pidfile=celerybeat.pid --logfile=celerybeat.log --autoreload --autoreload-ignore celerybeat.pid --autoreload-ignore celerybeat.log
# celery -A task_producer flower --loglevel=info --detach --uid=1000 --gid=1000 --umask=0022 --workdir=/home/developer/PycharmProjects/CeleryProject --pidfile=flower.pid --logfile=flower.log --autoreload --autoreload-ignore flower.pid --autoreload-ignore flower.log
