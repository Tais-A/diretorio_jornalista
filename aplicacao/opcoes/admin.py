from django.contrib import admin
from .models import Pais, EstadoCivil, Genero, Etnia, TipoDeRedeSocial, TipoDeVeiculo

# Register your models here.
admin.site.register(EstadoCivil)
admin.site.register(Genero)
admin.site.register(Etnia)
admin.site.register(TipoDeRedeSocial)
admin.site.register(TipoDeVeiculo)