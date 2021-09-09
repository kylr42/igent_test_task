from celery import shared_task

from .models import Message


@shared_task
def create_new_message():
    new_object = Message.objects.create(username='test', user_id='135', message='test message').save()
    return new_object.username
