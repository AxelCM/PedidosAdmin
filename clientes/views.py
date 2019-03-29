from django.shortcuts import render
from django.urls import reverse ,reverse_lazy
from django.views.generic import FormView
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
