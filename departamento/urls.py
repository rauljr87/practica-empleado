from django.contrib import admin
from django.urls import path
from .views import NewDepartamentoView

# def prueba(self):
#    return print("Prueba")

app_name = 'departamento_app'

urlpatterns = [
    # path('', prueba, name='prueba'),
    # FormView
    path('new_departamento/', NewDepartamentoView.as_view(), name='new_departamento'),
]
