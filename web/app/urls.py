from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('perguntas/', views.perguntas),
    path('noticias/', views.noticias),
]
