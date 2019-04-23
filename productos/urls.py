from django.urls import path

from productos.views import CreateProduct , CatalogoList , CatalogoView , UpdateProducto

urlpatterns = [
    path('crear/producto/' , CreateProduct.as_view(), name='crear_producto'),
    path('ver/catalogo/lista' , CatalogoList.as_view() , name='catalogo_list'),
    path('catalogo' , CatalogoView.as_view() , name='catalogo'),
    path('editar/producto/<int:pk>/', UpdateProducto.as_view() , name='editar_producto')



]
