from django.contrib import admin
from .models import Pais, EstadoCivil, Genero, TipoDeRedeSocial, TipoDeVeiculo, RedesSociais

# Register your models here.
admin.site.register(EstadoCivil)
admin.site.register(Genero)
admin.site.register(TipoDeRedeSocial)
admin.site.register(TipoDeVeiculo)
admin.site.register(RedesSociais)