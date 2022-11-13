# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["text","image", "description", "price", "completed", "timestamp", "updated", "user"]
