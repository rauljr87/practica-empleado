from django.contrib import admin
from django.urls import path
from .views import NewDepartamentoView, DepartamentoListView

# def prueba(self):
#    return print("Prueba")


app_name = 'departamento_app'


urlpatterns = [
    # path('', prueba, name='prueba'),
    # ListView
    path('lista_departamento/', DepartamentoListView.as_view(), name='lista_departamento'),
    # FormView
    path('new_departamento/', NewDepartamentoView.as_view(), name='new_departamento'),

]
