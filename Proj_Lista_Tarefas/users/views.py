from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Funcao do django para trabalhar com opcoes de logout
from django.contrib.auth import logout, login, authenticate
# Formulario de criacao de usuarios.
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Saida do usuario do sistema e fechamento da sessao."""
    # Desta forma que eu deslogo um usuario. Existe este funcao
    # para receber o request da pagina, ele executa o encerramento
    # do user.
    logout(request)
    # Retorno para page inicial
    return HttpResponseRedirect(reverse('index'))


def registro_user(request):
    """Formulario para criacao de users."""
    # Se eu nao estou enviando algo para o request (POST),
    # é pq eu preciso de um form limpo.
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # Recebo o um post e preencho o formulario dentro do BD.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Salvo os dados do user em uma instancia
            new_user = form.save()

            # faz o longin do user e redireciona para page inicial.
            # Esta funcao "authenticate()" serve para validar os dados
            # de usuario no bd, onde eu direciono os vlrs do dict new_user
            # para dentro do bd em cada campo. O detalhe é o pw, ele recebe
            # dois mas eu preciso enviar apenas um password.
            user_autenticado = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            # Aqui uso outra funcao para executar o login do user.
            login(request, user_autenticado)

            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/registro.html', context)
