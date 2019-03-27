from django.db import models





class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    n_representante = models.CharField('Nombre del Representante' , max_length=100)
    nombre_comercial = models.CharField('Nombre Comercial' , max_length=100)
    telefono = models.CharField('No. Telefono' , max_length=10)
    direccion = models.CharField('Direccion' , max_length=150)
    mayorista = models.BooleanField('Mayorista' , default=False)
    distribuidor = models.BooleanField('Distribuidor' , default=False)
    email = models.EmailField('Correo Electronico' , max_length=254, blank=True , null=True)
    nit = models.CharField('Nit' , max_length=15 , default='C/F')

    def __str__(self):
        return "%s" % (self.nombre_comercial)
