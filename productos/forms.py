from django import forms

from productos.models import Producto , Categoria



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

class CategoriaForm(forms.ModelForm):

    class Meta:

        model = Categoria
        fields = (
        'nombre',
        )
