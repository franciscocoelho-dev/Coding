from django.shortcuts import render
from django.http import HttpResponse

def funcao_saudacao(request):
    msg = 'Olá Dev, seja bem-vindo'
    return HttpResponse(msg)
