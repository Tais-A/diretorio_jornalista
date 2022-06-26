from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# from .user import User

from .associacao import Associacao
from .revisor import Revisor
from .jornalista import Jornalista
