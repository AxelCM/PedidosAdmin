from django import forms
from pedidos.models import PedidoVentas , ItemPedido , Abono
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

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
        'cantidad'
        )



class AbonoForm(forms.ModelForm):

    class Meta:
       model = Abono
       fields = ['fecha' ,'cantidad']
       widgets = {
        'fecha': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
