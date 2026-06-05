from django.shortcuts import render
from .models import Topicos, Sub_topicos
from .forms import Topico_Form, Sub_topico
# Http404 serve para levantarmos uma aviso de page nao encontrada
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# Esta biblioteca serve para definir quais views eu
# exijo login realizado.
from django.contrib.auth.decorators import login_required


def index(request):
    """ Renderiza a pagina principal"""
    return render(request, 'lista_tarefas/index.html')


# Decorador para exigir login do user para acessar a view.
# Se ele não tiver logado, ele deverá desviar o user para
# tela de login. Para isto é necessário configurar o settings
# com a key "LOGIN_URL ="
@login_required
def topicos(request):
    """ Apresenta as tarefas principais """

    # Acrescentado 'filter(owner=request.user)' para filtrar topicos que sao
    # o usuario logado, o problema é que somente isto nao adianta. Se tivermos
    # o endereco da url, ele consegue acessar.
    topicos_lista = Topicos.objects.\
        filter(owner=request.user).\
        order_by('date_added')

    context = {'topicos_lista': topicos_lista}
    return render(request, 'lista_tarefas/topicos_lista.html', context)


@login_required
def sub_topicos(request, topico_id):
    """ Listas de sub topicos ligados por FK com a tabela topicos. """

    topico = Topicos.objects.get(id=topico_id)

    # Esta logica serve para pegarmos a instancia que o django trouxe
    # que possui todas as colunas da tabela e estou pegando a coluna
    # de owner da tab e verificando contra o user que está fazendo o request,
    # se ele for diferente eu chamo uma fx pronta do django para acusar page
    # nao encontrada.
    if topico.owner != request.user:
        raise Http404
    else:
        sub_topicos_do_topico = topico.sub_topicos_set.order_by('-date_added')
        context = {'topico': topico,
                   'sub_topicos_do_topico': sub_topicos_do_topico}
        # print(context)
        # print(sub_topicos_do_topico)

        return render(request, 'lista_tarefas/topico_lista.html', context)


@login_required
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

        if form.is_valid():
            # Para receber os dados e nao injetar no BD ainda até
            # colocar o owner.
            novo_topico = form.save(commit=False)
            # Eu adiciono aos dados o campo 'owner' que é igual ao campo
            # no BD e instacio nele o user de request que é o ID do usuario.
            novo_topico.owner = request.user
            novo_topico.save()

            return HttpResponseRedirect(reverse('topicos'))

    context = {'form': form}
    return render(request, 'lista_tarefas/novo_topico.html', context)


@login_required
def new_sub_topicos(request, topico_id):
    """ Entradas para novos subtopicos do tópico pai. """
    topico = Topicos.objects.get(id=topico_id)
    print(f'========> {topico.id}')
    if request.method != 'POST':
        # Para apresentar o mesmo formulario em branco já
        # que não houve envio de infos.
        form = Sub_topico()
    else:
        # PONTO IMPORTANTE, aqui os meus dados não estão completos
        # eu só tenho o texto, ainda não posso salvar em BD, pois ainda
        # preciso adicionar novas informações além do texto de input.
        # Assim montamos uma nova instancia com chave e vlr no DATA.
        form = Sub_topico(data=request.POST)
        if form.is_valid():
            # O fato de usar o "commit=False" permite salvar os dados 
            # de texto em background e não injetar no BD ainda, para 
            # que possamos manipular ele.
            nova_entrada = form.save(commit=False)
            # Pego o topico da funcao "new_sub_topicos" ao qual obtive
            # o ID do pai e estou injetando nos dados como k=topico_pai
            # vlr= topico da função.
            nova_entrada.sub_topicos = topico
            print(f'DADOS SALVOS NO BD: {nova_entrada}')
            nova_entrada.save()

            # Aqui algo novo, eu redireciono a page passando um arg para ela,
            # preenchendo o param que ela precisa para achar os sub_topicos
            # ligados ao topico pai.
            return HttpResponseRedirect(reverse('sub_topicos_tarefas',
                                                args=[topico.id]))

    context = {'topico': topico, 'form': form}
    return render(request, 'lista_tarefas/novo_sub_topico.html', context)


@login_required
def edit_sub_topico(request, sub_topico_id):
    """ Edição de subtopicos que estão dentro de tópicos."""

    # Busco o id da subtarefa que tenho interesse
    sub_topico_id = Sub_topicos.objects.get(id=sub_topico_id)
    # Busco o id da tarefa PAI que é a FK
    topico_id = sub_topico_id.sub_topicos_id

    if topico_id != request.user:
        raise Http404
    else:

        print(f'============>  {topico_id}')

        if request.method != 'POST':
            # Resgato um form preenchido com os dados no BD, neste caso
            # peguei o form dos subtopicos e com (instance=sub_topico_id)
            # é possível trazer o texto gravado para este ID de subtopico.
            form = Sub_topico(instance=sub_topico_id)

        else:
            # Neste caso, se quero atualizar os dados do form, a função
            # (instance=sub_topico_id, data=request.POST) permite que:
            # instance traga os dados e o data, repreencha os dados 
            # ao qual estão no front e que serão enviados para o BD no mesmo
            # id ao qual peguei em "sub_topico_id"
            form = Sub_topico(instance=sub_topico_id, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('sub_topicos_tarefas',
                                                    args=[topico_id]))

        context = {'sub_topico_id': sub_topico_id, 'topico_id': topico_id,
                   'form': form}
        return render(request, 'lista_tarefas/editar_sub_topico.html', context)
