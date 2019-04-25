from django.urls import path

from productos.views import (CreateProduct , CatalogoList , CatalogoView , UpdateProducto ,
CreateCategoria, RemoveCategoria, CategoriaList , UpdateCategoria , search_producto , search_producto_categoria,
LoginView , LogoutView
)

urlpatterns = [
    path('crear/producto/' , CreateProduct.as_view(), name='crear_producto'),
    path('crear/categoria/' , CreateCategoria.as_view(), name='crear_categoria'),
    path('ver/catalogo/lista' , CatalogoList.as_view() , name='catalogo_list'),
    path('ver/categoria/lista/' , CategoriaList.as_view() , name='list_categoria'),
    path('catalogo' , CatalogoView.as_view() , name='catalogo'),
    path('editar/producto/<int:pk>/', UpdateProducto.as_view() , name='editar_producto'),
    path('editar/categoria/<int:pk>/', UpdateCategoria.as_view() , name='editar_categoria'),
    path('eliminar/categoria/<int:pk>/' , RemoveCategoria.as_view() , name='remove_categoria'),
    path('eliminar/categoria/<int:pk>/' , RemoveCategoria.as_view() , name='remove_categoria'),
    path('buscar/producto/' , search_producto , name='buscar_producto'),
    path('buscar/producto/categoria' , search_producto_categoria , name='buscar_producto_categoria'),
    path('login' , LoginView.as_view() , name='login'),
    path('logout' , LoginView.as_view() , name='logout'),





]
