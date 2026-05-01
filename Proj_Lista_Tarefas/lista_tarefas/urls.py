from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('topicos', views.topicos, name='topicos'),
    path('subtopicos/<topico_id>/', views.sub_topicos, name='sub_topicos_tarefas'),
    # URL para tratar a entrada de novos tópicos através de forms.
    path('new_topico', views.novo_topico, name='novo_topico'),
]

