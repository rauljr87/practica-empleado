from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado


# 1.- Listar todos los empleados de la empresa.


class ListAllEmpleados(ListView):
    """ Lista todos los empleados de la empresa """

    template_name = 'persona/list_all.html'
    model = Empleado
    # variable para el template
    # context_object_name = 'lista'


# 2.- Listar todos los empleados que pertenecen a una área de la empresa


class ListByAreaEmpleado(ListView):
    """ Lista todos los empleados de la empresa por su área """

    template_name = 'persona/list_by_area.html'
    queryset = Empleado.objects.filter(
        departamento__short_name='informatica',
    )

# 3.- Listar empleados por trabajo.
# 4.- Listar empleados por palabra clave.
# 5.- Listar habilidades de un empleado.
