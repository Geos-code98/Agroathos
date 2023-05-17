from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import cultivo
from apps.menu.models import MaterialMMPP

# Create your models here.
class MaestraRegion(models.Model):
	
	desc=models.CharField("Region",max_length=50,blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMaestraRegion")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMaestraRegion",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	
	class Meta:
		verbose_name = 'Maestra Region'
		verbose_name_plural = 'Maestra Region'

	def __str__(self):
		return "%s" % (self.desc)




class MaestraClientes(models.Model):

	anexo_region = models.ForeignKey(MaestraRegion, on_delete=models.CASCADE, related_name="AnexoClienteRegion")
	cliente=models.CharField("Cliente",max_length=50,blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMaestraCliente")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMaestraCliente",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Maestra Clientes'
		verbose_name_plural = 'Maestra Clientes'

	def __str__(self):
		return "%s-%s" % (self.anexo_region, self.cliente)
	

class EstadoPedido(models.Model):

	
	estado=models.CharField("Estado Pedido",max_length=50,blank=True,null=True)

	class Meta:
		verbose_name = 'Etapa Pedido'
		verbose_name_plural = 'Etapa Pedido'

	def __str__(self):
		return "%s" % (self.estado)


class TipoTransporte(models.Model):
	
	desc=models.CharField("Tipo Transporte",max_length=50,blank=True,null=True)
	
	
	
	class Meta:
		verbose_name = 'Tipo Transporte'
		verbose_name_plural = 'Tipo Transporte'

	def __str__(self):
		return "%s" % (self.desc)



class CategoriaCultivo(models.Model):
	
	desc=models.CharField("Categoria",max_length=50,blank=True,null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoCategoria")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionCategpriaCult", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCategoriaCult",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
		
	
	class Meta:
		verbose_name = 'Cateoria Cultivo'
		verbose_name_plural = 'Categoria Cultivo'

	def __str__(self):
		return "%s-%s" % (self.anexo_cultivo,self.desc)

class MarcaPT(models.Model):
	
	desc=models.CharField("Marca",max_length=50,blank=True,null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoMarcaCultivo")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMarcaProdT", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMarcaProdT",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	
	class Meta:
		verbose_name = 'Marca Prod. Terminado'
		verbose_name_plural = 'Marca Prod. Terminado'

	def __str__(self):
		return "%s-%s" % (self.anexo_cultivo,self.desc)


class TipoEnvase(models.Model):
	
	desc=models.CharField("Tipo Envase",max_length=50,blank=True,null=True)
	
	
	class Meta:
		verbose_name = 'Tipo Envase Prod. Terminado'
		verbose_name_plural = 'Tipo Envase Prod. Terminado'

	def __str__(self):
		return "%s" % (self.desc)

class UnidadMaterial(models.Model):
	
	desc=models.CharField("Unidad Material",max_length=50,blank=True,null=True)
	
	
	class Meta:
		verbose_name = 'Unidad Material Prod. Terminado'
		verbose_name_plural = 'Unidad Material Prod. Terminado'

	def __str__(self):
		return "%s" % (self.desc)


class MaterialPT(models.Model):

	cod_material=models.CharField("Codigo Material",max_length=50,blank=True,null=True)
	desc_material=models.CharField("Descripcion Material",max_length=150,blank=True,null=True)
	grupo_art=models.IntegerField("Grupo Articulo", blank=True, null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoMatPT")
	anexo_categoria = models.ForeignKey(CategoriaCultivo, on_delete=models.CASCADE, related_name="AnexoCategoriaMatPT")
	cod_sap=models.CharField("Codigo Sap",max_length=50,blank=True,null=True)

	anexo_marca = models.ForeignKey(MarcaPT, on_delete=models.CASCADE, related_name="AnexoMarcaMatPT")
	anexo_envase = models.ForeignKey(TipoEnvase, on_delete=models.CASCADE, related_name="AnexoEnvaseMatPT")
	anexo_unidad = models.ForeignKey(UnidadMaterial, on_delete=models.CASCADE, related_name="AnexoUnidadMatPT",null=True, blank=True)	
	peso_neto=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	calibre=models.CharField("Calibre",max_length=50,blank=True,null=True)
	


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMaestraMateriales")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMaestraMateriales",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Material Producto Terminado'
		verbose_name_plural = 'Material Producto Terminado'

	def __str__(self):
		return "%s" % (self.desc_material)

class PlanVentas(models.Model):
	fecha_despacho = models.DateField("Fecha Despacho",null=True, blank=True)
	fecha_produccion=models.DateField("Fecha Produccion",null=True, blank=True)
	num_pedido=models.IntegerField("Numero Pedido", blank=True, null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoPlVentas")
	
	anexo_cliente = models.ForeignKey(MaestraClientes, on_delete=models.CASCADE, related_name="AnexoClientesPlVentas")
	anexo_estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, related_name="AnexoEstadoPlVentas")
	anexo_transporte = models.ForeignKey(TipoTransporte, on_delete=models.CASCADE, related_name="AnexoTransportePlVentas")

	num_semana=models.IntegerField("Semana", blank=True, null=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPlVentas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPlVentas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Plan Ventas'
		verbose_name_plural = 'Plan Ventas'

	def __str__(self):
		return "%s" % (self.num_pedido)


class DetallePlanVentas(models.Model):
	
	pos_pedido=models.IntegerField("Posicion Pedido", blank=True, null=True)
	anexo_material=models.ForeignKey(MaterialPT, on_delete=models.CASCADE, related_name="AnexoMaterialPlVentas")
	desc_material=models.CharField("Descrpcion Material",max_length=50,blank=True,null=True)
	un_material=models.CharField("Unidad Material",max_length=50,blank=True,null=True)
	peso_material=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	cant_cajas=models.IntegerField("Cantidad Cajas", blank=True, null=True)
	kpg=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	anexo_categoria = models.CharField("Categoria",max_length=50,blank=True,null=True)
	anexo_calibre = models.CharField("Calibre",max_length=50,blank=True,null=True)
	anexo_variedad = models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, related_name="AnexoPlVentasVariedad", blank=True, null=True)
	cajas_palet=models.IntegerField("Cajas Palet", blank=True, null=True)
	cant_palet=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetPlVentas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetPlVentas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Detalle Plan Ventas'
		verbose_name_plural = 'Detalle Plan Ventas'

	def __str__(self):
		return "%s" % ( self.pos_pedido)

	@property
	def suma_cajas(self):
		consumos = self.AnexoDetallePedOrden.all()
		cant = 0
		for con in consumos:
			cant += con.consumo
		return int(cant)

	@property
	def resto_cajas(self):
		return self.cant_cajas - self.suma_cajas



class OrdenProceso(models.Model):
	
	anexo_detalle=models.ForeignKey(DetallePlanVentas, on_delete=models.CASCADE, related_name="AnexoDetallePedOrden",blank=True,null=True)
	nro_orden=models.IntegerField("Nro Orden", blank=True, null=True)
	


	desc_material=models.CharField("Descrpcion Material",max_length=50,blank=True,null=True)
	
	
	cant_cajas=models.IntegerField("Cantidad Cajas", blank=True, null=True)
	kpg=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	consumo=models.IntegerField("Consumos Cajas", blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionOrdenProceso")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModOrdenProceso",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Orden Proceso'
		verbose_name_plural = 'Orden Proceso'

	def __str__(self):
		return "%s-%s" % (self.anexo_detalle, self.nro_orden)




class ProgramaProduccionPlanta(models.Model):
	
	anexo_orden=models.ForeignKey(OrdenProceso, on_delete=models.CASCADE, related_name="AnexoProgramaOrden",blank=True,null=True)
	pos_orden=models.IntegerField("Posicion Orden", blank=True, null=True)
	desc_material=models.CharField("Descrpcion Material",max_length=50,blank=True,null=True)
	
	cant_cajas=models.IntegerField("Cantidad Cajas", blank=True, null=True)
	kpg=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	consumo=models.IntegerField("Consumos Cajas", blank=True, null=True)
	fecha_programada = models.DateField("Fecha Programada",null=True, blank=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPProduccionPlanta")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPProduccionPlanta",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Programa Produccion Planta'
		verbose_name_plural = 'Programa Produccion Planta'

	def __str__(self):
		return "%s-%s" % (self.anexo_orden, self.pos_orden)


class PlanVentas2021(models.Model):

	anio_campana=models.CharField("Año Campaña",max_length=50,blank=True,null=True)
	cultivo=models.CharField("Año Campaña",max_length=50,blank=True,null=True)
	anio=models.IntegerField("Año", blank=True, null=True)
	trimestre=models.IntegerField("Trimestre", blank=True, null=True)
	mes=models.IntegerField("Mes", blank=True, null=True)
	semana=models.IntegerField("Numero Pedido", blank=True, null=True)
	fecha_inicio = models.DateField("Fecha Inicio",null=True, blank=True)
	codigo_cliente=models.CharField("Codigo Cliente",max_length=50,blank=True,null=True)
	nombre_cliente=models.CharField("Nombre Cliente",max_length=50,blank=True,null=True)
	cod_material=models.CharField("Codigo Material",max_length=50,blank=True,null=True)
	desc_material=models.CharField("Descripcion Material",max_length=50,blank=True,null=True)
	um=models.CharField("Unidad de Medida",max_length=50,blank=True,null=True)
	cantidad=models.DecimalField(max_digits=9, decimal_places=1, blank=True, null=True)
	kgt=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	tipo_despacho=models.CharField("Tipo Despacho",max_length=50,blank=True,null=True)
	destino=models.CharField("Destino",max_length=50,blank=True,null=True)
	pais=models.CharField("Pais",max_length=50,blank=True,null=True)
	region=models.CharField("Region",max_length=50,blank=True,null=True)
	continente=models.CharField("Continente",max_length=50,blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPlVentas2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPlVentas2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Plan Ventas 2021'
		verbose_name_plural = 'Plan Ventas 2021'

	def __str__(self):
		return "%s" % (self.nombre_cliente)
