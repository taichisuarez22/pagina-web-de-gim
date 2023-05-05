from django.contrib import admin
from paginaweb.models import Profesor, Instrucciones

class ProfesorAdmin(admin.ModelAdmin):
	list_display = ('direccion', 'nombre','rut','fecha_ingreso','email','telefono')
	search_fields = ('nombre', 'telefono')
	ordering = ('nombre')

class InstruccionesAdmin(admin.ModelAdmin):
	search_fields = ('clase', 'horas','precio')
	list_display = ('profesor', 'precio','clase','foto')

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Instrucciones)