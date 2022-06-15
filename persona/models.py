from django.db import models

from departamento.models import Departamento

# tabla para base de datos


class Empleado(models.Model):
    """ Tabla de datos Empleado """

    JOB_CHOICES = (
        {'0': 'CONTADOR'},
        {'1': 'ADMINISTRADOR'},
        {'2': 'ECONOMISTA'},
        {'4': 'OTRO'}
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
