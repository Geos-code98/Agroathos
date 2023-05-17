from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import cultivo
from apps.menu.models import Estado
from apps.menu.models import VersionAgronomica
from apps.menu.models import Estado
from apps.menu.models import fundo
from apps.menu.models import ProgramaProduccion
# Create your models here.

class ProductosSanidad(models.Model):
	subgrupo= models.CharField("SubGrupo", max_length=50,null=True, blank=True)
	partidarc= models.CharField("Partida RC", max_length=50,null=True, blank=True)
	producto= models.CharField("Familia", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProductoSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProductoSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Grupos-Productos Sanidad'
		verbose_name_plural = 'Grupos-Productos Sanidad'

	def __str__(self):
		return "%s" % ( self.producto)

class IngredientesSanidad(models.Model):
	ingrediente= models.CharField("Ingredientes", max_length=200)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionIngredientesSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModIngredientesSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ingredientes Sanidad'
		verbose_name_plural = 'Ingredientes Sanidad'

	def __str__(self):
		return "%s" % (self.ingrediente)


class ToxicologiaSanidad(models.Model):
	toxico= models.CharField("Toxicologia", max_length=50)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionToxicologiaSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModToxicologiaSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Toxicologia Sanidad'
		verbose_name_plural = 'Toxicologia Sanidad'

	def __str__(self):
		return "%s" % (self.toxico)

class PlagasEnfermedadesSanidad(models.Model):

	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoPlagasEnfSanidad",null=True, blank=True)
	tipo= models.CharField("Tipo", max_length=50,null=True, blank=True)
	nombre_comun= models.CharField("Nombre Comun", max_length=50,null=True, blank=True)
	nombre_cientifico= models.CharField("Nombre Especifico", max_length=50,null=True, blank=True)

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPlagasEnfSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPlagasEnfSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Plagas Enfermedades Sanidad'
		verbose_name_plural = 'Plagas Enfermedades Sanidad'

	def __str__(self):
		return "%s-%s-%s" % (self.id,self.nombre_comun, self.nombre_cientifico)


class TipoMetodoSanidad(models.Model):
	metodo= models.CharField("Metodo", max_length=50,null=True, blank=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTipoMetodoSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTipoMetodoSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Tipo Metodo Sanidad'
		verbose_name_plural = 'Tipo Metodo Sanidad'

	def __str__(self):
		return "%s" % (self.metodo)

class EquiposSanidad(models.Model):
	anexo_zona= models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="UsercreacionEquipoZona")
	
	equipo= models.CharField("Equipo", max_length=50,null=True, blank=True)
	equipo_sap= models.CharField("Equipos SAP", max_length=50,null=True, blank=True)
	tequipo=models.CharField("Tipo de Equipo", max_length=50,null=True, blank=True)
	implemento= models.CharField("Implemento", max_length=50,null=True, blank=True)
	factor=models.DecimalField(max_digits=9, decimal_places=1, blank=True, null=True)

	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="UsercreacionEquipoEstado")
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEquipoSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEquipoSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Equipo Sanidad'
		verbose_name_plural = 'Equipo Sanidad'

	def __str__(self):
		return "%s-%s" % (self.equipo, self.implemento)

