from django.urls import path

from .views import *

urlpatterns = [
    path("cadastro", cadastro_historico, name="cadastro_historico"),
    path("edita", cadastro_historico, name="edita_historico"),
    path("lista", cadastro_historico, name="lista_historico"),
]
