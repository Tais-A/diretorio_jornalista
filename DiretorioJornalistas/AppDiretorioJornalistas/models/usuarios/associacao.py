from AppDiretorioJornalistas.models.usuarios import *
from AppDiretorioJornalistas.models.opcoes import RedeSocial


class Associacao(models.Model):
    nome_fantasia = models.CharField( max_length=50)
    razao_social = models.CharField(max_length=50)
    cnpj= models.CharField(max_length=14)
    ddd_telefone = models.CharField(max_length=2)
    telefone = models.CharField(max_length=9)
    email = models.EmailField(max_length=254)
    rede_social = models.ForeignKey(RedeSocial, on_delete=models.CASCADE)
    presidente = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{}'.format(self.nome_fantasia)