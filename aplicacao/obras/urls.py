from django.urls import path

from .views import *

urlpatterns = [
    path("cadastro", cadastro_obra, name="cadastro_obra"),
    path("edita", cadastro_obra, name="edita_obra"),
    path("lista", cadastro_obra, name="lista_obra"),
]
