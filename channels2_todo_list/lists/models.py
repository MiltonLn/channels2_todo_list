import uuid

from django.db import models


class TODOList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo_list = models.ForeignKey(TODOList, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
