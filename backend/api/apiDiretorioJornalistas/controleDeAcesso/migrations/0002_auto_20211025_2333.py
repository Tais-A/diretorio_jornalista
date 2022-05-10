# Generated by Django 3.2.7 on 2021-10-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleDeAcesso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='funcao',
            field=models.IntegerField(blank=True, choices=[(4, 'Usuario'), (1, 'Admin'), (2, 'Revisor'), (3, 'Jornalista')], null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.IntegerField(blank=True, choices=[(2, 'Masculino'), (1, 'Femino'), (3, 'Não Binário')], null=True),
        ),
    ]