from django.shortcuts import render

def gestao_home(request):
    return render(request, 'index.html')

