from django.shortcuts import render
from django.http import HttpResponse


# No retorno da view, eu sempre devolvo o request e o caminho
# do meu template em html, dentro da pasta template.
def tasklist(request):
    return render(request, 'tasks/list.html')


# Precisamos ter cuidado com os parametros passado pela url, eles são
# nomeados, ele precisam ser iguais.
def yourName(request, name_param):
    # Daqui para frente, o nome que darei para o parametro, pode ser qq um.
    # Mas o mesmo nome que devo levar para template do html.
    return render(request, 'tasks/yourname.html', {'name_param2': name_param})
