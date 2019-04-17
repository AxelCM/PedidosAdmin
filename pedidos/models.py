from django.db import models

# Create your models here.
from productos.models import Producto
from clientes.models import Cliente
from datetime import *

class TipoPago(models.Model):
    tipo_pago = models.CharField('Tipo de Pago' , max_length=25)

    def __str__(self):
        return "%s" % (self.tipo_pago)


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

    def Abonado(self):
        abonos = Abono.objects.filter(id_pedido=self.id_pedido)
        suma = 0
        for abono in abonos:
            haber = abono.cantidad
            suma += haber
        return suma

    def Saldo(self):
        saldo = self.totalpedido()
        haber = self.Abonado()
        bal = saldo - haber
        return bal

    def EDT(self):
        pedidos = PedidoVentas.objects.filter(id_pedido=self.id_pedido)
        suma = 0
        for pedido in pedidos:
            saldo = self.Saldo()
            suma += saldo
        return saldo

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
    fecha = models.DateTimeField(auto_now_add=True)
    create_at = models.DateField(auto_now_add=True)
    id_pedido = models.ForeignKey(PedidoVentas , on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad' , default=1)

    def sub_total(self):
        subtotal= self.producto.precio * self.cantidad
        return subtotal

    def itemtotal(self):
        items = ItemPedido.objects.filter(producto=self.producto)
        total = 0
        for item in items:
            cant = item.cantidad
            total += cant
        return total

    # def despacho(self):
    #     hoy = datetime.today()
    #     items = ItemPedido.objects.filter(create_at=hoy)
    #     total = 0
    #     for item in items:
    #         cant = item.cantidad
    #         total += cant
    #         return total


    def __str__(self):
        return "%s" % (self.producto)



class Abono(models.Model):

    id_abono = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(PedidoVentas , on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha' , auto_now_add=True)
    cantidad = models.DecimalField('Monto' , default=0  , decimal_places=2 , max_digits=9)
    tipo_pago = models.ForeignKey(TipoPago , on_delete=models.CASCADE)
    observaciones = models.TextField('Observaciones' , default=' ' ,  max_length=250 , blank=True , null=True)

    def __str__(self):
        return "%s %s" % (self.id_pedido , self.cantidad)

    def totalpedido(self):
        #pd = PedidoVentas.objects.get(id_pedido=self.id_pedido)

        items = ItemPedido.objects.filter(id_pedido=self.id_pedido)
        total = 0
        for item in items:
            cantidad = item.cantidad
            value = item.producto.precio
            total += cantidad * value
        return total

    def Abonado(self):
        abonos = Abono.objects.filter(id_pedido=self.id_pedido)
        suma = 0
        for abono in abonos:
            haber = abono.cantidad
            suma += haber
        return suma

    def Saldo(self):
        saldo = self.totalpedido()
        haber = self.Abonado()
        bal = saldo - haber
        return bal



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
