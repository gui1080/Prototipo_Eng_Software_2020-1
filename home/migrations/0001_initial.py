# Generated by Django 3.0.7 on 2020-06-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novo_Tesouro_Direto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('vencimento', models.DateField()),
                ('indexador', models.CharField(max_length=255)),
                ('taxa', models.CharField(max_length=255)),
                ('preco_unidade', models.CharField(max_length=255)),
            ],
        ),
    ]
