from django.db import models

from obras.models import ObraJornalistica
from opcoes.models import Estados, Cidades

class Livro(models.Model):
    isbn10 = models.IntegerField(blank=True, null=True)
    isbn13 = models.IntegerField(blank=True, null=True)
    editora = models.CharField(max_length=254)
    ano_publicacao = models.DateField()
    paginas = models.IntegerField()
    obra_jornalistica = models.ForeignKey(ObraJornalistica, on_delete=models.DO_NOTHING)
    estado = models.ForeignKey(Estados, on_delete=models.DO_NOTHING)
    cidade = models.ForeignKey(Cidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.obra_jornalistica)

    def ano_publicacao(self):
        return self.ano.strtime('%Y')


