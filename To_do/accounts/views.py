from django.shortcuts import render
# PARA USAR UM FORM DO DJANGO
from django.contrib.auth.forms import UserCreationForm
# Reverse_lazy funciona como o redirection mas para este caso precisa ser esta fx
from django.urls import reverse_lazy
# GENERIC DEIXA CRIARMOS UMA CLASSE GENERICA DE VIEW
from django.views import generic


# CRIACAO DE UMA CLASSE, ASSIM NÃO USAMOS AS F(X)
class SignUp(generic.CreateView):
    # CRIACAO DO FORM NECESSARIO
    form_class = UserCreationForm
    # USO DO REVERSE PARA REDIRECIONAR O USER PARA O LOGIN QUANDO ELE FIZER O CADASTRO
    success_url = reverse_lazy('login')
    # TEMPLATE QUE O DJANGO USARÁ QUE FICARÁ EM TEMPLATES
    template_name = 'registration/register.html'
