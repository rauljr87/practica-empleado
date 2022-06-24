from django.contrib import admin
from .models import Empleado, Habilidades


# Clase para decorador modelos registrados


class EmpleadoAdmin(admin.ModelAdmin):
    """ Class para decorar model Empleado """

    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        # campo externo
        'full_name',
    )

    # función para campo externo, parámetro el objeto del modelo
    def full_name(self, obj):
        """ Función para habilitar campo externo, la función debe tener el mismo nombre del campo externo"""

        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    # search
    search_fields = ('first_name', 'last_name',)
    # filter
    list_filter = ('departamento', 'job', 'habilidades',)
    # filtro horizontal solo sirve para many to many
    filter_horizontal = ('habilidades',)


# registro de model Empleado y class EmpleadoAdmin para decorar
admin.site.register(Empleado, EmpleadoAdmin)
# registro de model Habilidades
admin.site.register(Habilidades)
