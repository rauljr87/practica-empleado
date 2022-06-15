from django.db import models


# tabla para base de datos


class Departamento(models.Model):
    """ Crea una tabla Departamento """

    # campos
    name = models.CharField('Nombre', max_length=100)
    short_name = models.CharField('Nombre Corto', max_length=20, blank=True)
    anulate = models.BooleanField('Anulado', default=False)
