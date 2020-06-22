# Generated by Django 3.0.7 on 2020-06-18 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tesouro_direto_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesouro_direto_compra',
            name='data_compra',
        ),
        migrations.AddField(
            model_name='tesouro_direto_compra',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Novo_Tesouro_Direto'),
        ),
    ]
