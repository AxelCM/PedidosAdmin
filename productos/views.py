#from django
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render , get_object_or_404 , render_to_response
from django.urls import reverse , reverse_lazy
from django.views.generic import View , TemplateView , DetailView , CreateView , ListView , UpdateView , DeleteView

#from models
from productos.models import Producto , Categoria
from productos.forms import ProductoForm , CategoriaForm

#from others
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class CatalogoList(ListView):
    model = Producto

    template_name = 'productos/catalogo_list.html'
    paginate_by = 25
    queryset = productos = Producto.objects.all().order_by("nombre")

class CatalogoView(TemplateView):
    template_name = 'productos/catalogo.html'


    def get_context_data(request , *args , **kwargs):
        productos = Producto.objects.all()
        categorias = Categoria.objects.all().order_by('nombre')
        return {'productos': productos , 'categorias': categorias}

class UpdateProducto(UpdateView):
    model = Producto
    fields = ['nombre',
            'picture',
            'codigo',
            'precio',
        ]
    success_url = reverse_lazy('catalogo_list')
    template_name = 'productos/form_update_producto.html'

class HomeView(View):
    def get(self , request , *args , **kwargs):
        return render(request, 'productos/charts.html', {})

def get_data(request , *args , **kwards):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class CharData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        users = User.objects.all().count()
        products = Producto.objects.all().count()
        labels = ['Vendedores', 'Productos', 'Prueba', 'Otros2', 'Purple', 'Orange']
        default_items = [users, products, 5, 8, 11, 12]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

class ProductoDetailView(DetailView):
    """User detail view."""

    template_name = 'productos/product.html'
    slug_field = 'id_producto'
    slug_url_kwarg = 'id_producto'
    queryset = Producto.objects.all()
    context_object_name = 'productos'


def view_product(request, id_producto):
    productos = Producto.objects.get(pk=id_producto)
    return render(request, 'productos/product.html', {'productos': productos })

class CreateProduct(CreateView):

    template_name = 'productos/form_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('catalogo')

    def get_context_data(self , *args , **kwargs):
        categorias = Categoria.objects.all()
        return {'categorias' : categorias}

##############################################

class CreateCategoria(CreateView):

    template_name = 'productos/form_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('index')

class UpdateCategoria(UpdateView):
    model = Categoria
    fields = ['nombre',
        ]
    success_url = reverse_lazy('list_categoria')
    template_name = 'productos/form_update_categoria.html'

class RemoveCategoria(DeleteView):
    model = Categoria
    success_url = reverse_lazy('list_categoria')
    template_name = 'productos/remove_categoria.html'

class CategoriaList(ListView):
    model = Categoria
    template_name = 'productos/categoria_list.html'
    paginate_by = 10
    queryset = Categoria.objects.all().order_by("nombre")



def search_producto(request):
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(nombre__icontains=query)
            | Q(codigo__icontains=query)
            )
        results = Producto.objects.filter(qset)
    else:
        results = []
    return render_to_response("productos/search_producto.html", {"results": results ,"query": query })

def search_producto_categoria(request):
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(categoria__nombre__icontains=query)
            # | Q(codigo__icontains=query)
            )
        results = Producto.objects.filter(qset)
    else:
        results = []
    return render_to_response("productos/search_producto_categoria.html", {"results": results ,"query": query })
