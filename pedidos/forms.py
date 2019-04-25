from django import forms
from pedidos.models import PedidoVentas , ItemPedido , Abono
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime
from productos.models import Producto
from django.forms.models import model_to_dict

class PedidoForm(forms.ModelForm):

    class Meta:

        model = PedidoVentas
        fields = (
        'cliente',
        )

class AddProductoForm(forms.ModelForm):

    class Meta:

        model = ItemPedido
        fields = (
        'id_pedido',
        'producto',
        'cantidad',
        )

    # def precio_producto(self):
    #     id_pedido = self.cleaned_data['id_pedido']
    #     producto = self.cleaned_data['producto']
    #     cantidad = self.cleaned_data['cantidad']
    #     producto_taken = Producto.objects.get(nombre=producto)
    #     if producto_taken:
    #         precio = producto_taken.precio
    #         valid_data['precio'] = precio
    #     return valid_data
    #
    # def save(self , *args , **kwargs):
    #     data = self.cleaned_data
    #     itempedido = ItemPedido.objects.create(**data)
    #     itempedido.save()

    # def save(self):
    #     id_pedido = self.cleaned_data['id_pedido']
    #     producto = self.cleaned_data['producto']
    #     cantidad = self.cleaned_data['cantidad']
    #     producto_taken = Producto.objects.get(nombre=producto)
    #     if producto_taken:
    #         precio = producto_taken.precio
    #     itempedido = ItemPedido.objects.create(
    #     id_pedido=id_pedido ,
    #     producto=producto ,
    #     cantidad=cantidad,
    #     precio=precio,
    #     )
    #     itempedido.save()




class AbonoForm(forms.ModelForm):

    class Meta:
       model = Abono
       fields = ['id_pedido' ,'cantidad' , 'tipo_pago' , 'observaciones']

class AbonarForm(forms.ModelForm):

    class Meta:
       model = Abono
       fields = ['id_pedido' , 'tipo_pago' ]
