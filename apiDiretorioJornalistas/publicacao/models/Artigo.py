from publicacao.models import *

class Artigo(models.Model):
    user = models.ForeignKey(User, related_name='autor', on_delete=models.CASCADE)
    titulo = models.CharField(null = False, max_length=50)
    veiculo = models.IntegerField(choices=OPCOES_VEICULOS) 
    descricao = models.TextField(null = False)

    def __str__(self):
        return '{},{}'.format(self.titulo, self.veiculo)