from django.urls import path
from .views import funcao_saudacao

urlpatterns = [
    path('', funcao_saudacao)
]