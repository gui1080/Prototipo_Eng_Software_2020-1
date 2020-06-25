from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import Tesouro_Direto_Compra, AdvancedUserRegistration, Fundo_Investimento_Compra, Renda_Fixa_Compra

# nos formularios de compra nos interessa apenas o produto e quanto se vai comprar

class Renda_Fixa_CompraForm(ModelForm):

    class Meta:
        model = Renda_Fixa_Compra
        fields = ['valor', 'produto']

class Tesouro_Direto_CompraForm(ModelForm):

    class Meta:
        model = Tesouro_Direto_Compra
        fields = ['valor', 'produto']

class Fundo_Investimento_CompraForm(ModelForm):

    class Meta:
        model = Fundo_Investimento_Compra
        fields = ['valor', 'produto']

# criação de user default facilita os processos de login e logout
# documentação: https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# nesse formulario se pegam as info do user, cada registro fica atrelado a um user default
class AdvancedUserRegistrationForm(ModelForm):

    class Meta:
        model = AdvancedUserRegistration
        fields = ['nome', 'endereco', 'telefone', 'cep', 'cod_banco', 'cod_agencia', 'numero_de_conta', 'cpf']
