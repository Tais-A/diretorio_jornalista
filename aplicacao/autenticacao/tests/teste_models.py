from tests import *
from ..models import Jornalista, Revisor, Associacao

class AutenticacaoTestCase(TestCase):

  pass

class JornalistaTestCase(TestCase):
  
  # def setUp(self):
  #   Jornalista.objects.create()

  # def test_model_criado_no_banco(self):
  #   jornalista = Jornalista.objects.get(nome='')

  #   self.assertEqual(jornalista.__str__(), '')
  pass  





# class Revisor(models.Model):
#     id = models.IntegerField(primary_key=True)
#     usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
#     associacao = models.ForeignKey(Associacao, models.DO_NOTHING)

# class Jornalista(models.Model):
#     id = models.IntegerField(primary_key=True)
#     associacao = models.ForeignKey(Associacao, models.DO_NOTHING)
#     revisor_responsavel = models.ForeignKey('Revisor', models.DO_NOTHING, db_column='revisor_responsavel')
#     publico = models.BooleanField()
#     usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
#     nome_de_guerra = models.CharField(max_length=-1)
#     cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
#     data_de_nascimento = models.DateField()
#     telefone = models.IntegerField()
#     rede_sociais = models.ForeignKey('RedeSociais', models.DO_NOTHING)
#     etnia = models.ForeignKey(Etnia, models.DO_NOTHING)
#     cidade = models.ForeignKey(Cidade, models.DO_NOTHING)
#     genero = models.ForeignKey(Genero, models.DO_NOTHING)
#     estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING)
#     registro = models.IntegerField(blank=True, null=True)
#     diploma = models.CharField(max_length=-1, blank=True, null=True)
#     update_at = models.DateTimeField()
#     create_at = models.DateTimeField()
#     obra_jornalistica = models.ForeignKey('ObraJornalistica', models.DO_NOTHING)

# class Associacao(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nome_fantasia = models.CharField(max_length=-1)
#     razao_social = models.CharField(max_length=-1)
#     cnpj = models.IntegerField()
#     telefone = models.CharField(max_length=-1)
#     email = models.CharField(max_length=-1)
#     presidente = models.CharField(max_length=-1)
#     rede_sociais = models.ForeignKey('RedeSociais', models.DO_NOTHING)
