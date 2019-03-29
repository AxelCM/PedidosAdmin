from django.db import models

# Create your models here.
from productos.models import Producto
from clientes.models import Cliente

class PedidoVentas(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)
    #producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
    date = models.DateField('Fecha de Pedido' , auto_now_add=True)
    #date_des = models.DateField('Fecha de Despacho', auto_now_add=True)
    #cantidad_pedida = models.IntegerField ('Cantidad Pedida' , default=0)


    def totalpedido(self):
        #pd = PedidoVentas.objects.get(id_pedido=self.id_pedido)

        items = ItemPedido.objects.filter(id_pedido=self.id_pedido)
        total = 0
        for item in items:
            cantidad = item.cantidad
            value = item.producto.precio
            total += cantidad * value
        return total

    def conteoItems(self):
        i_count = ItemPedido.objects.filter(id_pedido=self.id_pedido).count()
        return i_count

    def __str__(self):
        return "%s %s %s %s" % ("Pedido No.", self.id_pedido, "-", self.cliente)

    class Meta:
        verbose_name_plural  = 'Pedidos'
        verbose_name = 'Pedido'

class PedidoEnvio(models.Model):
    id_envio = models.OneToOneField(PedidoVentas , on_delete=models.CASCADE)
    date = models.DateField('Fecha de Pedido' , auto_now_add=True)
    cantidad_entregada = models.IntegerField ('Cantidad Entregada' , default=0)


    def costo_total(self):
        pass

class ItemPedido(models.Model):
    id_pedido = models.ForeignKey(PedidoVentas , on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad' , default=1)

    def sub_total(self):
        subtotal= self.producto.precio * self.cantidad
        return subtotal

    def __str__(self):
        return "%s" % (self.producto)



# def totalpedido(self , id_pedido ):
#     pd = PedidoEnvio.objects.get(pk=id_pedido)
#     item = ItemPedido.objects.filter(id_pedido=pd)
#     def sub_total(self):
#         subtotal= self.producto.precio * self.cantidad
#         return subtotal
#
#     for i in item :
#         total = sub_total() + total
#         return total
