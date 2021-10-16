from django.urls import path
from . import views


urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<int:id_noticia>/', views.noticia_page, name='noticia_page'),
]
