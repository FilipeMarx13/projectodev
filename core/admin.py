from django.contrib import admin
from core.models import cadastro_pessoa
# Register your models here.

class pessoaadmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'idade',)


admin.site.register(cadastro_pessoa, pessoaadmin)


