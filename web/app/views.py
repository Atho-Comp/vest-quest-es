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
    return render(request, 'app/index.html')


def perguntas(request):
    return HttpResponse('perguntas')


def noticias(request):
    return HttpResponse('noticias')
