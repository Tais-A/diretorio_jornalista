from controleDeAcesso.models import *
from django.db.models import Sum, Count

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    imagem = models.ImageField(null=True, blank = True)
    raça_etnia = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(City, null=True, related_name='city', on_delete=models.SET_NULL)
    funcao = models.IntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token= models.CharField(max_length=255, null=True, blank=True)

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
    
    def show_scoring_average(self):
        from .Rating import Rating
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aggregate(Sum('value'),Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = ratings['value__sum'] /ratings ['user__count']
                scoring_average = round(scoring_average, 2)
                return scoring_average
            return 'Sem avaliações'
        except:
            return 'Sem avaliações'
