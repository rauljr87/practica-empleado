from django.db import models


# tabla para base de datos


class Departamento(models.Model):
    """ Crea una tabla Departamento """

    # campos
    name = models.CharField('Nombre', max_length=100, editable=True)
    short_name = models.CharField('Nombre Corto', max_length=20, blank=True, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    # Meta, vendría a ser tipo decorador de atributos
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        # no permite que se registre un atributo o dos atributo dos veces
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name
