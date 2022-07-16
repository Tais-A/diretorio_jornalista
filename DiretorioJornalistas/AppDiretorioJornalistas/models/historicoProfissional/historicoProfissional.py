from AppDiretorioJornalistas.models.historicoProfissional import *
from AppDiretorioJornalistas.models.usuarios import Jornalista, Revisor
from AppDiretorioJornalistas.models.opcoes import VeiculoDeComunicacao

class HistoricoProfissional(models.Model):
    titulo = models.CharField(_(""), max_length=50)
    veiculo = models.ForeignKey(VeiculoDeComunicacao, verbose_name=_(""), on_delete=models.CASCADE)
    descricao = models.TextField(null = False)
    cargo = models.CharField(_(""), max_length=50)
    data_inicio = models.DateField(_(""))
    data_terminio = models.DateField(_(""))
    referencia = models.CharField(_(""), max_length=50)
    contato_da_referencia = models.CharField(_(""), max_length=50)
    validado = models.BooleanField(_(""))
    revisor_responsavel = models.ForeignKey(Revisor, verbose_name=_(""), on_delete=models.CASCADE)
    jornalista = models.ForeignKey(Jornalista, verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.titulo)