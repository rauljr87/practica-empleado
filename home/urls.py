from django.urls import path
from .views import PruebaView


app_name = 'home'

urlpatterns = [
    path('prueba/', PruebaView.as_view(), name='Prueba')
]