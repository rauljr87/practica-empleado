from django.shortcuts import render
# vistas genéricas
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
# models
from .models import Prueba


class PruebaView(TemplateView):
    """ Muestra un template """

    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    """ Lista un variable queryset """

    template_name = 'home/lista.html'
    # variable para el template
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    """ Lista los objetos creados """

    template_name = "home/lista_prueba.html"
    model = Prueba
    # variable para el template
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    """ Crea objetos """

    template_name = "home/add.html"
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad']
