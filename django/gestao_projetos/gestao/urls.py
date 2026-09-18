from django.urls import path
from .views import gestao_home

urlpatterns = [
    path('', gestao_home)
]