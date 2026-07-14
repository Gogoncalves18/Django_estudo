from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklist, name='task-list'),
    path('yourname/<str:name_param>', views.yourName, name='nome'),
    path('newtask/', views.newTask, name='new-task'),
    path('task/<int:param_id>', views.taskView, name="task-view"),
]
