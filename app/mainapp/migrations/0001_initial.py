# Generated by Django 3.2.7 on 2021-09-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('user_id', models.CharField(max_length=50, verbose_name='User ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Dispatch time')),
            ],
        ),
    ]