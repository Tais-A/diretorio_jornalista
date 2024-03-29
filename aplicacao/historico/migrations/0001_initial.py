# Generated by Django 4.0.6 on 2022-07-24 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0001_initial'),
        ('opcoes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=254)),
                ('cargo', models.CharField(max_length=254)),
                ('data_inicio', models.DateField()),
                ('data_de_termino', models.DateField()),
                ('duracao', models.TextField()),
                ('referencia', models.CharField(max_length=254)),
                ('contato_da_referencia', models.CharField(max_length=254)),
                ('validado', models.BooleanField(blank=True, null=True)),
                ('revisor_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.revisor')),
                ('veiculo_de_comunicacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opcoes.veiculodecomunicacao')),
            ],
        ),
    ]
