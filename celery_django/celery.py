import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')


app = Celery('celery_django')
app.conf.enable_utc = False
app.conf.update(timezone = "Ameica/Sao_Paulo")

app.config_from_object('django.conf.settings', namespace='CELERY')

# Celery beat config
app.conf.beat_schedule = {
    'atualiza-banco-todos-dias-00:00':{
        'task': 'exemplo.tasks.atualiza_banco',
        'schedule': crontab()
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
