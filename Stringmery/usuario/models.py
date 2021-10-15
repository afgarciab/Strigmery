from django.db import models


class usuario (models.Model):


    nombre= models.CharField(max_length=50)
    dirs = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    documento = models.FloatField(null= True, blank= True , default = None)


    def __str__(self):

        return '{}'.format(self.nombre)
