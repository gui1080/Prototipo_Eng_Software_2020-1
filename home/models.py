from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

# Create your models here.

# RENDA FIXA
class Novo_Renda_Fixa(models.Model):

    CLASSE = (
    ('CDB', 'CDB'),
    ('LCA', 'LCA'),
    ('LCI', 'LCI'),
    ('LF', 'LF'),
    ('LC', 'LC'),
    )

    nome = models.CharField(max_length=255)
    vencimento = models.PositiveIntegerField()
    classe = models.CharField(max_length=255, null=True, choices=CLASSE)
    horario_limite = models.CharField(max_length=255)
    preco_unidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
        # retorna o titulo como string para aparecer na listagem de posts

# COMPRANDO RENDA FIXA
class Renda_Fixa_Compra(models.Model):

    comprador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    valor = models.PositiveIntegerField()
    produto = models.ForeignKey(Novo_Renda_Fixa, null=True, on_delete=models.SET_NULL)
    id_compra = models.PositiveIntegerField(default='123456')
    dia_da_compra = models.DateField(("Date"), default=datetime.date.today)

# FUNDO DE INVESTIMENTO
class Novo_Fundo_Investimento(models.Model):

    CLASSE = (
    ('Ação', 'Ação'),
    ('Cambial', 'Cambial'),
    ('Multimercado', 'Multimercado'),
    ('Renda Fixa', 'Renda Fixa'),
    )

    PRAZO = (
    ('D+1', 'D+1'),
    ('D+4', 'D+4'),
    ('D+30', 'D+30'),
    ('D+60', 'D+60'),
    )

    nome = models.CharField(max_length=255)
    preco_unidade = models.PositiveIntegerField()
    classe = models.CharField(max_length=255, null=True, choices=CLASSE)
    prazo = models.CharField(max_length=255, null=True, choices=PRAZO)
    def __str__(self):
        return self.nome
        # retorna o titulo como string para aparecer na listagem de posts

# COMPRANDO FUNDO DE INVESTIMENTO
class Fundo_Investimento_Compra(models.Model):

    comprador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    valor = models.PositiveIntegerField()
    produto = models.ForeignKey(Novo_Fundo_Investimento, null=True, on_delete=models.SET_NULL)
    id_compra = models.PositiveIntegerField(default='123456')
    dia_da_compra = models.DateField(("Date"), default=datetime.date.today)

# TESOURO DIRETO
class Novo_Tesouro_Direto(models.Model):

    INDEXADOR = (
    ('IPCA', 'IPCA'),
    ('SELIC', 'SELIC'),
    ('Prefixado', 'Prefixado'),
    )

    nome = models.CharField(max_length=255)
    vencimento = models.DateField()
    indexador = models.CharField(max_length=255, null=True, choices=INDEXADOR)
    taxa = models.CharField(max_length=255)
    preco_unidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
        # retorna o titulo como string para aparecer na listagem de posts

# COMPRANDO TESOURO DIRETO
class Tesouro_Direto_Compra(models.Model):

    comprador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    valor = models.PositiveIntegerField()
    produto = models.ForeignKey(Novo_Tesouro_Direto, null=True, on_delete=models.SET_NULL)
    id_compra = models.PositiveIntegerField(default='123456')
    dia_da_compra = models.DateField(("Date"), default=datetime.date.today)

    # def __str__(self):
        # return self.valor

# PEGANDO INFOS DO USUARIO
# o usuario fica atrelado a cada registro de advanced register
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
