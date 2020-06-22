from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Novo_Tesouro_Direto(models.Model):
    nome = models.CharField(max_length=255)
    vencimento = models.DateField()
    indexador = models.CharField(max_length=255)
    taxa = models.CharField(max_length=255)
    preco_unidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
        # retorna o titulo como string para aparecer na listagem de posts

class Tesouro_Direto_Compra(models.Model):

    comprador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    valor = models.PositiveIntegerField()
    produto = models.ForeignKey(Novo_Tesouro_Direto, null=True, on_delete=models.SET_NULL)
    id_compra = models.PositiveIntegerField(default='123456')
    #dia_da_compra = models.DateField(auto_now_add=True)

    # def __str__(self):
        # return self.valor

class AdvancedUserRegistration(models.Model):

    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=155)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    cod_banco = models.DecimalField(decimal_places=0,max_digits=7)
    cod_agencia = models.DecimalField(decimal_places=0,max_digits=6)
    numero_de_conta = models.DecimalField(decimal_places=0,max_digits=30)
    cpf = models.DecimalField(decimal_places=0,max_digits=11)

    def __str__(self):
        return self.nome
