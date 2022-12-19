from django.contrib import admin
from .models import Associacao, Revisor, Jornalista

# Register your models here.
admin.site.register(Associacao)
admin.site.register(Revisor)
admin.site.register(Jornalista)