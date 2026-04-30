from django.shortcuts import render
# Para trazer a estrutura do BD para view. Não posso esquecer o "." antes
# do models para direcionar qual models eu quero. 
from .models import Topicos

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

def topicos(request):
    """ Apresenta as tarefas principais """
    # Neste caso instaciamos neste var topicos_lista todos os 
    # obj que leio no BD da tabela topicos, ordenando pelo campo de data
    topicos_lista = Topicos.objects.order_by('date_added')

    # É obrigado criarmos um contexto de dados de chave e vlr com os obj
    # que li do BD para depois joga-los para html via request.
    context = {'topicos_lista': topicos_lista}
    # Preciso renderizar a page com estes 3 args.
    return render(request, 'lista_tarefas/topicos_lista.html', context)

