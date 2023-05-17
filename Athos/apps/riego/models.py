from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import cultivo
from apps.menu.models import Estado
from apps.menu.models import fundo
from apps.menu.models import ProgramaProduccion
from apps.maestras.models import TanquesAthos

# Create your models here.
class ProductosRiego(models.Model):
	subgrupo= models.CharField("SubGrupo", max_length=50,null=True, blank=True)
	partidarc= models.CharField("Partida RC", max_length=50,null=True, blank=True)
	familia= models.CharField("Familia", max_length=50,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Productos Riego'
		verbose_name_plural = 'Productos Riego'

	def __str__(self):
		return "%s" % (self.familia)



class MetodoRiego(models.Model):
	metodo= models.CharField("Metodo", max_length=50)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMetodoRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMetodoRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Metodo Riego'
		verbose_name_plural = 'Metodo Riego'

	def __str__(self):
		return "%s" % (self.metodo)



class EquiposRiego(models.Model):
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaRiego")
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoRiego")
	equipo= models.CharField("Equipo", max_length=50)
	descripcion= models.CharField("Descripcion", max_length=50)
	reservorio= models.CharField("Reservorio", max_length=50)
	anexo_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoRiego")
	factor_correccion=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	centro_costo=models.BigIntegerField(blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEquipoRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEquipoRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Equipo Riego'
		verbose_name_plural = 'Equipo Riego'

	def __str__(self):
		return "%s-%s" % (self.equipo,self.descripcion)


class PozosRiego(models.Model):
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaPozoRiego")
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoPozoRiego",blank=True, null=True)
	anio=models.IntegerField("Año", blank=True, null=True)
	nombre= models.CharField("Nombre de Pozo", max_length=50)
	codigo= models.CharField("Codigo Autorizacion", max_length=50)
	npozo= models.IntegerField("NroPozo", blank=True, null=True)
	capacidad=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	capacidad_real=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	caudal_autorizado=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	factor_correccion=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

	capacidad_ene=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_feb=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_mar=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_abr=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_may=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_jun=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_jul=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_ago=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_sep=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_oct=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_nov=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	capacidad_dic=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPozoRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPozoRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Pozo Riego'
		verbose_name_plural = 'Pozo Riego'

	def __str__(self):
		return "%s-%s" % (self.codigo, self.nombre)

class LeyNutricionRiego(models.Model):

	codigo= models.IntegerField("Codigo Material", blank=True, null=True)
	anexo_producto = models.ForeignKey(ProductosRiego, on_delete=models.CASCADE, related_name="AnexoLeyProductosRiego")
	nombre= models.CharField("Nombre Comercial", max_length=50)
	um= models.CharField("UM", max_length=50)
	n=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	p2o5=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	k2o=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	cao=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	mgo=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	s=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	fe=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	mn=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	b=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	zn=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	mo=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ci=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	cu=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	h2o=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	kc=models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionLeyRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModLeyRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ley Nutricion Riego'
		verbose_name_plural = 'Ley Nutricion Riego'

	def __str__(self):
		return "%s-%s" % (self.codigo, self.nombre)



class OperadoresRiegoAthos(models.Model):
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoOperadorZonaR",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoOperadorFundoR",null=True, blank=True)	
	codigo_sap=models.IntegerField(blank=True, null=True)
	dni= models.CharField("DNI", max_length=50,null=True, blank=True)
	descripcion= models.CharField("Descripcion", max_length=50,null=True, blank=True)
	funcion= models.CharField("Funcion", max_length=50,null=True, blank=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoOperadorEstadoR")

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionOperadorRieAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModOperadorRieAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Operador Riego Athos'
		verbose_name_plural = 'Operador Riego Athos'

	def __str__(self):
		return "%s-%s" % (self.dni, self.descripcion)




class ProyeccionSemanalRiego(models.Model):
	anio= models.IntegerField("Año", blank=True, null=True)
	semana= models.IntegerField("Semana", blank=True, null=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoProyeccionCultivoRiego")
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoProyeccionZonaRiego")
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoProyeccionFundoRiego")

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProyeccionSemanalRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProyeccionSemanalRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Proyeccion Semanal Riego'
		verbose_name_plural = 'Proyeccion Semanal Riego'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.semana, self.anexo_cultivo, self.fecha_hora_creacion, self.usuario_creacion)

class DetalleProyeccionSemanalRiego(models.Model):
	anexo_detalle = models.ForeignKey(ProyeccionSemanalRiego, on_delete=models.CASCADE, related_name="AnexoDetProyeccionCultivoRiego")
	anexo_ley = models.ForeignKey(LeyNutricionRiego, on_delete=models.CASCADE, related_name="AnexoLeyDetalleProySemRiego")
	anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPepDetalleProySemRiego",null=True, blank=True)

	semana_1=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	semana_2=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	semana_3=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	semana_4=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetProyeccionSemanalRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetProyeccionSemanalRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Proyeccion Semanal Riego'
		verbose_name_plural = 'Detalle-Proyeccion Semanal Riego'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_ley, self.fecha_hora_creacion, self.usuario_creacion)

class SemDetalleProyeccionSemanalRiego(models.Model):
	anexo_detalle = models.ForeignKey(DetalleProyeccionSemanalRiego, on_delete=models.CASCADE, related_name="AnexoDetProyeccionCultivoRiego")
	
	sem2=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem3=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem4=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSemDetProyeccionSemanalRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSemDetProyeccionSemanalRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Proyeccion Semanal Riego-Sem x'
		verbose_name_plural = 'Detalle-Proyeccion Semanal Riego-Sem x'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle, self.fecha_hora_creacion, self.usuario_creacion)






