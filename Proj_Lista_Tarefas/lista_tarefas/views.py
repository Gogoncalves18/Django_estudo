from django.shortcuts import render
from .models import Topicos

# Trago o form para a view. 
from .forms import Topico_Form

# Com esta classe eu posso redirecionar a ação para qq rota.
from django.http import HttpResponseRedirect

# Com esta classe que simplifico a url main que pode mudar no deploy
# desta forma eu posso usar apenas os names dentro do urls.py.
from django.urls import reverse



def index(request):
    """ Renderiza a pagina principal"""
    return render(request, 'lista_tarefas/index.html')

def topicos(request):
    """ Apresenta as tarefas principais """
    topicos_lista = Topicos.objects.order_by('date_added')

    context = {'topicos_lista': topicos_lista}
    return render(request, 'lista_tarefas/topicos_lista.html', context)


def sub_topicos(request, topico_id):
    """ Listas de sub topicos ligados por FK com a tabela topicos. """

    topico = Topicos.objects.get(id = topico_id)
    sub_topicos_do_topico = topico.sub_topicos_set.order_by('-date_added')
    context = {'topico': topico, 'sub_topicos_do_topico': sub_topicos_do_topico}
    print(context)
    print(sub_topicos_do_topico)

    return render(request, 'lista_tarefas/topico_lista.html', context)


def novo_topico(request):
    """ Inserção de novos tópicos no BD """

    # Como toda page olha para view e faz o processo de requisição, neste
    # caso eu posso rodar uma condicional para saber se ele está enviando
    # dados do form ou não.
    if request.method != 'POST':

        # Se não tem nada no form, eu reabro o form zera com esta função
        # importada do meu arquivo forms.py.
        form = Topico_Form()

    else:
        # Quando eu tenho dados para inserir provenientes do form, é só
        # colocá-lo no form criado para a TAB junto com o "request.POST".
        # Mas isto tudo precisa ser instanciado, aqui em 'form'.
        form = Topico_Form(request.POST)

        # Faço uma validação do Django para ver se não há nada no form
        # que fere a estrutura de dados do BD, como tipagem de dados.
        if form.is_valid():
            # Aqui o Django injeta no BD as informações preenchidas no form.
            form.save()

            # Como terminamos de excutar os dados, redireciono a página para
            # rota 'topicos' para que o usuário decida o que fazer. Este método
            # é o mais indicado pois estou usando as referências internas do
            # django (names dentro das urls), para não se perder quando trocar
            # de servidor.
            return HttpResponseRedirect(reverse('topicos'))
    
    context = {'form': form}
    return render(request, 'lista_tarefas/novo_topico.html', context)
