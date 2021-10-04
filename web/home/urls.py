from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('perguntas/', views.perguntas, name='perguntas')
]