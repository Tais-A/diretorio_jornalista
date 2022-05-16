from curriculo.models import *

class ExpProfissional(models.Model):
    locais_de_trabalho = models.ForeignKey(LocalDeTrabalho, on_delete=models.CASCADE)
    titulos = models.CharField(max_length=100, blank=True, null=True)
    outros_aspectos_profissionais = models.CharField(max_length=255, blank=True, null=True)