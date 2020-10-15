from django.db import models
from uuid import uuid4


class DancersLog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    time = models.TextField()
    method = models.TextField()
    url = models.TextField()
    client = models.TextField()
    client_id = models.TextField()
    params = models.TextField()
    headers = models.TextField()
    data = models.TextField()

    class Meta:
        db_table = 'dancers_stat'


class ClubsLog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    time = models.TextField()
    method = models.TextField()
    url = models.TextField()
    client = models.TextField()
    client_id = models.TextField()
    params = models.TextField()
    headers = models.TextField()
    data = models.TextField()

    class Meta:
        db_table = 'clubss_stat'


class CompetitionsLog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    time = models.TextField()
    method = models.TextField()
    url = models.TextField()
    client = models.TextField()
    client_id = models.TextField()
    params = models.TextField()
    headers = models.TextField()
    data = models.TextField()

    class Meta:
        db_table = 'competitions_stat'





