from controleDeAcesso.models import *

class Usuario(models.Model):
    nome = models.CharField(primary_key=True, max_length=65)
    data_nascimento = models.DateField()
    raça_etnia = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(City, null=True, related_name='city', on_delete=models.SET_NULL)
    funcao = models.IntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token= models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return '{}'.format(self.nome)

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
        