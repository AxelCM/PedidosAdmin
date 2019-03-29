"""AdminPedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import  static
from django.conf import settings
from django.conf.urls import url
from productos.views import HomeView , get_data , CharData , CatalogoView  ,  view_product , IndexView
from pedidos.views import PedidoDetailView

urlpatterns = [
    url('home' , HomeView.as_view() , name='home'),
    url('detail/pedido/<int:id_pedido>/', PedidoDetailView.as_view() , name='detail_pedido'),
    url('catalogo' , CatalogoView.as_view() , name='catalogo'),
    url('api/chart/data' , CharData.as_view()),
    url('api/data' , get_data , name='api-data'),
    #url('detail/<int:pk>/' , view_product , name='detail_product'),
    #url('detail/pedido/<int:id_pedido>/' , detail_pedido , name='detail_pedido'),
    url('detail/producto/(?P<id_producto>[0-9])/$' , view_product , name='detail'),

    #url('detail/pedido/(?P<id_pedido>[0-9])/$' , detail_pedido , name='detail_pedido'),
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
    path('', include('clientes.urls')),
    path('', include('pedidos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
