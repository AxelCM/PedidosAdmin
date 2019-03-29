from django.urls import path

from clientes.views import Register

urlpatterns = [
    path('registrar/cliente/' , Register.as_view() , name='register_client'),

]
