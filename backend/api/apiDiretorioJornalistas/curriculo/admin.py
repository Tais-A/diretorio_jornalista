from django.contrib import admin
from .models import *

# Register your models here.
class CurriculoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user','update_at')

admin.site.register(Curriculo, CurriculoAdmin)
admin.site.register(ExpProfissional)
admin.site.register(Formacao)
admin.site.register(Idioma)
admin.site.register(LocalDeTrabalho)