class RegistroProyeccionSemanalRiego(models.Model):
	anexo_detalle = models.ForeignKey(ProyeccionSemanalRiego, on_delete=models.CASCADE, related_name="AnexoRegProyeccionCultivoRiego")
	anexo_ley = models.ForeignKey(LeyNutricionRiego, on_delete=models.CASCADE, related_name="AnexoLeyRegProySemRiego", blank=True, null=True)
	sem2=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem3=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem4=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	sem5=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRegProyeccionSemanalRiego")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRegProyeccionSemanalRiego",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle Semanal-Proyeccion Semanal Riego'
		verbose_name_plural = 'Detalle Semanal-Proyeccion Semanal Riego'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle, self.fecha_hora_creacion, self.usuario_creacion)


class RegistroRiegoFertilizacion(models.Model):
	anio=models.IntegerField(blank=True,null=True)
	semana=models.IntegerField(blank=True,null=True)

	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoRiegoFerti")
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaRiegoFert")
	anexo_fundo = models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoRiegofert")
	anexo_pep=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPRiego")
	anexo_metodo = models.ForeignKey(MetodoRiego, on_delete=models.CASCADE, related_name="AnexoRegistroFertRiego")
	anexo_equipo = models.ForeignKey(EquiposRiego, on_delete=models.CASCADE, related_name="AnexoEquiposFertRiego")
	nroreserva=models.IntegerField(blank=True,null=True)
	
	area=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRegRiegFer")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRegRiegFer",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Capa1-Registro Riego Fertizacion'
		verbose_name_plural = 'Capa1-Registro Riego Fertizacion'

	def __str__(self):
		return "%s-%s-%s-%s-%s" % (self.anexo_pep,self.nroreserva, self.anexo_cultivo, self.fecha_hora_creacion, self.usuario_creacion)
	

class TanqueRiegoFertilizacion(models.Model):
	
	desc=models.IntegerField(blank=True, null=True)
	

	

	class Meta:
		verbose_name = 'Tanque Riego Fertizacion'
		verbose_name_plural = 'Tanque Riego Fertizacion'

	def __str__(self):
		return "%s" % (self.desc)
	





class DetalleRegistroRiegoFertilizacion(models.Model):

	anexo_detalle = models.ForeignKey(RegistroRiegoFertilizacion, on_delete=models.CASCADE, related_name="AnexoDetRegRiegoFert")
	anexo_fecha=models.DateField("fecha",null=True, blank=True)
	turno=models.CharField("Turno", max_length=100,blank=True, null=True)
	hectareaje=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	kc=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	m3=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	anexo_tanque = models.ForeignKey(TanqueRiegoFertilizacion, on_delete=models.CASCADE, related_name="AnexoTanqueRiegoFert",blank=True, null=True)

	pulso1=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	pulso2=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	pulso3=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	pulso4=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	pulso5=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	eto_acu=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	valvula=models.CharField("Valvula", max_length=100, blank=True, null=True)	
	proporcion=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	solucion_madre=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetRegRiegFer")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetRegRiegFer",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Capa2-Detalle  Riego '
		verbose_name_plural = 'Capa2-Detalle  Riego '

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_detalle.anexo_pep,self.anexo_fecha,self.anexo_detalle.nroreserva,self.turno)



	@property
	def suma_consumo(self):
		consumos = self.AnexoDetalleRegRiegoFertilizacion1.all()
		suma = 0
		for con in consumos:
			suma += con.consumo
		return (suma)

	@property
	def resto_consumo(self):
		return self.m3 - self.suma_consumo





