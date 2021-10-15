from django.db import models
from producto.models import Producto
from pedido.models import Pedido
class comercio (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    nombre= models.CharField(max_length=50)
    dirs = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)


    def _str_(self):

        return '{}'.format(self.nombre)
# Create your models here.
