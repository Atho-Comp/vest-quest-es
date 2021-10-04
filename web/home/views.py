from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method != 'POST':
        return render(request, 'home/index.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')

    print(nome, email)

    return render(request, 'home/index.html', {
        'nome': nome
    })

def perguntas(request):
    return HttpResponse('pagina perguntas')
