from django.shortcuts import render
from .models import (
    Noticia,
)

# Create your views here.
def noticias(request):
    noticias = Noticia.objects.all()

    return render(request, 'noticias/index.html', {
        'noticias': noticias
    })


def noticia_page(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)

    return render(request, 'noticias/noticia.html', {
        'noticia': noticia,
    })

