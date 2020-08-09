#imports from Django
from django.contrib import admin


#imports from Models
from clientes.models import Cliente



#Clase adminsitrativa para uso del Admin de Django
class ClienteAdmin(admin.ModelAdmin):

    list_display = ['nombre' ,'id_cliente' ,  'direccion' , 'nit']

#Registro de las vistas del Admin de Django
admin.site.register(Cliente , ClienteAdmin)
