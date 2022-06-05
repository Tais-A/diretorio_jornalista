from AppDiretorioJornalistas.models.usuarios import *
from AppDiretorioJornalistas.models.opcoes import RedeSocial, OPCOES_CIDADE, OPCOES_ESTADO, OPCOES_GENERO, OPCOES_ETNIA, OPCOES_ESTADO_CIVIL


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    associacao = models.ForeignKey(Associacao,on_delete=models.CASCADE)
    nome_de_guerra = models.CharField( max_length=50)
    cpf = models.CharField( max_length=11)
    data_de_nascimento = models.DateField(default=None, null=True, blank=True)
    ddd_telefone = models.CharField( max_length=2)
    telefone = models.CharField( max_length=9)
    rede_social = models.ForeignKey(RedeSocial,on_delete=models.CASCADE)
    raca = models.IntegerField(choices=OPCOES_ETNIA)
    estado = models.IntegerField(choices=OPCOES_ESTADO)
    cidade = models.IntegerField(choices=OPCOES_CIDADE)
    genero = models.IntegerField(choices=OPCOES_GENERO, blank=True, null=True)
    estado_civil = models.IntegerField(choices=OPCOES_ESTADO_CIVIL)
    foto = models.ImageField(null=True, blank = True)
    registro = models.CharField( max_length=50)
    diploma = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey(Revisor,on_delete=models.CASCADE)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Usuario.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
    