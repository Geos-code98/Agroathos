from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import CentrosAthos
from apps.menu.models import cultivo
from apps.menu.models import Estado
# Create your models here.

class TasaCambioAthos(models.Model):
	fecha=models.DateField("fecha",blank=True, null=True)
	compra=models.DecimalField(max_digits=5, decimal_places=3 ,blank=True, null=True)
	
	venta=models.DecimalField(max_digits=5, decimal_places=3,blank=True, null=True)
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTasadeCambio")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTasadeCambio",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Tipo Cambio Athos '
		verbose_name_plural = 'Tipo Cambio Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.compra, self.venta)

