# Generated by Django 4.0.5 on 2022-09-20 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0004_alter_jornalista_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associacao',
            name='rede_sociais',
        ),
        migrations.RemoveField(
            model_name='jornalista',
            name='diploma',
        ),
        migrations.RemoveField(
            model_name='jornalista',
            name='historico_profissional',
        ),
        migrations.RemoveField(
            model_name='jornalista',
            name='obras_jornalisticas',
        ),
        migrations.RemoveField(
            model_name='jornalista',
            name='rede_social',
        ),
    ]
