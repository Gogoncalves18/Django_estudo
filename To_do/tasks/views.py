from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
# Para gerar mensagens no front end
from django.contrib import messages


def tasklist(request):
    tasks_field = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks_f': tasks_field})


def yourName(request, name_param):
    return render(request, 'tasks/yourname.html', {'name_param2': name_param})


def taskView(request, param_id):
    # Este "get_object_or_404" é uma fx que busca os dados da tab task com o
    # param da PK     # se não encontrar em lança um 404.
    task = get_object_or_404(Task, pk=param_id)
    # Devolvo para o front a tarefa em uma dict
    return render(request, 'tasks/task.html', {'task_web': task})


def newTask(request):
    # Este if verifica que estou fazendo um post em minha page
    if request.method == 'POST':
        # Pego os dados do form que usou o metodo post e instancio ele
        form = TaskForm(request.POST)

        # Uso uma funcao de validacao se é uma formulario, do django
        if form.is_valid():
            # Seto ele para guarda o cache dos dados mais ainda nao inserir no
            # BD
            # ele fica instanciado em task
            task = form.save(commit=False)
            # Altero o campo done que está dentro do objeto instanciado
            task.done = 'doing'
            # Então salvo
            task.save()
            # Ai direciono ele para um determinado caminho
            return redirect('/')
    else:
        # instancio ele para jogar para o front
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


def editTask(request, param_id):
    # Este "get_object_or_404" é uma fx que busca os dados da tab task com o
    # param da PK     # se não encontrar em lança um 404.
    task = get_object_or_404(Task, pk=param_id)
    # Para deixar o form preenchido quando o user chamar o front
    form = TaskForm(instance=task)

    # Valido se estou executando o post na page
    if (request.method == 'POST'):
        # Pego os dados do form que usou o metodo post e instancio ele e junto
        # coloco o objeto task
        form = TaskForm(request.POST, instance=task)
        if (form.is_valid()):
            # Salvo os dados
            task.save()
            return redirect('/')
        # Se ocorrer algum erro no form, redireciono a page original
        else:
            return render(request,
                          'tasks/edittask.html',
                          {'form': form, 'task': task})
    # Se não tiver executando o post apenas carrego os dados do form
    else:
        # Aqui eu monto duas dict para o front, um com o form formatado pelo
        # django e outro com os dados da task pois quero usar algumas
        # infos dela para preencher no template
        return render(request,
                      'tasks/edittask.html',
                      {'form': form, 'task': task})


def deleteTask(request, param_id):
    task = get_object_or_404(Task, pk=param_id)
    # Deletar o obj da PK encontrada, se ele encontrar pk, caso contrario 
    # subira um 404
    task.delete()
    # Funcao para entregar mensagem para o front.
    messages.info(request, 'Tarefa deletada com sucesso!')
    messages.error(request, 'FUDEU COM TUDO!')

    return redirect('/')
