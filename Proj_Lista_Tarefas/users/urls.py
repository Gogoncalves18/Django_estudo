from django.urls import path

# Importação para usar as funções de autenticacao do django
from django.contrib.auth import views as auth_views
from . import views


# A função "LoginView.as_view" permite usar um padrão de login do django.
# Este padrão precisa receber "template_name='users/login.html'" como param.
urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'),
        name='login'),
    path('logout', views.logout_view, name='logout_user'),
    path('reg_user', views.registro_user, name='reg_usuario')
]
