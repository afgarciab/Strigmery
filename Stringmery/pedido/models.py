from django.db import models
from persona.models import persona
from usuario.models import usuario
from comercio.models import comercio
class Pedido(models.Model):

    usuario1 = models.ForeignKey(usuario, on_delete=models.CASCADE, default = None)
    persona1 = models.ForeignKey(persona, on_delete=models.CASCADE, default = None)
    comercio1 = models.ForeignKey(comercio, on_delete=models.CASCADE, default = None)
    estado = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    peso = models.FloatField(null=True, blank=True, default=None)
    volumen = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.peso, self.volumen)
        return '{}'.format(self.name)
# Create your models here.
