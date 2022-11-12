# todo_api/models.py
from django.db import models
from django.conf import settings

class Todo(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task