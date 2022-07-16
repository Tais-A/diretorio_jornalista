from AppDiretorioJornalistas.models.obraJornalistica import *

class ObraJornalistica(models.Model):
    titulo = models.CharField(_(""), max_length=150)
    descricao = models.TextField(_("", max_length = 500))
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.titulo)