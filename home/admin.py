from django.contrib import admin

# Register your models here.

from home.models import Novo_Tesouro_Direto
from home.models import Tesouro_Direto_Compra
from home.models import AdvancedUserRegistration

admin.site.register(Novo_Tesouro_Direto)
admin.site.register(Tesouro_Direto_Compra)
admin.site.register(AdvancedUserRegistration)
