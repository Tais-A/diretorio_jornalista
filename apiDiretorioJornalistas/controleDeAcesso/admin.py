from django.contrib import admin
from .models import *

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'cidade', 'funcao','created_at')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Confiabilidade)


