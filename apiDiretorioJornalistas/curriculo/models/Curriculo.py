from curriculo.models import *

class Curriculo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exp_profissional=models.ManyToManyField(ExpProfissional, blank=True)
    formacao=models.ManyToManyField(Formacao, blank=True)
    idioma=models.ManyToManyField(Idioma, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{}'.format(self.user.username)
