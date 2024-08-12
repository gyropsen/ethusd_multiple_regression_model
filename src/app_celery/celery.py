from celery import Celery

from src.app_celery import celeryconfig

app = Celery("app_celery")
app.config_from_object(celeryconfig)

if __name__ == "__main__":
    app.start()
