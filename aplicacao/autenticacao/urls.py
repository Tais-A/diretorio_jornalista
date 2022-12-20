from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', home_view), #Busca de joranlistas e Glossario
    path('',  lista_jornalistas_view, name='jornalistas'),

    path('jornalista', dados_jornalista_view, name="dados-jornalista"),
    path('jornalista/cadastro', cadastro_jornalista_view, name="cadastro-jornalista"),
    # path('jornalista/salvar', salvar, name="salvar"),

    #re_path(r'^adicionajornalista/$', AddJornalistaView.as_view(), name="add_jornalista"),


    path('revisor/<int:id>', lista_jornalistas_associados_view, name="jornalista-associados"),
    path('revisor/<int:id>/valida/<int:id_jornalista>', valida_jornalista_view, name="valida-jornalista"),


    path("login", login_view, name='login'),
    path("register", register_view, name='register'), 
    path("logout", logout_view, name='logout' ),
]