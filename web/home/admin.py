from django.contrib import admin
from .models import (
    User,
    Pergunta,
    Alternativa,
    Banca,
    Vestibular,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'alternativa_certa', 'banca', 'vestibular', 'alternativas')


class AlternativasAdmin(admin.ModelAdmin):
    list_display = ('id', 'a', 'b', 'c', 'd', 'e')


class BancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class VestibularAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(User, UserAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Banca, BancaAdmin)
admin.site.register(Vestibular, VestibularAdmin)
admin.site.register(Alternativa, AlternativasAdmin)

