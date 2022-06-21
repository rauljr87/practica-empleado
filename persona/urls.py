from django.contrib import admin
from django.urls import path
from .views import (
    ListAllEmpleados,
    ListByAreaEmpleado,
    ListByJobs,
    ListEmpleadosByKword,
    ListHabilidadesEmpleado,
    EmpleadoDetailView,
    EmpleadoCreateView,
    SuccessView,
    EmpleadoUpdateView,
    EmpleadoDeleteView,
    InicioTemplateView,
)


app_name = 'persona_app'

urlpatterns = [
    # Inicio TemplateView
    path('', InicioTemplateView.as_view(), name='inicio'),   
    path('list_all/', ListAllEmpleados.as_view(), name='list_all'),
    # ListView
    # short_name, variable declarada para aplicar filtro de empleados por departamento
    path('list_by_area/<short_name>/', ListByAreaEmpleado.as_view(), name='list_by_area'),
    # job, variable declarada para aplicar filtro de empleados por trabajo
    path('list_by_job/<job>/', ListByJobs.as_view(), name='list_by_job'),
    path('list_by_kword/', ListEmpleadosByKword.as_view(), name='list_by_kword'),
    path('list_by_habilidades/', ListHabilidadesEmpleado.as_view(), name='list_by_habilidades'),
    # DetailView
    path('detail_empleado/<pk>/', EmpleadoDetailView.as_view(), name='detail_empleado'),
    # UpdateView
    path('add_empleado/', EmpleadoCreateView.as_view(), name='add_empleado'),
    # TemplateView
    path('success/', SuccessView.as_view(), name='success'),
    # UpdateView
    path('update_empleado/<pk>/', EmpleadoUpdateView.as_view(), name='update_empleado'),
    # DeleteView
    path('delete_empleado/<pk>/', EmpleadoDeleteView.as_view(), name='delete_empleado'),
]
