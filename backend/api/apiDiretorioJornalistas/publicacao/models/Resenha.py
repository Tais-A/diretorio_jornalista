from publicacao.models import *

class Resenha(models.Model):
    titulo = models.CharField(null = False, max_length=50)
    veiculo = models.IntegerField(choices=OPCOES_VEICULOS) 
    descricao = models.TextField(null = False)

    def __str__(self):
        return '{},{}'.format(self.nome, self.veiculo)