from app_rest.models import Todo
# FUNCAO DO FRAMEW QUE DEFINE OS METODOS QUE PODEMOS USAR EM NOSSA VIEW
from rest_framework.decorators import api_view
from app_rest.serializers import Todo_Serializer
from rest_framework.response import Response
# VALIDADOR DE STATUS DE REQUEST DO FRAMEW
from rest_framework import status


# NESTE DECORATOR EU PASSO A FUNCAO get PARA OBTER INFOS DO BD
@api_view(['GET', 'POST'])
def todo_list(request):
    # VALIDA O METODO PARA TRATAR A SAIDA OU ENTRADA DE DADOS
    if request.method == 'GET':
        # BUSCO TODOS OS OBJ DO BD
        todo = Todo.objects.all()

        # AQUI PRECISO PASSAR O PARAM MANY PQ EU ESPERO RECEBER VÁRIOS OBJS.
        # PRECISO IMPORTAR A DEF QUE EU FIZ NO ARQ SERIALIZER
        # PRECISO IMPORTAR A FX DO FRAMEWORK PARA RESPONDER A ESTE REQUEST
        serializer = Todo_Serializer(todo, many=True)

        # AQUI EU DEVOLVO OS VLRS INSTANCIADO E COM A FX '.data' PARA ELE FORMATAR
        return Response(serializer.data)

    elif request.method == 'POST':
        # PEGO O ENVIO DE DADOS VIA POST PARA SALVAR NO FRAMEWORK
        serializer = Todo_Serializer(data=request.data)
        # VALIDA SE OS DADOS ESTAO ADEQUADOS
        if serializer.is_valid():
            serializer.save()
            # USA UM VALIDADOR DE STATUS DO PROPRIO FRAMEW
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # EM CASO DE ERRO, VOLTO A MENSAGEM
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
