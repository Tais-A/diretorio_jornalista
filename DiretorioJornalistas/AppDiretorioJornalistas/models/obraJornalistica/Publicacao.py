from publicacao.models import *
from AppDiretorioJornalistas.models.opcoes import VeiculoDeComunicacao, OPCOES_TIPO_PUBLICACAO

class Publicacao(models.Model):
    obra = models.ForeignKey(ObraJornalistica, verbose_name=_(""), on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=OPCOES_TIPO_PUBLICACAO) 
    veiculo = models.ForeignKey(VeiculoDeComunicacao, verbose_name=_(""), on_delete=models.CASCADE)
    data = models.DateField(_(""))
    link = models.URLField(_(""), max_length=200, blank=True, null = True)
    anexo = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)


    def __str__(self):
        return '{},{}'.format(self.tipo, self.veiculo)