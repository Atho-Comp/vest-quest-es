from django.http.response import HttpResponse
from django.shortcuts import render
from .models import User


def index(request):
    if request.method != 'POST':
        return render(request, 'home/index.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')

    user = User(
        nome=nome,
        sobrenome=sobrenome,
        email=email
    )

    user.save()

    return render(request, 'home/index.html', {
        'message': 'Obrigado por se inscrever'
    })


def perguntas(request):
    return HttpResponse('pagina perguntas')
