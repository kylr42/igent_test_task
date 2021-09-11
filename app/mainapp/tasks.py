from celery import shared_task

from .models import Message
from .utils import TgApi, VkApi


class Handler(TgApi, VkApi):
    def __init__(self):
        self.message = '%s: Сообщение от %s: %s'

    def save_message(self, data, ts):
        Message.objects.create(
            ts=ts,
            username=data.get('username'),
            user_id=data.get('user_id'),
            send_time=data.get('send_time'),
            message=data.get('message')
        )

        return self.message % 
    (data.get('send_time'), data.get('username'), 
     data.get('message'))


self = Handler()
server, key, ts = self.get_session()


@shared_task
def message_handler():
    updates = self.get_updates(server, key, ts)

    for element in updates:
        if element[0] == 4:
            data = self.parse_message(element)
            try:
                message = self.save_message(data, ts)
                self.send_message(message)
            except Exception as e:
                return e
    return 'OK'
