from django.db import models

class Pedido(models.Model):
    estado = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    peso = models.FloatField(null=True, blank=True, default=None)
    volumen = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.peso, self.volumen)
        return '{}'.format(self.name)
# Create your models here.
