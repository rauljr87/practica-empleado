from django.contrib import admin
from django.urls import path


def prueba(self):
    return print("Prueba")


app_name = 'departamento'

urlpatterns = [
    path('', prueba, name='prueba'),
]
