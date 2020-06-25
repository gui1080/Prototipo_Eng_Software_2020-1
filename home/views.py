# Guilherme Braga - aprendendo Django

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser, Tesouro_Direto_CompraForm, AdvancedUserRegistrationForm, Fundo_Investimento_CompraForm, Renda_Fixa_CompraForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from home.models import Novo_Tesouro_Direto

from random import randint


#-----------------------------------------------------------------------------------------

# pagina de quem acaba de entrar no site, com area de registro, login e visita
def welcome(request):

    return render(request, 'welcome.html')

# pagina default com produtos e servicos
def home(request):

    return render(request, 'home.html')

#-----------------------------------------------------------------------------------------

# vendo os produtos disponiveis (o superuser cadastra isso na pagina de adm)

def fundo_de_investimento(request):

    try:
        meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)
    except AdvancedUserRegistration.DoesNotExist:
        meu_cadastro = None

    fis = Novo_Fundo_Investimento.objects.all()

    form = Fundo_Investimento_CompraForm()

    context = {'form':form,
                'fis':fis,
                'cadastro':meu_cadastro,
    }

    if request.method == 'POST':

        # formulario original a ser conferido abaixo
        form = Fundo_Investimento_CompraForm(request.POST)

        checando_validade = form.save(commit=False)
        produto = checando_validade.produto

        preco_minimo = int(produto.preco_unidade)
        preco_compra = int(checando_validade.valor)

        if (preco_compra < preco_minimo):
            # o comprador nao pode continuar!
            messages.warning(request, 'Por favor, compre pelo menos o valor mínimo para este produto!')
            return redirect('/home/fundo_de_investimento')

        if form.is_valid():
            instance=form.save(commit=False)
            instance.comprador = request.user
            instance.id_compra = randint(100000, 999999)
            instance.save()
            return redirect('/home')

    return render(request, 'fundo_de_investimento.html', context)



def renda_fixa(request):

    try:
        meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)
    except AdvancedUserRegistration.DoesNotExist:
        meu_cadastro = None

    rfs = Novo_Renda_Fixa.objects.all()

    form = Renda_Fixa_CompraForm()

    context = { 'form':form, 'rfs':rfs, 'cadastro':meu_cadastro, }

    if request.method == 'POST':

        # formulario original a ser conferido abaixo
        form = Renda_Fixa_CompraForm(request.POST)

        checando_validade = form.save(commit=False)
        produto = checando_validade.produto

        preco_minimo = int(produto.preco_unidade)
        preco_compra = int(checando_validade.valor)

        if (preco_compra < preco_minimo):
            # o comprador nao pode continuar!
            messages.warning(request, 'Por favor, compre pelo menos o valor mínimo para este produto!')
            return redirect('/home/renda_fixa')

        if form.is_valid():
            instance=form.save(commit=False)
            instance.comprador = request.user
            instance.id_compra = randint(100000, 999999)
            instance.save()
            return redirect('/home')

    return render(request, 'renda_fixa.html', context)



def tesouro_direto(request):

    try:
        meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)
    except AdvancedUserRegistration.DoesNotExist:
        meu_cadastro = None


    tds = Novo_Tesouro_Direto.objects.all()

    form = Tesouro_Direto_CompraForm()
    context = { 'form':form,
                'tds':tds,
                'cadastro':meu_cadastro,
               }

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


#-----------------------------------------------------------------------------------------

# deletando as compras do usuario

def deletar_TesouroDireto(request, Tesouro_Direto_Compra_id):

    compra = Tesouro_Direto_Compra.objects.get(pk=Tesouro_Direto_Compra_id)
    compra.delete()

    return redirect('/home')



def deletar_FundodeInvestimento(request, fundo_de_investimento_id):

    compra = Fundo_Investimento_Compra.objects.get(pk=fundo_de_investimento_id)
    compra.delete()

    return redirect('/home')



def deletar_RendaFixa(request, renda_fixa_id):

    compra = Renda_Fixa_Compra.objects.get(pk=renda_fixa_id)
    compra.delete()

    return redirect('/home')


#-----------------------------------------------------------------------------------------

# manipulando usuarios e cadastros

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



def logout_user(request):

    logout(request)
    return redirect('login')


#-----------------------------------------------------------------------------------------

# area default do que o usuario pode fazer ao se autenticar

login_required(login_url='login')
def meu_cadastro(request):

    try:
        meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)
    except AdvancedUserRegistration.DoesNotExist:
        meu_cadastro = None

    print(meu_cadastro)

    context = { 'cadastro':meu_cadastro }

    return render(request, 'meu_cadastro.html', context)


login_required(login_url='login')
def minhas_compras(request):

    try:
        meu_cadastro = AdvancedUserRegistration.objects.get(usuario = request.user)
    except AdvancedUserRegistration.DoesNotExist:
        meu_cadastro = None

    compras_td = Tesouro_Direto_Compra.objects.filter(comprador = request.user)
    compras_fi = Fundo_Investimento_Compra.objects.filter(comprador = request.user)
    compras_rf = Renda_Fixa_Compra.objects.filter(comprador = request.user)

    context = { 'compras_td':compras_td, 'compras_fi':compras_fi, 'compras_rf':compras_rf, 'cadastro':meu_cadastro }


    return render(request, 'minhas_compras.html', context)



login_required(login_url='login')
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
