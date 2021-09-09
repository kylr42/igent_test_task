from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=100, verbose_name='Username')
    user_id = models.CharField(max_length=50, verbose_name='User ID')
    message = models.TextField(verbose_name='Message')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Dispatch time')

    def __str__(self):
        return self.message[:15]
