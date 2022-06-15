from django.db import models


class Departamento(models.Model):
    """ Crea una tabla Departamento """

    name = models.CharField('Nombre', max_length=100)
    short_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)
