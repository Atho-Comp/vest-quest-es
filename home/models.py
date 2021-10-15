from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
