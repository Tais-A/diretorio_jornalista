from django.db import models

OPCOES_VEICULO = {
    (1, 'Jornal'),
    (2, 'Revista'),
    (3, 'Rádio'),
    (4, 'TV'),
    (5, 'Site/Blog'),
    (6, 'Rede Social'), 
    (7, 'Plataforma de Video'),
    (8, 'Podcast')
}

class VeiculoDeComunicacao(models.Model):
  nome = models.CharField(max_length=50)
  tipo = models.IntegerField(choices=OPCOES_VEICULO)