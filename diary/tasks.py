from celery import shared_task
from django.contrib.auth.models import User
from .utils import send_notification  # Assume you have a function for sending notifications

@shared_task
def send_reminder(user_id):
    user = User.objects.get(id=user_id)
    send_notification(user, "Don't forget to create your diary entry today!")
