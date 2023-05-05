from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from gim.views import *
from paginaweb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('somos/', somos, name='somos'),
    path('buscar/', buscar, name='buscar'),
    path('contacto/',contacto, name='contacto'),
    path('registro/', usuario_nuevo, name='registro'),
    path('privado/', privado, name='privado'),
    path('ingresar/', ingresar, name='ingresar'),
    path('salir/', salir, name='salir'),
    path('agregar/',agregar, name='agregar'),
]
