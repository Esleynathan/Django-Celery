from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')


@app.task(bind = True, max_retries=20, default_retry_delay=1)
def exibir(self):

    x = randint(1, 9)
    if x > 9:
        return x
    else:
        self.retry(countdown = 2**self.request.retries)
        raise ValueError('Error')