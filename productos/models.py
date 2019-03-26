from django.db import models


class Producto(models.Model):
    nombre = models.CharField('nombre' , max_length=100 )


    def __str__ (self):
        return "%s" % (self.nombre)
