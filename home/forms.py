from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import Tesouro_Direto_Compra, AdvancedUserRegistration, Fundo_Investimento_Compra, Renda_Fixa_Compra

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

# criação de user é uma modificação da criação default
# documentação: https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AdvancedUserRegistrationForm(ModelForm):

    class Meta:
        model = AdvancedUserRegistration
        fields = ['nome', 'endereco', 'telefone', 'cep', 'cod_banco', 'cod_agencia', 'numero_de_conta', 'cpf']
