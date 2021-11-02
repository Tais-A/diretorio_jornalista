from controleDeAcesso.models import *

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, null=True, related_name='estado', on_delete=models.SET_NULL)
    nome = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.estado.nome)