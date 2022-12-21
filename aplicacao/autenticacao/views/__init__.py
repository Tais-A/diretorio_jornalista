from django.shortcuts import render

from .authViews import login_view, register_view, logout_view
from .homeViews import home_view, lista_jornalistas_view
from .jornalistasViews import cadastro_jornalista_view, dados_jornalista_view, edita_jornalista_view
from .revisorViews import valida_jornalista_view, lista_jornalistas_associados_view