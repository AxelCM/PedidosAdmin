from django import forms

from productos.models import Producto



class ProductoForm(forms.ModelForm):

    class Meta:

        model = Producto
        fields = (
        'nombre',
        'picture',
        'codigo',
        'precio',
        'categoria',
        )
