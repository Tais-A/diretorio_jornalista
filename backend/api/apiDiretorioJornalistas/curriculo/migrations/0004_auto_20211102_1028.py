# Generated by Django 3.2.7 on 2021-11-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0003_auto_20211102_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='compreende',
            field=models.IntegerField(blank=True, choices=[(3, 'Bem'), (4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='escreve',
            field=models.IntegerField(blank=True, choices=[(3, 'Bem'), (4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='fala',
            field=models.IntegerField(blank=True, choices=[(3, 'Bem'), (4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='ler',
            field=models.IntegerField(blank=True, choices=[(3, 'Bem'), (4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco')], null=True),
        ),
    ]