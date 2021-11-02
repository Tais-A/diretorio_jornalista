from curriculo.models import *

class Idioma(models.Model):
    idioma = models.CharField( max_length=50)
    fala = models.IntegerField(choices=PROFICIENCY_CHOICE, blank=True, null = True)
    ler = models.IntegerField(choices=PROFICIENCY_CHOICE, blank=True, null = True)
    escreve = models.IntegerField(choices=PROFICIENCY_CHOICE, blank=True, null = True)
    compreende = models.IntegerField(choices=PROFICIENCY_CHOICE, blank=True, null = True)

    def __str__(self) -> str:
        return '{}'.format(self.idioma)