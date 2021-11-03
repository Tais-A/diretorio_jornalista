from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

OPCOES_VEICULOS = {
    (1, 'Jornal'),
    (2, 'Revista'),
    (3, 'Rádio'),
    (4, 'TV'),
    (5, 'Site/Blog'),
    (6, 'Rede Social'), 
    (7, 'Plataforma de Video'),
    (8, 'Podcast')
}

from .Artigo import Artigo
from .Coluna import Coluna
from .Entrevista import Entrevista
from .Livro import Livro
from .Noticia import Noticia
from .Reportagem import Reportagem
from .Resenha import Resenha