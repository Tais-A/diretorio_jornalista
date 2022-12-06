from django.contrib import admin
from .models import Livro, ObraJornalistica, Publicao, TipoDePublicacao

# Register your models here.
admin.site.register(ObraJornalistica)
admin.site.register(TipoDePublicacao)
admin.site.register(Publicao)
admin.site.register(Livro)