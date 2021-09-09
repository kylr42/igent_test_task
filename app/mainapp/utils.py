import time

import requests
from django.conf import settings


class VkApi:
    ts = None
    vk_version = '5.65'
    vk_token = settings.VK_TOKEN
    user_url = 'https://api.vk.com/method/users.get'
    session_url = 'https://api.vk.com/method/messages.getLongPollServer'
    updates_url = "https://%s?key=%s&ts=%s"

    def parse_message(self, element):
        params = {'name_case': 'gen', 'access_token': self.vk_token, 'v': self.vk_version}
        if element[3] - 2000000000 > 0:
            params['user_ids'] = element[6]['from']
        else:
            params['user_ids'] = element[3]
        user = requests.get(self.user_url, params=params).json().get('response')[0]
        data = {
            'username': f'{user.get("first_name")} {user.get("last_name")}',
            'user_id': params['user_ids'],
            'send_time': time.ctime(element[4]).split()[3],
            'message': element[5]
        }
        return data

    def get_session(self):
        params = {'access_token': self.vk_token, 'v': self.vk_version}
        session = requests.get(self.session_url, params=params).json()['response']
        return session.get('server'), session.get('key'), session.get('ts')

    def get_updates(self, server, key, ts):
        url = self.updates_url % (server, key, self.ts if self.ts else ts)
        params = {'act': 'a_check', 'wait': '10', 'mode': '2', 'version': '2'}
        response = requests.get(url, params=params).json()
        self.ts = response.get('ts')
        return response.get('updates')


class TgApi:
    tg_token = settings.TG_TOKEN
    chat_id = settings.TG_CHAT_ID
    url = f'https://api.telegram.org/bot{tg_token}/sendMessage'

    def send_message(self, text):
        answer = {'chat_id': self.chat_id, 'text': text}
        r = requests.post(self.url, json=answer)
        return r.json()
