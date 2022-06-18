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
    # filtro a través de un queryset
    # queryset = Empleado.objects.filter(
    #    # filtro queryset por short_name a departamento
    #    departamento__short_name='informatica',
    # )

    # optimizando el filtro
    def get_queryset(self):
        """ Retorna lista filtrando los empleados por departamento """

        # pasamos, mediante kwargs, la variable declarada en la url para aplicar filtro por departamento
        area = self.kwargs['short_name']

        lista = Empleado.objects.filter(
            # filtro queryset por short_name a departamento del modelo Empleado
            departamento__short_name=area
        )
        return lista


# 3.- Listar empleados por trabajo.


class ListByJobs(ListView):
    """ Lista todos los empleados de la empresa por trabajo """

    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        """ Retorna lista filtrando los empleados por trabajo """

        # pasamos, mediante kwargs, la variable declarada en la url para aplicar filtro por trabajo
        job = self.kwargs['job']

        lista = Empleado.objects.filter(
            # filtro queryset por job a departamento del modelo Empleado
            job=job
        )
        return lista


# 4.- Listar empleados por palabra clave.
# 5.- Listar habilidades de un empleado.
