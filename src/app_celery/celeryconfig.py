from celery.schedules import crontab
from src.config import config

broker_url = config.rabbitmq.rabbitmq_url
# result_backend = config.rabbitmq.rabbitmq_url

timezone = 'UTC'
broker_connection_retry_on_startup = True
include = ['src.app_celery.tasks']

beat_schedule = {
    'update-model-every-day': {
        'task': 'src.app_celery.tasks.periodic_update_data',
        'schedule': crontab(hour="0", minute="0"),
    },
    # '': {}
}

# celery -A src.app_celery.celery worker -l INFO
# celery -A src.app_celery.celery beat -s ~/PycharmProjects/lessons/Sky_pro_homeworks/without_correlation/
