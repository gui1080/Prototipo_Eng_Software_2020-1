# Guilherme Braga - aprendendo Django

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser, Tesouro_Direto_CompraForm, AdvancedUserRegistrationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from home.models import Novo_Tesouro_Direto

from random import randint

# user teste, sem privilégios de adm
# user: testeagr
# password: Ag45fGhe095

def welcome(request):

    return render(request, 'welcome.html')

def tesouro_direto(request):
    tds = Novo_Tesouro_Direto.objects.all()

    form = Tesouro_Direto_CompraForm()
    context = { 'form':form,
                    'tds':tds }

    if request.method == 'POST':

        # formulario original a ser conferido abaixo
        form = Tesouro_Direto_CompraForm(request.POST)

        # copiando para compararmos o valor do produto dentro do Novo_Tesouro_Direto
        # com o valor da compra. Se o valor n corresponde ao minimo, impedimos a compra
        checando_validade = form.save(commit=False)
        produto = checando_validade.produto

        preco_minimo = int(produto.preco_unidade)
        preco_compra = int(checando_validade.valor)

        if (preco_compra < preco_minimo):
            # o comprador nao pode continuar!
            messages.warning(request, 'Por favor, compre pelo menos o valor mínimo para este produto!')
            return redirect('/home/tesouro_direto')

        if form.is_valid():
            instance=form.save(commit=False)
            instance.comprador = request.user
            instance.id_compra = randint(100000, 999999)
            instance.save()
            return redirect('/home')


    return render(request, 'tesouro_direto.html', context)


def home(request):

    return render(request, 'home.html')


def register(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()

            # messages.sucess(request, 'Acccount created!')

            return redirect('register_advanced')

    context = {'form':form}
    return render(request, 'register.html', context)

def advanced_register(request):

    form = AdvancedUserRegistrationForm()

    context = {'form':form}

    if request.method == 'POST':
        form = AdvancedUserRegistrationForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            return redirect('/login')


    return render(request, 'advanced_register.html', context)



def meu_cadastro(request):

    meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)

    context = { 'cadastro':meu_cadastro }

    return render(request, 'meu_cadastro.html', context)



def minhas_compras(request):

    compras = Tesouro_Direto_Compra.objects.filter(comprador = request.user)

    context = { 'compras':compras }


    return render(request, 'minhas_compras.html', context)


def alterar_dados(request):

    post = AdvancedUserRegistration.objects.get(usuario = request.user)

    if request.method == "POST":
        form = AdvancedUserRegistrationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('meu_cadastro')
    else:
        form = AdvancedUserRegistrationForm(instance=post)

    context = {'form': form}
    return render(request, 'advanced_register.html', context)

def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.sucess(request, 'Welcome!')
            return redirect('home')
        else:
            messages.info(request, 'bad login!')

    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
