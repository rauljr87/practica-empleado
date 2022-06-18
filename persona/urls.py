from django.contrib import admin
from django.urls import path
from .views import (
    ListAllEmpleados,
    ListByAreaEmpleado,
    ListByJobs,
)


app_name = 'persona'

urlpatterns = [
    path('list_all/', ListAllEmpleados.as_view(), name='list_all'),
    # short_name, variable declarada para aplicar filtro de empleados por departamento
    path('list_by_area/<short_name>/', ListByAreaEmpleado.as_view(), name='list_by_area'),
    # job, variable declarada para aplicar filtro de empleados por trabajo
    path('list_by_job/<job>/', ListByJobs.as_view(), name='list_by_job'),
]