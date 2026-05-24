from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('topicos', views.topicos, name='topicos'),
    path('subtopicos/<topico_id>/', views.sub_topicos, name='sub_topicos_tarefas'),
    # URL para tratar a entrada de novos tópicos através de forms.
    path('new_topico', views.novo_topico, name='novo_topico'),

    # Quando direcionar para pagina do novo subtopico, faremos um parsing de 
    # param, ao qual será o ID do topico
    path('new_sub_topico/<topico_id>', views.new_sub_topicos, name='novo_sub_topico'),
    path('edit_sub_topico/<sub_topico_id>', views.edit_sub_topico, name='editar_sub_topico'),
]

