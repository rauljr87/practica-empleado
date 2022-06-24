# models de django
from django.db import models
# models
from departamento.models import Departamento
# third party
from ckeditor.fields import RichTextField


# tabla para base de datos


class Habilidades(models.Model):
    """ Conjunto de varias habilidades para empleados """

    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


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
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    # relación one to many
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # archivo estático, img
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # relación many to many
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    # Meta, vendría a ser tipo decorador de atributos
    class Meta:
        verbose_name = 'El Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        # ordering = ['-first_name', 'last_name']
        ordering = ['first_name', 'last_name']
        # no permite que se registre uno o dos atributos dos veces, que se repita
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
