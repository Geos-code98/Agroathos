from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import CentrosAthos
from apps.menu.models import cultivo
from apps.menu.models import Estado
# Create your models here.

class ProveedoresAthos(models.Model):
	anexo_centro=models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroProveedor",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoProveedor",null=True, blank=True)
	ruc= models.BigIntegerField("RUC")
	proveedor= models.CharField("PROVEEDOR", max_length=200)
	anexo_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoProveedor")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProveedor")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProveedor",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Proveedores Athos '
		verbose_name_plural = 'Proveedores Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.ruc, self.proveedor, self.anexo_estado)

class TipoOperacion(models.Model):
	desc= models.CharField("TipoOperacion", max_length=30)
	
	
	

	class Meta:
		verbose_name = 'Tipo Operacion'
		verbose_name_plural = 'Tipo Operacion'

	def __str__(self):
		return "%s" % ( self.desc)
class Monedas(models.Model):
	desc= models.CharField("Monedas", max_length=30)
	
	
	

	class Meta:
		verbose_name = 'Monedas'
		verbose_name_plural = 'Monedas'

	def __str__(self):
		return "%s" % ( self.desc)

class EstadoLogistica(models.Model):
	desc= models.CharField("estados", max_length=30)
	
	
	

	class Meta:
		verbose_name = 'Estado Logistica'
		verbose_name_plural = 'Estado Logistica'

	def __str__(self):
		return "%s" % ( self.desc)


class CartillaProveedoresAthos(models.Model):
	anexo_centro=models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentrosProveedor",null=True, blank=True)
	anexo_tipo=models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, related_name="AnexoTOProveedor",null=True, blank=True)
	anexo_proveedor=models.ForeignKey(ProveedoresAthos, on_delete=models.CASCADE, related_name="AnexoCartillaProveedor",null=True, blank=True)
	factura= models.CharField("Factura", max_length=200,null=True, blank=True)
	orden= models.BigIntegerField("Orden",null=True, blank=True)
	anticipo= models.BigIntegerField("Anticipo",null=True, blank=True)
	anexo_moneda = models.ForeignKey(Monedas, on_delete=models.CASCADE, related_name="AnexoMonedasProveedor")
	fecha=models.DateField("Fecha de Vencimiento")
	valor= models.IntegerField("Valor",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=200,null=True, blank=True)
	anexo_estado=models.ForeignKey(EstadoLogistica, on_delete=models.CASCADE, related_name="AnexoEstadoProveedor",null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionCartillaProveedor")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCartillaProveedor",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Cartillas Proveedores Athos '
		verbose_name_plural = 'Cartillas Proveedores Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.factura, self.orden, self.anexo_estado)