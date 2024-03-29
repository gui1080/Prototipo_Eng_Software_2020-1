"""eng_soft_prototipo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.welcome, name="welcome"),

    # manipulando usuario
    path('register/', views.register, name="register"),
    path('register/advanced_register', views.advanced_register, name="register_advanced"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    # paginas disponiveis ao usuario
    path('home/', views.home, name="home"),
    path('minhas_compras/', views.minhas_compras, name="minhas_compras"),
    path('minhas_compras/deletar_td/<int:Tesouro_Direto_Compra_id>', views.deletar_TesouroDireto, name="deletar_TesouroDireto"),
    path('minhas_compras/deletar_fi/<int:fundo_de_investimento_id>', views.deletar_FundodeInvestimento, name="deletar_FundodeInvestimento"),
    path('minhas_compras/deletar_rf/<int:renda_fixa_id>', views.deletar_RendaFixa, name="deletar_RendaFixa"),
    path('meu_cadastro/', views.meu_cadastro, name="meu_cadastro"),
    path('home/tesouro_direto/', views.tesouro_direto, name="tesouro_direto"),
    path('home/fundo_de_investimento/', views.fundo_de_investimento, name="fundo_de_investimento"),
    path('home/renda_fixa/', views.renda_fixa, name="renda_fixa"),
    path('meu_cadastro/alterar_dados/', views.alterar_dados, name="alterar_dados"),

]
