from django.urls import path

from productos.views import CreateProduct

urlpatterns = [
    path('crear/producto/' , CreateProduct.as_view(), name='crear_producto'),



]
