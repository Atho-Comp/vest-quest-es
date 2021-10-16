from django.contrib import admin
from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')

admin.site.register(Noticia, NoticiaAdmin)