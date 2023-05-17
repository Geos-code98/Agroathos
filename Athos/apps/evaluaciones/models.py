from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import UbicacionFundo
from apps.menu.models import ProgramaProduccion
from apps.menu.models import ejezona
from apps.menu.models import fundo

from apps.menu.models import LPaletas
from apps.maestras.models import PresentacionesAthos
from apps.menu.models import Turno

from apps.menu.models import CentrosAthos
from apps.menu.models import cultivo
from apps.menu.models import variedad
from apps.menu.models import TurnoProgramaProduccion

from apps.maestras.models import ClientesAthos
from apps.maestras.models import CalibresAthos
from apps.maestras.models import MaestraPresentacionesAthos
from apps.maestras.models import AcomodoAthos
from apps.maestras.models import LineaEmpaqueAthos
from apps.maestras.models import AuxiliaresCampoAthos
from apps.maestras.models import MaestraFundoCultivo

from apps.acopio_athos.granada.models import TipoCalidadFruta

from apps.planta.granada_planta.models import LineasPlanta

from apps.menu.models import MaterialMMPP
from apps.sanidad.models import ProductosAutorizados
from apps.menu.models import Planta

# Create your models here.

class SelectorRespuestaEscalaCalidad(models.Model):
	
	
	desc= models.CharField("Respuesta Escala", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Respuesta Escala Calidad '
		verbose_name_plural = 'Selector Respuesta Escala Calidad'

	def __str__(self):
		return "%s" % (self.desc)

class SelectorRespuestaSiNoCalidad(models.Model):
	
	
	desc= models.CharField("Respuesta SiNO", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Respuesta SiNO Calidad '
		verbose_name_plural = 'Selector Respuesta SiNO Calidad'

	def __str__(self):
		return "%s" % (self.desc)
class SectoresAthos(models.Model):
	sector= models.CharField("sector", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvSector")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvSector",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'sector '
		verbose_name_plural = 'sectores'

	def __str__(self):
		return "%s" % ( self.sector)

class TipoEvaluacionBr(models.Model):
	desc= models.CharField("Tipo ev", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo EV '
		verbose_name_plural = 'Tipo EV'

	def __str__(self):
		return "%s" % ( self.desc)

class EvFenBrotesArandanos(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEv",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEv",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvBrotes")
	
	valvula= models.CharField("Valvula", max_length=30)
	anexo_tipo=models.ForeignKey(TipoEvaluacionBr, on_delete=models.CASCADE, related_name="AnexoTipoEVBr",null=True, blank=True)



	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenBrotes")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenBrotes",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Fenologia Brotes Arandanos '
		verbose_name_plural = 'Ev. Fenologia Brotes Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.ubicacion, self.ubicacion.id)

class DetallePlantaEvFenBrotesArandanos(models.Model):
	anexo_evaluacion = models.ForeignKey(EvFenBrotesArandanos, on_delete=models.CASCADE, related_name="AnexoEVDetalle",null=True, blank=True)
	n_planta= models.DecimalField(max_digits=7, decimal_places=0,null=True, blank=True)
	ancho= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	largo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cant_ramas= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetPlanta")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvDetPlanta",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Detalle-Ev. Fen. Brote Detalle Planta Arandanos '
		verbose_name_plural = 'Detalle-Ev. Fen. Brotes Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s" % (self.n_planta, self.cant_ramas)

class NBrotes(models.Model):
	nbrotes= models.IntegerField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionNBrotes")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModNbrotes",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Nbrotes '
		verbose_name_plural = 'NBrotes'

	def __str__(self):
		return "%s" % ( self.nbrotes)

class NDiametro (models.Model):
	ndiametro= models.IntegerField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDiametro")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDiametro",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'NDiametro '
		verbose_name_plural = 'NDiametro'

	def __str__(self):
		return "%s" % ( self.ndiametro)

class tipoyema (models.Model):
	yema= models.CharField(max_length=30,null=True, blank=True)
	

	class Meta:
		verbose_name = 'Tipo Yema'
		verbose_name_plural = 'Tipo de Yemas'

	def __str__(self):
		return "%s" % ( self.yema)


class BrotePlantaEvFenBrotesArandanos(models.Model):
	anexo_detalle = models.ForeignKey(DetallePlantaEvFenBrotesArandanos, on_delete=models.CASCADE, related_name="AnexoEVDetalleBrote",null=True, blank=True)
	anexo_diametro = models.ForeignKey(NDiametro, on_delete=models.CASCADE,null=True, blank=True)
	diametro= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	anexo_brote = models.ForeignKey(NBrotes, on_delete=models.CASCADE,null=True, blank=True)
	anexo_yema = models.ForeignKey(tipoyema, on_delete=models.CASCADE,null=True, blank=True)

	altura= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	diametrobrote= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	nudos= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hojas= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	A1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	L1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	A2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	L2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	A3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	L3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	axilas= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	
	yhinchada= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	yescamosa= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	ycargador=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	botonfloral= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	botonrosado= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	flor= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cuajado= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	verde1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	verde2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	verde3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	verde4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	
	verderojo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojoverde= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojoazul= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	azulrojo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	maduro= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionBrote")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvBrote",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ev. Fen. Brote Detalle Planta Arandanos '
		verbose_name_plural = 'Ev. Fen. Brotes Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_evaluacion.ubicacion,self.usuario_creacion, self.fecha_hora_creacion)

class EvFenRaicesArandanos(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvRaAr",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvRaAr",null=True, blank=True)

	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoUbiEvRaices")
	
	valvula= models.CharField("Valvula", max_length=30)
	observacion= models.CharField("Observacion", max_length=250,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenRaices")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenRaices",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Fenologia Raices Arandanos '
		verbose_name_plural = 'Ev. Fenologia  Raices Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.anexo_zona,self.ubicacion)

class DetalleEvFenRaicesArandanos(models.Model):
	
	anexo_detalle = models.ForeignKey(EvFenRaicesArandanos, on_delete=models.CASCADE, related_name="AnexoDetEvRaices")
	num_planta= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	ancho= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	largo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	alto= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	altura_molde= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvFenRaices")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvFenRaices",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle Ev. Fenologia Raices Arandanos '
		verbose_name_plural = 'Detalle Ev. Fenologia  Raices Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_detalle, self.num_planta)

class ZonaRaices (models.Model):
	zona= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'zona '
		verbose_name_plural = 'zonas'

	def __str__(self):
		return "%s" % ( self.zona)

class RaicesEvFenRaicesArandanos(models.Model):
	
	anexo_raices = models.ForeignKey(DetalleEvFenRaicesArandanos, on_delete=models.CASCADE, related_name="AnexoRaicesDetEvRaices")
	sr= models.IntegerField(null=True, blank=True)
	re= models.IntegerField(null=True, blank=True)
	rfs= models.IntegerField(null=True, blank=True)
	rfj= models.IntegerField(null=True, blank=True)
	rfjb= models.IntegerField(null=True, blank=True)
	anexo_cuadrante = models.ForeignKey(NDiametro, on_delete=models.CASCADE, related_name="AnexoCuadranteRaices",null=True, blank=True)
	anexo_zona = models.ForeignKey(ZonaRaices, on_delete=models.CASCADE, related_name="AnexoZonaRaices",null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRaicesEvFenRaices")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModRaicesEvFenRaices",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Raices Ev. Fenologia Raices Arandanos '
		verbose_name_plural = 'Raices Ev. Fenologia  Raices Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_raices, self.sr)

class SelectorAthos (models.Model):
	selector= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'SelectorAthos '
		verbose_name_plural = 'SelectorAthos'

	def __str__(self):
		return "%s" % ( self.selector)

class ControlProductoTerminado(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoCPT", blank=True, null=True)
	

	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoCptTurno",null=True, blank=True)
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCptCentros",null=True, blank=True)
	anexo_linea=models.ForeignKey(LineaEmpaqueAthos, on_delete=models.CASCADE, related_name="AnexoCptLineaE",null=True, blank=True)
	anexo_pagina=models.ForeignKey(SelectorAthos, on_delete=models.CASCADE, related_name="AnexoPaginaControl", blank=True, null=True)
	observacion=models.CharField(max_length=300, blank=True, null= True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserCreacionCPT")
	fecha = models.DateField("Fecha",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación")
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCPT",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Control Producto Terminado'
		verbose_name_plural = ' Control Producto Terminado'

	def __str__(self):
		return "%s-%s" % ( self.fecha_hora_creacion,self.usuario_creacion)

class DetalleControlProductoTerminado(models.Model):
	anexo_detalle=models.ForeignKey(ControlProductoTerminado, on_delete=models.CASCADE, related_name="AnexoDetalleCPT", blank=True, null=True)
	anexo_muestra=models.ForeignKey(SelectorAthos, on_delete=models.CASCADE, related_name="AnexoDetalleMuestra", blank=True, null=True)
	npalet= models.IntegerField(null=True, blank=True, unique=True)
	trazabilidad= models.CharField("Trazabilidad", max_length=250,null=True, blank=True)
	anexo_presentaciong=models.ForeignKey(PresentacionesAthos, on_delete=models.CASCADE, related_name="AnexoPresentaciongCPT", blank=True, null=True)
	anexo_cliente=models.ForeignKey(ClientesAthos, on_delete=models.CASCADE, related_name="AnexoDetalleCliente", blank=True, null=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoDetalleVariedad", blank=True, null=True)
	anexo_calibre=models.ForeignKey(CalibresAthos, on_delete=models.CASCADE, related_name="AnexoDetalleCalibre", blank=True, null=True)
	anexo_presentacion=models.ForeignKey(MaestraPresentacionesAthos, on_delete=models.CASCADE, related_name="AnexoDetalleMaestraP", blank=True, null=True)
	
	tamano_pulpa= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	peso_neto= models.IntegerField(null=True, blank=True)
	homogeneidad= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	anexo_acomodo=models.ForeignKey(AcomodoAthos, on_delete=models.CASCADE, related_name="AnexoDetalleAcomodo", blank=True, null=True)
	firme= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	sensitivo= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	blando= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	n1= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	n2= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	n3= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	n4= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	pudricion= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	micelio= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	heridas= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	deshidratacion= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	desgarro= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	exudacion= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	machucon= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	polvo= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	deforme= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	russet= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	presencia= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	restos= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	inmadura_verde= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	inmadura_rojo= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	
	bajo_calibre= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	material_extrano= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	cochinilla= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	mosca_fruta= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	arana_fruta= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	globito= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	decoloracion= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	fruta_hinchada= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)

	p1= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p2= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p3= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p4= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p5= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p6= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p7= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p8= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p9= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p10= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p11= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	p12= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetCPT")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetCPT",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'CDet ontrol Producto Terminado'
		verbose_name_plural = 'Det  Control Producto Terminado'

	def __str__(self):
		return "%s-%s-%s-%s" % ( self.npalet, self.trazabilidad,self.fecha_hora_creacion,self.usuario_creacion)

class EvFenBrotesArandanosSem(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvSem",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvSem",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvBrotesSem")
	
	valvula= models.CharField("Valvula", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenBrotesSem1")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenBrotesSem1",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Sem-Ev. Fenologia Brotes Arandanos '
		verbose_name_plural = 'Sem-Ev. Fenologia Brotes Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.ubicacion, self.ubicacion.id)

class DetallePlantaEvFenBrotesArandanosSem(models.Model):
	anexo_evaluacion = models.ForeignKey(EvFenBrotesArandanosSem, on_delete=models.CASCADE, related_name="AnexoEVDetalleSem",null=True, blank=True)
	n_planta= models.DecimalField(max_digits=5, decimal_places=0,null=True, blank=True)
	nramas= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	nbrotes= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)

	verde1= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	verde2= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	verde3= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	verde4= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	
	
	verderojo= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	rojoverde= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	rojoazul= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	azulrojo= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)
	maduro= models.DecimalField(max_digits=8, decimal_places=4,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetPlantaSem")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvDetPlantaSem",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Sem-Ev. Fen. Brote Detalle Planta Arandanos '
		verbose_name_plural = 'Sem-Ev. Fen. Brotes Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s" % (self.n_planta, self.fecha_hora_creacion)

class BrotePlantaEvFenBrotesArandanosSem(models.Model):
	anexo_detalle = models.ForeignKey(DetallePlantaEvFenBrotesArandanosSem, on_delete=models.CASCADE, related_name="AnexoEVDetalleBroteSem",null=True, blank=True)
	
	
	verde4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	
	verderojo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojoverde= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojoazul= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	azulrojo= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	maduro= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionBroteSem1")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvBroteSem1",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Sem-Ev. Fen. Brote Detalle Planta Arandanos '
		verbose_name_plural = 'Sem-Ev. Fen. Brotes Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s" % (self.id, self.fecha_hora_creacion)

class SectorPlagaAthos (models.Model):
	selector= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Plagas Athos '
		verbose_name_plural = 'Selector Plagas Athos'

	def __str__(self):
		return "%s" % ( self.selector)

class EvSanPlagasArandanos(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvSanPl",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvSanPl",null=True, blank=True)
	anexo_sector = models.ForeignKey(SectorPlagaAthos, on_delete=models.CASCADE, related_name="AnexoSectorEvSanPl",null=True, blank=True)
	area_eval= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoUbiEvSanPl")
	anexo_pagina=models.ForeignKey(SelectorAthos, on_delete=models.CASCADE, related_name="AnexoPaginaEv", blank=True, null=True)

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvSanPl")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvSanPl",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Ev. Sanidad Plagas Arandanos '
		verbose_name_plural = 'Ev. Sanidad  Plagas Arandanos'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.ubicacion)

class GruposPlagasArandanos(models.Model):
	
	anexo_evaluacion=models.ForeignKey(EvSanPlagasArandanos, on_delete=models.CASCADE, related_name="AnexoGruposPlagas",null=True, blank=True)	
	grupo= models.CharField("Grupos", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionGruposPlagas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModGruposPlagas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Grupos Ev. Sanidad Plagas Arandanos '
		verbose_name_plural = 'Grupos Ev. Sanidad  Plagas Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_evaluacion, self.grupo)

class SubGruposPlagasArandanos(models.Model):
	
	anexo_sub=models.ForeignKey(GruposPlagasArandanos, on_delete=models.CASCADE, related_name="AnexoPlagasAr",null=True, blank=True)	
	subgrupo= models.CharField("Grupos", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionAnexoPlagasAr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModAnexoPlagasAr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'SubGrupo EV  Plagas Arandanos '
		verbose_name_plural = 'SubGrupo  EV Plagas Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_sub, self.subgrupo)

class VariablesPlagasArandanos(models.Model):
	
	anexo_var=models.ForeignKey(SubGruposPlagasArandanos, on_delete=models.CASCADE, related_name="AnexoVarAr",null=True, blank=True)	
	valor=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	acaro_hialino_nplanta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	arana_roja_nplanta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	argy_spha_nfrutos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	argy_spha_nlarvasgr=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	argy_spha_nlarvaspe=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	argy_spha_nplantas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cigarrita_individuos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_porplantas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_nadultos_corona=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_nadultos_planta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ninfas_corona=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ovisacos_corona=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ovisacos_planta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_adultos_brotes=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_adultos_ramas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ninfas_frutos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ninfas_brotes=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ninfas_ramas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ovisacos_brotes=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cochi_hari_ovisacos_ramas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	crypto_plantas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	diabro=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	gryllus=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	helio_plantas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	helio_frutos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	helio_larvasgr=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	helio_larvaspe=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	helio_posturas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	membracidos_nplanta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	mosca_blanca_ninfa=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	mosca_blanca_adulta=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	mosca_fruta_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	plecto_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	prosco_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pulgones_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pulgones_brotes=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pulgones_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	queresas_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	queresas_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	spodo_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	spodo_larvargr=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	spodo_larvape=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	spodo_masa=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	trips_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	aranas_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cocci_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	crisopas_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	cryptola_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	otros_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	alternaria_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	grado_infestacion=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	antra_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	botritis_flores=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	botritis_frutos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	botritis_num=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	lasio_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pestalo_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pestalo_ramas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	phyto_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	planta_quemadas_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	planta_quemadas_ramas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	roya_por=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	roya_grado=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_ancha_hojas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_ancha_cotiledones=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_ancha_hojas2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_angosta_focos=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_angosta_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	hoja_angosta_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	abejas=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionAnexoVarAr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModAnexoVarAr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Variable EV  Plagas Arandanos '
		verbose_name_plural = 'Variables  EV Plagas Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_var, self.fecha_hora_creacion)


class EvFenFrutoArandanos(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvFruto",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvFruto",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvFruto")
	
	valvula= models.CharField("Valvula", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenFrutos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenFrutos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev Fenologica Frutos'
		verbose_name_plural = 'Ev Fenologica Frutos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.fecha, self.ubicacion, self.fecha_hora_creacion, self.usuario_creacion)

class SelectorEvFrutos (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector EV Frutos '
		verbose_name_plural = 'Selector EV Frutos'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class DetalleEvFenFrutoArandanos(models.Model):
	
	anexo_detalle=models.ForeignKey(EvFenFrutoArandanos, on_delete=models.CASCADE, related_name="AnexoDetEvFruto",null=True, blank=True)
	nbaya=models.IntegerField(null=True, blank=True)
	calibre=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	anexo_selector=models.ForeignKey(SelectorEvFrutos, on_delete=models.CASCADE, related_name="AnexoSelectorEvFruto",null=True, blank=True)
	
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvFenFrutos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvFenFrutos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Det-Ev Fenologica Frutos'
		verbose_name_plural = 'Det-Ev Fenologica Frutos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.ubicacion,self.fecha_hora_creacion, self.usuario_creacion)

class EvFenPlanasa(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvPlanasa",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvPlanasa",null=True, blank=True)

	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoUbiEvPlanasa")
	
	valvula= models.CharField("Valvula", max_length=30)
	observacion= models.CharField("Observacion", max_length=250,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenPlanasa")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenPlanasa",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Fenologia Planasa'
		verbose_name_plural = 'Ev. Fenologia  Planasa'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_fundo, self.ubicacion,self.fecha_hora_creacion)

class SelectorEvPlanasa (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector EV Planasa'
		verbose_name_plural = 'Selector EV Planasa'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class SelectorBroteEvPlanasa (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Brote EV Planasa'
		verbose_name_plural = 'Selector  Brote EV Planasa'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class DetalleEvFenPlanasa(models.Model):
	
	anexo_detalle=models.ForeignKey(EvFenPlanasa, on_delete=models.CASCADE, related_name="AnexoDetalleEvPlanasa",null=True, blank=True)
	anexo_brote=models.ForeignKey(SelectorBroteEvPlanasa, on_delete=models.CASCADE, related_name="AnexoSelBroteEvPlanasa",null=True, blank=True)
	cod_planta= models.CharField("Codigo Planta", max_length=30)
	altura_planta= models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	cantidad= models.IntegerField(null=True, blank=True)
	anexo_selector=models.ForeignKey(SelectorEvPlanasa, on_delete=models.CASCADE, related_name="AnexoSelectorEvPlanasa",null=True, blank=True)
	longitud1= models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	longitud2= models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	diametro= models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	nro_hojas= models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvFenPlanasa")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvFenPlanasa",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Ev. Fenologia Planasa'
		verbose_name_plural = 'Detalle-Ev. Fenologia  Planasa'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.ubicacion, self.usuario_creacion,self.fecha_hora_creacion)

class EvCalDefectosCampo(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvCalCampo",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvCalCampo",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCalCampo")
	

	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalCampo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalCampo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Defectos Campos '
		verbose_name_plural = 'Ev. Calidad Defectos Campos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.ubicacion, self.ubicacion.id)

class SelectorTipoCalidad (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Tipo Calidad-Ev. Calidad'
		verbose_name_plural = 'Selector  Tipo Calidad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class SelectorCasetaCalidad (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Caseta Calidad-Ev. Calidad'
		verbose_name_plural = 'Selector  Caseta Calidad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class SelectorTipoEnvase(models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Tipo de Envase Calidad-Ev. Calidad'
		verbose_name_plural = 'Selector  Tipo de Envase Calidad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class SelectorTipoEnvasePlanta(models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Tipo de Envase Calidad-Ev. Calidad Planta'
		verbose_name_plural = 'Selector  Tipo de Envase Calidad -Ev. Calidad Planta'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class SelectorNroEvalCalidad (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Nro Eval Calidad-Ev. Calidad'
		verbose_name_plural = 'Selector  Nro Eval Calidad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class DetalleEvCalDefectosCampo(models.Model):
	anexo_detalle=models.ForeignKey(EvCalDefectosCampo, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalCampo",null=True, blank=True)
	valvula= models.CharField("Valvula", max_length=300,null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadEvCalCampo",null=True, blank=True)
	densidad= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	reingreso= models.IntegerField(null=True, blank=True)
	anexo_tipo = models.ForeignKey(SelectorTipoCalidad, on_delete=models.CASCADE, related_name="AnexoTipoDetalleRvCal")
	muestra= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	exportable= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	remanente= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	desgarro= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	inmadurez= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	polvo= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	bayas= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	restos_florales= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	heridas= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	bajo_calibre= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	pudricion= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cochinilla= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fruta_decolorada= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	anexo_caseta = models.ForeignKey(SelectorCasetaCalidad, on_delete=models.CASCADE, related_name="AnexoCasetaEvCal",null=True, blank=True)
	anexo_tipo_envase = models.ForeignKey(SelectorTipoEnvase, on_delete=models.CASCADE, related_name="AnexoTipoEnvaseEvCal",null=True, blank=True)
	anexo_evaluacion = models.ForeignKey(SelectorNroEvalCalidad, on_delete=models.CASCADE, related_name="AnexoNroEvCal",null=True, blank=True)
	
	
	dni= models.CharField(max_length=10, null=True, blank=True)
	anexo_auxiliares = models.ForeignKey(AuxiliaresCampoAthos, on_delete=models.CASCADE, related_name="AnexoAuxiliarEvCal")
	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalCampo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalCampo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle-Ev. Calidad Defectos Campos '
		verbose_name_plural = 'Detalle-Ev. Calidad Defectos Campos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle, self.fecha_hora_creacion, self.usuario_creacion)

class SelectorTipoPrioridad (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Tipo Prioridad-Ev. Calidad'
		verbose_name_plural = 'Selector  Tipo Prioridad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class EvCalAcopioPlanta(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoLanzadoEvCal",null=True, blank=True)
	fecha=models.DateField("Fecha de Ingreso",null=True, blank=True)
	idacopio= models.IntegerField(null=True, blank=True, unique=True)
	tpulpa= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_mediano=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_grande=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_extra=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_jumbo=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_micelio_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_herida_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_deshidratacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_desgarro_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_exudacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_machucon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_polvo_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_deformes_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_russet_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_presenciap_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_restos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutaiv_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutair_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_bajoc_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_materiale_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_cochinilla_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_pulgon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_moscaf_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_aranas_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)	

	fir_m6_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m7_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m8_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m9_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m10_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m11_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m12_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m13_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m14_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m15_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_blandos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_desgarro2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	tol_frutosr4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_frutosr4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	anexo_prioridad=models.ForeignKey(SelectorTipoPrioridad, on_delete=models.CASCADE, related_name="AnexoPriorid",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)
	
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalAcopio")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalAcopio",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Acopio Planta '
		verbose_name_plural = 'Ev. Calidad Acopio Planta'

	def __str__(self):
		return "%s-%s-%s" % (self.idacopio, self.fecha_hora_creacion, self.usuario_creacion)

#ICA-EVCALACOPIO2021-1

class SelectorTipoFirmeza (models.Model):
	desc= models.CharField(max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Selector Tipo Firmeza-Ev. Calidad'
		verbose_name_plural = 'Selector  Tipo Firmeza -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class EvCalAcopioPlantaArIca2021(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoLanzadoEvCalArIca2021",null=True, blank=True)
	fecha=models.DateField("Fecha de Ingreso",null=True, blank=True)
	idacopio= models.IntegerField(null=True, blank=True, unique=True)
	tpulpa= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_mediano=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_grande=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_extra=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_jumbo=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_micelio_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_herida_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_deshidratacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_desgarro_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_exudacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_machucon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_polvo_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_deformes_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_russet_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_presenciap_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_restos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutaiv_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutair_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_bajoc_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_materiale_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_cochinilla_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_moscaf_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_aranas_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m1_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza1",null=True, blank=True)
	fir_m1_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza2",null=True, blank=True)
	fir_m1_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza3",null=True, blank=True)
	fir_m1_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza4",null=True, blank=True)

	fir_m2_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza5",null=True, blank=True)
	fir_m2_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza6",null=True, blank=True)
	fir_m2_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza7",null=True, blank=True)
	fir_m2_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza8",null=True, blank=True)

	fir_m3_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza9",null=True, blank=True)
	fir_m3_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza10",null=True, blank=True)
	fir_m3_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza11",null=True, blank=True)
	fir_m3_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza12",null=True, blank=True)

	fir_m4_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza13",null=True, blank=True)
	fir_m4_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza14",null=True, blank=True)
	fir_m4_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza15",null=True, blank=True)
	fir_m4_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza16",null=True, blank=True)

	fir_m5_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza17",null=True, blank=True)
	fir_m5_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza18",null=True, blank=True)
	fir_m5_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza19",null=True, blank=True)
	fir_m5_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza20",null=True, blank=True)	

	fir_m6_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza21",null=True, blank=True)
	fir_m6_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza22",null=True, blank=True)
	fir_m6_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza23",null=True, blank=True)
	fir_m6_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza24",null=True, blank=True)

	fir_m7_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza25",null=True, blank=True)
	fir_m7_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza26",null=True, blank=True)
	fir_m7_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza27",null=True, blank=True)
	fir_m7_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza28",null=True, blank=True)

	fir_m8_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza29",null=True, blank=True)
	fir_m8_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza30",null=True, blank=True)
	fir_m8_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza31",null=True, blank=True)
	fir_m8_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza32",null=True, blank=True)

	fir_m9_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza33",null=True, blank=True)
	fir_m9_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza34",null=True, blank=True)
	fir_m9_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza35",null=True, blank=True)
	fir_m9_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza36",null=True, blank=True)

	fir_m10_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza37",null=True, blank=True)
	fir_m10_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza38",null=True, blank=True)
	fir_m10_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza39",null=True, blank=True)
	fir_m10_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza40",null=True, blank=True)

	fir_m11_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza41",null=True, blank=True)
	fir_m11_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza42",null=True, blank=True)
	fir_m11_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza43",null=True, blank=True)
	fir_m11_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza44",null=True, blank=True)
	fir_m12_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza45",null=True, blank=True)
	fir_m12_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza46",null=True, blank=True)
	fir_m12_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza47",null=True, blank=True)
	fir_m12_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza48",null=True, blank=True)

	fir_m13_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza49",null=True, blank=True)
	fir_m13_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza50",null=True, blank=True)
	fir_m13_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza51",null=True, blank=True)
	fir_m13_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza52",null=True, blank=True)

	fir_m14_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza53",null=True, blank=True)
	fir_m14_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza54",null=True, blank=True)
	fir_m14_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza55",null=True, blank=True)
	fir_m14_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza56",null=True, blank=True)

	fir_m15_1=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza57",null=True, blank=True)
	fir_m15_2=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza58",null=True, blank=True)
	fir_m15_3=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza59",null=True, blank=True)
	fir_m15_4=models.ForeignKey(SelectorTipoFirmeza, on_delete=models.CASCADE, related_name="AnexoTipoFirmeza60",null=True, blank=True)

	tol_blandos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_blandos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_desgarro2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	tol_frutosr4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_frutosr4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	anexo_prioridad=models.ForeignKey(SelectorTipoPrioridad, on_delete=models.CASCADE, related_name="AnexoPrioridArIca2021",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)
	
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalAcopioArIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Acopio Planta '
		verbose_name_plural = 'Ev. Calidad Acopio Planta'

	def __str__(self):
		return "%s-%s-%s" % (self.idacopio, self.fecha_hora_creacion, self.usuario_creacion)

class EvCalAcopioPlantaArIca202202(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoLanzadoEvCalArIca202202",null=True, blank=True)
	fecha=models.DateField("Fecha de Ingreso",null=True, blank=True)
	idacopio= models.IntegerField(null=True, blank=True, unique=True)
	tpulpa= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_mediano=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_grande=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_extra=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_jumbo=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_micelio_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_herida_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_deshidratacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_desgarro_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_exudacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_machucon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_polvo_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_deformes_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_russet_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_presenciap_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_restos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutaiv_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutair_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_bajoc_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_materiale_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_cochinilla_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_moscaf_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_aranas_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)	

	fir_m6_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m7_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m8_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m9_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m10_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m11_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m12_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m13_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m14_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m15_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_blandos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_desgarro2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	tol_frutosr4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_frutosr4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	anexo_prioridad=models.ForeignKey(SelectorTipoPrioridad, on_delete=models.CASCADE, related_name="AnexoPrioridArIca202202",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalAcopioArIca202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)

	class Meta:
		verbose_name = 'Ev. Calidad Acopio Planta 202202'
		verbose_name_plural = 'Ev. Calidad Acopio Planta 202202'

	def __str__(self):
		return "%s-%s-%s" % (self.idacopio, self.fecha_hora_creacion, self.usuario_creacion)

class EvCalAcopioPlantaArCaraz2021(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoLanzadoEvCalArCaraz2021",null=True, blank=True)
	fecha=models.DateField("Fecha de Ingreso",null=True, blank=True)
	idacopio= models.IntegerField(null=True, blank=True, unique=True)
	tpulpa= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_mediano=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_grande=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_extra=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_jumbo=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_micelio_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_herida_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_deshidratacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_desgarro_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_exudacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_machucon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_polvo_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_deformes_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_russet_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_presenciap_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_restos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutaiv_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutair_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_bajoc_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_materiale_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_cochinilla_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_pulgon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_moscaf_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_aranas_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)	

	fir_m6_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m7_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m8_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m9_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m10_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m11_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m12_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m13_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m14_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m15_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_blandos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_desgarro2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	tol_frutosr4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_frutosr4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	anexo_prioridad=models.ForeignKey(SelectorTipoPrioridad, on_delete=models.CASCADE, related_name="AnexoPrioridArCaraz2021",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)
	
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalAcopioArCaraz2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalAcopioArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Acopio Planta-Ar Caraz 2021 '
		verbose_name_plural = 'Ev. Calidad Acopio Planta- Ar Caraz 2021'

	def __str__(self):
		return "%s-%s-%s" % (self.idacopio, self.fecha_hora_creacion, self.usuario_creacion)

class EvCalAcopioPlantaArCaraz202202(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoLanzadoEvCalArCaraz202202",null=True, blank=True)
	fecha=models.DateField("Fecha de Ingreso",null=True, blank=True)
	idacopio= models.IntegerField(null=True, blank=True, unique=True)
	anexo_tipo_envase = models.ForeignKey(SelectorTipoEnvasePlanta, on_delete=models.CASCADE, related_name="AnexoTipoEnvasePlantaEvCal",null=True, blank=True)
	tpulpa= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	dl_tamano1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dl_tamano4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	dc_mediano=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_grande=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_extra=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	dc_jumbo=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	nb_n1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	nb_n4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	cd_pudricion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_pudricion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	cd_blando_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_blando_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_micelio_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_micelio_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_herida_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_herida_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_deshidratacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_deshidratacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_desgarro_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_desgarro_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_exudacion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_exudacion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_machucon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_machucon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_partidura_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_partidura_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_partidura_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_partidura_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_fruta_hinchada_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_fruta_hinchada_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_fruta_hinchada_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_fruta_hinchada_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cd_globito_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_globito_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_globito_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cd_globito_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_polvo_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_polvo_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_deformes_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_deformes_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_picadura_ave_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_picadura_ave_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_picadura_ave_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_picadura_ave_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_russet_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_russet_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_cicatriz_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_cicatriz_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_cicatriz_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_cicatriz_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_presenciap_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_presenciap_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_restos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_restos_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutaiv_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutaiv_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_frutair_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_frutair_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_bajoc_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_bajoc_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_materiale_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_materiale_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cal_decoloracion_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_decoloracion_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_decoloracion_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cal_decoloracion_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_cochinilla_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_cochinilla_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_pulgon_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_pulgon_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_moscaf_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_moscaf_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fit_aranas_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fit_aranas_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	sol_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	sol_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	aci_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	aci_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	cpu_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	cpu_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m2_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m3_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m3_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m5_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m5_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)	

	fir_m6_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m6_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m7_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m7_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m8_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m8_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m9_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m9_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m10_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m10_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m11_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m11_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m12_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m12_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m13_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m13_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m14_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m14_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	fir_m15_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	fir_m15_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_1=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_blandos_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_def_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_desgarro2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	
	tol_frutosr4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp2_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos3_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_frutosr4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_restosf3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp3_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_blandos4_3=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_cic2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	tol_def2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_desgarro2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_deshidratado2_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_frutosr4_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_polvo1_4=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosf4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	tol_restosp4_2=models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)

	anexo_prioridad=models.ForeignKey(SelectorTipoPrioridad, on_delete=models.CASCADE, related_name="AnexoPrioridArCaraz202202",null=True, blank=True)
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalAcopioArCaraz202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalAcopioArCaraz202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ev. Calidad Acopio Planta-Ar Caraz 202202'
		verbose_name_plural = 'Ev. Calidad Acopio Planta- Ar Caraz 202202'

	def __str__(self):
		return "%s-%s-%s" % (self.idacopio, self.fecha_hora_creacion, self.usuario_creacion)

class EvCartillaDrenado(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvCartillaDrenado",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvCartillaDrenado",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCartillaDrenado")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCartillaDrenado")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCartillaDrenado",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Ev. Cartilla de Drenado '
		verbose_name_plural = 'Ev. Cartilla de Drenado'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.anexo_fundo, self.ubicacion)


class SelectorUbiDetEvCartillaDrenado(models.Model):
	desc= models.CharField("Ubicacion", max_length=300,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector-Detalle-Ev. Cartilla Drenado '
		verbose_name_plural = 'Selector Detalle-Ev. Cartilla Drenado'

	def __str__(self):
		return "%s" % (self.desc)

class SelectorPulsoDetEvCartillaDrenado(models.Model):
	
	
	desc= models.CharField("Pulso", max_length=300,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Pulso-Detalle-Ev. Cartilla Drenado '
		verbose_name_plural = 'Pulso-Detalle-Ev. Cartilla Drenado'

	def __str__(self):
		return "%s" % (self.desc)


class DetalleEvCartillaDrenado(models.Model):
	anexo_detalle=models.ForeignKey(EvCartillaDrenado, on_delete=models.CASCADE, related_name="AnexoDetalleEvCartillaDrenado",null=True, blank=True)
	valvula= models.CharField("Valvula", max_length=300,null=True, blank=True)
	
	
	volumen_drenado= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	volumen_drenado_1m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_1m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_1m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)


	volumen_drenado_1f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_1f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_1f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)



	volumen_drenado_2i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_2i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_2i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)




	volumen_drenado_2m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_2m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_2m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	volumen_drenado_2f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_2f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_2f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)


	volumen_drenado_3i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_3i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_3i= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	volumen_drenado_3m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_3m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_3m= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	volumen_drenado_3f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	volumen_maceta_3f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
	ce_3f= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	pulso= models.CharField("Valvua", max_length=300,null=True, blank=True)
	

	
	observacion= models.CharField("Observacion", max_length=300,null=True, blank=True)
	
	
	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCartillaDrenado")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCartillaDrenado",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	
	class Meta:
		verbose_name = 'Detalle-Ev. Cartilla Drenado '
		verbose_name_plural = 'Detalle-Ev. Cartilla Drenado'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.ubicacion, self.fecha_hora_creacion, self.usuario_creacion)



class SelTipoTrabajadorEvCalPodaAr(models.Model):
	
	
	desc= models.CharField("Tipo Trabajador", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Tipo Trabajador Ev. Cal Poda '
		verbose_name_plural = 'Selector Tipo Trabajador Ev. Cal Poda'

	def __str__(self):
		return "%s" % (self.desc)

class SelectorTCalidad(models.Model):
	
	
	desc= models.CharField("TCalidad", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector TCalidad Ev. Cal Poda '
		verbose_name_plural = 'Selector TCalidad Ev. Cal Poda'

	def __str__(self):
		return "%s" % (self.desc)


class SelectorDistribucionPoda(models.Model):
	
	
	desc= models.CharField("Distribucion", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Distribucion Ev. Cal Poda '
		verbose_name_plural = 'Selector Distribucion Ev. Cal Poda'

	def __str__(self):
		return "%s" % (self.desc)

class SelTrabajadorEvCalPodaAr(models.Model):
	
	
	desc= models.CharField("Trabajador", max_length=200,null=True, blank=True)
	anexo_tipo=models.ForeignKey(SelTipoTrabajadorEvCalPodaAr, on_delete=models.CASCADE, related_name="AnexoTipoTrabajadorEvCalPodaAr",null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSelTrabajadorEVCalPodaAr",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSelTrabajadorEVCalPodaAr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Trabajador Ev. Cal Poda '
		verbose_name_plural = 'Selector Trabajador Ev. Cal Poda'

	def __str__(self):
		return "%s" % (self.desc)


class EvCalPodaAr(models.Model):
	fecha= models.DateField("Fecha",null=True, blank=True)
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvCalPodaAr",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvCalPodaAr",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoEvCalPodaAr",null=True, blank=True)
	anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPEPEvCalPodaAr",null=True, blank=True)
	
	anexo_trabajador=models.ForeignKey(SelTrabajadorEvCalPodaAr, on_delete=models.CASCADE, related_name="AnexoTrabajadorEvCalPodaAr",null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalPodaAr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalPodaAr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Ev. Cal Poda Arandano'
		verbose_name_plural = 'Ev. Cal Poda Arandano'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.anexo_zona, self.anexo_fundo)


class DetalleEvCalPodaAr(models.Model):
	
	anexo_detalle=models.ForeignKey(EvCalPodaAr, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalPodaAr",null=True, blank=True)
	
	anexo_responsable=models.ForeignKey(SelTrabajadorEvCalPodaAr, on_delete=models.CASCADE, related_name="AnexoZonaEvCalPodaAr",null=True, blank=True)
	dni= models.BigIntegerField(null=True, blank=True)
	valvula= models.CharField("Valvula", max_length=200,null=True, blank=True)
	anexo_valvula= models.ForeignKey(TurnoProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoValvulaEvCalPodaAr",null=True, blank=True)
	anexo_tcalidad=models.ForeignKey(SelectorTCalidad, on_delete=models.CASCADE, related_name="AnexoTCalidadEvCalPodaAr",null=True, blank=True)
	anexo_produccion=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPProduccionEvCalPodaAr",null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadEvCalPodaAr",null=True, blank=True)
	anexo_distribucion=models.ForeignKey(SelectorDistribucionPoda, on_delete=models.CASCADE, related_name="AnexoDistribucionEvCalPodaAr",null=True, blank=True)
	
	num_ramas= models.IntegerField(null=True, blank=True)
	num_ramas_debajo= models.IntegerField(null=True, blank=True)
	num_ramas_encima= models.IntegerField(null=True, blank=True)
	
	num_tirasavias= models.IntegerField(null=True, blank=True)
	num_ramas_5mm= models.IntegerField(null=True, blank=True)
	num_ramas_16mm= models.IntegerField(null=True, blank=True)
	
	ramas_cruzados= models.IntegerField(null=True, blank=True)
	ramas_daniocorte=models.IntegerField(null=True, blank=True)
	ramas_delgados5= models.IntegerField(null=True, blank=True)
	ramas_flujo3=models.IntegerField(null=True, blank=True)
	corte_recto=models.IntegerField(null=True, blank=True)
	
	altura_rama= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	anexo_preg1=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="AnexoPREG1EvCalPodaAr",null=True, blank=True)
	anexo_preg2=models.ForeignKey(SelectorRespuestaEscalaCalidad, on_delete=models.CASCADE, related_name="AnexoPREG2EvCalPodaAr",null=True, blank=True)
	anexo_preg3=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="AnexoPREG3EvCalPodaAr",null=True, blank=True)
	anexo_preg4=models.ForeignKey(SelectorRespuestaEscalaCalidad, on_delete=models.CASCADE, related_name="AnexoPREG4EvCalPodaAr",null=True, blank=True)
	anexo_preg5=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="AnexoPREG5EvCalPodaAr",null=True, blank=True)
	
	observacion= models.CharField("Observacion", max_length=250,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleEvCalPodaAr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleEvCalPodaAr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Detalle Ev. Cal Poda Arandano'
		verbose_name_plural = 'Detalle Ev. Cal Poda Arandano'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle,self.anexo_produccion)

class EvCalMuestreoCosechaHg2021(models.Model):
    fecha=models.DateField("Fecha de Enfriado")
    anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaMuestreoCosechaHg2021",null=True, blank=True)
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoMuestreoCosechaHg2021",null=True, blank=True)
    ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCalMuestreoCosechaHg2021")
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMuestreoCosechaHg2021")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMuestreoCosechaHg2021",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    class Meta:
        verbose_name = 'Ev. Calidad Cosecha Higo 2021 '
        verbose_name_plural = 'Ev. Calidad Cosecha Higo 2021'

    def __str__(self):
        return "%s-%s-%s" % (self.anexo_zona, self.ubicacion, self.usuario_creacion)


class DetalleEvCalMuestreoCosechaHg2021(models.Model):
	anexo_detalle=models.ForeignKey(EvCalMuestreoCosechaHg2021, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalHg2021",null=True, blank=True)
	valvula= models.CharField("Sector", max_length=250,null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadEvCalHg2021",null=True, blank=True)
	dni= models.BigIntegerField(null=True, blank=True)

	densidad= models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
	reingreso= models.IntegerField(null=True, blank=True)
	anexo_caseta = models.ForeignKey(SelectorCasetaCalidad, on_delete=models.CASCADE, related_name="AnexoCasetaEvCalMuestreoCosechaHG2021",null=True, blank=True)
	anexo_tipo = models.ForeignKey(SelectorTipoCalidad, on_delete=models.CASCADE, related_name="AnexoTipoEvCalHg2021")
    
	nfrutas= models.IntegerField(null=True, blank=True)
	inmaduro= models.IntegerField(null=True, blank=True)
	sobremaduro= models.IntegerField(null=True, blank=True)
	mal_corte= models.IntegerField(null=True, blank=True)
	danio_mecanico= models.IntegerField(null=True, blank=True)
	latex= models.IntegerField(null=True, blank=True)
	excremento_ave= models.IntegerField(null=True, blank=True)
	estadio_2= models.IntegerField(null=True, blank=True)

	optimo= models.IntegerField(null=True, blank=True)
	fruta_suelo=models.IntegerField(null=True, blank=True)

	anexo_auxiliares = models.ForeignKey(AuxiliaresCampoAthos, on_delete=models.CASCADE, related_name="AnexoAuxiliarEvCalHg2021")
	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	exportable= models.IntegerField(null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalHg2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalHg2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
	class Meta:
		verbose_name = 'Detalle Ev.Calidad Muestreo Cosecha Higo 2021'
		verbose_name_plural = 'Detalle Ev. Calidad Muestreo cosecha higo 2021'
   
	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle, self.anexo_auxiliares, self.dni)


class EvCalMuestreoPlantaHgIca2021(models.Model):
    fecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
    anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaMuestreoPlantaHgIca2021",null=True, blank=True)
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoMuestreoPlantaHgIca2021",null=True, blank=True)
    ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCalMuestreoPlantaHgIca2021")
    nro_guia= models.CharField("Nro Guia", max_length=250,null=True, blank=True)
    anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadMuestreoPlantaHgIca2021",null=True, blank=True)
    fecha_cosecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
    njabas= models.IntegerField(null=True, blank=True)
    peso_planta= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
    peso_promedio= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
    hora_ingreso = models.TimeField("Hora Ingreso",blank=True, null=True)
    hora_inicio = models.TimeField("Hora Inicio",blank=True, null=True)
    temperatura_pulpa= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    peso_muestra= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMuestreoPlantaHgIca2021")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMuestreoPlantaHgIca2021",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    class Meta:
        verbose_name = 'Ev. Calidad Planta Higo Ica 2021 '
        verbose_name_plural = 'Ev. Calidad Planta Higo Ica 2021' 
    def __str__(self):
        return "%s-%s-%s" % (self.anexo_zona, self.ubicacion, self.usuario_creacion)




class SelectorEstadiosCalidad(models.Model):
	
	
	desc= models.CharField("Estadios", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Estadios Calidad '
		verbose_name_plural = 'Selector Estadios Calidad'

	def __str__(self):
		return "%s" % (self.desc)


class SelectorFirmezaCalidad(models.Model):
	
	
	desc= models.CharField("Firmeza", max_length=200,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Firmeza Calidad '
		verbose_name_plural = 'Selector Firmeza Calidad'

	def __str__(self):
		return "%s" % (self.desc)


class DetalleEvCalMuestreoPlantaHgIca2021(models.Model):
   	anexo_detalle=models.ForeignKey(EvCalMuestreoPlantaHgIca2021, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalPlantaHgIca2021",null=True, blank=True)

   	exportable11=models.IntegerField(null=True, blank=True)
   	exportable13=models.IntegerField(null=True, blank=True)
   	exportable15=models.IntegerField(null=True, blank=True)
   	exportable18=models.IntegerField(null=True, blank=True)
   	exportable20=models.IntegerField(null=True, blank=True)
   	exportable24=models.IntegerField(null=True, blank=True)
   	exportable27=models.IntegerField(null=True, blank=True)
   	exportable30=models.IntegerField(null=True, blank=True)

   	pudricion11=models.IntegerField(null=True, blank=True)
   	pudricion13=models.IntegerField(null=True, blank=True)
   	pudricion15=models.IntegerField(null=True, blank=True)
   	pudricion18=models.IntegerField(null=True, blank=True)
   	pudricion20=models.IntegerField(null=True, blank=True)
   	pudricion24=models.IntegerField(null=True, blank=True)
   	pudricion27=models.IntegerField(null=True, blank=True)
   	pudricion30=models.IntegerField(null=True, blank=True)

   	micelio11=models.IntegerField(null=True, blank=True)
   	micelio13=models.IntegerField(null=True, blank=True)
   	micelio15=models.IntegerField(null=True, blank=True)
   	micelio18=models.IntegerField(null=True, blank=True)
   	micelio20=models.IntegerField(null=True, blank=True)
   	micelio24=models.IntegerField(null=True, blank=True)
   	micelio27=models.IntegerField(null=True, blank=True)
   	micelio30=models.IntegerField(null=True, blank=True)

   	pasmado11=models.IntegerField(null=True, blank=True)
   	pasmado13=models.IntegerField(null=True, blank=True)
   	pasmado15=models.IntegerField(null=True, blank=True)
   	pasmado18=models.IntegerField(null=True, blank=True)
   	pasmado20=models.IntegerField(null=True, blank=True)
   	pasmado24=models.IntegerField(null=True, blank=True)
   	pasmado27=models.IntegerField(null=True, blank=True)
   	pasmado30=models.IntegerField(null=True, blank=True)

   	sobremaduro11=models.IntegerField(null=True, blank=True)
   	sobremaduro13=models.IntegerField(null=True, blank=True)
   	sobremaduro15=models.IntegerField(null=True, blank=True)
   	sobremaduro18=models.IntegerField(null=True, blank=True)
   	sobremaduro20=models.IntegerField(null=True, blank=True)
   	sobremaduro24=models.IntegerField(null=True, blank=True)
   	sobremaduro27=models.IntegerField(null=True, blank=True)
   	sobremaduro30=models.IntegerField(null=True, blank=True)

   	danio_latex11=models.IntegerField(null=True, blank=True)
   	danio_latex13=models.IntegerField(null=True, blank=True)
   	danio_latex15=models.IntegerField(null=True, blank=True)
   	danio_latex18=models.IntegerField(null=True, blank=True)
   	danio_latex20=models.IntegerField(null=True, blank=True)
   	danio_latex24=models.IntegerField(null=True, blank=True)
   	danio_latex27=models.IntegerField(null=True, blank=True)
   	danio_latex30=models.IntegerField(null=True, blank=True)

   	ostiolo_abierto11=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto13=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto15=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto18=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto20=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto24=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto27=models.IntegerField(null=True, blank=True)
   	ostiolo_abierto30=models.IntegerField(null=True, blank=True)

   	danio_mecanico11=models.IntegerField(null=True, blank=True)
   	danio_mecanico13=models.IntegerField(null=True, blank=True)
   	danio_mecanico15=models.IntegerField(null=True, blank=True)
   	danio_mecanico18=models.IntegerField(null=True, blank=True)
   	danio_mecanico20=models.IntegerField(null=True, blank=True)
   	danio_mecanico24=models.IntegerField(null=True, blank=True)
   	danio_mecanico27=models.IntegerField(null=True, blank=True)
   	danio_mecanico30=models.IntegerField(null=True, blank=True)

   	pedunculo_malcortado11=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado13=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado15=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado18=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado20=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado24=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado27=models.IntegerField(null=True, blank=True)
   	pedunculo_malcortado30=models.IntegerField(null=True, blank=True)

   	agrietado11=models.IntegerField(null=True, blank=True)
   	agrietado13=models.IntegerField(null=True, blank=True)
   	agrietado15=models.IntegerField(null=True, blank=True)
   	agrietado18=models.IntegerField(null=True, blank=True)
   	agrietado20=models.IntegerField(null=True, blank=True)
   	agrietado24=models.IntegerField(null=True, blank=True)
   	agrietado27=models.IntegerField(null=True, blank=True)
   	agrietado30=models.IntegerField(null=True, blank=True)

   	deshidratado11=models.IntegerField(null=True, blank=True)
   	deshidratado13=models.IntegerField(null=True, blank=True)
   	deshidratado15=models.IntegerField(null=True, blank=True)
   	deshidratado18=models.IntegerField(null=True, blank=True)
   	deshidratado20=models.IntegerField(null=True, blank=True)
   	deshidratado24=models.IntegerField(null=True, blank=True)
   	deshidratado27=models.IntegerField(null=True, blank=True)
   	deshidratado30=models.IntegerField(null=True, blank=True)

   	bajo_calibre11=models.IntegerField(null=True, blank=True)
   	bajo_calibre13=models.IntegerField(null=True, blank=True)
   	bajo_calibre15=models.IntegerField(null=True, blank=True)
   	bajo_calibre18=models.IntegerField(null=True, blank=True)
   	bajo_calibre20=models.IntegerField(null=True, blank=True)
   	bajo_calibre24=models.IntegerField(null=True, blank=True)
   	bajo_calibre27=models.IntegerField(null=True, blank=True)
   	bajo_calibre30=models.IntegerField(null=True, blank=True)

   	deformes11=models.IntegerField(null=True, blank=True)
   	deformes13=models.IntegerField(null=True, blank=True)
   	deformes15=models.IntegerField(null=True, blank=True)
   	deformes18=models.IntegerField(null=True, blank=True)
   	deformes20=models.IntegerField(null=True, blank=True)
   	deformes24=models.IntegerField(null=True, blank=True)
   	deformes27=models.IntegerField(null=True, blank=True)
   	deformes30=models.IntegerField(null=True, blank=True)

   	cicatriz11=models.IntegerField(null=True, blank=True)
   	cicatriz13=models.IntegerField(null=True, blank=True)
   	cicatriz15=models.IntegerField(null=True, blank=True)
   	cicatriz18=models.IntegerField(null=True, blank=True)
   	cicatriz20=models.IntegerField(null=True, blank=True)
   	cicatriz24=models.IntegerField(null=True, blank=True)
   	cicatriz27=models.IntegerField(null=True, blank=True)
   	cicatriz30=models.IntegerField(null=True, blank=True)

   	manchas11=models.IntegerField(null=True, blank=True)
   	manchas13=models.IntegerField(null=True, blank=True)
   	manchas15=models.IntegerField(null=True, blank=True)
   	manchas18=models.IntegerField(null=True, blank=True)
   	manchas20=models.IntegerField(null=True, blank=True)
   	manchas24=models.IntegerField(null=True, blank=True)
   	manchas27=models.IntegerField(null=True, blank=True)
   	manchas30=models.IntegerField(null=True, blank=True)

   	inmadurez_verde11=models.IntegerField(null=True, blank=True)
   	inmadurez_verde13=models.IntegerField(null=True, blank=True)
   	inmadurez_verde15=models.IntegerField(null=True, blank=True)
   	inmadurez_verde18=models.IntegerField(null=True, blank=True)
   	inmadurez_verde20=models.IntegerField(null=True, blank=True)
   	inmadurez_verde24=models.IntegerField(null=True, blank=True)
   	inmadurez_verde27=models.IntegerField(null=True, blank=True)
   	inmadurez_verde30=models.IntegerField(null=True, blank=True)

   	excremento_ave11=models.IntegerField(null=True, blank=True)
   	excremento_ave13=models.IntegerField(null=True, blank=True)
   	excremento_ave15=models.IntegerField(null=True, blank=True)
   	excremento_ave18=models.IntegerField(null=True, blank=True)
   	excremento_ave20=models.IntegerField(null=True, blank=True)
   	excremento_ave24=models.IntegerField(null=True, blank=True)
   	excremento_ave27=models.IntegerField(null=True, blank=True)
   	excremento_ave30=models.IntegerField(null=True, blank=True)

   	picado_ave11=models.IntegerField(null=True, blank=True)
   	picado_ave13=models.IntegerField(null=True, blank=True)
   	picado_ave15=models.IntegerField(null=True, blank=True)
   	picado_ave18=models.IntegerField(null=True, blank=True)
   	picado_ave20=models.IntegerField(null=True, blank=True)
   	picado_ave24=models.IntegerField(null=True, blank=True)
   	picado_ave27=models.IntegerField(null=True, blank=True)
   	picado_ave30=models.IntegerField(null=True, blank=True)

   	danio_trips11=models.IntegerField(null=True, blank=True)
   	danio_trips13=models.IntegerField(null=True, blank=True)
   	danio_trips15=models.IntegerField(null=True, blank=True)
   	danio_trips18=models.IntegerField(null=True, blank=True)
   	danio_trips20=models.IntegerField(null=True, blank=True)
   	danio_trips24=models.IntegerField(null=True, blank=True)
   	danio_trips27=models.IntegerField(null=True, blank=True)
   	danio_trips30=models.IntegerField(null=True, blank=True)

   	danio_queresa11=models.IntegerField(null=True, blank=True)
   	danio_queresa13=models.IntegerField(null=True, blank=True)
   	danio_queresa15=models.IntegerField(null=True, blank=True)
   	danio_queresa18=models.IntegerField(null=True, blank=True)
   	danio_queresa20=models.IntegerField(null=True, blank=True)
   	danio_queresa24=models.IntegerField(null=True, blank=True)
   	danio_queresa27=models.IntegerField(null=True, blank=True)
   	danio_queresa30=models.IntegerField(null=True, blank=True)

   	danio_aranita11=models.IntegerField(null=True, blank=True)
   	danio_aranita13=models.IntegerField(null=True, blank=True)
   	danio_aranita15=models.IntegerField(null=True, blank=True)
   	danio_aranita18=models.IntegerField(null=True, blank=True)
   	danio_aranita20=models.IntegerField(null=True, blank=True)
   	danio_aranita24=models.IntegerField(null=True, blank=True)
   	danio_aranita27=models.IntegerField(null=True, blank=True)
   	danio_aranita30=models.IntegerField(null=True, blank=True)

   	danio_mosca11=models.IntegerField(null=True, blank=True)
   	danio_mosca13=models.IntegerField(null=True, blank=True)
   	danio_mosca15=models.IntegerField(null=True, blank=True)
   	danio_mosca18=models.IntegerField(null=True, blank=True)
   	danio_mosca20=models.IntegerField(null=True, blank=True)
   	danio_mosca24=models.IntegerField(null=True, blank=True)
   	danio_mosca27=models.IntegerField(null=True, blank=True)
   	danio_mosca30=models.IntegerField(null=True, blank=True)

   	anexo_estadio_brix1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1",null=True, blank=True)
   	brix1=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

   	anexo_estadio_brix2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2",null=True, blank=True)
   	brix2=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

   	anexo_estadio_brix3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3",null=True, blank=True)
   	brix3=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

   	anexo_estadio_firmeza1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1F",null=True, blank=True)
   	anexo_firmeza1=models.ForeignKey(SelectorFirmezaCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1Firmeza",null=True, blank=True)

   	anexo_estadio_firmeza2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadi2F",null=True, blank=True)
   	anexo_firmeza2=models.ForeignKey(SelectorFirmezaCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2Firmeza",null=True, blank=True)

   	anexo_estadio_firmeza3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3F",null=True, blank=True)
   	anexo_firmeza3=models.ForeignKey(SelectorFirmezaCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3Firmeza",null=True, blank=True)

   	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
   	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

   	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalPlantaHgIca2021")
   	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
   	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalPlantaHgIca2021",null=True, blank=True)
   	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

   	class Meta:
   		verbose_name = 'Detalle Ev.Calidad Muestreo Planta Higo 2021'
   		verbose_name_plural = 'Detalle Ev. Calidad Muestreo Planta higo 2021'
   		def __str__(self):
   			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)

#EV CALIDAD MUESTREO PLANTA HG ICA 2022
class EvCalMuestreoPlantaHgIca2022(models.Model):
	fecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
	nro_ticket= models.CharField("Nro Ticket", max_length=250,null=True, blank=True)
	temperatura_pulpa= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	peso_muestra= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	exportable11=models.IntegerField(null=True, blank=True)
	exportable13=models.IntegerField(null=True, blank=True)
	exportable15=models.IntegerField(null=True, blank=True)
	exportable18=models.IntegerField(null=True, blank=True)
	exportable20=models.IntegerField(null=True, blank=True)
	exportable24=models.IntegerField(null=True, blank=True)
	exportable27=models.IntegerField(null=True, blank=True)
	exportable30=models.IntegerField(null=True, blank=True)

	pudricion11=models.IntegerField(null=True, blank=True)
	pudricion13=models.IntegerField(null=True, blank=True)
	pudricion15=models.IntegerField(null=True, blank=True)
	pudricion18=models.IntegerField(null=True, blank=True)
	pudricion20=models.IntegerField(null=True, blank=True)
	pudricion24=models.IntegerField(null=True, blank=True)
	pudricion27=models.IntegerField(null=True, blank=True)
	pudricion30=models.IntegerField(null=True, blank=True)

	micelio11=models.IntegerField(null=True, blank=True)
	micelio13=models.IntegerField(null=True, blank=True)
	micelio15=models.IntegerField(null=True, blank=True)
	micelio18=models.IntegerField(null=True, blank=True)
	micelio20=models.IntegerField(null=True, blank=True)
	micelio24=models.IntegerField(null=True, blank=True)
	micelio27=models.IntegerField(null=True, blank=True)
	micelio30=models.IntegerField(null=True, blank=True)

	pasmado11=models.IntegerField(null=True, blank=True)
	pasmado13=models.IntegerField(null=True, blank=True)
	pasmado15=models.IntegerField(null=True, blank=True)
	pasmado18=models.IntegerField(null=True, blank=True)
	pasmado20=models.IntegerField(null=True, blank=True)
	pasmado24=models.IntegerField(null=True, blank=True)
	pasmado27=models.IntegerField(null=True, blank=True)
	pasmado30=models.IntegerField(null=True, blank=True)

	sobremaduro11=models.IntegerField(null=True, blank=True)
	sobremaduro13=models.IntegerField(null=True, blank=True)
	sobremaduro15=models.IntegerField(null=True, blank=True)
	sobremaduro18=models.IntegerField(null=True, blank=True)
	sobremaduro20=models.IntegerField(null=True, blank=True)
	sobremaduro24=models.IntegerField(null=True, blank=True)
	sobremaduro27=models.IntegerField(null=True, blank=True)
	sobremaduro30=models.IntegerField(null=True, blank=True)

	danio_latex11=models.IntegerField(null=True, blank=True)
	danio_latex13=models.IntegerField(null=True, blank=True)
	danio_latex15=models.IntegerField(null=True, blank=True)
	danio_latex18=models.IntegerField(null=True, blank=True)
	danio_latex20=models.IntegerField(null=True, blank=True)
	danio_latex24=models.IntegerField(null=True, blank=True)
	danio_latex27=models.IntegerField(null=True, blank=True)
	danio_latex30=models.IntegerField(null=True, blank=True)

	ostiolo_abierto11=models.IntegerField(null=True, blank=True)
	ostiolo_abierto13=models.IntegerField(null=True, blank=True)
	ostiolo_abierto15=models.IntegerField(null=True, blank=True)
	ostiolo_abierto18=models.IntegerField(null=True, blank=True)
	ostiolo_abierto20=models.IntegerField(null=True, blank=True)
	ostiolo_abierto24=models.IntegerField(null=True, blank=True)
	ostiolo_abierto27=models.IntegerField(null=True, blank=True)
	ostiolo_abierto30=models.IntegerField(null=True, blank=True)

	danio_mecanico11=models.IntegerField(null=True, blank=True)
	danio_mecanico13=models.IntegerField(null=True, blank=True)
	danio_mecanico15=models.IntegerField(null=True, blank=True)
	danio_mecanico18=models.IntegerField(null=True, blank=True)
	danio_mecanico20=models.IntegerField(null=True, blank=True)
	danio_mecanico24=models.IntegerField(null=True, blank=True)
	danio_mecanico27=models.IntegerField(null=True, blank=True)
	danio_mecanico30=models.IntegerField(null=True, blank=True)

	pedunculo_malcortado11=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado13=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado15=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado18=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado20=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado24=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado27=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado30=models.IntegerField(null=True, blank=True)

	agrietado11=models.IntegerField(null=True, blank=True)
	agrietado13=models.IntegerField(null=True, blank=True)
	agrietado15=models.IntegerField(null=True, blank=True)
	agrietado18=models.IntegerField(null=True, blank=True)
	agrietado20=models.IntegerField(null=True, blank=True)
	agrietado24=models.IntegerField(null=True, blank=True)
	agrietado27=models.IntegerField(null=True, blank=True)
	agrietado30=models.IntegerField(null=True, blank=True)

	deshidratado11=models.IntegerField(null=True, blank=True)
	deshidratado13=models.IntegerField(null=True, blank=True)
	deshidratado15=models.IntegerField(null=True, blank=True)
	deshidratado18=models.IntegerField(null=True, blank=True)
	deshidratado20=models.IntegerField(null=True, blank=True)
	deshidratado24=models.IntegerField(null=True, blank=True)
	deshidratado27=models.IntegerField(null=True, blank=True)
	deshidratado30=models.IntegerField(null=True, blank=True)

	bajo_calibre11=models.IntegerField(null=True, blank=True)
	bajo_calibre13=models.IntegerField(null=True, blank=True)
	bajo_calibre15=models.IntegerField(null=True, blank=True)
	bajo_calibre18=models.IntegerField(null=True, blank=True)
	bajo_calibre20=models.IntegerField(null=True, blank=True)
	bajo_calibre24=models.IntegerField(null=True, blank=True)
	bajo_calibre27=models.IntegerField(null=True, blank=True)
	bajo_calibre30=models.IntegerField(null=True, blank=True)

	deformes11=models.IntegerField(null=True, blank=True)
	deformes13=models.IntegerField(null=True, blank=True)
	deformes15=models.IntegerField(null=True, blank=True)
	deformes18=models.IntegerField(null=True, blank=True)
	deformes20=models.IntegerField(null=True, blank=True)
	deformes24=models.IntegerField(null=True, blank=True)
	deformes27=models.IntegerField(null=True, blank=True)
	deformes30=models.IntegerField(null=True, blank=True)

	cicatriz11=models.IntegerField(null=True, blank=True)
	cicatriz13=models.IntegerField(null=True, blank=True)
	cicatriz15=models.IntegerField(null=True, blank=True)
	cicatriz18=models.IntegerField(null=True, blank=True)
	cicatriz20=models.IntegerField(null=True, blank=True)
	cicatriz24=models.IntegerField(null=True, blank=True)
	cicatriz27=models.IntegerField(null=True, blank=True)
	cicatriz30=models.IntegerField(null=True, blank=True)

	manchas11=models.IntegerField(null=True, blank=True)
	manchas13=models.IntegerField(null=True, blank=True)
	manchas15=models.IntegerField(null=True, blank=True)
	manchas18=models.IntegerField(null=True, blank=True)
	manchas20=models.IntegerField(null=True, blank=True)
	manchas24=models.IntegerField(null=True, blank=True)
	manchas27=models.IntegerField(null=True, blank=True)
	manchas30=models.IntegerField(null=True, blank=True)

	inmadurez_verde11=models.IntegerField(null=True, blank=True)
	inmadurez_verde13=models.IntegerField(null=True, blank=True)
	inmadurez_verde15=models.IntegerField(null=True, blank=True)
	inmadurez_verde18=models.IntegerField(null=True, blank=True)
	inmadurez_verde20=models.IntegerField(null=True, blank=True)
	inmadurez_verde24=models.IntegerField(null=True, blank=True)
	inmadurez_verde27=models.IntegerField(null=True, blank=True)
	inmadurez_verde30=models.IntegerField(null=True, blank=True)

	excremento_ave11=models.IntegerField(null=True, blank=True)
	excremento_ave13=models.IntegerField(null=True, blank=True)
	excremento_ave15=models.IntegerField(null=True, blank=True)
	excremento_ave18=models.IntegerField(null=True, blank=True)
	excremento_ave20=models.IntegerField(null=True, blank=True)
	excremento_ave24=models.IntegerField(null=True, blank=True)
	excremento_ave27=models.IntegerField(null=True, blank=True)
	excremento_ave30=models.IntegerField(null=True, blank=True)

	picado_ave11=models.IntegerField(null=True, blank=True)
	picado_ave13=models.IntegerField(null=True, blank=True)
	picado_ave15=models.IntegerField(null=True, blank=True)
	picado_ave18=models.IntegerField(null=True, blank=True)
	picado_ave20=models.IntegerField(null=True, blank=True)
	picado_ave24=models.IntegerField(null=True, blank=True)
	picado_ave27=models.IntegerField(null=True, blank=True)
	picado_ave30=models.IntegerField(null=True, blank=True)

	danio_trips11=models.IntegerField(null=True, blank=True)
	danio_trips13=models.IntegerField(null=True, blank=True)
	danio_trips15=models.IntegerField(null=True, blank=True)
	danio_trips18=models.IntegerField(null=True, blank=True)
	danio_trips20=models.IntegerField(null=True, blank=True)
	danio_trips24=models.IntegerField(null=True, blank=True)
	danio_trips27=models.IntegerField(null=True, blank=True)
	danio_trips30=models.IntegerField(null=True, blank=True)

	danio_queresa11=models.IntegerField(null=True, blank=True)
	danio_queresa13=models.IntegerField(null=True, blank=True)
	danio_queresa15=models.IntegerField(null=True, blank=True)
	danio_queresa18=models.IntegerField(null=True, blank=True)
	danio_queresa20=models.IntegerField(null=True, blank=True)
	danio_queresa24=models.IntegerField(null=True, blank=True)
	danio_queresa27=models.IntegerField(null=True, blank=True)
	danio_queresa30=models.IntegerField(null=True, blank=True)

	danio_aranita11=models.IntegerField(null=True, blank=True)
	danio_aranita13=models.IntegerField(null=True, blank=True)
	danio_aranita15=models.IntegerField(null=True, blank=True)
	danio_aranita18=models.IntegerField(null=True, blank=True)
	danio_aranita20=models.IntegerField(null=True, blank=True)
	danio_aranita24=models.IntegerField(null=True, blank=True)
	danio_aranita27=models.IntegerField(null=True, blank=True)
	danio_aranita30=models.IntegerField(null=True, blank=True)

	danio_mosca11=models.IntegerField(null=True, blank=True)
	danio_mosca13=models.IntegerField(null=True, blank=True)
	danio_mosca15=models.IntegerField(null=True, blank=True)
	danio_mosca18=models.IntegerField(null=True, blank=True)
	danio_mosca20=models.IntegerField(null=True, blank=True)
	danio_mosca24=models.IntegerField(null=True, blank=True)
	danio_mosca27=models.IntegerField(null=True, blank=True)
	danio_mosca30=models.IntegerField(null=True, blank=True)

	anexo_estadio_brix1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1ICA",null=True, blank=True)
	brix1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_estadio_brix2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2ICA",null=True, blank=True)
	brix2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_estadio_brix3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3ICA",null=True, blank=True)
	brix3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1FirmezaICA",null=True, blank=True)
	valor_firmeza1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2FirmezaICA",null=True, blank=True)
	valor_firmeza2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3FirmezaICA",null=True, blank=True)
	valor_firmeza3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMuestreoPlantaHgIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMuestreoPlantaHgIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Planta Higo Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Planta Higo Ica 2022' 
	def __str__(self):
		return "%s-%s" % (self.nro_ticket, self.usuario_creacion)

#EV CALIDAD MUESTREO PLANTA HG NEPEÑA 2022
class EvCalMuestreoPlantaHgNep2022(models.Model):
	fecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
	nro_ticket= models.CharField("Nro Ticket", max_length=250,null=True, blank=True)
	temperatura_pulpa= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	peso_muestra= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	exportable11=models.IntegerField(null=True, blank=True)
	exportable13=models.IntegerField(null=True, blank=True)
	exportable15=models.IntegerField(null=True, blank=True)
	exportable18=models.IntegerField(null=True, blank=True)
	exportable20=models.IntegerField(null=True, blank=True)
	exportable24=models.IntegerField(null=True, blank=True)
	exportable27=models.IntegerField(null=True, blank=True)
	exportable30=models.IntegerField(null=True, blank=True)

	pudricion11=models.IntegerField(null=True, blank=True)
	pudricion13=models.IntegerField(null=True, blank=True)
	pudricion15=models.IntegerField(null=True, blank=True)
	pudricion18=models.IntegerField(null=True, blank=True)
	pudricion20=models.IntegerField(null=True, blank=True)
	pudricion24=models.IntegerField(null=True, blank=True)
	pudricion27=models.IntegerField(null=True, blank=True)
	pudricion30=models.IntegerField(null=True, blank=True)

	micelio11=models.IntegerField(null=True, blank=True)
	micelio13=models.IntegerField(null=True, blank=True)
	micelio15=models.IntegerField(null=True, blank=True)
	micelio18=models.IntegerField(null=True, blank=True)
	micelio20=models.IntegerField(null=True, blank=True)
	micelio24=models.IntegerField(null=True, blank=True)
	micelio27=models.IntegerField(null=True, blank=True)
	micelio30=models.IntegerField(null=True, blank=True)

	pasmado11=models.IntegerField(null=True, blank=True)
	pasmado13=models.IntegerField(null=True, blank=True)
	pasmado15=models.IntegerField(null=True, blank=True)
	pasmado18=models.IntegerField(null=True, blank=True)
	pasmado20=models.IntegerField(null=True, blank=True)
	pasmado24=models.IntegerField(null=True, blank=True)
	pasmado27=models.IntegerField(null=True, blank=True)
	pasmado30=models.IntegerField(null=True, blank=True)

	sobremaduro11=models.IntegerField(null=True, blank=True)
	sobremaduro13=models.IntegerField(null=True, blank=True)
	sobremaduro15=models.IntegerField(null=True, blank=True)
	sobremaduro18=models.IntegerField(null=True, blank=True)
	sobremaduro20=models.IntegerField(null=True, blank=True)
	sobremaduro24=models.IntegerField(null=True, blank=True)
	sobremaduro27=models.IntegerField(null=True, blank=True)
	sobremaduro30=models.IntegerField(null=True, blank=True)

	danio_latex11=models.IntegerField(null=True, blank=True)
	danio_latex13=models.IntegerField(null=True, blank=True)
	danio_latex15=models.IntegerField(null=True, blank=True)
	danio_latex18=models.IntegerField(null=True, blank=True)
	danio_latex20=models.IntegerField(null=True, blank=True)
	danio_latex24=models.IntegerField(null=True, blank=True)
	danio_latex27=models.IntegerField(null=True, blank=True)
	danio_latex30=models.IntegerField(null=True, blank=True)

	ostiolo_abierto11=models.IntegerField(null=True, blank=True)
	ostiolo_abierto13=models.IntegerField(null=True, blank=True)
	ostiolo_abierto15=models.IntegerField(null=True, blank=True)
	ostiolo_abierto18=models.IntegerField(null=True, blank=True)
	ostiolo_abierto20=models.IntegerField(null=True, blank=True)
	ostiolo_abierto24=models.IntegerField(null=True, blank=True)
	ostiolo_abierto27=models.IntegerField(null=True, blank=True)
	ostiolo_abierto30=models.IntegerField(null=True, blank=True)

	danio_mecanico11=models.IntegerField(null=True, blank=True)
	danio_mecanico13=models.IntegerField(null=True, blank=True)
	danio_mecanico15=models.IntegerField(null=True, blank=True)
	danio_mecanico18=models.IntegerField(null=True, blank=True)
	danio_mecanico20=models.IntegerField(null=True, blank=True)
	danio_mecanico24=models.IntegerField(null=True, blank=True)
	danio_mecanico27=models.IntegerField(null=True, blank=True)
	danio_mecanico30=models.IntegerField(null=True, blank=True)

	pedunculo_malcortado11=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado13=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado15=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado18=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado20=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado24=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado27=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado30=models.IntegerField(null=True, blank=True)

	agrietado11=models.IntegerField(null=True, blank=True)
	agrietado13=models.IntegerField(null=True, blank=True)
	agrietado15=models.IntegerField(null=True, blank=True)
	agrietado18=models.IntegerField(null=True, blank=True)
	agrietado20=models.IntegerField(null=True, blank=True)
	agrietado24=models.IntegerField(null=True, blank=True)
	agrietado27=models.IntegerField(null=True, blank=True)
	agrietado30=models.IntegerField(null=True, blank=True)

	deshidratado11=models.IntegerField(null=True, blank=True)
	deshidratado13=models.IntegerField(null=True, blank=True)
	deshidratado15=models.IntegerField(null=True, blank=True)
	deshidratado18=models.IntegerField(null=True, blank=True)
	deshidratado20=models.IntegerField(null=True, blank=True)
	deshidratado24=models.IntegerField(null=True, blank=True)
	deshidratado27=models.IntegerField(null=True, blank=True)
	deshidratado30=models.IntegerField(null=True, blank=True)

	bajo_calibre11=models.IntegerField(null=True, blank=True)
	bajo_calibre13=models.IntegerField(null=True, blank=True)
	bajo_calibre15=models.IntegerField(null=True, blank=True)
	bajo_calibre18=models.IntegerField(null=True, blank=True)
	bajo_calibre20=models.IntegerField(null=True, blank=True)
	bajo_calibre24=models.IntegerField(null=True, blank=True)
	bajo_calibre27=models.IntegerField(null=True, blank=True)
	bajo_calibre30=models.IntegerField(null=True, blank=True)

	deformes11=models.IntegerField(null=True, blank=True)
	deformes13=models.IntegerField(null=True, blank=True)
	deformes15=models.IntegerField(null=True, blank=True)
	deformes18=models.IntegerField(null=True, blank=True)
	deformes20=models.IntegerField(null=True, blank=True)
	deformes24=models.IntegerField(null=True, blank=True)
	deformes27=models.IntegerField(null=True, blank=True)
	deformes30=models.IntegerField(null=True, blank=True)

	cicatriz11=models.IntegerField(null=True, blank=True)
	cicatriz13=models.IntegerField(null=True, blank=True)
	cicatriz15=models.IntegerField(null=True, blank=True)
	cicatriz18=models.IntegerField(null=True, blank=True)
	cicatriz20=models.IntegerField(null=True, blank=True)
	cicatriz24=models.IntegerField(null=True, blank=True)
	cicatriz27=models.IntegerField(null=True, blank=True)
	cicatriz30=models.IntegerField(null=True, blank=True)

	manchas11=models.IntegerField(null=True, blank=True)
	manchas13=models.IntegerField(null=True, blank=True)
	manchas15=models.IntegerField(null=True, blank=True)
	manchas18=models.IntegerField(null=True, blank=True)
	manchas20=models.IntegerField(null=True, blank=True)
	manchas24=models.IntegerField(null=True, blank=True)
	manchas27=models.IntegerField(null=True, blank=True)
	manchas30=models.IntegerField(null=True, blank=True)

	inmadurez_verde11=models.IntegerField(null=True, blank=True)
	inmadurez_verde13=models.IntegerField(null=True, blank=True)
	inmadurez_verde15=models.IntegerField(null=True, blank=True)
	inmadurez_verde18=models.IntegerField(null=True, blank=True)
	inmadurez_verde20=models.IntegerField(null=True, blank=True)
	inmadurez_verde24=models.IntegerField(null=True, blank=True)
	inmadurez_verde27=models.IntegerField(null=True, blank=True)
	inmadurez_verde30=models.IntegerField(null=True, blank=True)

	excremento_ave11=models.IntegerField(null=True, blank=True)
	excremento_ave13=models.IntegerField(null=True, blank=True)
	excremento_ave15=models.IntegerField(null=True, blank=True)
	excremento_ave18=models.IntegerField(null=True, blank=True)
	excremento_ave20=models.IntegerField(null=True, blank=True)
	excremento_ave24=models.IntegerField(null=True, blank=True)
	excremento_ave27=models.IntegerField(null=True, blank=True)
	excremento_ave30=models.IntegerField(null=True, blank=True)

	picado_ave11=models.IntegerField(null=True, blank=True)
	picado_ave13=models.IntegerField(null=True, blank=True)
	picado_ave15=models.IntegerField(null=True, blank=True)
	picado_ave18=models.IntegerField(null=True, blank=True)
	picado_ave20=models.IntegerField(null=True, blank=True)
	picado_ave24=models.IntegerField(null=True, blank=True)
	picado_ave27=models.IntegerField(null=True, blank=True)
	picado_ave30=models.IntegerField(null=True, blank=True)

	danio_trips11=models.IntegerField(null=True, blank=True)
	danio_trips13=models.IntegerField(null=True, blank=True)
	danio_trips15=models.IntegerField(null=True, blank=True)
	danio_trips18=models.IntegerField(null=True, blank=True)
	danio_trips20=models.IntegerField(null=True, blank=True)
	danio_trips24=models.IntegerField(null=True, blank=True)
	danio_trips27=models.IntegerField(null=True, blank=True)
	danio_trips30=models.IntegerField(null=True, blank=True)

	danio_queresa11=models.IntegerField(null=True, blank=True)
	danio_queresa13=models.IntegerField(null=True, blank=True)
	danio_queresa15=models.IntegerField(null=True, blank=True)
	danio_queresa18=models.IntegerField(null=True, blank=True)
	danio_queresa20=models.IntegerField(null=True, blank=True)
	danio_queresa24=models.IntegerField(null=True, blank=True)
	danio_queresa27=models.IntegerField(null=True, blank=True)
	danio_queresa30=models.IntegerField(null=True, blank=True)

	danio_aranita11=models.IntegerField(null=True, blank=True)
	danio_aranita13=models.IntegerField(null=True, blank=True)
	danio_aranita15=models.IntegerField(null=True, blank=True)
	danio_aranita18=models.IntegerField(null=True, blank=True)
	danio_aranita20=models.IntegerField(null=True, blank=True)
	danio_aranita24=models.IntegerField(null=True, blank=True)
	danio_aranita27=models.IntegerField(null=True, blank=True)
	danio_aranita30=models.IntegerField(null=True, blank=True)

	danio_mosca11=models.IntegerField(null=True, blank=True)
	danio_mosca13=models.IntegerField(null=True, blank=True)
	danio_mosca15=models.IntegerField(null=True, blank=True)
	danio_mosca18=models.IntegerField(null=True, blank=True)
	danio_mosca20=models.IntegerField(null=True, blank=True)
	danio_mosca24=models.IntegerField(null=True, blank=True)
	danio_mosca27=models.IntegerField(null=True, blank=True)
	danio_mosca30=models.IntegerField(null=True, blank=True)

	anexo_estadio_brix1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1NEP",null=True, blank=True)
	brix1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_estadio_brix2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2NEP",null=True, blank=True)
	brix2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_estadio_brix3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3NEP",null=True, blank=True)
	brix3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza1=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio1FirmezaNEP",null=True, blank=True)
	valor_firmeza1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza2=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio2FirmezaNEP",null=True, blank=True)
	valor_firmeza2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_firmeza3=models.ForeignKey(SelectorEstadiosCalidad, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalEstadio3FirmezaNEP",null=True, blank=True)
	valor_firmeza3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMuestreoPlantaHgNep2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMuestreoPlantaHgNep2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Planta Higo Nep 2022 '
		verbose_name_plural = 'Ev. Calidad Planta Higo Nep 2022' 
	def __str__(self):
		return "%s-%s" % (self.nro_ticket, self.usuario_creacion)

class EvCalMuestreoPlantaHgNep202202(models.Model):
	fecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
	anexo_planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoMuestreoPlantaHg2022",null=True, blank=True)
	nro_ticket= models.CharField("Nro Ticket", max_length=250,null=True, blank=True)
	temperatura_pulpa= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	peso_muestra= models.DecimalField(max_digits=12, decimal_places=3,null=True, blank=True)

	exportable11=models.IntegerField(null=True, blank=True)
	exportable13=models.IntegerField(null=True, blank=True)
	exportable15=models.IntegerField(null=True, blank=True)
	exportable18=models.IntegerField(null=True, blank=True)
	exportable20=models.IntegerField(null=True, blank=True)
	exportable24=models.IntegerField(null=True, blank=True)
	exportable27=models.IntegerField(null=True, blank=True)
	exportable30=models.IntegerField(null=True, blank=True)

	pudricion11=models.IntegerField(null=True, blank=True)
	pudricion13=models.IntegerField(null=True, blank=True)
	pudricion15=models.IntegerField(null=True, blank=True)
	pudricion18=models.IntegerField(null=True, blank=True)
	pudricion20=models.IntegerField(null=True, blank=True)
	pudricion24=models.IntegerField(null=True, blank=True)
	pudricion27=models.IntegerField(null=True, blank=True)
	pudricion30=models.IntegerField(null=True, blank=True)

	micelio11=models.IntegerField(null=True, blank=True)
	micelio13=models.IntegerField(null=True, blank=True)
	micelio15=models.IntegerField(null=True, blank=True)
	micelio18=models.IntegerField(null=True, blank=True)
	micelio20=models.IntegerField(null=True, blank=True)
	micelio24=models.IntegerField(null=True, blank=True)
	micelio27=models.IntegerField(null=True, blank=True)
	micelio30=models.IntegerField(null=True, blank=True)

	pasmado11=models.IntegerField(null=True, blank=True)
	pasmado13=models.IntegerField(null=True, blank=True)
	pasmado15=models.IntegerField(null=True, blank=True)
	pasmado18=models.IntegerField(null=True, blank=True)
	pasmado20=models.IntegerField(null=True, blank=True)
	pasmado24=models.IntegerField(null=True, blank=True)
	pasmado27=models.IntegerField(null=True, blank=True)
	pasmado30=models.IntegerField(null=True, blank=True)

	sobremaduro11=models.IntegerField(null=True, blank=True)
	sobremaduro13=models.IntegerField(null=True, blank=True)
	sobremaduro15=models.IntegerField(null=True, blank=True)
	sobremaduro18=models.IntegerField(null=True, blank=True)
	sobremaduro20=models.IntegerField(null=True, blank=True)
	sobremaduro24=models.IntegerField(null=True, blank=True)
	sobremaduro27=models.IntegerField(null=True, blank=True)
	sobremaduro30=models.IntegerField(null=True, blank=True)

	danio_latex11=models.IntegerField(null=True, blank=True)
	danio_latex13=models.IntegerField(null=True, blank=True)
	danio_latex15=models.IntegerField(null=True, blank=True)
	danio_latex18=models.IntegerField(null=True, blank=True)
	danio_latex20=models.IntegerField(null=True, blank=True)
	danio_latex24=models.IntegerField(null=True, blank=True)
	danio_latex27=models.IntegerField(null=True, blank=True)
	danio_latex30=models.IntegerField(null=True, blank=True)

	ostiolo_abierto11=models.IntegerField(null=True, blank=True)
	ostiolo_abierto13=models.IntegerField(null=True, blank=True)
	ostiolo_abierto15=models.IntegerField(null=True, blank=True)
	ostiolo_abierto18=models.IntegerField(null=True, blank=True)
	ostiolo_abierto20=models.IntegerField(null=True, blank=True)
	ostiolo_abierto24=models.IntegerField(null=True, blank=True)
	ostiolo_abierto27=models.IntegerField(null=True, blank=True)
	ostiolo_abierto30=models.IntegerField(null=True, blank=True)

	danio_mecanico11=models.IntegerField(null=True, blank=True)
	danio_mecanico13=models.IntegerField(null=True, blank=True)
	danio_mecanico15=models.IntegerField(null=True, blank=True)
	danio_mecanico18=models.IntegerField(null=True, blank=True)
	danio_mecanico20=models.IntegerField(null=True, blank=True)
	danio_mecanico24=models.IntegerField(null=True, blank=True)
	danio_mecanico27=models.IntegerField(null=True, blank=True)
	danio_mecanico30=models.IntegerField(null=True, blank=True)

	pedunculo_malcortado11=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado13=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado15=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado18=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado20=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado24=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado27=models.IntegerField(null=True, blank=True)
	pedunculo_malcortado30=models.IntegerField(null=True, blank=True)

	agrietado11=models.IntegerField(null=True, blank=True)
	agrietado13=models.IntegerField(null=True, blank=True)
	agrietado15=models.IntegerField(null=True, blank=True)
	agrietado18=models.IntegerField(null=True, blank=True)
	agrietado20=models.IntegerField(null=True, blank=True)
	agrietado24=models.IntegerField(null=True, blank=True)
	agrietado27=models.IntegerField(null=True, blank=True)
	agrietado30=models.IntegerField(null=True, blank=True)

	deshidratado11=models.IntegerField(null=True, blank=True)
	deshidratado13=models.IntegerField(null=True, blank=True)
	deshidratado15=models.IntegerField(null=True, blank=True)
	deshidratado18=models.IntegerField(null=True, blank=True)
	deshidratado20=models.IntegerField(null=True, blank=True)
	deshidratado24=models.IntegerField(null=True, blank=True)
	deshidratado27=models.IntegerField(null=True, blank=True)
	deshidratado30=models.IntegerField(null=True, blank=True)

	bajo_calibre11=models.IntegerField(null=True, blank=True)
	bajo_calibre13=models.IntegerField(null=True, blank=True)
	bajo_calibre15=models.IntegerField(null=True, blank=True)
	bajo_calibre18=models.IntegerField(null=True, blank=True)
	bajo_calibre20=models.IntegerField(null=True, blank=True)
	bajo_calibre24=models.IntegerField(null=True, blank=True)
	bajo_calibre27=models.IntegerField(null=True, blank=True)
	bajo_calibre30=models.IntegerField(null=True, blank=True)

	deformes11=models.IntegerField(null=True, blank=True)
	deformes13=models.IntegerField(null=True, blank=True)
	deformes15=models.IntegerField(null=True, blank=True)
	deformes18=models.IntegerField(null=True, blank=True)
	deformes20=models.IntegerField(null=True, blank=True)
	deformes24=models.IntegerField(null=True, blank=True)
	deformes27=models.IntegerField(null=True, blank=True)
	deformes30=models.IntegerField(null=True, blank=True)

	cicatriz11=models.IntegerField(null=True, blank=True)
	cicatriz13=models.IntegerField(null=True, blank=True)
	cicatriz15=models.IntegerField(null=True, blank=True)
	cicatriz18=models.IntegerField(null=True, blank=True)
	cicatriz20=models.IntegerField(null=True, blank=True)
	cicatriz24=models.IntegerField(null=True, blank=True)
	cicatriz27=models.IntegerField(null=True, blank=True)
	cicatriz30=models.IntegerField(null=True, blank=True)

	manchas11=models.IntegerField(null=True, blank=True)
	manchas13=models.IntegerField(null=True, blank=True)
	manchas15=models.IntegerField(null=True, blank=True)
	manchas18=models.IntegerField(null=True, blank=True)
	manchas20=models.IntegerField(null=True, blank=True)
	manchas24=models.IntegerField(null=True, blank=True)
	manchas27=models.IntegerField(null=True, blank=True)
	manchas30=models.IntegerField(null=True, blank=True)

	inmadurez_verde11=models.IntegerField(null=True, blank=True)
	inmadurez_verde13=models.IntegerField(null=True, blank=True)
	inmadurez_verde15=models.IntegerField(null=True, blank=True)
	inmadurez_verde18=models.IntegerField(null=True, blank=True)
	inmadurez_verde20=models.IntegerField(null=True, blank=True)
	inmadurez_verde24=models.IntegerField(null=True, blank=True)
	inmadurez_verde27=models.IntegerField(null=True, blank=True)
	inmadurez_verde30=models.IntegerField(null=True, blank=True)

	excremento_ave11=models.IntegerField(null=True, blank=True)
	excremento_ave13=models.IntegerField(null=True, blank=True)
	excremento_ave15=models.IntegerField(null=True, blank=True)
	excremento_ave18=models.IntegerField(null=True, blank=True)
	excremento_ave20=models.IntegerField(null=True, blank=True)
	excremento_ave24=models.IntegerField(null=True, blank=True)
	excremento_ave27=models.IntegerField(null=True, blank=True)
	excremento_ave30=models.IntegerField(null=True, blank=True)

	picado_ave11=models.IntegerField(null=True, blank=True)
	picado_ave13=models.IntegerField(null=True, blank=True)
	picado_ave15=models.IntegerField(null=True, blank=True)
	picado_ave18=models.IntegerField(null=True, blank=True)
	picado_ave20=models.IntegerField(null=True, blank=True)
	picado_ave24=models.IntegerField(null=True, blank=True)
	picado_ave27=models.IntegerField(null=True, blank=True)
	picado_ave30=models.IntegerField(null=True, blank=True)

	danio_trips11=models.IntegerField(null=True, blank=True)
	danio_trips13=models.IntegerField(null=True, blank=True)
	danio_trips15=models.IntegerField(null=True, blank=True)
	danio_trips18=models.IntegerField(null=True, blank=True)
	danio_trips20=models.IntegerField(null=True, blank=True)
	danio_trips24=models.IntegerField(null=True, blank=True)
	danio_trips27=models.IntegerField(null=True, blank=True)
	danio_trips30=models.IntegerField(null=True, blank=True)

	danio_queresa11=models.IntegerField(null=True, blank=True)
	danio_queresa13=models.IntegerField(null=True, blank=True)
	danio_queresa15=models.IntegerField(null=True, blank=True)
	danio_queresa18=models.IntegerField(null=True, blank=True)
	danio_queresa20=models.IntegerField(null=True, blank=True)
	danio_queresa24=models.IntegerField(null=True, blank=True)
	danio_queresa27=models.IntegerField(null=True, blank=True)
	danio_queresa30=models.IntegerField(null=True, blank=True)

	danio_aranita11=models.IntegerField(null=True, blank=True)
	danio_aranita13=models.IntegerField(null=True, blank=True)
	danio_aranita15=models.IntegerField(null=True, blank=True)
	danio_aranita18=models.IntegerField(null=True, blank=True)
	danio_aranita20=models.IntegerField(null=True, blank=True)
	danio_aranita24=models.IntegerField(null=True, blank=True)
	danio_aranita27=models.IntegerField(null=True, blank=True)
	danio_aranita30=models.IntegerField(null=True, blank=True)

	danio_mosca11=models.IntegerField(null=True, blank=True)
	danio_mosca13=models.IntegerField(null=True, blank=True)
	danio_mosca15=models.IntegerField(null=True, blank=True)
	danio_mosca18=models.IntegerField(null=True, blank=True)
	danio_mosca20=models.IntegerField(null=True, blank=True)
	danio_mosca24=models.IntegerField(null=True, blank=True)
	danio_mosca27=models.IntegerField(null=True, blank=True)
	danio_mosca30=models.IntegerField(null=True, blank=True)

	sst_estadio2_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio2_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio2_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	sst_estadio3_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio3_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio3_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	sst_estadio4_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio4_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	sst_estadio4_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)


	firmeza_estadio2_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_4=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_5=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_6=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_7=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_8=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_9=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio2_10=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	firmeza_estadio3_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_4=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_5=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_6=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_7=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_8=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_9=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio3_10=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	firmeza_estadio4_1=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_2=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_3=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_4=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_5=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_6=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_7=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_8=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_9=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_estadio4_10=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMuestreoPlantaHgNep202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMuestreoPlantaHgNep202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Planta Higo Nep 202202'
		verbose_name_plural = 'Ev. Calidad Planta Higo Nep 202202' 
	def __str__(self):
		return "%s-%s" % (self.nro_ticket, self.usuario_creacion)

class EvCalBrixGrIca2021(models.Model):
    anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoBrixCUltivoGrIca2021",null=True, blank=True)
    anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaBrixGrIca2021",null=True, blank=True)
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoBrixGrIca2021",null=True, blank=True)
    ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCalrixGrIca2021")
    anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadMrixGrIca2021",null=True, blank=True)
    fecha=models.DateField("Fecha de Enfriado",null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalBrixGrIca2021")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalBrixGrIca2021",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    class Meta:
        verbose_name = 'Ev. Calidad Brix Granada Ica 2021 '
        verbose_name_plural = 'Ev. Calidad Brix Granada Ica 2021' 
    def __str__(self):
        return "%s-%s-%s" % (self.anexo_zona, self.ubicacion, self.usuario_creacion)


class SelectorLlenadoArilo (models.Model):
	desc= models.CharField("Desc de llenado arilo",max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Llenado Arilo'
		verbose_name_plural = 'Selector  Llenado Arilo'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)




class DetalleEvCalBrixGrIca2021(models.Model):
   	anexo_detalle=models.ForeignKey(EvCalBrixGrIca2021, on_delete=models.CASCADE, related_name="AnexoDetalleEvcalBrixGrIca2021",null=True, blank=True)
   	anexo_sector=models.ForeignKey(TurnoProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoTurnoPPEvCalrixGrIca2021",null=True, blank=True)
   	peso=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	#diametro== diametro ecuatorial
   	diametro=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	diametro_polar=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	color_interno=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	color_externo=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	brix=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	gasto_naoh=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	acidez=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	indice_madurez=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
   	sector= models.CharField("Sector", max_length=200,null=True, blank=True)
   	peso_arilo=models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
   	peso_cascara=models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
   	anexo_llenado=models.ForeignKey(SelectorLlenadoArilo, on_delete=models.CASCADE,null=True, blank=True)

   	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalBrixGrIca2021")
   	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
   	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalBrixGrIca2021",null=True, blank=True)
   	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

   	class Meta:
   		verbose_name = 'Detalle Ev.Calidad Brix Gr- 2021'
   		verbose_name_plural = 'Detalle Ev. Calidad Brix Gr- 2021'
   		def __str__(self):
   			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)



#ev-cal-materia-prima-granada-ica-2021
class EvCalMmppGrIca2021(models.Model):
	npalet=models.IntegerField(null=True, blank=True)
	anexo_tipocalidad=models.ForeignKey(TipoCalidadFruta, on_delete=models.CASCADE, related_name="AnexoTipoMmppGrIca2021",null=True, blank=True)
	anexo_fundo= models.CharField("Fundo", max_length=200,null=True, blank=True)
	anexo_fecha_cosecha= models.CharField("Fecha Cosecha", max_length=200,null=True, blank=True)
	anexo_nro_guia= models.CharField("Nro Guia", max_length=200,null=True, blank=True)
	anexo_pep= models.CharField("Pep", max_length=200,null=True, blank=True)
	anexo_variedad= models.CharField("Variedad", max_length=200,null=True, blank=True)
	fecha_evaluacion=models.DateField("Fecha de Evaluacion",null=True, blank=True)
	temperatura_pulpa=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	peso_muestra=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalMmppGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalMmppGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Materia Prima Granada Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Materia Prima Granada Ica 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.npalet, self.anexo_tipocalidad, self.anexo_fundo)


class DetalleEvCalMmppGrIca2021(models.Model):
	anexo_detalle = models.ForeignKey(EvCalMmppGrIca2021, on_delete=models.CASCADE, related_name="AnexoDetEvCalMmppGrIca2021")
	brix1=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	brix2=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	brix3=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	brix4=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	
	acidez1=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	acidez2=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	acidez3=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	acidez4=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	acidez5=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	
	indice_madurez1=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	indice_madurez2=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	indice_madurez3=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	indice_madurez4=models.DecimalField(max_digits=18, decimal_places=3,null=True, blank=True)
	
	alternaria=models.IntegerField(null=True, blank=True)
	gelechi=models.IntegerField(null=True, blank=True)
	sobremaduracion=models.IntegerField(null=True, blank=True)
	arilo_pardo=models.IntegerField(null=True, blank=True)
	cydia=models.IntegerField(null=True, blank=True)
	conforme=models.IntegerField(null=True, blank=True)
	
	color_interna1=models.IntegerField(null=True, blank=True)
	color_interna2=models.IntegerField(null=True, blank=True)
	color_interna3=models.IntegerField(null=True, blank=True)
	color_interna4=models.IntegerField(null=True, blank=True)
	color_interna5=models.IntegerField(null=True, blank=True)

	color_externa1=models.IntegerField(null=True, blank=True)
	color_externa2=models.IntegerField(null=True, blank=True)
	color_externa25=models.IntegerField(null=True, blank=True)
	color_externa3=models.IntegerField(null=True, blank=True)
	color_externa35=models.IntegerField(null=True, blank=True)
	color_externa4=models.IntegerField(null=True, blank=True)
	color_externa5=models.IntegerField(null=True, blank=True)

	color_ext1_int1=models.IntegerField(null=True, blank=True)
	color_ext1_int2=models.IntegerField(null=True, blank=True)
	color_ext1_int3=models.IntegerField(null=True, blank=True)
	color_ext1_int4=models.IntegerField(null=True, blank=True)
	color_ext1_int5=models.IntegerField(null=True, blank=True)

	color_ext2_int1=models.IntegerField(null=True, blank=True)
	color_ext2_int2=models.IntegerField(null=True, blank=True)
	color_ext2_int3=models.IntegerField(null=True, blank=True)
	color_ext2_int4=models.IntegerField(null=True, blank=True)
	color_ext2_int5=models.IntegerField(null=True, blank=True)

	color_ext25_int1=models.IntegerField(null=True, blank=True)
	color_ext25_int2=models.IntegerField(null=True, blank=True)
	color_ext25_int3=models.IntegerField(null=True, blank=True)
	color_ext25_int4=models.IntegerField(null=True, blank=True)
	color_ext25_int5=models.IntegerField(null=True, blank=True)

	color_ext3_int1=models.IntegerField(null=True, blank=True)
	color_ext3_int2=models.IntegerField(null=True, blank=True)
	color_ext3_int3=models.IntegerField(null=True, blank=True)
	color_ext3_int4=models.IntegerField(null=True, blank=True)
	color_ext3_int5=models.IntegerField(null=True, blank=True)

	color_ext35_int1=models.IntegerField(null=True, blank=True)
	color_ext35_int2=models.IntegerField(null=True, blank=True)
	color_ext35_int3=models.IntegerField(null=True, blank=True)
	color_ext35_int4=models.IntegerField(null=True, blank=True)
	color_ext35_int5=models.IntegerField(null=True, blank=True)

	color_ext4_int1=models.IntegerField(null=True, blank=True)
	color_ext4_int2=models.IntegerField(null=True, blank=True)
	color_ext4_int3=models.IntegerField(null=True, blank=True)
	color_ext4_int4=models.IntegerField(null=True, blank=True)
	color_ext4_int5=models.IntegerField(null=True, blank=True)

	color_ext5_int1=models.IntegerField(null=True, blank=True)
	color_ext5_int2=models.IntegerField(null=True, blank=True)
	color_ext5_int3=models.IntegerField(null=True, blank=True)
	color_ext5_int4=models.IntegerField(null=True, blank=True)
	color_ext5_int5=models.IntegerField(null=True, blank=True)

	cat1_4=models.IntegerField(null=True, blank=True)
	cat1_5=models.IntegerField(null=True, blank=True)
	cat1_6=models.IntegerField(null=True, blank=True)
	cat1_7=models.IntegerField(null=True, blank=True)
	cat1_8=models.IntegerField(null=True, blank=True)
	cat1_9=models.IntegerField(null=True, blank=True)
	cat1_10=models.IntegerField(null=True, blank=True)
	cat1_12=models.IntegerField(null=True, blank=True)
	cat1_14=models.IntegerField(null=True, blank=True)
	cat1_16=models.IntegerField(null=True, blank=True)
	cat1_18=models.IntegerField(null=True, blank=True)
	cat1_20=models.IntegerField(null=True, blank=True)
	cat1_22=models.IntegerField(null=True, blank=True)
	cat1_24=models.IntegerField(null=True, blank=True)
	
	cat2_cicatriz_4=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_5=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_6=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_7=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_8=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_9=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_10=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_12=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_14=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_16=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_18=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_20=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_22=models.IntegerField(null=True, blank=True)
	cat2_cicatriz_24=models.IntegerField(null=True, blank=True)

	cat2_thrips_4=models.IntegerField(null=True, blank=True)
	cat2_thrips_5=models.IntegerField(null=True, blank=True)
	cat2_thrips_6=models.IntegerField(null=True, blank=True)
	cat2_thrips_7=models.IntegerField(null=True, blank=True)
	cat2_thrips_8=models.IntegerField(null=True, blank=True)
	cat2_thrips_9=models.IntegerField(null=True, blank=True)
	cat2_thrips_10=models.IntegerField(null=True, blank=True)
	cat2_thrips_12=models.IntegerField(null=True, blank=True)
	cat2_thrips_14=models.IntegerField(null=True, blank=True)
	cat2_thrips_16=models.IntegerField(null=True, blank=True)
	cat2_thrips_18=models.IntegerField(null=True, blank=True)
	cat2_thrips_20=models.IntegerField(null=True, blank=True)
	cat2_thrips_22=models.IntegerField(null=True, blank=True)
	cat2_thrips_24=models.IntegerField(null=True, blank=True)

	cat2_deformes_4=models.IntegerField(null=True, blank=True)
	cat2_deformes_5=models.IntegerField(null=True, blank=True)
	cat2_deformes_6=models.IntegerField(null=True, blank=True)
	cat2_deformes_7=models.IntegerField(null=True, blank=True)
	cat2_deformes_8=models.IntegerField(null=True, blank=True)
	cat2_deformes_9=models.IntegerField(null=True, blank=True)
	cat2_deformes_10=models.IntegerField(null=True, blank=True)
	cat2_deformes_12=models.IntegerField(null=True, blank=True)
	cat2_deformes_14=models.IntegerField(null=True, blank=True)
	cat2_deformes_16=models.IntegerField(null=True, blank=True)
	cat2_deformes_18=models.IntegerField(null=True, blank=True)
	cat2_deformes_20=models.IntegerField(null=True, blank=True)
	cat2_deformes_22=models.IntegerField(null=True, blank=True)
	cat2_deformes_24=models.IntegerField(null=True, blank=True)

	cat2_deshidratadol_4=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_5=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_6=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_7=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_8=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_9=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_10=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_12=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_14=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_16=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_18=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_20=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_22=models.IntegerField(null=True, blank=True)
	cat2_deshidratadol_24=models.IntegerField(null=True, blank=True)
	
	cat2_manchas_4=models.IntegerField(null=True, blank=True)
	cat2_manchas_5=models.IntegerField(null=True, blank=True)
	cat2_manchas_6=models.IntegerField(null=True, blank=True)
	cat2_manchas_7=models.IntegerField(null=True, blank=True)
	cat2_manchas_8=models.IntegerField(null=True, blank=True)
	cat2_manchas_9=models.IntegerField(null=True, blank=True)
	cat2_manchas_10=models.IntegerField(null=True, blank=True)
	cat2_manchas_12=models.IntegerField(null=True, blank=True)
	cat2_manchas_14=models.IntegerField(null=True, blank=True)
	cat2_manchas_16=models.IntegerField(null=True, blank=True)
	cat2_manchas_18=models.IntegerField(null=True, blank=True)
	cat2_manchas_20=models.IntegerField(null=True, blank=True)
	cat2_manchas_22=models.IntegerField(null=True, blank=True)
	cat2_manchas_24=models.IntegerField(null=True, blank=True)

	cat2_palidas_4=models.IntegerField(null=True, blank=True)
	cat2_palidas_5=models.IntegerField(null=True, blank=True)
	cat2_palidas_6=models.IntegerField(null=True, blank=True)
	cat2_palidas_7=models.IntegerField(null=True, blank=True)
	cat2_palidas_8=models.IntegerField(null=True, blank=True)
	cat2_palidas_9=models.IntegerField(null=True, blank=True)
	cat2_palidas_10=models.IntegerField(null=True, blank=True)
	cat2_palidas_12=models.IntegerField(null=True, blank=True)
	cat2_palidas_14=models.IntegerField(null=True, blank=True)
	cat2_palidas_16=models.IntegerField(null=True, blank=True)
	cat2_palidas_18=models.IntegerField(null=True, blank=True)
	cat2_palidas_20=models.IntegerField(null=True, blank=True)
	cat2_palidas_22=models.IntegerField(null=True, blank=True)
	cat2_palidas_24=models.IntegerField(null=True, blank=True)

	cat2_pedunculo_4=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_5=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_6=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_7=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_8=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_9=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_10=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_12=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_14=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_16=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_18=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_20=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_22=models.IntegerField(null=True, blank=True)
	cat2_pedunculo_24=models.IntegerField(null=True, blank=True)

	cat2_rajadas_4=models.IntegerField(null=True, blank=True)
	cat2_rajadas_5=models.IntegerField(null=True, blank=True)
	cat2_rajadas_6=models.IntegerField(null=True, blank=True)
	cat2_rajadas_7=models.IntegerField(null=True, blank=True)
	cat2_rajadas_8=models.IntegerField(null=True, blank=True)
	cat2_rajadas_9=models.IntegerField(null=True, blank=True)
	cat2_rajadas_10=models.IntegerField(null=True, blank=True)
	cat2_rajadas_12=models.IntegerField(null=True, blank=True)
	cat2_rajadas_14=models.IntegerField(null=True, blank=True)
	cat2_rajadas_16=models.IntegerField(null=True, blank=True)
	cat2_rajadas_18=models.IntegerField(null=True, blank=True)
	cat2_rajadas_20=models.IntegerField(null=True, blank=True)
	cat2_rajadas_22=models.IntegerField(null=True, blank=True)
	cat2_rajadas_24=models.IntegerField(null=True, blank=True)

	cat2_recuperable_4=models.IntegerField(null=True, blank=True)
	cat2_recuperable_5=models.IntegerField(null=True, blank=True)
	cat2_recuperable_6=models.IntegerField(null=True, blank=True)
	cat2_recuperable_7=models.IntegerField(null=True, blank=True)
	cat2_recuperable_8=models.IntegerField(null=True, blank=True)
	cat2_recuperable_9=models.IntegerField(null=True, blank=True)
	cat2_recuperable_10=models.IntegerField(null=True, blank=True)
	cat2_recuperable_12=models.IntegerField(null=True, blank=True)
	cat2_recuperable_14=models.IntegerField(null=True, blank=True)
	cat2_recuperable_16=models.IntegerField(null=True, blank=True)
	cat2_recuperable_18=models.IntegerField(null=True, blank=True)
	cat2_recuperable_20=models.IntegerField(null=True, blank=True)
	cat2_recuperable_22=models.IntegerField(null=True, blank=True)
	cat2_recuperable_24=models.IntegerField(null=True, blank=True)

	cat2_russet_4=models.IntegerField(null=True, blank=True)
	cat2_russet_5=models.IntegerField(null=True, blank=True)
	cat2_russet_6=models.IntegerField(null=True, blank=True)
	cat2_russet_7=models.IntegerField(null=True, blank=True)
	cat2_russet_8=models.IntegerField(null=True, blank=True)
	cat2_russet_9=models.IntegerField(null=True, blank=True)
	cat2_russet_10=models.IntegerField(null=True, blank=True)
	cat2_russet_12=models.IntegerField(null=True, blank=True)
	cat2_russet_14=models.IntegerField(null=True, blank=True)
	cat2_russet_16=models.IntegerField(null=True, blank=True)
	cat2_russet_18=models.IntegerField(null=True, blank=True)
	cat2_russet_20=models.IntegerField(null=True, blank=True)
	cat2_russet_22=models.IntegerField(null=True, blank=True)
	cat2_russet_24=models.IntegerField(null=True, blank=True)

	cat2_danio_4=models.IntegerField(null=True, blank=True)
	cat2_danio_5=models.IntegerField(null=True, blank=True)
	cat2_danio_6=models.IntegerField(null=True, blank=True)
	cat2_danio_7=models.IntegerField(null=True, blank=True)
	cat2_danio_8=models.IntegerField(null=True, blank=True)
	cat2_danio_9=models.IntegerField(null=True, blank=True)
	cat2_danio_10=models.IntegerField(null=True, blank=True)
	cat2_danio_12=models.IntegerField(null=True, blank=True)
	cat2_danio_14=models.IntegerField(null=True, blank=True)
	cat2_danio_16=models.IntegerField(null=True, blank=True)
	cat2_danio_18=models.IntegerField(null=True, blank=True)
	cat2_danio_20=models.IntegerField(null=True, blank=True)
	cat2_danio_22=models.IntegerField(null=True, blank=True)
	cat2_danio_24=models.IntegerField(null=True, blank=True)

	cat2_insolacion_4=models.IntegerField(null=True, blank=True)
	cat2_insolacion_5=models.IntegerField(null=True, blank=True)
	cat2_insolacion_6=models.IntegerField(null=True, blank=True)
	cat2_insolacion_7=models.IntegerField(null=True, blank=True)
	cat2_insolacion_8=models.IntegerField(null=True, blank=True)
	cat2_insolacion_9=models.IntegerField(null=True, blank=True)
	cat2_insolacion_10=models.IntegerField(null=True, blank=True)
	cat2_insolacion_12=models.IntegerField(null=True, blank=True)
	cat2_insolacion_14=models.IntegerField(null=True, blank=True)
	cat2_insolacion_16=models.IntegerField(null=True, blank=True)
	cat2_insolacion_18=models.IntegerField(null=True, blank=True)
	cat2_insolacion_20=models.IntegerField(null=True, blank=True)
	cat2_insolacion_22=models.IntegerField(null=True, blank=True)
	cat2_insolacion_24=models.IntegerField(null=True, blank=True)

	cati_rajada_sa_4=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_5=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_6=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_7=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_8=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_9=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_10=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_12=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_14=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_16=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_18=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_20=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_22=models.IntegerField(null=True, blank=True)
	cati_rajada_sa_24=models.IntegerField(null=True, blank=True)

	desc_pesome_4=models.IntegerField(null=True, blank=True)
	
	desc_deshisev_4=models.IntegerField(null=True, blank=True)
	desc_deshisev_5=models.IntegerField(null=True, blank=True)
	desc_deshisev_6=models.IntegerField(null=True, blank=True)
	desc_deshisev_7=models.IntegerField(null=True, blank=True)
	desc_deshisev_8=models.IntegerField(null=True, blank=True)
	desc_deshisev_9=models.IntegerField(null=True, blank=True)
	desc_deshisev_10=models.IntegerField(null=True, blank=True)
	desc_deshisev_12=models.IntegerField(null=True, blank=True)
	desc_deshisev_14=models.IntegerField(null=True, blank=True)
	desc_deshisev_16=models.IntegerField(null=True, blank=True)
	desc_deshisev_18=models.IntegerField(null=True, blank=True)
	desc_deshisev_20=models.IntegerField(null=True, blank=True)
	desc_deshisev_22=models.IntegerField(null=True, blank=True)
	desc_deshisev_24=models.IntegerField(null=True, blank=True)

	desc_magullado_4=models.IntegerField(null=True, blank=True)
	desc_magullado_5=models.IntegerField(null=True, blank=True)
	desc_magullado_6=models.IntegerField(null=True, blank=True)
	desc_magullado_7=models.IntegerField(null=True, blank=True)
	desc_magullado_8=models.IntegerField(null=True, blank=True)
	desc_magullado_9=models.IntegerField(null=True, blank=True)
	desc_magullado_10=models.IntegerField(null=True, blank=True)
	desc_magullado_12=models.IntegerField(null=True, blank=True)
	desc_magullado_14=models.IntegerField(null=True, blank=True)
	desc_magullado_16=models.IntegerField(null=True, blank=True)
	desc_magullado_18=models.IntegerField(null=True, blank=True)
	desc_magullado_20=models.IntegerField(null=True, blank=True)
	desc_magullado_22=models.IntegerField(null=True, blank=True)
	desc_magullado_24=models.IntegerField(null=True, blank=True)

	desc_moscaf_4=models.IntegerField(null=True, blank=True)
	desc_moscaf_5=models.IntegerField(null=True, blank=True)
	desc_moscaf_6=models.IntegerField(null=True, blank=True)
	desc_moscaf_7=models.IntegerField(null=True, blank=True)
	desc_moscaf_8=models.IntegerField(null=True, blank=True)
	desc_moscaf_9=models.IntegerField(null=True, blank=True)
	desc_moscaf_10=models.IntegerField(null=True, blank=True)
	desc_moscaf_12=models.IntegerField(null=True, blank=True)
	desc_moscaf_14=models.IntegerField(null=True, blank=True)
	desc_moscaf_16=models.IntegerField(null=True, blank=True)
	desc_moscaf_18=models.IntegerField(null=True, blank=True)
	desc_moscaf_20=models.IntegerField(null=True, blank=True)
	desc_moscaf_22=models.IntegerField(null=True, blank=True)
	desc_moscaf_24=models.IntegerField(null=True, blank=True)

	desc_gelechi_4=models.IntegerField(null=True, blank=True)
	desc_gelechi_5=models.IntegerField(null=True, blank=True)
	desc_gelechi_6=models.IntegerField(null=True, blank=True)
	desc_gelechi_7=models.IntegerField(null=True, blank=True)
	desc_gelechi_8=models.IntegerField(null=True, blank=True)
	desc_gelechi_9=models.IntegerField(null=True, blank=True)
	desc_gelechi_10=models.IntegerField(null=True, blank=True)
	desc_gelechi_12=models.IntegerField(null=True, blank=True)
	desc_gelechi_14=models.IntegerField(null=True, blank=True)
	desc_gelechi_16=models.IntegerField(null=True, blank=True)
	desc_gelechi_18=models.IntegerField(null=True, blank=True)
	desc_gelechi_20=models.IntegerField(null=True, blank=True)
	desc_gelechi_22=models.IntegerField(null=True, blank=True)
	desc_gelechi_24=models.IntegerField(null=True, blank=True)

	desc_hongosi_4=models.IntegerField(null=True, blank=True)
	desc_hongosi_5=models.IntegerField(null=True, blank=True)
	desc_hongosi_6=models.IntegerField(null=True, blank=True)
	desc_hongosi_7=models.IntegerField(null=True, blank=True)
	desc_hongosi_8=models.IntegerField(null=True, blank=True)
	desc_hongosi_9=models.IntegerField(null=True, blank=True)
	desc_hongosi_10=models.IntegerField(null=True, blank=True)
	desc_hongosi_12=models.IntegerField(null=True, blank=True)
	desc_hongosi_14=models.IntegerField(null=True, blank=True)
	desc_hongosi_16=models.IntegerField(null=True, blank=True)
	desc_hongosi_18=models.IntegerField(null=True, blank=True)
	desc_hongosi_20=models.IntegerField(null=True, blank=True)
	desc_hongosi_22=models.IntegerField(null=True, blank=True)
	desc_hongosi_24=models.IntegerField(null=True, blank=True)

	desc_inmadurez_4=models.IntegerField(null=True, blank=True)
	desc_inmadurez_5=models.IntegerField(null=True, blank=True)
	desc_inmadurez_6=models.IntegerField(null=True, blank=True)
	desc_inmadurez_7=models.IntegerField(null=True, blank=True)
	desc_inmadurez_8=models.IntegerField(null=True, blank=True)
	desc_inmadurez_9=models.IntegerField(null=True, blank=True)
	desc_inmadurez_10=models.IntegerField(null=True, blank=True)
	desc_inmadurez_12=models.IntegerField(null=True, blank=True)
	desc_inmadurez_14=models.IntegerField(null=True, blank=True)
	desc_inmadurez_16=models.IntegerField(null=True, blank=True)
	desc_inmadurez_18=models.IntegerField(null=True, blank=True)
	desc_inmadurez_20=models.IntegerField(null=True, blank=True)
	desc_inmadurez_22=models.IntegerField(null=True, blank=True)
	desc_inmadurez_24=models.IntegerField(null=True, blank=True)
	
	desc_insolacion_4=models.IntegerField(null=True, blank=True)
	desc_insolacion_5=models.IntegerField(null=True, blank=True)
	desc_insolacion_6=models.IntegerField(null=True, blank=True)
	desc_insolacion_7=models.IntegerField(null=True, blank=True)
	desc_insolacion_8=models.IntegerField(null=True, blank=True)
	desc_insolacion_9=models.IntegerField(null=True, blank=True)
	desc_insolacion_10=models.IntegerField(null=True, blank=True)
	desc_insolacion_12=models.IntegerField(null=True, blank=True)
	desc_insolacion_14=models.IntegerField(null=True, blank=True)
	desc_insolacion_16=models.IntegerField(null=True, blank=True)
	desc_insolacion_18=models.IntegerField(null=True, blank=True)
	desc_insolacion_20=models.IntegerField(null=True, blank=True)
	desc_insolacion_22=models.IntegerField(null=True, blank=True)
	desc_insolacion_24=models.IntegerField(null=True, blank=True)

	desc_quereza_4=models.IntegerField(null=True, blank=True)
	desc_quereza_5=models.IntegerField(null=True, blank=True)
	desc_quereza_6=models.IntegerField(null=True, blank=True)
	desc_quereza_7=models.IntegerField(null=True, blank=True)
	desc_quereza_8=models.IntegerField(null=True, blank=True)
	desc_quereza_9=models.IntegerField(null=True, blank=True)
	desc_quereza_10=models.IntegerField(null=True, blank=True)
	desc_quereza_12=models.IntegerField(null=True, blank=True)
	desc_quereza_14=models.IntegerField(null=True, blank=True)
	desc_quereza_16=models.IntegerField(null=True, blank=True)
	desc_quereza_18=models.IntegerField(null=True, blank=True)
	desc_quereza_20=models.IntegerField(null=True, blank=True)
	desc_quereza_22=models.IntegerField(null=True, blank=True)
	desc_quereza_24=models.IntegerField(null=True, blank=True)

	desc_botritis_4=models.IntegerField(null=True, blank=True)
	desc_botritis_5=models.IntegerField(null=True, blank=True)
	desc_botritis_6=models.IntegerField(null=True, blank=True)
	desc_botritis_7=models.IntegerField(null=True, blank=True)
	desc_botritis_8=models.IntegerField(null=True, blank=True)
	desc_botritis_9=models.IntegerField(null=True, blank=True)
	desc_botritis_10=models.IntegerField(null=True, blank=True)
	desc_botritis_12=models.IntegerField(null=True, blank=True)
	desc_botritis_14=models.IntegerField(null=True, blank=True)
	desc_botritis_16=models.IntegerField(null=True, blank=True)
	desc_botritis_18=models.IntegerField(null=True, blank=True)
	desc_botritis_20=models.IntegerField(null=True, blank=True)
	desc_botritis_22=models.IntegerField(null=True, blank=True)
	desc_botritis_24=models.IntegerField(null=True, blank=True)

	desc_cochinilla_4=models.IntegerField(null=True, blank=True)
	desc_cochinilla_5=models.IntegerField(null=True, blank=True)
	desc_cochinilla_6=models.IntegerField(null=True, blank=True)
	desc_cochinilla_7=models.IntegerField(null=True, blank=True)
	desc_cochinilla_8=models.IntegerField(null=True, blank=True)
	desc_cochinilla_9=models.IntegerField(null=True, blank=True)
	desc_cochinilla_10=models.IntegerField(null=True, blank=True)
	desc_cochinilla_12=models.IntegerField(null=True, blank=True)
	desc_cochinilla_14=models.IntegerField(null=True, blank=True)
	desc_cochinilla_16=models.IntegerField(null=True, blank=True)
	desc_cochinilla_18=models.IntegerField(null=True, blank=True)
	desc_cochinilla_20=models.IntegerField(null=True, blank=True)
	desc_cochinilla_22=models.IntegerField(null=True, blank=True)
	desc_cochinilla_24=models.IntegerField(null=True, blank=True)

	desc_pudricion_4=models.IntegerField(null=True, blank=True)
	desc_pudricion_5=models.IntegerField(null=True, blank=True)
	desc_pudricion_6=models.IntegerField(null=True, blank=True)
	desc_pudricion_7=models.IntegerField(null=True, blank=True)
	desc_pudricion_8=models.IntegerField(null=True, blank=True)
	desc_pudricion_9=models.IntegerField(null=True, blank=True)
	desc_pudricion_10=models.IntegerField(null=True, blank=True)
	desc_pudricion_12=models.IntegerField(null=True, blank=True)
	desc_pudricion_14=models.IntegerField(null=True, blank=True)
	desc_pudricion_16=models.IntegerField(null=True, blank=True)
	desc_pudricion_18=models.IntegerField(null=True, blank=True)
	desc_pudricion_20=models.IntegerField(null=True, blank=True)
	desc_pudricion_22=models.IntegerField(null=True, blank=True)
	desc_pudricion_24=models.IntegerField(null=True, blank=True)

	desc_rajadasae_4=models.IntegerField(null=True, blank=True)
	desc_rajadasae_5=models.IntegerField(null=True, blank=True)
	desc_rajadasae_6=models.IntegerField(null=True, blank=True)
	desc_rajadasae_7=models.IntegerField(null=True, blank=True)
	desc_rajadasae_8=models.IntegerField(null=True, blank=True)
	desc_rajadasae_9=models.IntegerField(null=True, blank=True)
	desc_rajadasae_10=models.IntegerField(null=True, blank=True)
	desc_rajadasae_12=models.IntegerField(null=True, blank=True)
	desc_rajadasae_14=models.IntegerField(null=True, blank=True)
	desc_rajadasae_16=models.IntegerField(null=True, blank=True)
	desc_rajadasae_18=models.IntegerField(null=True, blank=True)
	desc_rajadasae_20=models.IntegerField(null=True, blank=True)
	desc_rajadasae_22=models.IntegerField(null=True, blank=True)
	desc_rajadasae_24=models.IntegerField(null=True, blank=True)



	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalMmppGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalMmppGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Detalle Ev. Calidad Materia Prima Granada Ica 2022 '
		verbose_name_plural = 'Detalle Ev. Calidad Materia Prima Granada Ica 2022'
		def __str__(self):
			return "%s-%s" % (self.anexo_detalle.npalet, self.fecha_hora_creacion)


#ev-cal-control descarte-granada-ica-2022
class EvCalControlDescarteGrIca2022(models.Model):
	fecha_proceso=models.DateField("Fecha de Evaluacion",null=True, blank=True)
	anexo_linea=models.ForeignKey(LineasPlanta, on_delete=models.CASCADE, related_name="AnexoLineasDescGrIca2021",null=True, blank=True)
	controlador_prod= models.CharField("Controladora Produccion", max_length=200,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalDescarteGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalDescarteGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Control Descarte Granada Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Control Descarte Granada Ica 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.fecha_proceso, self.anexo_linea, self.controlador_prod)

#detalle-ev-cal-control descarte-granada-ica-2022
class DetalleEvCalControlDescarteGrIca2022(models.Model):
	anexo_detalle=models.ForeignKey(EvCalControlDescarteGrIca2022, on_delete=models.CASCADE, related_name="AnexoDetalleDescGrIca2021",null=True, blank=True)
	hora_inspeccion = models.TimeField("Hora Inspeccion", blank=True, null=True)
	fecha_cosecha=models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_proveedor= models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoZonaDescGrIca2021",null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadDescGrIca2021",null=True, blank=True)
	
	cat1_exportable=models.IntegerField(null=True, blank=True)
	cat2_exportable=models.IntegerField(null=True, blank=True)
	catind_exportable=models.IntegerField(null=True, blank=True)

	rajadas_ae=models.IntegerField(null=True, blank=True)
	rajadas_golpe=models.IntegerField(null=True, blank=True)
	insolacion_fuerte=models.IntegerField(null=True, blank=True)
	danio_mecanico=models.IntegerField(null=True, blank=True)
	bajo_peso=models.IntegerField(null=True, blank=True)
	danio_roedor=models.IntegerField(null=True, blank=True)
	alternaria=models.IntegerField(null=True, blank=True)
	cochinilla=models.IntegerField(null=True, blank=True)
	inmadures_verde=models.IntegerField(null=True, blank=True)
	gelechi=models.IntegerField(null=True, blank=True)
	pudricion=models.IntegerField(null=True, blank=True)
	hongo_corona=models.IntegerField(null=True, blank=True)
	quereza=models.IntegerField(null=True, blank=True)
	golpe_fuerte=models.IntegerField(null=True, blank=True)

	botrytis=models.IntegerField(null=True, blank=True)
	cicatriz=models.IntegerField(null=True, blank=True)
	corona_deshidratada=models.IntegerField(null=True, blank=True)
	rajada_severo=models.IntegerField(null=True, blank=True)
	danio_mecanico_pl=models.IntegerField(null=True, blank=True)
	danio_ave=models.IntegerField(null=True, blank=True)
	deforme=models.IntegerField(null=True, blank=True)
	golpe_fuerte_pl=models.IntegerField(null=True, blank=True)
	insolacion_leve=models.IntegerField(null=True, blank=True)
	manchas=models.IntegerField(null=True, blank=True)
	pudricion_corona=models.IntegerField(null=True, blank=True)
	rajadas_hongos=models.IntegerField(null=True, blank=True)
	rajadas_golpe_pl=models.IntegerField(null=True, blank=True)
	russet=models.IntegerField(null=True, blank=True)

	arilo_pardo=models.IntegerField(null=True, blank=True)
	desh_severo_cuerpo=models.IntegerField(null=True, blank=True)
	pres_mosca_fruta=models.IntegerField(null=True, blank=True)
	
	observacion= models.CharField("observacion", max_length=200,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalControlDescarteGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalControlDescarteGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev.Calidad Det Control Descarte Granada Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Det Control Descarte Granada Ica 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_detalle, self.hora_inspeccion, self.fecha_cosecha)


#EV CALIDAD DESCARTE ARANDANO 2022
class TipoEvaluacionAr(models.Model):
	desc= models.CharField("Tipo ev", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo EV Arandano'
		verbose_name_plural = 'Tipo EV Arandano'

	def __str__(self):
		return "%s" % ( self.desc)

class EvCalControlDescarteAr2022(models.Model):
	fecha_proceso = models.DateField("Fecha de Evaluacion",null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoDescarteAr2022", null=True, blank=True)
	anexo_tipo = models.ForeignKey(TipoEvaluacionAr, on_delete=models.CASCADE, related_name="AnexoTipoEvDescarteAr2022", null=True, blank=True)
	anexo_fundo = models.ForeignKey(MaestraFundoCultivo, on_delete=models.CASCADE, related_name="AnexoFundoEvDescarteAr2022", null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadDescarteAr2022", null=True, blank=True)
	ticket = models.IntegerField(null=True, blank=True)
	fecha_cosecha = models.DateField("Fecha Cosecha", null=True, blank=True)
	cantidad_muestra = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalDescarteArIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalDescarteArIca2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Control Descarte Arandano Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Control Descarte Arandano Ica 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.fecha_proceso, self.anexo_fundo, self.anexo_tipo)

class DetalleEvCalControlDescarteAr2022(models.Model):
	anexo_detalle=models.ForeignKey(EvCalControlDescarteAr2022, on_delete=models.CASCADE, related_name="AnexoDetalleDescArIca2022", null=True, blank=True)

	#EXPORTABLE
	exportable1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	exportable2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	exportable2_5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	exportable3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	exportable4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#DEF. CONDICION
	condicion1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion6 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion8 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion9 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion11 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion13 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	condicion14 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#DEF. CALIDAD
	calidad1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad6 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad8 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad9 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad11 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calidad13 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#DEF. FITOSANITARIO
	fitosanitario1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	fitosanitario2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	fitosanitario3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	fitosanitario4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	fitosanitario5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalControlDescarteArIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalControlDescarteArIca2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	class Meta:
		verbose_name = 'Ev.Calidad Det Control Descarte Arandano Ica 2022 '
		verbose_name_plural = 'Ev. Calidad Det Control Descarte Arandano Ica 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)


#CONTROL DESCARTE AR2022
class EvControlDescarteAr202202(models.Model):
	fecha_proceso = models.DateField("Fecha de Evaluacion",null=True, blank=True)
	anexo_fundo = models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvControlDescarteAr202202", null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoControlVariedadDescarteAr202202", null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvDescarteAr202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvDescarteAr202202", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Control Descarte Arandano 202202'
		verbose_name_plural = 'Ev. Control Descarte Arandano 202202'
		def __str__(self):
			return "%s-%s-%s" % (self.fecha_proceso, self.anexo_fundo, self.anexo_tipo)

class EvControlDescarteAr2022(models.Model):
	fecha_proceso = models.DateField("Fecha de Evaluacion",null=True, blank=True)
	anexo_fundo = models.ForeignKey(MaestraFundoCultivo, on_delete=models.CASCADE, related_name="AnexoFundoEvControlDescarteAr2022", null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoControlTurnoDescarteAr2022", null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoControlVariedadDescarteAr2022", null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvDescarteAr2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvDescarteAr2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Control Descarte Arandano 2022 '
		verbose_name_plural = 'Ev. Control Descarte Arandano 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.fecha_proceso, self.anexo_fundo, self.anexo_tipo)

class DetalleEvControlDescarteAr2022(models.Model):
	anexo_detalle=models.ForeignKey(EvControlDescarteAr2022, on_delete=models.CASCADE, related_name="AnexoDetalleDescArIca2022", null=True, blank=True)
	
	fecha_cosecha = models.DateField("Fecha de Cosecha",null=True, blank=True)
	
	#ACOPIO
	acopio1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#SELECCION
	seleccion1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	seleccion2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#CALIBRADO
	calibrado1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#EMPAQUE
	empaque1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#CALIDAD
	calidad1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvControlDescarteAr2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvControlDescarteAr2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Det Control Descarte Arandano 2022'
		verbose_name_plural = 'Ev. Det Control Descarte Arandano 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)

class DetalleEvControlDescarteAr202202(models.Model):
	anexo_detalle=models.ForeignKey(EvControlDescarteAr202202, on_delete=models.CASCADE, related_name="AnexoDetalleDescArIca202202", null=True, blank=True)
	
	fecha_cosecha = models.DateField("Fecha de Cosecha",null=True, blank=True)
	anexo_fundo = models.ForeignKey(MaestraFundoCultivo, on_delete=models.CASCADE, related_name="AnexoFundoEvControlDescarteAr202202", null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoControlTurnoDescarteAr202202", null=True, blank=True)

	#ACOPIO
	acopio1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	acopio2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#SELECCION
	seleccion1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	seleccion2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#CALIBRADO
	calibrado1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	calibrado4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#EMPAQUE
	empaque1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque6 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	empaque7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	#CALIDAD
	calidad1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvControlDescarteAr202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvControlDescarteAr202202", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Det Control Descarte Arandano 202202'
		verbose_name_plural = 'Ev. Det Control Descarte Arandano 202202'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)

class TipoAlveoloCalidad (models.Model):
	desc= models.CharField("Desc de Material",max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Tipo de Alveolo -Ev. Calidad'
		verbose_name_plural = 'Selector Tipo de Alveolo  -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class TipoBolsaCalidad (models.Model):
	desc=models.CharField("Descripcion Material",max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Tipo de Bolsa-Ev. Calidad'
		verbose_name_plural = 'Selector  Tipo de Bolsa -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class PresentacionMaterialCalidad (models.Model):
	desc=models.CharField("Descripcion Material",max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Selector Presentacio Material -Ev. Calidad'
		verbose_name_plural = 'Selector  Presentacio Material  -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)



class MaterialesCalidad (models.Model):
	marca= models.CharField("Marca de Material",max_length=50,null=True, blank=True)
	desc=models.CharField("Descripcion Material",max_length=50,null=True, blank=True)
	peso= models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	anexo_alveolo = models.ForeignKey(TipoAlveoloCalidad, on_delete=models.CASCADE,null=True, blank=True)
	anexo_bolsa = models.ForeignKey(TipoBolsaCalidad, on_delete=models.CASCADE,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMatEvCalidad2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMatEvCalidad2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
		
	class Meta:
		verbose_name = 'Materiales Calidad- Ev. Calidad'
		verbose_name_plural = 'Materiales Calidad -Ev. Calidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.marca)

class EvCalControlPesosGrIca2022 (models.Model):
	fecha_evaluacion=models.DateField("Fecha Evaluacion",null=True, blank=True)
	anexo_linea = models.ForeignKey(LineasPlanta, on_delete=models.CASCADE,null=True, blank=True)
	supervisor=models.CharField("Supervisor Linea",max_length=50,null=True, blank=True)
	inspector=models.CharField("Inspector Calidad",max_length=50,null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalControlPesoGrIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalControlPesoGrIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
		
	class Meta:
		verbose_name = 'Ev. Calidad Control Pesos Gr Ica 2022'
		verbose_name_plural = 'Ev. Calidad Control Pesos Gr Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.fecha_evaluacion, self.anexo_linea)


class DetalleEvCalControlPesosGrIca2022 (models.Model):
	anexo_detalle = models.ForeignKey(EvCalControlPesosGrIca2022, on_delete=models.CASCADE,null=True, blank=True)
	anexo_presentacion = models.ForeignKey(PresentacionMaterialCalidad, on_delete=models.CASCADE,null=True, blank=True)
	marca=models.ForeignKey(MaterialesCalidad, on_delete=models.CASCADE,null=True, blank=True)
	anexo_cliente = models.ForeignKey(ClientesAthos, on_delete=models.CASCADE,null=True, blank=True)
	hora_evaluacion=models.TimeField("Hora Evaluacion",null=True, blank=True)
	
	anexo_calibre1 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,related_name="AnexoCal1EvCalPeso2022",null=True, blank=True)
	peso_neto1= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre2 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal2EvCalPeso2022", blank=True)
	peso_neto2= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre3 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal3EvCalPeso2022", blank=True)
	peso_neto3= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre4 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal4EvCalPeso2022", blank=True)
	peso_neto4= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre5 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal5EvCalPeso2022", blank=True)
	peso_neto5= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre6 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal6EvCalPeso2022", blank=True)
	peso_neto6= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre7 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal7EvCalPeso2022", blank=True)
	peso_neto7= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre8 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal8EvCalPeso2022", blank=True)
	peso_neto8= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre9 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal9EvCalPeso2022", blank=True)
	peso_neto9= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
	
	anexo_calibre10 = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE,null=True,related_name="AnexoCal10EvCalPeso2022", blank=True)
	peso_neto10= models.DecimalField(max_digits=9, decimal_places=3,null=True, blank=True)
		
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalControlPesoGrIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalControlPesoGrIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
		
	class Meta:
		verbose_name = 'Det-Ev. Calidad Control Pesos Gr Ica 2022'
		verbose_name_plural = 'Det-Ev. Calidad Control Pesos Gr Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.fecha_evaluacion, self.anexo_linea)


class EvPlantonesPlNaz2022(models.Model):
	anexo_fundo = models.ForeignKey(fundo, on_delete=models.CASCADE,null=True, blank=True)
	fecha_evaluacion=models.DateField("Fecha Evaluacion",null=True, blank=True)
	anexo_produccion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE,null=True, blank=True)
	anexo_turno = models.ForeignKey(TurnoProgramaProduccion, on_delete=models.CASCADE,null=True, blank=True)
	hora_evaluacion=models.TimeField("Hora Evaluacion",null=True, blank=True)
	supervisor=models.CharField("Supervisor Linea",max_length=30,null=True, blank=True)
	anexo_variedad = models.ForeignKey(variedad, on_delete=models.CASCADE,null=True, blank=True)
	n_personas=models.CharField("Personas Sembrando",max_length=4,null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvPlantPaltaIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvPlantPaltaIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
        
	class Meta:
		verbose_name = 'Ev. Plantones de Palta Ica 2022'
		verbose_name_plural = 'Ev. Plantones de Palta Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.fecha_evaluacion, self.anexo_produccion)

class DetalleEvPlantonesPlNaz2022(models.Model):
	anexo_detalle = models.ForeignKey(EvPlantonesPlNaz2022, on_delete=models.CASCADE,null=True, blank=True)
	nombres=models.CharField("Nombre del Personal",max_length=30,null=True, blank=True)
	primera_ausencia=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Primera_Ausencia")
	segunda_ausencia=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Segunda_Ausencia")
	tercera_ausencia=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Tercera_Ausencia")
	presencia_planta=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Presencia_Planta")
	presencia_suelo=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Presencia_Suelo")
	siembra_profunda=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Siembra_Profundo")
	tutor_posicionado=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Tutor_Posicionado")
	buen_siembra=models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE,null=True, blank=True, related_name="Buen_Siembra")
	promedio_planta=models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	observacion=models.CharField("Observación",max_length=70,null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvPlantPaltaIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvPlantPaltaIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
        
	class Meta:
		verbose_name = 'Det-Ev. Plantones de Palta Nazca 2022'
		verbose_name_plural = 'Det-Ev. Plantones de Palta Nazca 2022'

	def __str__(self):
		return "%s-%s" % ( self.nombres, self.promedio_planta)

#CARTILLA MUESTRAS CAJAS EMPACADAS GR2022
class SelectorCategoriaCalidad(models.Model):

	desc= models.CharField("Respuesta Categoria", max_length=200,null=True, blank=True)
    
	class Meta:
		verbose_name = 'Selector Respuesta Categoria Calidad '
		verbose_name_plural = 'Selector Respuesta Categoria Calidad'

	def __str__(self):
		return "%s" % (self.desc)

class EvMuestrasCajasEmpacadasGR2022(models.Model):
	fecha_evaluacion = models.DateField("Fecha Evaluacion",null=True, blank=True)
	responsable = models.IntegerField("Inspector / Supervisor",null=True, blank=True)
	npalet = models.IntegerField(null=True, blank=True, unique=True)
	hora_inspeccion = models.TimeField("Hora Inspeccion", blank=True, null=True)
	anexo_categoria = models.ForeignKey(SelectorCategoriaCalidad, on_delete=models.CASCADE, max_length=200, blank=True, null=True)
	marca_caja = models.CharField("Marca de Caja", max_length=200, blank=True, null=True)
	variedad = models.CharField("Variedad", max_length=200, blank=True, null=True)
	anexo_calibre = models.ForeignKey(CalibresAthos, on_delete=models.CASCADE, related_name="AnexoCalibreCajasEmpacadasGrIca2022",null=True, blank=True)
	marca = models.CharField("Marca / Tipo de Bolsa",max_length=50,null=True, blank=True)
	marca_sticker = models.CharField("Marca de Sticker",max_length=50,null=True, blank=True)
	proveedor = models.CharField("Proveedor/Fundo",max_length=50,null=True, blank=True)
	fecha_cosecha = models.CharField("Fecha de Cosecha",max_length=50,null=True, blank=True)
	anexo_corte = models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="AnexoCorteCajasEmpacadasGrIca2022",null=True, blank=True)
	peso_neto = models.DecimalField(max_digits=7, decimal_places=3,null=True, blank=True)
	anexo_sobrepeso = models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="AnexoSobrepesoCajasEmpacadasGrIca2022",null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvMuestrasCajasEmpacadasGR2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvMuestrasCajasEmpacadasGR2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Ev. Muestras de Cajas Empacadas Gr Ica 2022'
		verbose_name_plural = 'Ev. Muestras de Cajas Empacadas Gr Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.fecha_evaluacion, self.anexo_categoria)

class DetalleEvMuestrasCajasEmpacadasGR2022(models.Model):
	anexo_detalle = models.ForeignKey(EvMuestrasCajasEmpacadasGR2022, on_delete=models.CASCADE,null=True, blank=True)
    
    #CAT1
	cicatriz_cat1 = models.IntegerField("Cicatrices", null=True, blank=True)
	danio_roce_cat1 = models.IntegerField("Daño por Roce", null=True, blank=True)
	deformes_cat1 = models.IntegerField("Deformes", null=True, blank=True)
	insolacion_leve_cat1 = models.IntegerField("Insolación Leve", null=True, blank=True)
	libre_defectos_cat1 =  models.IntegerField("Libre de Defectos", null=True, blank=True)
	manchas_cat1 = models.IntegerField("Manchas", null=True, blank=True)
	rajaduras_cat1 = models.IntegerField("Rajaduras", null=True, blank=True)
	suma_cat1 = models.IntegerField("Total de Cat1", null=True, blank=True)

    #CAT2
	insolacion_moderada_cat2 = models.IntegerField("Insolación Moderada", null=True, blank=True)
	cicatriz_cat2 = models.IntegerField("Cicatrices", null=True, blank=True)
	corona_deshidratada_cat2 = models.IntegerField("Corona Deshidratada Leve", null=True, blank=True)
	danio_mecanico_cat2 = models.IntegerField("Daño Mecanico", null=True, blank=True)
	danio_roce_cat2 = models.IntegerField("Daño por Roce", null=True, blank=True)
	golpe_leve_cat2 = models.IntegerField("Golpe Leve", null=True, blank=True)
	manchas_cat2 = models.IntegerField("Manchas", null=True, blank=True)
	rajaduras_cat2 = models.IntegerField("Rajaduras", null=True, blank=True)
	suma_cat2 = models.IntegerField("Total de Cat2", null=True, blank=True)

    #INDUSTRIAL
	cicatriz_industrial = models.IntegerField("Cicatrices", null=True, blank=True)
	danio_roce_industrial = models.IntegerField("Daño por Roce", null=True, blank=True)
	manchas_industrial = models.IntegerField("Manchas", null=True, blank=True)
	rajaduras_industrial = models.IntegerField("Rajaduras", null=True, blank=True)
	suma_industrial = models.IntegerField("Total de Industrial", null=True, blank=True)
	
	#DESCARTEs
	arilo_expuesto_descarte = models.IntegerField("Arilo Expuesto", null=True, blank=True)
	corona_deshidratada_descarte = models.IntegerField("Corona Deshidratada", null=True, blank=True)
	danio_plagas_descarte = models.IntegerField("Daño por Plagas", null=True, blank=True)
	golpe_fuerte_descarte = models.IntegerField("Golpe Fuerte", null=True, blank=True)
	insolado_fuerte_descarte = models.IntegerField("Insolado Fuerte", null=True, blank=True)
	pudricion_descarte = models.IntegerField("Pudricion", null=True, blank=True)
	rajados_severos_descarte = models.IntegerField("Rajados Severos", null=True, blank=True)
	suma_descarte = models.IntegerField("Total de Descarte", null=True, blank=True)

    #UNIDADES TOTALES MUESTREADAS
	unidades_totales_muestreadas = models.IntegerField("Unidades Totales Muestreadas", null=True, blank=True)
	porcentajes_totales_muestreados = models.CharField("Porcentajes Totales Muestreados", max_length=10, null=True, blank=True)
    
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleEvMuestrasCajasEmpacadasGR2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleEvMuestrasCajasEmpacadasGR2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
        
	class Meta:
		verbose_name = 'Det-Ev. Muestras de Cajas Empacadas Gr Ica 2022'
		verbose_name_plural = 'Det-Ev. Muestras de Cajas Empacadas Gr Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.anexo_detalle, self.anexo_categoria)

#CONTROL DE DESCARTE GR 2022
class EvControlDescarteGR2022(models.Model):
	fecha_proceso = models.DateField("Fecha Proceso",null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)
	material = models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, null=True, blank=True)

	santiaguillo = models.DecimalField("Santiaguillo", max_digits=9, decimal_places=3, null=True, blank=True)
	santiago_apostol = models.DecimalField("Santiago Apostol", max_digits=9, decimal_places=3, null=True, blank=True)
	los_pobres = models.DecimalField("Los Pobres", max_digits=9, decimal_places=3, null=True, blank=True)
	macacara = models.DecimalField("Macacara", max_digits=9, decimal_places=3, null=True, blank=True)
	santa_filomena = models.DecimalField("Santa Filomena", max_digits=9, decimal_places=3, null=True, blank=True)
	parcelas = models.DecimalField("Parcelas", max_digits=9, decimal_places=3, null=True, blank=True)
	sojo = models.DecimalField("Sojo", max_digits=9, decimal_places=3, null=True, blank=True)
	las_dunas = models.DecimalField("Las Dunas", max_digits=9, decimal_places=3, null=True, blank=True)
	lindero = models.DecimalField("Lindero", max_digits=9, decimal_places=3, null=True, blank=True)
	caylan = models.DecimalField("Caylan", max_digits=9, decimal_places=3, null=True, blank=True)
	total_descarte = models.DecimalField("Total", max_digits=10, decimal_places=3, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvControlDescarteGR2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvControlDescarteGR2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Ev. Control Descarte GR Ica 2022'
		verbose_name_plural = 'Ev. Control Descarte GR Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.fecha_proceso, self.anexo_turno)

#EVALUACION DE RAMAS
class TipoEvaluacionRm(models.Model):
	desc= models.CharField("Tipo evaluacion ramas", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo EV. Ramas'
		verbose_name_plural = 'Tipo EV. Ramas'

	def __str__(self):
		return "%s" % ( self.desc)

class EvFenRamasArandanos(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvRamas",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvRamas",null=True, blank=True)
	ubicacion = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvRamas")
	
	valvula= models.CharField("Valvula", max_length=30)
	anexo_tipo=models.ForeignKey(TipoEvaluacionRm, on_delete=models.CASCADE, related_name="AnexoTipoEVRamas",null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvFenRamas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvFenRamas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Ev. Fenologia Ramas Arandanos'
		verbose_name_plural = 'Ev. Fenologia Ramas Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.ubicacion, self.ubicacion.id)

class DetallePlantaEvFenRamasArandanos(models.Model):
	anexo_evaluacion = models.ForeignKey(EvFenRamasArandanos, on_delete=models.CASCADE, related_name="AnexoEVDetalle",null=True, blank=True)
	n_planta= models.IntegerField(null=True, blank=True)
	cant_ramas= models.IntegerField(null=True, blank=True)
	ramas_produccion= models.IntegerField(null=True, blank=True)
	tira_savia= models.IntegerField(null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetPlantaRamas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvDetPlantaRamas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Detalle-Ev. Fen. Ramas Detalle Planta Arandanos '
		verbose_name_plural = 'Detalle-Ev. Fen. Ramas Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s" % (self.n_planta, self.cant_ramas)

class RamaPlantaEvFenRamasArandanos(models.Model):
	anexo_detalle = models.ForeignKey(DetallePlantaEvFenRamasArandanos, on_delete=models.CASCADE, related_name="AnexoEVDetalleRamas",null=True, blank=True)
	anexo_diametro = models.ForeignKey(NDiametro, on_delete=models.CASCADE,null=True, blank=True)
	diametro= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	altura= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	num_ramas = models.IntegerField(null=True, blank=True)
	primera_poda = models.IntegerField(null=True, blank=True)
	segunda_poda = models.IntegerField(null=True, blank=True)
	tercera_poda = models.IntegerField(null=True, blank=True)
	cuarta_poda = models.IntegerField(null=True, blank=True)
	quinta_poda = models.IntegerField(null=True, blank=True)

	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRamas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvRamas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ev. Fen. Ramas Detalle Planta Arandanos'
		verbose_name_plural = 'Ev. Fen. Ramas Detalle Planta  Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_evaluacion.ubicacion,self.usuario_creacion, self.fecha_hora_creacion)	


#EV CAMARAS HUMEDAS
class TipoCondicionCamarasHumedas(models.Model):
	desc= models.CharField("Tipo Condicion", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Condicion Camaras Humedas'
		verbose_name_plural = 'Tipo Condicion Camaras Humedas'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoOrganoCamarasHumedas(models.Model):
	desc= models.CharField("Tipo Organo", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Organo Camaras Humedas'
		verbose_name_plural = 'Tipo Organo Camaras Humedas'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoUbicacionCamarasHumedas(models.Model):
	desc= models.CharField("Tipo Ubicacion", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Ubicacion Camaras Humedas'
		verbose_name_plural = 'Tipo Ubicacion Camaras Humedas'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoProductoCamarasHumedas(models.Model):
	desc= models.CharField("Tipo Producto", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Producto Camaras Humedas'
		verbose_name_plural = 'Tipo Producto Camaras Humedas'

	def __str__(self):
		return "%s" % ( self.desc)


class EvCamarasHumedas(models.Model):
	anexo_tipo_evaluacion = models.ForeignKey(TipoEvaluacionAr, on_delete=models.CASCADE, related_name="AnexoTipoEvaluacionCamarasHumedas2022", blank=True, null=True)
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE,null=True, blank=True, related_name="ZonaEvCamarasHumedas2022")
	anexo_fundo = models.ForeignKey(fundo, on_delete=models.CASCADE,null=True, blank=True, related_name="FundoEvCamarasHumedas2022")
	anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE,null=True, blank=True, related_name="PEPEvCamarasHumedas2022")
	sub_lote = models.CharField("Sub Lote", max_length=200,null=True, blank=True)
	fecha_instalacion = models.DateField("Fecha Evaluacion",null=True, blank=True)
	muestra = models.IntegerField(null=True, blank=True)
	anexo_variedad = models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadCamarasHumedas2022", blank=True, null=True)
	anexo_condicion = models.ForeignKey(TipoCondicionCamarasHumedas, on_delete=models.CASCADE, related_name="AnexoCondicionCamarasHumedas2022", blank=True, null=True)
	anexo_organo = models.ForeignKey(TipoOrganoCamarasHumedas, on_delete=models.CASCADE, related_name="AnexoOrganoCamarasHumedas2022", blank=True, null=True)
	anexo_ubicacion = models.ForeignKey(TipoUbicacionCamarasHumedas, on_delete=models.CASCADE, related_name="AnexoUbicacionCamarasHumedas2022", blank=True, null=True)
	anexo_producto = models.ForeignKey(ProductosAutorizados, on_delete=models.CASCADE, related_name="AnexoProductoCamarasHumedas2022", blank=True, null=True)
	anexo_producto2 = models.ForeignKey(TipoProductoCamarasHumedas, on_delete=models.CASCADE, related_name="AnexoProductoCamarasHumedas2022", blank=True, null=True)
	dias_aplicacion = models.IntegerField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCamarasHumedas2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCamarasHumedas2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Camaras Humedas 2022'
		verbose_name_plural = 'Ev. Camaras Humedas 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_pep, self.sub_lote, self.frutos_infestados)

class DetallePlantaEvCamarasHumedas(models.Model):
	anexo_detalle = models.ForeignKey(EvCamarasHumedas, on_delete=models.CASCADE,null=True, blank=True, related_name="AnexoDetEvCamarasHumedas2022")
	fecha_evaluacion = models.DateField("Fecha",null=True, blank=True)
	frutos_infestados = models.IntegerField(null=True, blank=True)
	botrytis_cinerea = models.IntegerField(null=True, blank=True)
	alternaria = models.IntegerField(null=True, blank=True)
	cladosporium_sp = models.IntegerField(null=True, blank=True)
	apergillus_niger = models.IntegerField(null=True, blank=True)
	pestalotiopsis_sp = models.IntegerField(null=True, blank=True)
	rhyzopus_spp = models.IntegerField(null=True, blank=True)
	penicillum_sp = models.IntegerField(null=True, blank=True)
	sin_esporular = models.IntegerField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCamarasHumedas2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCamarasHumedas2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Detalle Ev. Camaras Humedas 2022'
		verbose_name_plural = 'Detalle Ev. Camaras Humedas 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_pep, self.sub_lote, self.frutos_infestados)

#EV CALIDAD CONTROL DESCARTE HG 2022
class EvCalControlDescarteHg2022(models.Model):
	fecha_proceso = models.DateField("Fecha de Evaluacion",null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoDescarteHg2022", null=True, blank=True)
	anexo_tipo = models.ForeignKey(TipoEvaluacionAr, on_delete=models.CASCADE, related_name="AnexoTipoEvDescarteHg2022", null=True, blank=True)
	anexo_fundo = models.ForeignKey(MaestraFundoCultivo, on_delete=models.CASCADE, related_name="AnexoFundoEvDescarteHg2022", null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadDescarteHg2022", null=True, blank=True)
	ticket = models.IntegerField(null=True, blank=True)
	fecha_cosecha = models.DateField("Fecha Cosecha", null=True, blank=True)
	cantidad_muestra = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalDescarteHg2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalDescarteHg2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Ev. Calidad Control Descarte Higo 2022'
		verbose_name_plural = 'Ev. Calidad Control Descarte Higo 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.fecha_proceso, self.anexo_fundo, self.anexo_tipo)

class DetalleEvCalControlDescarteHg2022(models.Model):
	anexo_detalle=models.ForeignKey(EvCalControlDescarteHg2022, on_delete=models.CASCADE, related_name="AnexoDetalleDescArIca2022", null=True, blank=True)

	#EXPORTABLE
	exportable1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable6 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable7 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	exportable8 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	#DESCARTE
	descarte1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte6 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte7 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte8 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte9 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte10 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte11 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte12 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte13 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte14 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte15 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte16 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	descarte17 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalControlDescarteHg2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalControlDescarteHg2022", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	class Meta:
		verbose_name = 'Ev.Calidad Det Control Descarte Higo 2022 '
		verbose_name_plural = 'Ev. Calidad Det Control Descarte Higo 2022'
		def __str__(self):
			return "%s-%s-%s" % (self.anexo_detalle, self.usuario_creacion, self.fecha_hora_creacion)

#EV CAL. PROD. TERMINADOS HG
class ControlProductoTerminadoHg(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="AnexoCPTHg", blank=True, null=True)

	fecha = models.DateField("Fecha",null=True, blank=True)
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCptCentrosCPTHg",null=True, blank=True)
	anexo_linea=models.ForeignKey(LineaEmpaqueAthos, on_delete=models.CASCADE, related_name="AnexoCptLineaECPTHg",null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoCptTurnoCPTHg",null=True, blank=True)
	anexo_pagina=models.ForeignKey(SelectorAthos, on_delete=models.CASCADE, related_name="AnexoPaginaControlCPTHg", blank=True, null=True)
	observacion=models.CharField(max_length=30, blank=True, null= True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserCreacionCPTHg")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCPTHg",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Control Producto Terminado Hg'
		verbose_name_plural = ' Control Producto Terminado Hg'

	def __str__(self):
		return "%s-%s" % ( self.fecha_hora_creacion,self.usuario_creacion)

class DetalleControlProductoTerminadoHg(models.Model):
	anexo_detalle=models.ForeignKey(ControlProductoTerminadoHg, on_delete=models.CASCADE, related_name="AnexoDetalleCPTHg", blank=True, null=True)
	trazabilidad= models.CharField("Trazabilidad", max_length=250,null=True, blank=True)
	npalet= models.IntegerField(null=True, blank=True, unique=True)
	anexo_cliente=models.ForeignKey(ClientesAthos, on_delete=models.CASCADE, related_name="AnexoDetalleClienteCPTHg", blank=True, null=True)
	anexo_presentaciong=models.ForeignKey(PresentacionesAthos, on_delete=models.CASCADE, related_name="AnexoPresentaciongCPTHg", blank=True, null=True)
	anexo_presentacion=models.ForeignKey(MaestraPresentacionesAthos, on_delete=models.CASCADE, related_name="AnexoDetalleMaestraPCPTHg", blank=True, null=True)
	tamano_pulpa= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	anexo_calibre=models.ForeignKey(CalibresAthos, on_delete=models.CASCADE, related_name="AnexoDetalleCalibreCPTHg", blank=True, null=True)
	anexo_acomodo=models.ForeignKey(AcomodoAthos, on_delete=models.CASCADE, related_name="AnexoDetalleAcomodoCPTHg", blank=True, null=True)
	
	peso1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso5= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso6= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	condicion1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion5= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion6= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion7= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion8= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion9= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion10= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion11= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	calidad1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad5= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad6= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad7= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad8= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	fitosanitario1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	fitosanitario2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	fitosanitario3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	p1= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p2= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p3= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p4= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p5= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p6= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p7= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p8= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p9= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p10= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p11= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	p12= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetCPTHg")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetCPTHg",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Det Control Producto Terminado Hg'
		verbose_name_plural = 'Det Control Producto Terminado Hg'

	def __str__(self):
		return "%s-%s-%s-%s" % ( self.npalet, self.trazabilidad,self.fecha_hora_creacion,self.usuario_creacion)


#TIPO CALIBRES
class TipoCalibreAnalisisEficiencia(models.Model):
	desc = models.CharField("Tipo Calibre", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Calibre Analisis Eficiencia 2022'
		verbose_name_plural = 'Tipo Calibre Analisis Eficiencia 2022'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoEnvaseAnalisisEficiencia(models.Model):
	desc = models.CharField("Tipo Envase", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Envase Analisis Eficiencia 2022'
		verbose_name_plural = 'Tipo Envase Analisis Eficiencia 2022'

	def __str__(self):
		return "%s" % ( self.desc)

#EV EFICIENCIA SELECCION Y CALIBRADO
class EvEficienciaSeleccionCalibrado(models.Model):
	npalet= models.IntegerField(null=True, blank=True)
	anexo_planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoEvEficienciaSC2022",null=True, blank=True)
	anexo_calibre = models.ForeignKey(TipoCalibreAnalisisEficiencia, on_delete=models.CASCADE, related_name="AnexoTipoCalibreSC2022",null=True, blank=True)
	anexo_linea = models.ForeignKey(LineaEmpaqueAthos, on_delete=models.CASCADE, related_name="AnexoLineaEmpaqueSC2022",null=True, blank=True)
	anexo_envase = models.ForeignKey(TipoEnvaseAnalisisEficiencia, on_delete=models.CASCADE, related_name="AnexoEnvaseSC2022",null=True, blank=True)
	anexo_cliente = models.ForeignKey(ClientesAthos, on_delete=models.CASCADE, related_name="AnexoClienteSC2022", blank=True, null=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoCptTurnoSC2022",null=True, blank=True)

	firmeza_1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	bloom_1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	bloom_2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	bloom_3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	bloom_4 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	condicion1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion4 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion5 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion6 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion7 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion8 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion9 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	condicion10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	calidad1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad4 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad5 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad6 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad7 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad8 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad9 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	calidad12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	fitosanitario1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	fitosanitario2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	fitosanitario3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvEficienciaSC2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvEficienciaSC2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Evaluación de Eficiencia - Selección y Calibrado 2022'
		verbose_name_plural = 'Evaluación de Eficiencia - Selección y Calibrado 2022'

	def __str__(self):
		return "%s - %s - %s" % (self.npalet,self.fecha_hora_creacion,self.usuario_creacion)

#EV PRODUCTO TERMINADO ANTES DE DESPACHO 2022
class TipoEnvioPTDespacho(models.Model):
	desc = models.CharField("Tipo", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Envio P.T. Despacho 2022'
		verbose_name_plural = 'Tipo Envio P.T. Despacho 2022'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoInspeccionVisualEstado(models.Model):
	desc = models.CharField("Tipo", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Inspeccion Visual Estado 2022'
		verbose_name_plural = 'Tipo Inspeccion Visual Estado 2022'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoInspeccionVisualConformidad(models.Model):
	desc = models.CharField("Tipo", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Inspeccion Visual Conformidad 2022'
		verbose_name_plural = 'Tipo Inspeccion Visual Conformidad 2022'

	def __str__(self):
		return "%s" % ( self.desc)

class TipoInspeccionVisualDecision(models.Model):
	desc = models.CharField("Tipo", max_length=30)
	
	class Meta:
		verbose_name = 'Tipo Inspeccion Visual Desicion 2022'
		verbose_name_plural = 'Tipo Inspeccion Visual Desicion 2022'

	def __str__(self):
		return "%s" % ( self.desc)

class EvProductoTerminadoDespacho(models.Model):
	fecha = models.DateField("Fecha de Despacho")
	anexo_planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoEvPlantaPTDespacho2022",null=True, blank=True)
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoEvTurnoPTDespacho2022",null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvPTDespacho2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvPTDespacho2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Evaluación de P.T. Despacho 2022'
		verbose_name_plural = 'Evaluación de P.T. Despacho 2022'

	def __str__(self):
		return "%s - %s - %s" % (self.fecha,self.anexo_planta,self.anexo_turno)

class DetalleEvProductoTerminadoDespacho(models.Model):
	anexo_detalle = models.ForeignKey(EvProductoTerminadoDespacho, on_delete=models.CASCADE, related_name="AnexoDetalleEvPTDespacho2022", blank=True, null=True)
	npalet = models.IntegerField(null=True, blank=True)
	anexo_cliente = models.ForeignKey(ClientesAthos, on_delete=models.CASCADE, related_name="AnexoClienteEvPTDespacho2022", blank=True, null=True)
	trazabilidad = models.CharField("Trazabilidad", max_length=250,null=True, blank=True)
	anexo_envio = models.ForeignKey(TipoEnvioPTDespacho, on_delete=models.CASCADE, related_name="AnexoEnvioEvPTDespacho2022", blank=True, null=True)
	
	firmeza_clo1_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo1_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo2_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo3_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo4_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	firmeza_clo5_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	peso_cj01_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj01_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj02_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj03_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj04_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m06 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m07 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m08 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m09 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	peso_cj05_m12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_bloom = models.ForeignKey(TipoInspeccionVisualEstado, on_delete=models.CASCADE, related_name="AnexoInspeccionVisualEvPTDespacho2022", blank=True, null=True)
	anexo_bloom2 = models.ForeignKey(TipoInspeccionVisualEstado, on_delete=models.CASCADE, related_name="AnexoInspeccionVisual2EvPTDespacho2022", blank=True, null=True)
	anexo_bloom3 = models.ForeignKey(TipoInspeccionVisualEstado, on_delete=models.CASCADE, related_name="AnexoInspeccionVisual3EvPTDespacho2022", blank=True, null=True)
	anexo_bloom4 = models.ForeignKey(TipoInspeccionVisualEstado, on_delete=models.CASCADE, related_name="AnexoInspeccionVisual4EvPTDespacho2022", blank=True, null=True)
	anexo_bloom5 = models.ForeignKey(TipoInspeccionVisualEstado, on_delete=models.CASCADE, related_name="AnexoInspeccionVisual5EvPTDespacho2022", blank=True, null=True)

	deshidratados_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	deshidratados_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	deshidratados_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	deshidratados_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	deshidratados_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	blandos_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	blandos_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	blandos_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	blandos_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	blandos_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	pudricion_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pudricion_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pudricion_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pudricion_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pudricion_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	frutos_florales_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	frutos_florales_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	frutos_florales_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	frutos_florales_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	frutos_florales_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	pitting_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pitting_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pitting_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pitting_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	pitting_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	machucon_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	machucon_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	machucon_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	machucon_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	machucon_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	heridas_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	heridas_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	heridas_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	heridas_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	heridas_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	desgarro_pedicelar_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	desgarro_pedicelar_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	desgarro_pedicelar_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	desgarro_pedicelar_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	desgarro_pedicelar_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	decoloracion_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	decoloracion_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	decoloracion_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	decoloracion_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	decoloracion_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	rojizos_inmaduro_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojizos_inmaduro_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojizos_inmaduro_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojizos_inmaduro_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	rojizos_inmaduro_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	Exudado_cj01 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	Exudado_cj02 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	Exudado_cj03 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	Exudado_cj04 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	Exudado_cj05 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	anexo_etiquetado = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEtiquetadoEvPTDespacho2022", blank=True, null=True)
	anexo_etiquetado2 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEtiquetado2EvPTDespacho2022", blank=True, null=True)
	anexo_etiquetado3 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEtiquetado3EvPTDespacho2022", blank=True, null=True)
	anexo_etiquetado4 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEtiquetado4EvPTDespacho2022", blank=True, null=True)
	anexo_etiquetado5 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEtiquetado5EvPTDespacho2022", blank=True, null=True)

	anexo_embolsado = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEmbolsadoEvPTDespacho2022", blank=True, null=True)
	anexo_embolsado2 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEmbolsado2EvPTDespacho2022", blank=True, null=True)
	anexo_embolsado3 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEmbolsado3EvPTDespacho2022", blank=True, null=True)
	anexo_embolsado4 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEmbolsado4EvPTDespacho2022", blank=True, null=True)
	anexo_embolsado5 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoEmbolsado5EvPTDespacho2022", blank=True, null=True)

	anexo_arte_caja = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoArteCajaEvPTDespacho2022", blank=True, null=True)
	anexo_arte_caja2 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoArteCaja2EvPTDespacho2022", blank=True, null=True)
	anexo_arte_caja3 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoArteCaja3EvPTDespacho2022", blank=True, null=True)
	anexo_arte_caja4 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoArteCaja4EvPTDespacho2022", blank=True, null=True)
	anexo_arte_caja5 = models.ForeignKey(TipoInspeccionVisualConformidad, on_delete=models.CASCADE, related_name="AnexoArteCaja5EvPTDespacho2022", blank=True, null=True)

	anexo_decision = models.ForeignKey(TipoInspeccionVisualDecision, on_delete=models.CASCADE, related_name="AnexoDecisionEvPTDespacho2022", blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvPTDespacho2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvPTDespacho2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Det Evaluacion de P.T. Despacho 2022'
		verbose_name_plural = 'Det Evaluacion de P.T. Despacho 2022'

	def __str__(self):
		return "%s-%s-%s-%s" % ( self.npalet, self.trazabilidad,self.fecha_hora_creacion,self.usuario_creacion)
