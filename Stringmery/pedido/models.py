from django.db import models

class pedido (models.Model):


    nombre= models.CharField(max_length=50)
    dirs = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)



    def __str__(self):

        return '{}'.format(self.name)
