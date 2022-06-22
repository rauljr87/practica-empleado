from django.db import models


# tabla para base de datos


class Prueba(models.Model):
    """ Crea tabla DB Prueba """

    # campos
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + '-' + self.subtitulo + '-' + str(self.cantidad)
