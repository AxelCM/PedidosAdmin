from django.urls import path
from productos.views import IndexView 


urlpatterns = [
    #path('signup' , CreateAlumnoView.as_view(), name='signup'),
    path('' , IndexView.as_view() , name='index'),


]
