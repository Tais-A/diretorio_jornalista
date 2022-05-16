from django.urls import path
from controleDeAcesso.views.UsuarioView import editar_usuario, listar_usuario_view

urlpatterns = [
    path("", listar_usuario_view, name='usuarios'),
    path("<int:id>", listar_usuario_view, name ='usuario'),
    path("editar", editar_usuario,name='editar-usuario'),
]
