from django.shortcuts import render , get_object_or_404 , render_to_response
from django.views.generic import FormView , CreateView , TemplateView , DetailView , DeleteView , UpdateView , ListView
from django.urls import reverse , reverse_lazy
from django.db.models import Q  , Sum , Avg , Count
from django.contrib.auth import get_user_model


from pedidos.models import PedidoVentas , ItemPedido , Abono , TipoPago
from productos.models import Producto
from clientes.models import Cliente
from pedidos.forms import PedidoForm , AddProductoForm , AbonoForm , AbonarForm

from datetime import *

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'productos/index.html'

    def get_context_data(self , *args , **kwargs):
        users = User.objects.all()
        return {'users' : users}



class CreatePedido(CreateView):

    template_name = 'pedidos/form_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('pedidos_hoy')

    def get_context_data(self, *args, **kwargs):
        clientes = Cliente.objects.all()
        return {"clientes": clientes}

class AddProducto(CreateView):

    template_name = 'pedidos/form_addproducto.html'
    form_class = AddProductoForm
    #success_url = reverse_lazy('pedidos_hoy')

    def get_context_data(self, *args, **kwargs):
        pedidos = PedidoVentas.objects.all()
        productos = Producto.objects.all()
        return {"pedidos": pedidos , "productos" : productos}

    def get_success_url(self):
        return reverse('detail_pedido', kwargs={'id_pedido' : self.object.id_pedido.id_pedido})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AddProducto, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs


class RemoveProducto(DeleteView):
    model = ItemPedido
    #success_url = reverse_lazy('ver_pedidos')
    template_name = 'pedidos/remove_product.html'

    def get_success_url(self):
        return reverse('detail_pedido', kwargs={'id_pedido' : self.object.id_pedido.id_pedido})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(DeleteView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

class UpdateProduct(UpdateView):
    model = ItemPedido
    fields = ['cantidad']
    template_name = 'pedidos/form_update_product.html'
    #success_url = reverse_lazy('ver_pedidos')

    def get_success_url(self):
        return reverse('detail_pedido', kwargs={'id_pedido' : self.object.id_pedido.id_pedido})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(UpdateProduct, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs



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
        context['productos'] = Producto.objects.all()
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
        hoy = date.today()
        productos = ItemPedido.objects.all().order_by("producto__nombre").distinct("producto__nombre")
        items = ItemPedido.objects.values('producto__nombre').distinct().order_by('producto__nombre')
        pd_hoy = ItemPedido.objects.filter(fecha=hoy).order_by("producto__nombre").distinct("producto__nombre")


        return {'productos' : productos , 'items' : items , 'pd_hoy' : pd_hoy , 'hoy':hoy}

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

def search_pedido(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(date__icontains=query)
            |Q(cliente__nombre_comercial__icontains=query)
            )
        results = PedidoVentas.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("pedidos/result.html", {"results": results ,"query": query })

def search_producto(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(codigo__icontains=query)
            |Q(nombre__icontains=query)
            )
        results = Producto.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("pedidos/widget_search_product.html", {"results": results ,"query": query})

def search_despacho(request):
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(create_at__icontains=query)
            )
        results = ItemPedido.objects.filter(qset) #.distinct("producto__nombre")
        cantidad = ItemPedido.objects.filter(qset).order_by('-cantidad').annotate(total=Count('cantidad'))
        items = cantidad.filter(qset).annotate(total=Sum('cantidad'))
        # valor = 0
        # for cant in cantidad:
        #     items = cant.cantidad

    else:
        results = []
        items = []
        cantidad = []
    return render_to_response("pedidos/search_despacho.html", {"results": results ,"query": query , "cantidad" : cantidad , "items" : items})

def search_estado_cuenta(request):
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(cliente__nombre_comercial__icontains=query)
            )
        results = PedidoVentas.objects.filter(qset)
    else:
        results = []
    return render_to_response("pedidos/estados_de_cuenta.html", {"results": results ,"query": query })

class PedidosHoy(ListView):
    hoy = date.today()
    template_name = 'pedidos/pedidos_del_dia.html'
    model = PedidoVentas
    paginate_by = 10
    queryset = PedidoVentas.objects.filter(date=hoy).order_by('date')

#Busqueda de cliente para pedidos
def iniciar_pedido_widget(request):
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(nombre_comercial__icontains=query)
            )
        results = Cliente.objects.filter(qset)
    else:
        results = []
    return render(request  ,"pedidos/iniciar_pedido.html", {"results": results ,"query": query })

# class CreatePedidoWidget(CreateView):
#     model = PedidoVentas
