from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import (
    Noticia,
    Pergunta,
    Resposta,
    User,
)

# Create your views here.
def index(request):
    if request.method != 'POST':
        return render(request, 'app/index.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')

    u = User(
        nome=nome,
        sobrenome=sobrenome,
        email=email,
    )

    if User.objects.filter(email=u.email).exists():
        return render(request, 'app/index.html', {
            'msg': 'ja existe',
        })    

    u.save()

    return render(request, 'app/index.html', {
        'send': True,
    })


def perguntas(request):
    return HttpResponse('perguntas')


def noticias(request):
    return HttpResponse('noticias')
