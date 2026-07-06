from django.urls import path
from . import views

# Sempre devo entrar com 3 args para o
# path('caminho da url no site', 'view que esta a funcao, 'nome para o path)
urlpatterns = [
    path('', views.tasklist, name='task-list'),

    # Parte da url (<str:name_param>) para passarmos parametros via url,
    # unico cuidado este nome "name_param" é um param nomeado com a funcao, 
    # ambos os nomes deve ser iguais.
    path('yourname/<str:name_param>', views.yourName, name='nome')
]
