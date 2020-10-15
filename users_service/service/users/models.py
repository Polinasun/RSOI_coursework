from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class Users(BaseModel):
    first_name = models.TextField()
    last_name = models.TextField()
    patronymic = models.TextField()
    gender = models.CharField(max_length=1)
    age = models.TextField()
    
    class Meta:
        db_table = 'users'

