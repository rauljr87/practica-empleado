from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('persona.urls', namespace='persona')),
    # path('departamento', include('departamento.urls', namespace='departamento')),
]
