from django.db import models


class Producto(models.Model):
    nombre = models.CharField('nombre' , max_length=100 )
    precio = models.IntegerField('Precio' , default=0 )
    segundo = models.CharField('claro' , max_length=50)
    tercero =models.CharField('tercero' , max_length=50)

    def __str__ (self):
        return "%s" % (self.nombre)

    def precio_IVA (self):
        total = self.precio * 1.12
        return total
