from django import forms
from pedidos.models import PedidoVentas , ItemPedido


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

    # def save(self):
    #     cliente = self.cleaned_data['cliente']
    #     pedido = Cliente.objects.create(
    #     cliente=cliente ,
    #     )
    #     pedido.save()
