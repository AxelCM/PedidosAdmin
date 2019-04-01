from django import urls

from django.urls import path
from pedidos.views import CreatePedido , PedidoView , PedidoDetailView , AddProducto , RemoveProducto , UpdateProduct

urlpatterns = [
    path('crear/pedido/' , CreatePedido.as_view() , name='iniciar_pedido'),
    path('add/product/' , AddProducto.as_view() , name='agregar_producto'),
    path('remove/product/<int:pk>/' , RemoveProducto.as_view() , name='remove_product'),
    path('update/product/<int:pk>/' , UpdateProduct.as_view() , name='update_product'),
    path('ver/pedidos/' , PedidoView.as_view() , name='ver_pedidos'),
    path('detail/pedido/<int:id_pedido>/' , PedidoDetailView.as_view() , name='detail_pedido'),
    #path('detail/pedido/(?P<id_pedido>[0-9])/$' , detail_pedido , name='detail_pedido'),

]