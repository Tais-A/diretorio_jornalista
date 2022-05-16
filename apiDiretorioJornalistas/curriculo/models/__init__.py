from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

PROFICIENCY_CHOICE = {
    (1, 'Pouco'),
    (2, 'Razoavelmente'),
    (3, 'Bem'),
    (4, 'Fluente')
}

from .LocalDeTrabalho import LocalDeTrabalho
from .ExpProfissional import ExpProfissional
from .Formacao import Formacao
from .Idioma import Idioma
from .Curriculo import Curriculo
