from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lifebook.settings')

app = Celery('lifebook')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-daily-reminder': {
        'task': 'diary.tasks.send_reminder',
        'schedule': crontab(hour=8, minute=0),
        'args': (1,),  # Replace with dynamic user ID
    },
}