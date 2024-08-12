broker_url = 'amqp://rmuser:rmpassword@localhost:5672/'
result_backend = 'rpc://rmuser:rmpassword@localhost:5672/'

timezone = 'Europe/Moscow'
broker_connection_retry_on_startup = True
include = ['src.app_celery.tasks']

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'src.app_celery.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}


# celery -A src.app_celery.celery worker -l INFO
# celery -A src.app_celery.celery beat -s ~/PycharmProjects/lessons/Sky_pro_homeworks/without_correlation/
