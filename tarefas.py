from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')


@app.task(bind = True, max_retries=5, default_retry_delay=2, autoretry_for = (ZeroDivisionError, ValueError))
def exibir(self):

    x = randint(1, 9)
    if x > 7:
        return x
    else:
        raise ValueError('Error')