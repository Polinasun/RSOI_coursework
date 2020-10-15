from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class Photos(BaseModel):
    photo = models.TextField()
    name = models.TextField()
    comments = models.TextField()

    class Meta:
        db_table = 'clubs'


class Comments(BaseModel):
    text = models.ForeignKey(Photos, on_delete=models.CASCADE)
    user = models.UUIDField()

    class Meta:
        db_table = 'members'
