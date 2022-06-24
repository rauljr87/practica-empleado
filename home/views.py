from django.shortcuts import render
# generic views
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
# models
from .models import Prueba
# forms, asignarlo a la vista que está haciendo el CreateView
from .forms import PruebaForm


class PruebaView(TemplateView):
    """ Muestra un template """

    template_name = 'home/prueba.html'


class ResumeFoundationView(TemplateView):
    """ prueba de grids de framework css foundation """

    template_name = "home/resume_foundation.html"


class PruebaListView(ListView):
    """ Lista un variable queryset """

    template_name = 'home/lista.html'
    # variable para llamar desde el template
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    """ Lista los objetos creados """

    template_name = "home/lista_prueba.html"
    model = Prueba
    # variable para llamar desde el template
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    """ Crea objetos """

    template_name = "home/add.html"
    model = Prueba
    # se anulan el atributo fields, ya que estamos trabajando con el form
    # atributo para usar el formulario
    form_class = PruebaForm
    # url para cuando formulario exitoso
    # success_url = '.'
    success_url = '/'
