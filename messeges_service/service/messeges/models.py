from django.db import models
from uuid import uuid4


class Messege(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    chat_id = models.TextField()
    
    class Meta:
        db_table = 'Messeges'