class DetRequerimientoRiegoFert(models.Model):

	anexo_detalle = models.ForeignKey(RegistroRiegoFertilizacion, on_delete=models.CASCADE, related_name="AnexoDetReqRiegoFert1",blank=True, null=True)
	anexo_ley = models.ForeignKey(LeyNutricionRiego, on_delete=models.CASCADE, related_name="AnexoLeyDetRegRiegoFert1",blank=True, null=True)
	total_producto=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	lunes=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	martes=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	miercoles=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	jueves=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	viernes=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	sabado=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	domingo=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetReqRegRiegFer")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetReqRegRiegFer",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Capa2-Requerimiento de Fertilizantes '
		verbose_name_plural = 'Capa2-Requerimiento de Fertilizantes '

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_detalle,self.anexo_ley, self.fecha_hora_creacion, self.usuario_creacion)


	@property
	def suma_consumo(self):
		consumos = self.AnexoConsumoRegRiegoFert.all()
		suma = 0
		for con in consumos:
			suma += con.consumo
		return (suma)

	@property
	def resto_consumo(self):
		return self.total_producto - self.suma_consumo








class SelectorPulsoRiego(models.Model):
	selector=models.IntegerField(blank=True, null=True)


	class Meta:
		verbose_name = 'Selector Pulso Riego'
		verbose_name_plural = 'Selector Pulso Riego'

	def __str__(self):
		return "%s" % (self.selector)








class DetalleRequerimientoRiegot(models.Model):
	anexo_detalle = models.ForeignKey(DetalleRegistroRiegoFertilizacion, on_delete=models.CASCADE, related_name="AnexoDetalleRegRiegoFertilizacion1" , blank=True, null=True)
	
	
	fecha_consumo=models.DateField("Fecha Consumo", blank=True, null=True)
	consumo=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)	
	anexo_pulso = models.ForeignKey(SelectorPulsoRiego, on_delete=models.CASCADE, related_name="AnexoPulsoDetRiegoT" , blank=True, null=True)
	
	anexo_operador = models.ForeignKey(OperadoresRiegoAthos, on_delete=models.CASCADE, related_name="AnexoOpeDetRiegoT" , blank=True, null=True)
	
	hora_inicio=models.TimeField("Hora Inicio", blank=True, null=True)
	hora_final=models.TimeField("Hora Final", blank=True, null=True)
	
	codigo=models.CharField("Codigo Regador",max_length=150,blank=True,null=True)
	ph_agua=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ce_agua=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ph_solucion=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ce_solucion=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	tensio20=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	tensio30=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	
	tensio40=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	tensio60=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	tensio90=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	
	caudal_inicial=models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
	caudal_final=models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)

	paf=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	pdf=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	pdvr=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	observacion=models.CharField("Observacion",max_length=150,blank=True,null=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleConsumoReqRegRieg")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleConsumoReqRegRieg",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Capa3-COnsumo Requerimiento de Riego '
		verbose_name_plural = 'Capa3-COnsumo Requerimiento de Riego '

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_detalle.anexo_pep,self.fecha_consumo, self.hora_inicio)


class ConsumoRequerimientoRiegoFert(models.Model):

	anexo_detalle = models.ForeignKey(DetRequerimientoRiegoFert, on_delete=models.CASCADE, related_name="AnexoConsumoRegRiegoFert")
	consumo=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	fecha_consumo=models.DateField("Fecha Consumo", blank=True, null=True)
	anexo_riego=models.ForeignKey(DetalleRequerimientoRiegot, on_delete=models.CASCADE, related_name="AnexoDetalleRiegoF1",blank=True, null=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionConsumoReqRegRiegFer")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModConsumoReqRegRiegFer",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Capa3-Consumo Requerimiento de Fertilizantes '
		verbose_name_plural = 'Capa3-Consumo Requerimiento de Fertilizantes '

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_detalle,self.anexo_detalle.anexo_ley, self.fecha_consumo, self.usuario_creacion)




