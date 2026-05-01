# O include serve para eu redirecionar a ULR para o app desejado
from django.urls import path

# Uso o "." na importação pq ela esta na mesma pasta
from . import views

urlpatterns = [    
    # funcao para quando não digitar nada após o end_url, ele encaminha
    # para a url do app lista_tarefas dentro de uma função chamada INDEX
    # e de lá eu direciono para o html desejado.
    # name='index' é usado pelo o django para acionar as url sem depender
    # de end_url, isto ajuda no deploy.
    path('', views.index, name='index'),
    # Nova url que apresentará os topicos que irei criar em views.py
    path('topicos', views.topicos, name='topicos'),

    # URL para acessar subtopicos que estão ligados por uma FK com a tabela 
    # topicos. Importante ficar claro que eu envio para view um parametro que
    # é inserido nesta url através de "< >"
    path('subtopicos/<topico_id>/', views.sub_topicos, name='sub_topicos_tarefas'),
]

