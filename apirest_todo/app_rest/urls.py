from django.urls import path
from app_rest.views import todo_list

urlpatterns = [
    path('', todo_list, name='todo-lista'),
]
