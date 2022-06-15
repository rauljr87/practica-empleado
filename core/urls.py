from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('departamento', include('departamento.urls', namespace='departamento')),
    path('persona', include('persona.urls', namespace='persona'))
]