class TipoDosisSanidad(models.Model):
	tipo= models.CharField("Tipo de Dosis", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTipoDosisSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTipoDosisSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Tipo Dosis Sanidad'
		verbose_name_plural = 'Tipo Dosis Sanidad'

	def __str__(self):
		return "%s" % (self.tipo)

class LugaresAplicacionSanidad(models.Model):
	codigo= models.CharField("Codigo Lugar", max_length=50,null=True, blank=True)
	lugar= models.CharField("Lugar", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionLugarAplicacionanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModLugarAplicacionSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Lugares Aplicacion Sanidad'
		verbose_name_plural = 'Lugares Aplicacion Sanidad'

	def __str__(self):
		return "%s-%s" % (self.codigo, self.lugar)

class TractoresAthos(models.Model):
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoTractorZona",null=True, blank=True)
	codigo= models.CharField("Codigo Lugar", max_length=50,null=True, blank=True)
	marca= models.CharField("Marca", max_length=50,null=True, blank=True)
	modelo=models.CharField("Modelo", max_length=50,null=True, blank=True)
	placa=models.CharField("Placa", max_length=50,null=True, blank=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoTractorEstado")
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTractorAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTractorAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Tractores Athos'
		verbose_name_plural = 'Tractores Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.codigo, self.marca, self.placa)

class BoquillasSanidadAthos(models.Model):

	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaBoquilla",null=True, blank=True)
	codigo= models.CharField("Codigo", max_length=50,null=True, blank=True)
	boquilla= models.CharField("Boquilla", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionBoquillasAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModBoquillasAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Boquillas Athos'
		verbose_name_plural = 'Boquillas Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.boquilla, self.fecha_hora_creacion, self.usuario_creacion)

class OperadoresSanidadAthos(models.Model):
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoOperadorZona",null=True, blank=True)
	codigo_sap=models.IntegerField(blank=True, null=True)
	dni= models.CharField("DNI", max_length=50,null=True, blank=True)
	descripcion= models.CharField("Descripcion", max_length=50,null=True, blank=True)
	funcion= models.CharField("Funcion", max_length=50,null=True, blank=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoOperadorEstado")

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionOperadorAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModOperadorAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Operador Sanidad Athos'
		verbose_name_plural = 'Operador Sanidad Athos'

	def __str__(self):
		return "%s-%s" % (self.dni, self.descripcion)


class UbicacionProductosAutorizados(models.Model):

	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoUbicacionCultivoPr")
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionUbicacionPrAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModUbicacionPrAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ubicacion Productos Sanidad Athos'
		verbose_name_plural = 'Ubicacion Productos Sanidad Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_cultivo, self.fecha_hora_creacion, self.usuario_creacion)

class PermitidoSanidad(models.Model):
	desc=models.CharField("Descripcion", max_length=100,blank=True, null=True)
	class Meta:
		verbose_name = 'Permitido Sanidad'
		verbose_name_plural = 'Permitido Sanidad'

	def __str__(self):
		return "%s" % (self.desc)

class ProductosAutorizados(models.Model):

	anexo_detalle=models.ForeignKey(UbicacionProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoUbicacionProductos")
	anexo_producto=models.ForeignKey(ProductosSanidad, on_delete=models.CASCADE, related_name="AnexoPrProductosAutorizados")
	codigo_material=models.IntegerField(blank=True, null=True)
	nom_comercial=models.CharField("Nombre Comercial", max_length=100,blank=True, null=True)
	anexo_ingrediente=models.ForeignKey(IngredientesSanidad, on_delete=models.CASCADE, related_name="AnexoIngredientesProductos")
	anexo_toxico=models.ForeignKey(ToxicologiaSanidad, on_delete=models.CASCADE, related_name="AnexoToxicologiaProductos")
	um=models.CharField("UM", max_length=100,blank=True, null=True)
	pr=models.IntegerField(blank=True, null=True)
	uac=models.IntegerField(blank=True, null=True)
	equivalencia=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	nroaplicaciones=models.CharField("Nro Aplicaciones", max_length=100,blank=True, null=True)
	
	concentracion_ia=models.CharField("Concentracion IA", max_length=100,blank=True, null=True)
	formulacion=models.CharField("Concentracion IA", max_length=100,blank=True, null=True)		
	pc=models.IntegerField(blank=True, null=True)
	codigo_senasa=models.CharField("Concentracion IA", max_length=100,blank=True, null=True)	
	anexo_permitido=models.ForeignKey(PermitidoSanidad, on_delete=models.CASCADE, related_name="AnexoPermitidoSanidad",blank=True, null=True)
	anexo_versiones=models.ForeignKey(VersionAgronomica, on_delete=models.CASCADE, related_name="AnexoPrVersionSanidad",blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoPrEstadoSanidad",blank=True, null=True)

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProductosAutorizadosAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProductosAutorizadosAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Productos Permitidos Sanidad Athos'
		verbose_name_plural = 'Productos Permitidos Sanidad Athos'

	def __str__(self):
		return "%s-%s" % (self.codigo_material, self.nom_comercial)


class MaestraLMR(models.Model):

	destino= models.CharField("Destino", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMLMRAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMLMRAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Maestra LMR'
		verbose_name_plural = 'Maestra LMR'

	def __str__(self):
		return "%s" % (self.destino)





class DetalleProductosAutorizados(models.Model):

	anexo_detalle=models.ForeignKey(ProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoDetalleProductosAutorizados")
	anexo_plagas=models.ForeignKey(PlagasEnfermedadesSanidad, on_delete=models.CASCADE, related_name="AnexoPlagasProductosAutorizados")
	anexo_dosis=models.ForeignKey(TipoDosisSanidad, on_delete=models.CASCADE, related_name="AnexoDosisProductosAutorizados" ,blank=True, null=True)
	factor_premezcla=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	dosis_min=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	dosis_max=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	por_concentracion_min=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	por_concentracion_max=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleProductosAutorizadosAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleProductosAutorizadosAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Productos Sanidad Athos'
		verbose_name_plural = 'Detalle-Productos Sanidad Athos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_detalle,self.anexo_plagas, self.fecha_hora_creacion, self.usuario_creacion)



class DetalleLmrPa(models.Model):

	anexo_detalle=models.ForeignKey(ProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoProductosLmrAutorizados")
	anexo_lmr=models.ForeignKey(MaestraLMR, on_delete=models.CASCADE, related_name="AnexoLMRProductosAutorizados")
	dato_lmr=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleLMRProductosAutorizadosAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleLMRProductosAutorizadosAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	
	class Meta:
		verbose_name = 'Detalle LMR -Productos Sanidad Athos'
		verbose_name_plural = 'Detalle LMR -Productos Sanidad Athos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_detalle,self.anexo_lmr, self.fecha_hora_creacion, self.usuario_creacion)


class RptaMezcla(models.Model):

	mezcla= models.CharField("Rpta Mezcla", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Rpta-Mezcla'
		verbose_name_plural = 'Rpta-Mezcla'

	def __str__(self):
		return "%s" % (self.mezcla)

class UbicacionRegistroAplicacion(models.Model):

	nroreserva=models.IntegerField(blank=True, null=True)
	anexo_permitido=models.ForeignKey(PermitidoSanidad, on_delete=models.CASCADE, related_name="AnexoPermitidosUbiRegAplicacion", blank=True, null=True)

	anexo_fecha=models.DateField("Fecha", blank=True, null=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoRegistroAplicacion" ,null=True, blank=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeRegistroAplicacion" ,null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoRegistroAplicacion",null=True, blank=True)
	anexo_produccion=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoFundoRegistroAplicacion" ,null=True, blank=True)
	area_aplicada=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	vol_agua=models.IntegerField(blank=True, null=True)
	numero_tanque=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

	anexo_metodo= models.ForeignKey(TipoMetodoSanidad, on_delete=models.CASCADE, related_name="AnexoUbiTipoMetRegAplicacion",null=True, blank=True)
	anexo_equipo= models.ForeignKey(EquiposSanidad, on_delete=models.CASCADE, related_name="AnexoUbiEquiposRegAplicacion",null=True, blank=True)
	
	codigo_boquilla=models.CharField("Cod Boquilla", max_length=50,null=True, blank=True)
	num_boquilla=models.IntegerField(blank=True, null=True)
	presion=models.IntegerField(blank=True, null=True)
	capacidad_tanque=models.IntegerField(blank=True, null=True)

	anexo_tractor=models.ForeignKey(TractoresAthos, on_delete=models.CASCADE, related_name="AnexoTractorRegistroAplicacion",null=True, blank=True)
	marcha=models.CharField("Placa", max_length=50,null=True, blank=True)
	rpm=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	velocidad=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	
	fecha_aplicacion=models.DateField(blank=True, null=True)
	fecha_premezcla=models.DateField(blank=True, null=True)
	anexo_operario = models.ForeignKey(OperadoresSanidadAthos, on_delete=models.CASCADE, related_name="AnexoOpeRegistroAplicacion",blank=True, null=True)
	anexo_lugar=models.ForeignKey(LugaresAplicacionSanidad, on_delete=models.CASCADE, related_name="AnexoLugRegistroAplicacion",blank=True, null=True)
	observacion=models.CharField("Observacion", max_length=200,null=True, blank=True)

	idequipo=models.CharField("Equipo", max_length=100,blank=True, null=True)
	idoperario=models.CharField("Operario", max_length=100,blank=True, null=True)
	idtractor=models.CharField("Tractor", max_length=100,blank=True, null=True)	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionUbiRegAplicacionAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModUbiRegAplicacioAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Capa1-Ubicacion Registro Aplicacion Athos'
		verbose_name_plural = 'Capa1-Ubicacion Registro Aplicacion Athos'

	def __str__(self):
		return "%s-%s-%s-%s-%s" % (self.anexo_produccion,self.nroreserva,self.anexo_cultivo, self.fecha_hora_creacion, self.usuario_creacion)


class RegistroAplicacion(models.Model):

	anexo_detalle = models.ForeignKey(UbicacionRegistroAplicacion, on_delete=models.CASCADE, related_name="AnexoRegistroAplicacion")


	anexo_rpta = models.ForeignKey(RptaMezcla, on_delete=models.CASCADE, related_name="AnexoRplaMezclaAplicacion1",blank=True, null=True)
	anexo_listas = models.ForeignKey(ProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoProductosRegistroAplicacion",blank=True, null=True)
	dosis=models.DecimalField(blank=True, null=True,max_digits=9, decimal_places=3)
	dosis_real=models.DecimalField(blank=True, null=True,max_digits=9, decimal_places=3)

	total_producto=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	anexo_tipo= models.ForeignKey(TipoDosisSanidad, on_delete=models.CASCADE, related_name="AnexoTipoDRegAplicacion",blank=True, null=True)
	factor=models.DecimalField(blank=True, null=True,max_digits=9, decimal_places=3)
	tipo_dosis_real= models.ForeignKey(TipoDosisSanidad, on_delete=models.CASCADE, related_name="AnexoTipoDRegAplicacionReal", blank=True, null=True)

	hora_inicio= models.TimeField("Hora Inicio", blank=True, null=True)
	hora_final= models.TimeField("Hora Fin", blank=True, null=True)
	cod_aplicador=models.CharField("Cod Aplicador", max_length=50,null=True, blank=True)
	anexo_objetivo=models.ForeignKey(PlagasEnfermedadesSanidad, on_delete=models.CASCADE, related_name="AnexoDetalleObjRegistroAplicacion",blank=True, null=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRegAplicacionAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRegAplicacionAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Capa2-Registro Aplicacion Sanidad'
		verbose_name_plural = 'Capa2-Registro Aplicacion Sanidad'

	def __str__(self):
		return "%s-%s-%s-%s-%s-%s" % (self.anexo_detalle.id,self.anexo_detalle.anexo_produccion,self.anexo_detalle.nroreserva,self.anexo_listas, self.fecha_hora_creacion,self.usuario_creacion)


	@property
	def suma_consumo(self):
		consumos = self.AnexoDetRegistroAplicacion.all()
		suma = 0
		for con in consumos:
			suma += con.consumo_detalle
		return (suma)

	@property
	def resto_consumo(self):
		return self.total_producto - self.suma_consumo

class DetalleRegistroAplicacion(models.Model):
	anexo_detalle = models.ForeignKey(RegistroAplicacion, on_delete=models.CASCADE, related_name="AnexoDetRegistroAplicacion")
	
	consumo_detalle=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	fecha_consumo = models.DateField("Fecha Consumo",null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetRegAplicacionAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetRegAplicacionAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Capa3-detalle-Registro Aplicacion Sanidad'
		verbose_name_plural = 'Capa3-detalle -Registro Aplicacion Sanidad'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_detalle.anexo_produccion,self.anexo_detalle.anexo_detalle.nroreserva, self.fecha_hora_creacion)


class ConfirmativaRegistroAplicacion(models.Model):

	anexo_detalle = models.ForeignKey(UbicacionRegistroAplicacion, on_delete=models.CASCADE, related_name="AnexoConfirRegistroAplicacion")
		
	hora_inicio= models.TimeField("Hora Inicio", blank=True, null=True)
	hora_final= models.TimeField("Hora Fin", blank=True, null=True)

	anexo_aplicador = models.ForeignKey(OperadoresSanidadAthos, on_delete=models.CASCADE, related_name="AnexoConfirOperarioAplicacion",blank=True, null=True)
	
	cod_aplicador=models.CharField("Cod Aplicador", max_length=150,null=True, blank=True)
	
	temperatura=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	hr=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	vv=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	ph_antes=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ce_antes=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	ph_despues=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ce_despues=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	observaciones=models.CharField("Obs", max_length=150,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionConfirRegAplicacionAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModConfirRegAplicacionAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'Capa1-Confirmativa-Registro Aplicacion Sanidad'
		verbose_name_plural = 'Capa1-Confirmativa -Registro Aplicacion Sanidad'

	def __str__(self):
		return "%s-%s-%s" % (self.id,self.anexo_detalle, self.usuario_creacion )

class ProyeccionSemanalSanidad(models.Model):
	anio= models.IntegerField("Año", blank=True, null=True)
	semana= models.IntegerField("Semana", blank=True, null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoProyeccionCultivoSanidad")
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoProyeccionZonaSanidad")
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoProyeccionFundoSanidad")

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProyeccionSemanalSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProyeccionSemanalSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Proyeccion Semanal Sanidad'
		verbose_name_plural = 'Proyeccion Semanal Sanidad'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.semana, self.anexo_cultivo, self.fecha_hora_creacion, self.usuario_creacion)

class DetalleProyeccionSemanalSanidad(models.Model):
	anexo_detalle = models.ForeignKey(ProyeccionSemanalSanidad, on_delete=models.CASCADE, related_name="AnexoDetProyeccionCultivoSanidad")
	
	anexo_producto=models.ForeignKey(ProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoDetProyec",blank=True, null=True)
	cantidad=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetProyeccionSemanalSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetProyeccionSemanalSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Proyeccion Semanal Sanidad'
		verbose_name_plural = 'Detalle-Proyeccion Semanal Sanidad'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle, self.fecha_hora_creacion, self.usuario_creacion)


class RegistroProyeccionSemanalSanidad(models.Model):
	anexo_detalle = models.ForeignKey(DetalleProyeccionSemanalSanidad, on_delete=models.CASCADE, related_name="AnexoRegDetProyeccionCultivoSanidad")

	sem2=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem3=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem4=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRegProyeccionSemanalSanidad")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRegProyeccionSemanalSanidad",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle Semanal-Proyeccion Semanal Sanidad'
		verbose_name_plural = 'Detalle Semanal-Proyeccion Semanal Sanidad'

	def __str__(self):
		return "%s-%s-%s" % (self.sem2, self.fecha_hora_creacion, self.usuario_creacion)