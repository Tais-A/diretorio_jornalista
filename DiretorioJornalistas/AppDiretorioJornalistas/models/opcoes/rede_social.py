from django.db import models

OPCOES_REDE_SOCIAL = {
    (1, 'Site/Blog'),
    (2, 'Facebook'),
    (3, 'Youtube'),
    (4, 'Instagram'),
    (5, 'PodCast'),
    (6, 'LinkedIn'),
    (7, 'Twitter'),
    (8, 'OUtras'),
}

class RedeSocial(models.Model):
  link = models.URLField(max_length=200)
  tipo = models.IntegerField(choices=OPCOES_REDE_SOCIAL)