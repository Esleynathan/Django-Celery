from celery import Celery

app = Celery(broker='redis://127.0.0.1:6379/0')


@app.task
def exibir():
    return "teste"