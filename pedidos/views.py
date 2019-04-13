from django.shortcuts import render , get_object_or_404
from django.views.generic import FormView , CreateView , TemplateView , DetailView , DeleteView , UpdateView
from django.urls import reverse , reverse_lazy

from pedidos.models import PedidoVentas , ItemPedido , Abono , TipoPago
from productos.models import Producto
from clientes.models import Cliente
from pedidos.forms import PedidoForm , AddProductoForm , AbonoForm , AbonarForm

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
        context['abonos'] = Abono.objects.filter(id_pedido=id_pedidos)
        return context

def abonoNew(request):
    form = AbonoForm()
    return render(request, 'pedidos/tryforms.html', {'form': form})

class AddAbono(CreateView):

    template_name = 'pedidos/tryforms.html'
    form_class = AbonoForm
    success_url = reverse_lazy('index')

class AbonoAdd(CreateView):

    template_name = 'pedidos/form_abono.html'
    form_class = AbonoForm
    success_url = reverse_lazy('ver_saldo')

    def get_context_data(self, *args, **kwargs):
        pedidos = PedidoVentas.objects.all()
        tipo_pagos = TipoPago.objects.all()
        return {"pedidos": pedidos , "tipo_pagos" : tipo_pagos}


class SaldosViews(TemplateView):
    template_name = 'pedidos/saldos.html'

    def get_context_data(self , *args , **kwargs):

        pedidos = PedidoVentas.objects.all()
        abonos = Abono.objects.all()
        return {'pedidos': pedidos , 'abonos':abonos}

class DepachoDiarioView(TemplateView):
    template_name = 'pedidos/despacho.html'

    def get_context_data(self , *args , **kwargs):

        #productos = ItemPedido.objects.filter('producto_id').distinct()
        #item = Producto.objects.values_list("id_producto" , flat=True)
        #productos = ItemPedido.objects.filter(producto__id_producto=item).distinct()
        #productos = ItemPedido.objects.filter(producto__id_producto=item)
        productos = ItemPedido.objects.all().order_by("producto__nombre").distinct("producto__nombre")
        #productos = ItemPedido.objects.values_list("producto__id_producto").distinct()
        items = ItemPedido.objects.values('producto__nombre').distinct().order_by('producto__nombre')
        #productos = ItemPedido.objects.values('producto__nombre').distinct()
        #producto = ItemPedido.objects.values('producto__nombre').distinct()
        #items = ItemPedido.objects.filter(producto__nombre='producto')

        #items = ItemPedido.objects.all().order_by('producto')
        return {'productos' : productos , 'items' : items  }

class AbonarView(CreateView):
    template_name = 'pedidos/form_abono_2.html'
    form_class = AbonarForm
    success_url = reverse_lazy('abono_list')

    def get_context_data(self, *args, **kwargs):
        pedidos = PedidoVentas.objects.all()
        tipo_pagos = TipoPago.objects.all()
        return {"pedidos": pedidos , "tipo_pagos" : tipo_pagos}

class UpdateAbono(UpdateView):
    model = Abono
    fields = ['cantidad' , 'observaciones']
    success_url = reverse_lazy('index')
    template_name = 'pedidos/form_update_abono.html'

class AbonoList(TemplateView):
    template_name = 'pedidos/ultimo_abono.html'

    def get_context_data(self, *args, **kwargs):
        id = Abono.objects.all().order_by('-fecha')
        abonos = id[1:6]
        ultimo_abono = id[0]
        return {"abonos": abonos , "ultimo_abono" : ultimo_abono }
