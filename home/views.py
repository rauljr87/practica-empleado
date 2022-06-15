from django.shortcuts import render
# vistas genéricas
from django.views.generic import TemplateView, ListView
# models
from .models import Prueba

class PruebaView(TemplateView):
    """ Muestra un template """

    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    """ Lista un variable queryset """

    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'
