from django.contrib import admin

# Register your models here.

from home.models import Novo_Tesouro_Direto
from home.models import Tesouro_Direto_Compra
from home.models import AdvancedUserRegistration
from home.models import Novo_Fundo_Investimento
from home.models import Fundo_Investimento_Compra
from home.models import Renda_Fixa_Compra
from home.models import Novo_Renda_Fixa

# cada usuario default tem um cadastro de campos extra
admin.site.register(AdvancedUserRegistration)

# Tesouro direto - criar e comprar
admin.site.register(Novo_Tesouro_Direto)
admin.site.register(Tesouro_Direto_Compra)

# Fundo de investimento - criar e comprar
admin.site.register(Novo_Fundo_Investimento)
admin.site.register(Fundo_Investimento_Compra)

# Renda fixa - criar e comprar
admin.site.register(Novo_Renda_Fixa)
admin.site.register(Renda_Fixa_Compra)
