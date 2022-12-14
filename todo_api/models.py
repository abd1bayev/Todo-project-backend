# todo_api/models.py
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    text = models.CharField(max_length = 180)
    image = models.ImageField(upload_to='images_todo/')
    description = models.CharField(max_length = 250)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text