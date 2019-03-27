from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField('Categoria' , max_length=50)

    def __str__ (self):
        return "%s" % (self.nombre)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre' , max_length=100 )
    picture = models.ImageField(
        upload_to='productos/images',
        blank=True,
        null=True
    )
    codigo = models.CharField('Codigo' , max_length=100 , unique=False ) #Pendiente de colocar Unique
    precio = models.DecimalField('Precio' , default=0, max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)

    def __str__ (self):
        return "%s" % (self.nombre)

    # def precio_IVA (self):
    #     total = self.precio * 1.12
    #     return total

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    c_entrada = models.IntegerField('Cantidad' , default=0)
    c_salida= models.IntegerField('Cantidad' , default=0 )
