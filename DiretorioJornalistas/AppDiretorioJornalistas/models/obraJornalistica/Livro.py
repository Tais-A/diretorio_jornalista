from AppDiretorioJornalistas.models.obraJornalistica import *

class Livro(models.Model):
    obra = models.ForeignKey(ObraJornalistica, verbose_name=_(""), on_delete=models.CASCADE)
    isbn13 = models.CharField(blank=True, max_length=13)
    isbn10 = models.CharField(blank=True, max_length=13)
    editora = models.CharField(null=False, max_length=100)
    paginas = models.IntegerField(blank=True)
    estado = models.IntegerField(choices=OPCOES_ESTADOS)
    cidades = models.IntegerField(choices=OPCOES_CIDADES)
    ano = models.DateField(blank=True)

    def __str__(self):
        return '{}'.format(self.titulo)

    def ano_publicacao(self):
        return self.ano.strtime('%Y')