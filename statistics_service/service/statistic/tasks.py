from service.celery import celery_app
import time
from .models import DancersLog, ClubsLog, CompetitionsLog

@celery_app.task
def add_entry_stat(service, data):
    services = {'Clubs': ClubsLog, 'Dancers': DancersLog, 'Competitions': CompetitionsLog}
    model = services.get(service)
    entry = model.objects.create(**data)


