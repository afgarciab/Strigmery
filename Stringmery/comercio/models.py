from django.db import models

class comercio (models.Model):

    nombre= models.CharField(max_length=50)
    dirs = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)


    def _str_(self):

        return '{}'.format(self.nombre)
# Create your models here.
