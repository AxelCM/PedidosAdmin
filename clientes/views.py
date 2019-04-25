#Imports From Django
from django.shortcuts import render , render_to_response
from django.urls import reverse ,reverse_lazy
from django.db.models import Q
from django.views.generic import FormView , TemplateView , UpdateView , DetailView , ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout , login

#Imports from Forms of Models
from clientes.forms import RegisterClientForm


#Imports from Models
from clientes.models import Cliente



#Vista para crear un nuevo cliente, se usa el form_class de los forms.py un
#reverse para poder regresar a un url cuando todo se haga correctamente
class Register(LoginRequiredMixin ,FormView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'clientes/form_register.html'
    form_class = RegisterClientForm
    success_url = reverse_lazy('list_client')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

#Vista para ver los detalles de un cliente
class ClienteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'clientes/client_detail.html'
    slug_field = 'id_cliente'
    slug_url_kwarg = 'id_cliente'
    queryset = Cliente.objects.all()
    context_object_name = 'cliente'

#Vista para Listar a los clientes de manera Paginada en grupos del valor de "paginate_by"
class ClientesView(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'clientes/client_list.html'
    model = Cliente
    paginate_by = 5
    queryset = clientes = Cliente.objects.all().order_by("-id_cliente")

    # def get_context_data(self, *args , **kwargs):
    #     clientes = Cliente.objects.all()
    #     return {'clientes' : clientes}

#Vista para actualizar o editar la informacion de un objecto de un Modelo
#fields contiene todos los atributos que se van a modificar en el proceso
class UpdateClient(LoginRequiredMixin, SuccessMessageMixin ,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
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
    success_message = 'El Cliente se actualizo con correctamente'
    template_name = 'clientes/form_update_cliente.html'

#Funcion para buscar un query en los registros
#results contiene los resultados de la busqueda\
@login_required
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
