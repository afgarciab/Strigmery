from django.db import models
from comercio.models import comercio
from pedido.models import Pedido
class Producto(models.Model):
    comercio1 = models.ForeignKey(comercio, on_delete=models.CASCADE, default = None)

    imagen = models.CharField(max_length=50)
    pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE, default = None)
    descripcion = models.CharField(max_length=50)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    tiempo_alistamiento = models.DateTimeField(auto_now_add=True)
    tiempo_preparacion = models.DateTimeField(auto_now_add=True)
    tiempo_despacho = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.descripcion,self.cantidad)
        return '{}'.format(self.name)
# Create your models here.
