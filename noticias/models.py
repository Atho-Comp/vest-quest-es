from django.db import models
from django.utils.timezone import now

# Create your models here.

class Noticia(models.Model):
    url_image = models.TextField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text_body = models.TextField()
    date = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.title