# Generated by Django 4.0.5 on 2022-07-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDiretorioJornalistas', '0004_alter_jornalista_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornalista',
            name='estado_civil',
            field=models.IntegerField(choices=[(1, 'Solteiro'), (4, 'Viúvo'), (2, 'Casado'), (5, 'União Estável'), (3, 'Divorciado')]),
        ),
        migrations.AlterField(
            model_name='jornalista',
            name='genero',
            field=models.IntegerField(blank=True, choices=[(1, 'Femino'), (2, 'Masculino'), (3, 'Não Binário')], null=True),
        ),
        migrations.AlterField(
            model_name='jornalista',
            name='raca',
            field=models.IntegerField(choices=[(1, 'Preta'), (3, 'Amarela (Origem Asiática/Oriental)'), (4, 'Parda'), (6, 'Não Declarado'), (5, 'Indígena'), (2, 'Branca')]),
        ),
        migrations.AlterField(
            model_name='redesocial',
            name='tipo',
            field=models.IntegerField(choices=[(6, 'LinkedIn'), (1, 'Site/Blog'), (8, 'OUtras'), (4, 'Instagram'), (7, 'Twitter'), (3, 'Youtube'), (2, 'Facebook'), (5, 'PodCast')]),
        ),
        migrations.AlterField(
            model_name='veiculodecomunicacao',
            name='tipo',
            field=models.IntegerField(choices=[(5, 'Site/Blog'), (2, 'Revista'), (7, 'Plataforma de Video'), (8, 'Podcast'), (1, 'Jornal'), (6, 'Rede Social'), (3, 'Rádio'), (4, 'TV')]),
        ),
    ]
