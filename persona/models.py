from django.db import models

from departamento.models import Departamento

# tabla para base de datos


class Empleado(models.Model):
    """ Tabla de datos Empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('4', 'OTRO')
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None)

    # Meta, vendría a ser tipo decorador de atributos
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        # no permite que se registre un atributo o dos atributo dos veces
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name