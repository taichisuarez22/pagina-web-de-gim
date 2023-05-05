from django.db import models

class Profesor(models.Model):
	direccion = models.CharField(max_length=30)
	nombre = models.CharField(max_length=30)
	rut = models.IntegerField()
	fecha_ingreso= models.DateField(blank=True, null=True)
	email = models.EmailField()
	telefono = models.IntegerField()


	def __str__(self):
	 	return self.nombre 
	class Meta:
		verbose_name_plural="profesores"

class Instrucciones(models.Model):
	clase=models.CharField(max_length=50)
	horas=models.IntegerField()
	precio=models.DecimalField(max_digits=8,decimal_places=2)
	profesor= models.ForeignKey(Profesor, on_delete=models.CASCADE)
	foto=models.ImageField(upload_to='img')
	combate = 'combate'
	crossfit = 'crossfit'
	pesas= 'pesas'
	zumba = 'zumba'
	tipo_sel= [
	    (combate,'combate'),
	    (crossfit, 'crossfit'),
	    (pesas, 'pesas'),
	    (zumba, 'zumba'),
	]
	tipo = models.CharField(
		max_length=10,
		choices=tipo_sel,
		default=crossfit,
		)
	def __str__(self):
		return "%s %s" % (self.tipo,self.clase) 
	def __iter__(self):return [ self.profesor, self.precio, self.clase,]
	class Meta:
		verbose_name_plural="Instrucciones"

