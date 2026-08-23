# IMPORTO O MODELO DA TAB DO BD
from app_rest.models import Todo
# ESTA IMPORTACAO É PARA TRANSFORMAR OS DADOS EM UM PACOTE DE JSON
from rest_framework import serializers


# NECESSÁRIO CRIAR UMA CLASSE PARA A TRANSFORMACAO PARA JSON
class Todo_Serializer(serializers.ModelSerializer):
    # AQUI TEMOS O MESMO QUE O DJANGO DEFINE, UMA SUBCLASS META
    class Meta:
        # PRECISO INSTANCIAR MEU MODEL
        model = Todo
        # PRECISO IDENTIFICAR QUAIS SERÃO OS CAMPOS DE MAPEAMENTO
        fields = ['id', 'name', 'done', 'created_at']