class ExplotacionPozos(models.Model):
	fecha= models.DateField("Fecha", blank=True, null=True)
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeExplotacion")
	anexo_pozo = models.ForeignKey(PozosRiego, on_delete=models.CASCADE, related_name="AnexoExplotacionPozo")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionExplotacionPozo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModExplotacionPozo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'CAPA1-EXPLOTACION POZOS'
		verbose_name_plural = 'CAPA1-EXPLOTACION POZOS'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.anexo_zona, self.anexo_pozo)
	

class RptaExplotacionPozos(models.Model):
	
	rpta=models.CharField("Respuesta",max_length=50,blank=True,null=True)
	

	

	class Meta:
		verbose_name = 'Respuesta Explotacion pozos'
		verbose_name_plural = 'Respuesta Explotacion pozos'

	def __str__(self):
		return "%s" % (self.rpta)



class DetalleExplotacionPozos(models.Model):
	
	anexo_detalle = models.ForeignKey(ExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoDetalleExplotacion")
	hora_inicio=models.TimeField("Hora Inicio", blank=True, null=True)
	hora_final=models.TimeField("Hora Final", blank=True, null=True)
	hidro_inicial=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	hidro_final=models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

	nivel_estatico=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	nivel_dinamico=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ce=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
	ph=models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

	anexo_rpta1 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo1")
	anexo_rpta2 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo2")
	anexo_rpta3 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo3")
	anexo_rpta4 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo4")
	anexo_rpta5 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo5")
	anexo_rpta6 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo6")
	anexo_rpta7 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo7")
	anexo_rpta8 = models.ForeignKey(RptaExplotacionPozos, on_delete=models.CASCADE, related_name="AnexoRptaPozo8")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetExplotacionPozo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetExplotacionPozo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'CAPA2-DETALLE EXPLOTACION POZOS'
		verbose_name_plural = 'CAPA2-DETALLE EXPLOTACION POZOS'

	def __str__(self):
		return "%s-%s" % (self.anexo_detalle, self.fecha_hora_creacion)


class EstacionMeteorologica(models.Model):
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEstacion")
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEstacion",blank=True, null=True)
	fecha_hora = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	eto_mm=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	tem_min=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	tem_max=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	tem_pro=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	rad_min=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	rad_max=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	vel_min=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	vel_max=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	hr=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	precipitacion=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	hmen18=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	h18=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	hmay18=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
									
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEstacionMet")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEstacionMet",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Estacion Meteorologica'
		verbose_name_plural = 'Estacion Meteorologica'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_zona, self.anexo_fundo,self.fecha_hora_creacion)


#SOLUCIONES MADRES
class SolucionesMadres(models.Model):
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoSolucionesMadresZona",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoSolucionesMadresFundo",null=True, blank=True)
	anio= models.IntegerField(null=True, blank=True)
	semana= models.IntegerField(null=True, blank=True)
	numero_tanque=models.ForeignKey(TanquesAthos, on_delete=models.CASCADE, related_name="AnexoSolucionesMadresNumeroTanque", null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSolucionesMadres")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSolucionesMadres",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Soluciones Madres'
		verbose_name_plural = 'Soluciones Madres'
	
	def __str__(self):
		return "%s-%s" % ( self.anexo_fundo,self.anexo_zona)

class DetalleSolucionesMadres(models.Model):
	anexo_detalle = models.ForeignKey(SolucionesMadres, on_delete=models.CASCADE, related_name="AnexoDetSolucionesMadres")
	anexo_fertilizante = models.ForeignKey(LeyNutricionRiego, on_delete=models.CASCADE, related_name="AnexoDetalleSolucionesMadres",null=True, blank=True)
	cantidad= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleSolucionesMadres")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleSolucionesMadres",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Detalle Soluciones Madres'
		verbose_name_plural = 'Detalle Soluciones Madres'
		
	def __str__(self):
		return "%s-%s" % (self.anexo_detalle.anexo_zona ,self.anexo_fertilizante,self.cantidad)