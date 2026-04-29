from django.contrib import admin
# Necessario importar o models criado
from lista_tarefas.models import Topicos, Sub_topicos

# Register your models here.

# Função para atualizar a tabela no painel adm
admin.site.register(Topicos)
admin.site.register(Sub_topicos)