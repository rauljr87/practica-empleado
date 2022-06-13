from django.contrib import admin
from django.urls import path


def prueba_persona(self):
    return print('prueba persona')


app_name = 'persona'

urlpatterns = [
    path('', prueba_persona, name='pruebaPersona'),
]