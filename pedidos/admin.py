from django.contrib import admin

from pedidos.models import PedidoVentas , ItemPedido
# Register your models here.


class PedidoVentasAdmin(admin.ModelAdmin):
    raw_id_fields = ( "cliente",)
    search_fields = ['cliente' , 'id_pedido' , 'date']
    list_display = ['id_pedido' , 'cliente' , 'date' , 'totalpedido' , 'conteoItems']



class ItemPedidoAdmin(admin.ModelAdmin):
    raw_id_fields = ("producto",)
    search_fields = ['id_producto']
    list_display = ['id_pedido','cantidad', 'producto' , 'sub_total' ]


admin.site.register(PedidoVentas, PedidoVentasAdmin)
admin.site.register(ItemPedido , ItemPedidoAdmin)
