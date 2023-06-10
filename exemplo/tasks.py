from celery import shared_task
from time import sleep
from . models import DataAtual
from datetime import datetime

@shared_task
def minha_tarefa():
    sleep(10)
    return 'teste'

@shared_task(bind=True)
def atualiza_banco(self):
    data_atual = DataAtual.objects.all().first()
    data_atual.data_atual = datetime.now()
    data_atual.save()

    return 'Done'