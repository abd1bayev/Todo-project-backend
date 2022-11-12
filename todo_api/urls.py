# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('<int:todo_id>/', TodoDetailApiView.as_view()),
]