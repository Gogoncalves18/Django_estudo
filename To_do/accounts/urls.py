from django.urls import path
from . import views

urlpatterns = [
    # SignUp.as_view já é uma classe pronta do django para fazer
    # o registro de user
    path('register/', views.SignUp.as_view(), name="signup"),
]
