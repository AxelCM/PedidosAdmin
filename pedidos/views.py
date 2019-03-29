from django.shortcuts import render , get_object_or_404
from django.views.generic import FormView , CreateView , TemplateView , DetailView , DeleteView , UpdateView
from django.urls import reverse , reverse_lazy

from pedidos.models import PedidoVentas , ItemPedido
from productos.models import Producto
from clientes.models import Cliente
from pedidos.forms import PedidoForm , AddProductoForm

class CreatePedido(CreateView):

    template_name = 'pedidos/form_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('ver_pedidos')

    def get_context_data(self, *args, **kwargs):
        clientes = Cliente.objects.all()
        return {"clientes": clientes}

class AddProducto(CreateView):

    template_name = 'pedidos/form_addproducto.html'
    form_class = AddProductoForm
    success_url = reverse_lazy('agregar_producto')

    def get_context_data(self, *args, **kwargs):
        pedidos = PedidoVentas.objects.all()
        productos = Producto.objects.all()
        return {"pedidos": pedidos , "productos" : productos}

class RemoveProducto(DeleteView):
    model = ItemPedido
    success_url = reverse_lazy('ver_pedidos')
    template_name = 'pedidos/remove_product.html'

class UpdateProduct(UpdateView):
    model = ItemPedido
    fields = ['cantidad']
    success_url = reverse_lazy('ver_pedidos')
    template_name = 'pedidos/form_update_product.html'

class PedidoView(TemplateView):

    template_name='pedidos/ver_pedidos.html'

    def get_context_data(self , *args , **kwargs):
        pedidos = PedidoVentas.objects.all().order_by('cliente')
        return {'ped': pedidos}

#
# def detail_pedido(request, id_pedido):
#     pedidos = PedidoVentas.objects.get(pk=id_pedido)
#     items = ItemPedido.objects.filter(id_pedido=pedidos)
#     return render(request, 'pedidos/detail_pedido.html', {'items': items , 'pedido' : pedidos})

class PedidoDetailView(DetailView):
    """User detail view."""

    template_name = 'pedidos/detail_pedido.html'
    slug_field = 'id_pedido'
    slug_url_kwarg = 'id_pedido'
    queryset = PedidoVentas.objects.all()
    context_object_name = 'pedido'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        id_pedidos = self.get_object()
        context['items'] = ItemPedido.objects.filter(id_pedido=id_pedidos)
        return context
