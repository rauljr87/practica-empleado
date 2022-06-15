from django.shortcuts import render
# vistas genéricas
from django.views.generic import TemplateView


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'
