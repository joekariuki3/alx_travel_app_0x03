from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('crm')
