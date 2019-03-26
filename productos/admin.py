from django.contrib import admin

from productos.models import Producto

class ProductoAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'precio' , 'precio_IVA']
    search_fields  = ['nombre']




admin.site.register(Producto , ProductoAdmin)
