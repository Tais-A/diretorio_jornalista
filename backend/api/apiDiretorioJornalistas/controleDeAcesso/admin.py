from django.contrib import admin
from controleDeAcesso.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('nome', 'cidade', 'funcao','created_at')
    list_display_links = ('nome', 'funcao')

admin.site.register(Usuario, UsuarioAdmin)