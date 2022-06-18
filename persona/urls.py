from django.contrib import admin
from django.urls import path
from .views import (
    ListAllEmpleados,
    ListByAreaEmpleado,
)


app_name = 'persona'

urlpatterns = [
    path('list_all/', ListAllEmpleados.as_view(), name='list_all'),
    path('lis_by_area/', ListByAreaEmpleado.as_view(), name='list_by_area'),
]