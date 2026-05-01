from django.shortcuts import render
from .models import Topicos

# Create your views here.

def index(request):
    """ Renderiza a pagina principal"""
    return render(request, 'lista_tarefas/index.html')

def topicos(request):
    """ Apresenta as tarefas principais """
    topicos_lista = Topicos.objects.order_by('date_added')

    context = {'topicos_lista': topicos_lista}
    return render(request, 'lista_tarefas/topicos_lista.html', context)


# Nesta caso eu recebo a URL um paramentro que vem com o mesmo nome na url 
# <topico_id>, através dele eu pego o item que quero ver em tópicos
# e procuro os sub-topicos ligados a ele, uma vez que minha tabela de sub-topicos
# possui uma FK com a tab de topicos. Só devedemos cuidar que as tabs no BD
# são escritas com o "NOME DO APP"_"NOME DA TAB".
def sub_topicos(request, topico_id):
    """ Listas de sub topicos ligados por FK com a tabela topicos. """

    # Tendo a chave do tópicos, usamos a função abaixo para instanciar o obj topico
    # na VAR 'topico', sendo que eu entrego o vlr que veio pela URL para o campo 'id='
    # que existe na tab 'topico'.
    topico = Topicos.objects.get(id = topico_id)

    # Aqui está uma facilidade do Django, ele tem uma sub_função que me permite 
    # buscar todos os registros que possuem uma FK ligada a VAR 'topico' criada acima.
    # Fazemos isto facilmente acessando o obj de 'topico' que foi instanciado, acionando:
    # '.sub_topicos' - que é o nome da tab do BD que tem a FK.
    # '_set.order_by()' - para acionar uma sub-query do django que faz o trabalho de filtrar os 
    # subtópicos do tópico principal.
    # " '-date_added' " - param de order_by() para ordernar a data do mais novo para mais velho 
    # usando o sinal '-' na frente de 'date_added'.
    sub_topicos_do_topico = topico.sub_topicos_set.order_by('-date_added')
    context = {'topico': topico, 'sub_topicos_do_topico': sub_topicos_do_topico}
    print(context)
    print(sub_topicos_do_topico)

    # Devolvo para page os dados em um contexto maior.
    return render(request, 'lista_tarefas/topico_lista.html', context)