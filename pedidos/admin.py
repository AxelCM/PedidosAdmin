from django.contrib import admin

from pedidos.models import PedidoVentas , ItemPedido , Abono , TipoPago
# Register your models here.


class PedidoVentasAdmin(admin.ModelAdmin):
    raw_id_fields = ( "cliente",)
    search_fields = ['cliente' , 'id_pedido' , 'date']
    list_display = ['id_pedido' , 'cliente' , 'date' , 'totalpedido' , 'conteoItems' , 'Saldo']



class ItemPedidoAdmin(admin.ModelAdmin):
    raw_id_fields = ("producto",)
    search_fields = ['id_producto']
    list_display = ['id_pedido','cantidad', 'producto' , 'sub_total' , 'itemtotal']

class AbonoAdmin(admin.ModelAdmin):
    list_display = ['id_abono' , 'id_pedido' , 'fecha' , 'totalpedido', 'cantidad' ,  'Saldo']

class TipoPagoAdmin(admin.ModelAdmin):

    list_display = ['tipo_pago' , 'pk']


admin.site.register(PedidoVentas, PedidoVentasAdmin)
admin.site.register(Abono , AbonoAdmin)
admin.site.register(ItemPedido , ItemPedidoAdmin)
admin.site.register(TipoPago , TipoPagoAdmin)
