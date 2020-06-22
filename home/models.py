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

    # def __str__(self):
        # return self.valor

class AdvancedUserRegistration(models.Model):

    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #endereco
    #telefone
    #cep
    #cpf
    #cod_banco
    #cod_agencia
    #num_conta
    #nome
