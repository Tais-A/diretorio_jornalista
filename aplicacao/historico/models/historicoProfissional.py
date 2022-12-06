from django.db import models
from opcoes.models import VeiculoDeComunicacao
from autenticacao.models import Revisor

class HistoricoProfissional(models.Model):
    veiculo_de_comunicacao = models.ForeignKey(VeiculoDeComunicacao, on_delete=models.DO_NOTHING)
    descricao = models.CharField(max_length=254)
    cargo = models.CharField(max_length=254)
    data_inicio = models.DateField()
    data_de_termino = models.DateField()
    duracao = models.TextField()  # This field type is a guess.
    referencia = models.CharField(max_length=254)
    contato_da_referencia = models.CharField(max_length=254)
    validado = models.BooleanField(blank=True, null=True)
    revisor_responsavel = models.ForeignKey(Revisor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} - {} - {}/{}'.format(self.veiculo_de_comunicacao, 
                                        self.cargo, 
                                        self.data_inicio, 
                                        self.data_de_termino)

