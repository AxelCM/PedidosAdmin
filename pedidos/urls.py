from django import urls

from django.urls import path
from productos.views import ProductoDetailView
from pedidos.views import (IndexView, CreatePedido , PedidoView , PedidoDetailView ,
AddProducto , RemoveProducto , UpdateProduct ,abonoNew , AddAbono , SaldosViews,
AbonoAdd , DepachoDiarioView , AbonarView , UpdateAbono , AbonoList , search_pedido, search_producto,
search_despacho , PedidosHoy , search_estado_cuenta , iniciar_pedido_widget ,
PDFPedidoDetailView , despachoYPedidos , search_abono , iniciar_abono_widget,
search_reporte_pedidos_abonos , PDFPedidoAbonosDetailView , PDFDepachoDiarioView ,
FinalizarPedido, PedidosSinFinalizar,RemovePedido, PDFPedidosHoy , PDFCierreDiario,
search_abono_fecha ,reactivarPedido , DesactivarPedido
)

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('crear/pedido/' , CreatePedido.as_view() , name='iniciar_pedido'),
    path('ver/abono/lista' , AbonoList.as_view() , name='abono_list'),
    path('ver/pedidos/hoy' , PedidosHoy.as_view() , name='pedidos_hoy'),
    #path('crear/abono/' , AddAbono.as_view() , name='addAbono'),
    path('ingresar/abono' , AbonarView.as_view() , name='ingresar_abono'),
    path('crear/abono/' , AbonoAdd.as_view() , name='create_abono'),
    path('ver/saldos/' , SaldosViews.as_view() , name='ver_saldo'),
    path('add/product/' , AddProducto.as_view() , name='agregar_producto'),
    path('remove/product/<int:pk>/' , RemoveProducto.as_view() , name='remove_product'),
    path('remove/pedido/<int:pk>/' , RemovePedido.as_view() , name='remove_pedido'),
    path('update/product/<int:pk>/' , UpdateProduct.as_view() , name='update_product'),
    path('update/abono/<int:pk>/' , UpdateAbono.as_view() , name='update_abono'),
    path('ver/pedidos/' , PedidoView.as_view() , name='ver_pedidos'),
    path('ver/pedidos/sin_finalizar' , PedidosSinFinalizar.as_view() , name='pedidos_sin_finalizar'),
    path('hacer/abono/' , abonoNew , name='hacer_abono'),
    path('detail/pedido/<int:id_pedido>/' , PedidoDetailView.as_view() , name='detail_pedido'),
    path('detail/producto/<int:id_producto>/' , ProductoDetailView.as_view() , name='detail_producto'),
    #path('detail/pedido/(?P<id_pedido>[0-9])/$' , detail_pedido , name='detail_pedido'),
    path('search/pedido/', search_pedido , name="search_pedido"),
    path('search/producto/', search_producto , name="search_producto"),
    path('search/despacho/', search_despacho , name="search_despacho"),
    path('search/estado_cuenta/', search_estado_cuenta , name="search_estado_cuenta"),
    path('iniciar/pedido/' , iniciar_pedido_widget , name="init_pedido"),
    path('abonar/' , iniciar_abono_widget , name="init_abono"),
    #path('reporte/pedido/' , PedidoPDF.as_view() , name="reporte_pedido"),
    path('reporte/pedido/<int:id_pedido>/' , PDFPedidoDetailView.as_view() , name="reporte_pedido"),
    path('search/pedido/despachos/' , despachoYPedidos , name="despacho_pedido"),
    path('search/abono/' , search_abono  , name="search_abono"),
    path('search/reporte/pedidos/abonos/' , search_reporte_pedidos_abonos , name="search_reporte_pedido_abonos"),
    path('reporte/pedido/abonos/<int:id_pedido>/' , PDFPedidoAbonosDetailView.as_view() , name="reporte_pedido_abonos"),
    path('reporte/pedido/despacho/hoy/' , PDFDepachoDiarioView.as_view() , name='reporte_pedidos_hoy'),
    path('reporte/pedido/hoy/' , PDFPedidosHoy.as_view() , name='pdfreporte_pedidos_hoy'),
    path('cierre/diario/hoy/' , PDFCierreDiario.as_view() , name='cierre_diario'),
    path('finalizar/pedido/<int:id>/', FinalizarPedido , name="finalizar_pedido"),
    path('search/abono/fecha/' , search_abono_fecha , name='search_abono_fecha'),
    path('debugger/pedidos/' , reactivarPedido , name='activar_pedidos'),
    path('debugger/pedidos/desactivar/' , DesactivarPedido , name='desactivar_pedidos'),





]
