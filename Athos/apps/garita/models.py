from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from apps.menu.models import ejezona
from apps.menu.models import fundo
from apps.menu.models import RutasAthos
from apps.menu.models import PlacasVehiculares
from apps.menu.models import DetallePlacasVehiculares

# Create your models here.




class TrasladoGaritaAthos(models.Model):
	traslado=models.CharField("Traslado", max_length=50, null=True, blank=True)
	
	class Meta:
		verbose_name = ' Traslado Garita Athos'
		verbose_name_plural = 'Traslado Garita Athos'

	def __str__(self):
		return "%s-%s" % (self.id,self.traslado)


class GaritaAthos(models.Model):
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaGaritaAthos" ,null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFunGaritaAthos" ,null=True, blank=True)
	anexo_ruta=models.ForeignKey(DetallePlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoRutaPlacasAthos" ,null=True, blank=True)
	anexo_traslado=models.ForeignKey(TrasladoGaritaAthos, on_delete=models.CASCADE, related_name="AnexoTrasladoGaritaAthos" ,null=True, blank=True)
	
	qrcampo=models.CharField("QR Campo", max_length=50, null=True, blank=True)
	qrplaca=models.CharField("QR Placas", max_length=50, null=True, blank=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	chofer_ref=models.CharField("Chofer Referencial", max_length=50, null=True, blank=True)
	kilometraje=models.DecimalField(max_digits=8, decimal_places=0,null=True, blank=True)
	cantpasajeros=models.DecimalField(max_digits=4, decimal_places=0,null=True, blank=True)
	observacion=models.CharField(max_length=300, null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGaritaAthos", blank=True, null=True)
	fecha = models.DateField("Fecha", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGaritaAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Garita Athos'
		verbose_name_plural = 'Garita Athos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.fecha,self.anexo_zona,self.qrplaca,self.usuario_creacion)


class DetalleGaritaBusAthos(models.Model):
	anexo_detalle=models.ForeignKey(GaritaAthos, on_delete=models.CASCADE, related_name="AnexoDetalleGaritaBus" ,null=True, blank=True)
	dni=models.CharField("DNI", max_length=50, null=True, blank=True)
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoDetZonaGaritaAthos" ,null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoDetFunGaritaAthos" ,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionDetalleGaritaAthos", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionDetalleGaritaAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Detalle Bus Garita Athos'
		verbose_name_plural = 'Detalle Bus Garita Athos'

	def __str__(self):
		return "%s-%s" % (self.dni,self.fecha_hora_creacion)



