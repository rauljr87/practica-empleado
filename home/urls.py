from django.urls import path
from .views import (
    PruebaView,
    PruebaListView,
    ListarPrueba,
    PruebaCreateView,
    ResumeFoundationView
)


app_name = 'home_app'

urlpatterns = [
    path('prueba/', PruebaView.as_view(), name='prueba'),
    path('lista/', PruebaListView.as_view(), name='lista'),
    path('lista_prueba/', ListarPrueba.as_view(), name='lista_prueba'),
    path('add/', PruebaCreateView.as_view(), name='add'),
    path('resume_foundation/', ResumeFoundationView.as_view(), name='resume_foundation'),
]