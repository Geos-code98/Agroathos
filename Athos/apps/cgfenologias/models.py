from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import fenologia

from apps.menu.models import cultivo


# Create your models here.
class Macroproceso(models.Model):

	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivo",null=True, blank=True)
	desc= models.CharField("Descripcion Macroproceso", max_length=100)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMacroproceso")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMacroproceso",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'MacroProceso'
		verbose_name_plural = 'MacroProceso'

	def __str__(self):
		return "%s-%s" % (self.id, self.desc)

class Proceso(models.Model):
	anexo_macroproceso = models.ForeignKey(Macroproceso, on_delete=models.CASCADE, related_name="AnexoMacroproceso" ,null=True, blank=True)
	abreviatura=models.CharField("Descripcion Macroproceso", max_length=100)
	descripcion= models.CharField("Descripcion Macroproceso", max_length=100)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProceso")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProceso",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Proceso'
		verbose_name_plural = 'Proceso'

	def __str__(self):
		return "%s-%s" % (self.abreviatura, self.descripcion)


class ObjetivoProceso(models.Model):
	anexo_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, related_name="AnexoProceso" ,null=True, blank=True)
	descripcion= models.CharField("Objetivo", max_length=100)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionObjetivoProceso")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModObjetivoProceso",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Objetivo Proceso'
		verbose_name_plural = 'Objetivo Proceso'

	def __str__(self):
		return "%s-%s" % (self.id, self.descripcion)



class EstructuraPlanta(models.Model):
	descripcion= models.CharField("Estructura Planta", max_length=100)
	
	
	

	class Meta:
		verbose_name = 'Estructura Planta'
		verbose_name_plural = 'Estructura Planta'

	def __str__(self):
		return "%s-%s" % (self.id, self.descripcion)



class Hitos(models.Model):
	anexo_fenologia = models.ForeignKey(fenologia, on_delete=models.CASCADE, related_name="AnexoFenHitos",null=True, blank=True)
	descripcion= models.CharField("Descripcion Hitos", max_length=100)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionHitos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModHitos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Hitos'
		verbose_name_plural = 'Hitos'

	def __str__(self):
		return "%s-%s" % (self.id, self.descripcion)


class SubHitos(models.Model):
	anexo_hito = models.ForeignKey(Hitos, on_delete=models.CASCADE, related_name="AnexoSubHitos",null=True, blank=True)
	descripcion= models.CharField("Descripcion SubHitos", max_length=100)
	anexo_macro = models.ForeignKey(Macroproceso, on_delete=models.CASCADE, related_name="AnexoOMacroProceso",null=True, blank=True)
	anexo_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, related_name="AnexoProcesoSubhito",null=True, blank=True)
	anexo_objetivos = models.ForeignKey(ObjetivoProceso, on_delete=models.CASCADE, related_name="AnexoObjetivo")
	anexo_estructura = models.ForeignKey(EstructuraPlanta, on_delete=models.CASCADE, related_name="AnexoEstructura")
	valor=models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSUBHitos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSUBHitos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Hitos'
		verbose_name_plural = 'Hitos'

	def __str__(self):
		return "%s-%s" % (self.id, self.descripcion)