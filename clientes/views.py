from django.shortcuts import render , render_to_response
from django.urls import reverse ,reverse_lazy
from django.db.models import Q
from django.views.generic import FormView , TemplateView , UpdateView , DetailView , ListView
from clientes.forms import RegisterClientForm

from clientes.models import Cliente

# Create your views here.
class Register(FormView):

    template_name = 'clientes/form_register.html'
    form_class = RegisterClientForm
    success_url = reverse_lazy('list_client')


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

class ClientesView(ListView):
    template_name = 'clientes/client_list.html'
    model = Cliente
    paginate_by = 5
    queryset = clientes = Cliente.objects.all().order_by("-id_cliente")

    # def get_context_data(self, *args , **kwargs):
    #     clientes = Cliente.objects.all()
    #     return {'clientes' : clientes}


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


def search_cliente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre_comercial__icontains=query)
            # |Q(nombre_comercial__icontains=query)
            )
        results = Cliente.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("clientes/result.html", {"results": results ,"query": query})
