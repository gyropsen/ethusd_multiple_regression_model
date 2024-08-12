from src.app_celery.celery import app


@app.task
async def get_model(arg):
    print(arg)


@app.task
async def add(x, y):
    z = x + y
    print(z)
