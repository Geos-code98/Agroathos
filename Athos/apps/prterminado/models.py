from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductoTerminado(models.Model):
	
	qr= models.TextField("Lectura Qr", max_length=1000)
	traza1= models.CharField("traza", max_length=30,null=True, blank=True)
	traza2= models.CharField("traza", max_length=30,null=True, blank=True)
	traza3= models.CharField("traza", max_length=30,null=True, blank=True)
	traza4= models.CharField("traza", max_length=30,null=True, blank=True)
	traza5= models.CharField("traza", max_length=30,null=True, blank=True)
	traza6= models.CharField("traza", max_length=30,null=True, blank=True)
	traza7= models.CharField("traza", max_length=30,null=True, blank=True)
	traza8= models.CharField("traza", max_length=30,null=True, blank=True)
	traza9= models.CharField("traza", max_length=30,null=True, blank=True)
	traza10= models.CharField("traza", max_length=30,null=True, blank=True)
	traza11= models.CharField("traza", max_length=30,null=True, blank=True)
	traza12= models.CharField("traza", max_length=30,null=True, blank=True)
	traza13= models.CharField("traza", max_length=30,null=True, blank=True)
	traza14= models.CharField("traza", max_length=30,null=True, blank=True)
	traza15= models.CharField("traza", max_length=30,null=True, blank=True)
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPT")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPT",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Producto Terminado'
		verbose_name_plural = 'ModProducto Terminado'

	def __str__(self):
		return "%s-%s" % (self.id, self.qr)


class TempProductoTerminado(models.Model):
	anexo_pt=models.ForeignKey(ProductoTerminado, on_delete=models.CASCADE, related_name="AnexoPrTerminado",null=True, blank=True)
	
	temperatura= models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTempPr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTempPr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Temperatura Pr Terminado'
		verbose_name_plural = 'Temperatura Pr Terminado'

	def __str__(self):
		return "%s-%s" % (self.id, self.temperatura)
		