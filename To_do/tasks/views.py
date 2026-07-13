from django.shortcuts import render, get_object_or_404
# Importanto o ORM da tab do BD
from .models import Task


def tasklist(request):
    # Leio do BD os campos e para colocar em dict para enviar para o front
    tasks_field = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks_f': tasks_field})


def yourName(request, name_param):
    return render(request, 'tasks/yourname.html', {'name_param2': name_param})


def taskView(request, param_id):
    # Este "get_object_or_404" é uma fx que busca os dados da tab task com o
    # param da PK     # se não encontrar em lança um 404.
    task = get_object_or_404(Task, pk=param_id)
    # Devolvo para o front a tarefa em uma dict
    return render(request, 'tasks/task.html', {'task_web': task})
