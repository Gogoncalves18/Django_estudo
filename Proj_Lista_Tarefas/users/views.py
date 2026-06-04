from django.http import HttpResponseRedirect
from django.urls import reverse

# Funcao do django para trabalhar com opcoes de logout
from django.contrib.auth import logout


def logout_view(request):
    """Saida do usuario do sistema e fechamento da sessao."""
    # Desta forma que eu deslogo um usuario. Existe este funcao
    # para receber o request da pagina, ele executa o encerramento
    # do user.
    logout(request)
    # Retorno para page inicial
    return HttpResponseRedirect(reverse('index'))
