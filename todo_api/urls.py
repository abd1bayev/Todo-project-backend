# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('api/', TodoListApiView.as_view(), name="apitudu"),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view(),name="apitu"),
]