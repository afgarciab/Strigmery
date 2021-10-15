from django.db import models

class persona (models.Model):



    nombre= models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



    def __str__(self):

        return '{}'.format(self.nombre)
