from django.contrib import admin

from clientes.models import Cliente
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):

    list_display = ['nombre_comercial' ,'id_cliente' ,  'direccion' , 'nit']

admin.site.register(Cliente , ClienteAdmin)
