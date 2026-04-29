from django.shortcuts import render

# Create your views here.

# Esta funcao é acionada pelo url de rotas, ao ser acionada ela
# possui uma função request para responder para uma página html "front"
# recebendo requisições e respondendo-as para o html.
def index(request):
    """ Renderiza a pagina principal"""
    # aqui dentro crio toda a lógica 

    # Devolvo para o html os dados desta lógica via função RENDER.
    # Este arquivo deve ficar em uma pasta TEMPLATES dentro do app 
    # em questão.
    return render(request, 'lista_tarefas/index.html')
