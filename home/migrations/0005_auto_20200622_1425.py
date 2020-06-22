# Generated by Django 3.0.7 on 2020-06-22 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20200619_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novo_tesouro_direto',
            name='preco_unidade',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='AdvancedUserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=9)),
                ('cod_banco', models.DecimalField(decimal_places=0, max_digits=7)),
                ('cod_agencia', models.DecimalField(decimal_places=0, max_digits=6)),
                ('numero_de_conta', models.DecimalField(decimal_places=0, max_digits=30)),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=11)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
