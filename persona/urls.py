from django.contrib import admin
from django.urls import path
from .views import ListAllEmpleados


app_name = 'persona'

urlpatterns = [
    path('list_all/', ListAllEmpleados.as_view(), name='list_all'),
]