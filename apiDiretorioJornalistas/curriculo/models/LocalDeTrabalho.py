from curriculo.models import *

class LocalDeTrabalho(models.Model):
    nome_profissinal = models.CharField(primary_key=True, max_length=65)
    registro_profissional = models.CharField(max_length=65, blank=True, null=True)
    empresa_instituicao = models.CharField(max_length=65, blank=True, null=True)
    contato_do_jornalista = models.CharField(max_length=65, blank=True, null=True)

    def __str__(self) -> str:
        return '{}'.format(self.nome_profissinal)