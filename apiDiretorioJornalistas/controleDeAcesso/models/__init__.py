from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


OPCOES_GENERO = {
    (1, 'Femino'),
    (2, 'Masculino'),
    (3, 'Não Binário')
}

OPCOES_FUNCAO = {
    (1, 'Admin'),
    (2, 'Revisor'),
    (3, 'Jornalista'),
    (4, 'Usuario')
}

OPCOES_RACA = {
    (1, 'Preta'),
    (2, 'Branca'),
    (3, 'Amarela (Origem Asiática/Oriental)'),
    (4, 'Parda'),
    (5, 'Indígena'),
    (6, 'Não Declarado')
}

from .Estado import Estado
from .Cidade import Cidade
from .Confiabilidade import Confiabilidade
from .Usuario import Usuario