from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Alternativa(models.Model):
    a = models.TextField(blank=True)
    b = models.TextField(blank=True)
    c = models.TextField(blank=True)
    d = models.TextField(blank=True)
    e = models.TextField(blank=True)

class Vestibular(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome



class Banca(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome



class Pergunta(models.Model):
    texto = models.TextField()
    alternativa_certa = models.CharField(max_length=1)
    banca = models.ForeignKey(Banca, on_delete=DO_NOTHING)
    vestibular = models.ForeignKey(Vestibular, on_delete=DO_NOTHING)
    alternativas = models.ForeignKey(Alternativa, on_delete=DO_NOTHING)

    def __str__(self):
        return self.texto

