from publicacao.models import *
from controleDeAcesso.models import Cidade

class Livro(models.Model):
    titulo = models.CharField(null=False, max_length=100)
    isbn13 = models.CharField(blank=True, max_length=13)
    isbn10 = models.CharField(blank=True, max_length=13)
    editora = models.CharField(null=False, max_length=100)
    paginas = models.IntegerField(blank=True)
    cidade = models.ForeignKey(Cidade, blank=True, null=True,on_delete=models.SET_NULL)
    ano = models.DateField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.titulo)

    def ano_publicacao(self):
        return self.ano.strtime('%Y')