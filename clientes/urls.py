from django.urls import path

from clientes.views import Register , ClientesView  , ClienteDetailView , UpdateClient

urlpatterns = [
    path('registrar/cliente/' , Register.as_view() , name='register_client'),
    path('detail/clientes/<int:id_cliente>/' , ClienteDetailView.as_view() , name='detail_client'),
    path('ver/clientes/' , ClientesView.as_view() , name='list_client'),
    path('actualizar/cliente/<int:pk>/' , UpdateClient.as_view() , name='update_client')
    #path('editar/cliente/<int:pk>/' , UpdateClient.as_view() , name='update_client'),

]
