from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = {
    (1, 'Admin'),
    (2, 'Revisor'),
    (3, 'Jornalista'),
    (4, 'Usuario')
}

from .State import State
from .City import City
from .Rating import Rating
from .Usuario import Usuario