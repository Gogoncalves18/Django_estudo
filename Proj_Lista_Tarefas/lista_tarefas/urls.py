# O include serve para eu redirecionar a ULR para o app desejado
from django.urls import path

# Uso o "." na importação pq ela esta na mesma pasta
from . import views

urlpatterns = [    
    # funcao para quando não digitar nada após o end_url, ele encaminha
    # para a url do app lista_tarefas dentro de uma função chamada INDEX
    # e de lá eu direciono para o html desejado.
    path('', views.index),
]
