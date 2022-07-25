from django.db import models
from django.contrib.auth.models import User

from autenticacao.models import Revisor, Associacao
from opcoes.models import RedesSociais, OPCOES_CIDADE, OPCOES_ESTADO, Etnia, Genero, EstadoCivil
from obras.models import ObraJornalistica
from historico.models import HistoricoProfissional


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    associacao = models.ForeignKey(Associacao,on_delete=models.DO_NOTHING)
    nome_de_guerra = models.CharField( max_length=50)
    cpf = models.CharField( max_length=11)
    data_de_nascimento = models.DateField()
    ddd_telefone = models.CharField( max_length=2)
    telefone = models.CharField( max_length=9)
    rede_social = models.ForeignKey(RedesSociais,on_delete=models.CASCADE)
    etnia = models.ForeignKey(Etnia, on_delete=models.DO_NOTHING)
    estado = models.IntegerField(choices=OPCOES_ESTADO)
    cidade = models.IntegerField(choices=OPCOES_CIDADE)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.DO_NOTHING)
    foto = models.ImageField(null=True, blank = True)
    registro = models.CharField( max_length=50)
    diploma = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey(Revisor,on_delete=models.DO_NOTHING)
    obras_jornalisticas = models.ManyToManyField(ObraJornalistica)
    historico_profissional = models.ManyToManyField(HistoricoProfissional)


    def __str__(self):
        return '{}'.format(self.nome_de_guerra)
