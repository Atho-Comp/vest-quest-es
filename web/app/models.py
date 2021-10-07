from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()


class User(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Pergunta(models.Model):
    texto_pergunta = models.TextField()
    vestibular = models.CharField(max_length=255)
    banca = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    matéria = models.CharField(max_length=255)


class Resposta(models.Model):
    texto_resposta = models.TextField()
    status = models.BooleanField()
    alternativa = models.CharField(max_length=1)
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
