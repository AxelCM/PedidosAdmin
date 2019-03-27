from django.contrib import admin

from productos.models import Producto , Categoria

class ProductoAdmin(admin.ModelAdmin):

    list_display = ['nombre']
    search_fields  = ['nombre']


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nombre']

admin.site.register(Producto , ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
