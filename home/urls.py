from django.urls import path
from .views import PruebaView, PruebaListView, ListarPrueba


app_name = 'home'

urlpatterns = [
    path('prueba/', PruebaView.as_view(), name='prueba'),
    path('lista/', PruebaListView.as_view(), name='lista'),
    path('lista_prueba/', ListarPrueba.as_view(), name='lista_prueba')
]