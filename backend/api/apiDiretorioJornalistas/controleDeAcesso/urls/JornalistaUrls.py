from django.urls import path
from controleDeAcesso.views.JornalistaView import list_jornalistas_view

urlpatterns = [
    path("",  list_jornalistas_view, name='jornalistas'),
]
