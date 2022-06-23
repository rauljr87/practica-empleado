from xml.dom.expatbuilder import DOCUMENT_NODE
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, re_path, include
# configurar urls de media files
# importar archivo de configuración de django
from django.conf import settings
# importar paquete para generar urls estáticas
from django.conf.urls.static import static


""" 
Para generar urls estáticas de las imágenes que se añaden en la carpeta 'media', se debe concatenar el MEDIA_URL por medio del método
static(setting.MEDIA_URL)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('persona.urls', namespace='persona')),
    path('', include('departamento.urls', namespace='departamento')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
