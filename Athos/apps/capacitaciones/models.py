from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class RespuestaEncuesta(models.Model):
	
	rpta= models.CharField("Respuesta", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Respuesta-Encuesta-Capacitacion'
		verbose_name_plural = 'Respuesta-Encuesta-Capacitacion'

	def __str__(self):
		return "%s" % ( self.rpta)

class RespuestaNumericaEncuesta(models.Model):
	
	rpta= models.CharField("Respuesta", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'RespuestaNumerica -Encuesta-Capacitacion'
		verbose_name_plural = 'RespuestaNumerica -Encuesta-Capacitacion'

	def __str__(self):
		return "%s" % ( self.rpta)

class RespuestaAprobacion(models.Model):
	
	rpta= models.CharField("Respuesta Aprobacion", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Respuesta-Aprobacion-Capacitacion'
		verbose_name_plural = 'Respuesta-Aprobacion-Capacitacion'

	def __str__(self):
		return "%s" % ( self.rpta)


class EncuestaCapacitacion(models.Model):
	
	dni= models.CharField("Leer Dni", max_length=50,null=True, blank=True)
	fecha_capacitacion= models.DateField("Fecha fecha_capacitacion",null=True, blank=True)
	
	
	anexo_zona = models.ForeignKey("menu.ejezona", on_delete=models.CASCADE, related_name="AnexozonaEncuesta", blank=True, null=True)
	anexo_capacitacion = models.ForeignKey("menu.CapacitacionCapacitacion", on_delete=models.CASCADE, related_name="AnexoCapacitacionEncuesta", blank=True, null=True)
	
	anexo_rpta1 = models.ForeignKey(RespuestaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaEncuesta1")
	anexo_rpta2 = models.ForeignKey(RespuestaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaEncuesta2")
	
	anexo_rpta3 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta3",blank=True, null=True)
	anexo_rpta4 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta4",blank=True, null=True)
	anexo_rpta5 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta5",blank=True, null=True)
	
	anexo_rpta6 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta6",blank=True, null=True)
	anexo_rpta7 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta7",blank=True, null=True)
		
	imagen_justificacion1=models.ImageField(upload_to="justificacion_capacitacion" ,blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEncuestaCapacitacion")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEncuestaCapacitacion",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Encuesta Capacitacion'
		verbose_name_plural = 'Encuesta Capacitacion'

	def __str__(self):
		return "%s" % ( self.dni)


class EncuestaCapacitacionNew(models.Model):
	
	dni= models.CharField("Leer Dni", max_length=50,null=True, blank=True)
	
	
	anexo_zona = models.ForeignKey("menu.ejezona", on_delete=models.CASCADE, related_name="AnexozonaEncuestaNew", blank=True, null=True)
	anexo_capacitacion = models.ForeignKey("menu.CapacitacionCapacitacion", on_delete=models.CASCADE, related_name="AnexoCapacitacionEncuestaNew", blank=True, null=True)
	
	anexo_rpta1 = models.ForeignKey(RespuestaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaEncuesta1New")
	anexo_rpta2 = models.ForeignKey(RespuestaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaEncuesta2New")
	
	anexo_rpta3 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta3New",blank=True, null=True)
	anexo_rpta4 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta4New",blank=True, null=True)
	anexo_rpta5 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta5New",blank=True, null=True)
	
	anexo_rpta6 = models.ForeignKey(RespuestaNumericaEncuesta, on_delete=models.CASCADE, related_name="AnexoRespuestaNumericaEncuesta6New",blank=True, null=True)
		
	imagen_justificacion1=models.ImageField(upload_to="justificacion_capacitacion" ,blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEncuestaCapacitacionNew")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEncuestaCapacitacionNew",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Encuesta Capacitacion New'
		verbose_name_plural = 'Encuesta Capacitacion New'

	def __str__(self):
		return "%s" % ( self.dni)

