from django.contrib import admin
from .models import *

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'cidade', 'funcao','created_at')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Rating)


