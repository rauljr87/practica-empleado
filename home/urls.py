from django.urls import path
from .views import PruebaView, PruebaListView


app_name = 'home'

urlpatterns = [
    path('prueba/', PruebaView.as_view(), name='prueba'),
    path('lista/', PruebaListView.as_view(), name='lista')
]