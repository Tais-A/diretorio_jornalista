from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

ROLE_CHOICE = {
    (1, 'Admin'),
    (2, 'Revisor'),
    (3, 'Jornalista'),
    (4, 'Usuario')
}
class Usuario(models.Model):
    nome = models.CharField(primary_key=True, max_length=65)
    data_nascimento = models.DateField()
    raça_etnia = models.CharField(max_length=45)
    genero = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    funcao = models.IntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token= models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self) -> str:
        return '{}'.format(self.nome.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instace, **kwargs):
        try:
            instace.profile.save()
        except:
            pass
        