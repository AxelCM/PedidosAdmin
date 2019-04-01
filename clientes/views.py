from django.shortcuts import render
from django.urls import reverse ,reverse_lazy
from django.views.generic import FormView , TemplateView , UpdateView , DetailView
from clientes.forms import RegisterClientForm

from clientes.models import Cliente

# Create your views here.
class Register(FormView):

    template_name = 'clientes/form_register.html'
    form_class = RegisterClientForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class ClienteDetailView(DetailView):
    template_name = 'clientes/client_detail.html'
    slug_field = 'id_cliente'
    slug_url_kwarg = 'id_cliente'
    queryset = Cliente.objects.all()
    context_object_name = 'cliente'

class ClientesView(TemplateView):
    template_name = 'clientes/client_list.html'

    def get_context_data(self, *args , **kwargs):
        clientes = Cliente.objects.all()
        return {'clientes' : clientes}


class UpdateClient(UpdateView):
    model = Cliente
    fields = ['n_representante',
            'nombre_comercial',
            'telefono',
            'direccion',
            'mayorista',
            'email',
            'nit',
        ]
    success_url = reverse_lazy('list_client')
    template_name = 'clientes/form_update_cliente.html'
