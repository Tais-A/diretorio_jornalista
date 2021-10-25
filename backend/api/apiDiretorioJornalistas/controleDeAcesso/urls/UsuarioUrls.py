from django.urls import path
from controleDeAcesso.views.UsuarioView import list_usuario_view

urlpatterns = [
    path("", list_usuario_view, name='usuarios'),
    path("<int:id>", list_usuario_view, name ='usuario'),
]
