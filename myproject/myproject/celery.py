import os
from celery import Celery

# Устанавливаем модуль настроек Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


app = Celery('myproject')
