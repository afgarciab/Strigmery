from django.db import models

class Producto(models.Model):
    imagen = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    tiempo_alistamiento = models.DateTimeField(auto_now_add=True)
    tiempo_preparacion = models.DateTimeField(auto_now_add=True)
    tiempo_despacho = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.descripcion,self.cantidad)
        return '{}'.format(self.name)
# Create your models here.
