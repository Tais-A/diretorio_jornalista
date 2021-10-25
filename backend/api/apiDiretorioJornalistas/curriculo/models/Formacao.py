from curriculo.models import *

class Formacao(models.Model):
    tema = models.CharField(primary_key=True, max_length=65)
    instituicao = models.CharField(max_length=65)
    ano_conclusao = models.DateField()
    nivel_graduacao = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self) -> str:
        return '{} - {},{}'.format(self.tema, self.instituicao, self.ano_conclusao)