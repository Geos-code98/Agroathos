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
from apps.maestras.models import ClientesAthos
from apps.maestras.models import CalibresAthos
from apps.maestras.models import MaestraPresentacionesAthos
from apps.maestras.models import AcomodoAthos
from apps.maestras.models import LineaEmpaqueAthos
from apps.maestras.models import AuxiliaresCampoAthos
from apps.menu.models import TurnoProgramaProduccion

from apps.evaluaciones.models import SelectorRespuestaSiNoCalidad
from apps.evaluaciones.models import SelectorRespuestaEscalaCalidad


# Create your models here.


class EvCalCosechaGr(models.Model):
	fecha=models.DateField("Fecha de Evaluacion")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaEvCalCosechaGr",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoEvCalCosechaGr",null=True, blank=True)
	anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPEvCalCosechaGr")
	anexo_turno=models.ForeignKey(TurnoProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoTurnoPPEv",null=True, blank=True)
	sector= models.CharField("Sector", max_length=100, blank=True,null=True)
	
	qrsupervisor= models.CharField("Qr Supervisor", max_length=100, blank=True,null=True)
	anexo_supervisor = models.ForeignKey(AuxiliaresCampoAthos, on_delete=models.CASCADE, related_name="AnexoSupervisorEvCalCosechaGr",blank=True,null=True)
	
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE, related_name="AnexoVariedadEvCalCosechagrica2021", blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEvCalCosechaGr")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEvCalCosechaGr",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Cosecha Granada '
		verbose_name_plural = 'Ev. Calidad Cosecha Granada'

	def __str__(self):
		return "%s-%s-%s" % (self.fecha, self.anexo_pep, self.anexo_turno)

class DetalleEvCalCosechaGrCat1(models.Model):
	anexo_detalle=models.ForeignKey(EvCalCosechaGr, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalCosechaGrCat1",null=True, blank=True)
	total_fruta= models.IntegerField(null=True, blank=True)
	fruta_rajada= models.IntegerField(null=True, blank=True)
	fruta_clara2= models.IntegerField(null=True, blank=True)
	fruta_clara3= models.IntegerField(null=True, blank=True)
	fruta_cosechable_c3=models.IntegerField(null=True, blank=True)
	fruta_descarte= models.IntegerField(null=True, blank=True)
	dano_tijera= models.IntegerField(null=True, blank=True)
	sin_pedunculo= models.IntegerField(null=True, blank=True)
	con_pedunculo= models.IntegerField(null=True, blank=True)

	fruta_deforme= models.IntegerField(null=True, blank=True)
	fruta_deshidratada= models.IntegerField(null=True, blank=True)
	fruta_pquemada= models.IntegerField(null=True, blank=True)

	queresa= models.IntegerField(null=True, blank=True)
	fruta_hojas= models.IntegerField(null=True, blank=True)
	fruta_sana= models.IntegerField(null=True, blank=True)
	corona_deshidratada=models.IntegerField(null=True, blank=True)
	corona_botritis=models.IntegerField(null=True, blank=True)
	cochinilla=models.IntegerField(null=True, blank=True)
	color25=models.IntegerField(null=True, blank=True)
	qrevaluador= models.CharField("Qr Evaluador", max_length=100, blank=True,null=True)

	anexo_guantes = models.ForeignKey(SelectorRespuestaEscalaCalidad, on_delete=models.CASCADE, related_name="CalidadGuantes", blank=True, null=True)
	anexo_tijeras = models.ForeignKey(SelectorRespuestaEscalaCalidad, on_delete=models.CASCADE, related_name="CalidadTijeras", blank=True, null=True)
	anexo_jabas_burbupack = models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="CalidadJabasB", blank=True, null=True)
	anexo_jabas_sinb = models.ForeignKey(SelectorRespuestaSiNoCalidad, on_delete=models.CASCADE, related_name="CalidadJabasSB", blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleEvCalCosechaGrCat1")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleEvCalCosechaGrCat1",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle1-Categoria1 '
		verbose_name_plural = 'Detalle1-Categoria1'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_pep, self.fecha_hora_creacion, self.usuario_creacion)


class DetalleEvCalCosechaGrCat2(models.Model):
	anexo_detalle=models.ForeignKey(EvCalCosechaGr, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalCosechaGrCat2",null=True, blank=True)
	total_fruta= models.IntegerField(null=True, blank=True)
	fruta_cat1= models.IntegerField(null=True, blank=True)
	fruta_verde2=models.IntegerField(null=True, blank=True)
	qrevaluador= models.CharField("Qr Evaluador", max_length=100, blank=True,null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleEvCalCosechaGrCat2")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleEvCalCosechaGrCat2",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle2-Categoria2 '
		verbose_name_plural = 'Detalle2-Categoria2'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_pep, self.fecha_hora_creacion, self.usuario_creacion)

class DetalleEvCalCosechaGrDescarte(models.Model):
	anexo_detalle=models.ForeignKey(EvCalCosechaGr, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalCosechaGrDesc",null=True, blank=True)
	total_fruta= models.IntegerField(null=True, blank=True)
	fruta_cat1= models.IntegerField(null=True, blank=True)
	
	qrevaluador= models.CharField("Qr Evaluador", max_length=100, blank=True,null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionetalleEvCalCosechaGrDesc")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModetalleEvCalCosechaGrDesc",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle3-Categoria Descarte '
		verbose_name_plural = 'Detalle3-Categoria Descarte'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_pep, self.fecha_hora_creacion, self.usuario_creacion)



class DetalleEvCalCosechaGrCampo(models.Model):
	anexo_detalle=models.ForeignKey(EvCalCosechaGr, on_delete=models.CASCADE, related_name="AnexoDetalleEvCalCosechaGrCampo",null=True, blank=True)
	rajados= models.IntegerField(null=True, blank=True)
	r3= models.IntegerField(null=True, blank=True)
	r35= models.IntegerField(null=True, blank=True)
	r4= models.IntegerField(null=True, blank=True)
	r5= models.IntegerField(null=True, blank=True)
	fruta_verde_pl=models.IntegerField(null=True, blank=True)
	qrevaluador= models.CharField("Qr Evaluador", max_length=100, blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionetalleEvCalCosechaGrCampo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModetalleEvCalCosechaGrCampo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle4-Categoria Campo '
		verbose_name_plural = 'Detalle4-Categoria Campo'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle.anexo_pep, self.fecha_hora_creacion, self.usuario_creacion)




class EvCalidadMuestreoPlantaGr(models.Model):
	qrpalet= models.CharField("Qr Palet", max_length=100, blank=True,null=True)
	num_palet= models.IntegerField(null=True, blank=True)
	variedad= models.CharField("Variedad", max_length=100, blank=True,null=True)
	guia_remision= models.CharField("Guia Remision", max_length=100, blank=True,null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionetalleEvCalMuestroGrPlanta")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModetalleEvCalMuestroGrPlanta",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Ev. Calidad Muestreo  Planta -Granada '
		verbose_name_plural = 'Ev. Calidad Muestreo  Planta -Granada'

	def __str__(self):
		return "%s-%s" % (self.qrpalet, self.fecha_hora_creacion)


class DetalleEvCalidadMuestreoPlantaGr(models.Model):
	
	num_calibre= models.IntegerField(null=True, blank=True)

	cat1= models.IntegerField(null=True, blank=True)
	
	cat2_cicatrizm25= models.IntegerField(null=True, blank=True)
	cat2_manchasm25= models.IntegerField(null=True, blank=True)
	cat2_pedunculo= models.IntegerField(null=True, blank=True)
	cat2_rajadas= models.IntegerField(null=True, blank=True)
	cat2_russel= models.IntegerField(null=True, blank=True)
	cat2_danio= models.IntegerField(null=True, blank=True)
	cat2_levinsolacion= models.IntegerField(null=True, blank=True)
	cat2_manchasverdes= models.IntegerField(null=True, blank=True)
	cat2_deformes= models.IntegerField(null=True, blank=True)
	cat2_palidas= models.IntegerField(null=True, blank=True)
	cat2_corona=models.IntegerField(null=True, blank=True)
	cat2_recuperables=models.IntegerField(null=True, blank=True)

	cattin_rajada_sa=models.IntegerField(null=True, blank=True)
	

	desc_insolada= models.IntegerField(null=True, blank=True)
	desc_queresa= models.IntegerField(null=True, blank=True)
	desc_golpe= models.IntegerField(null=True, blank=True)
	desc_botrytis= models.IntegerField(null=True, blank=True)
	desc_rajadas_ae= models.IntegerField(null=True, blank=True)
	desc_inmadurez= models.IntegerField(null=True, blank=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetEvCalMuestroGrPlanta")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetEvCalMuestroGrPlanta",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Detalle Ev. Calidad Muestreo  Planta -Granada '
		verbose_name_plural = 'Detalle Ev. Calidad Muestreo  Planta -Granada'

	def __str__(self):
		return "%s-%s" % (self.num_calibre, self.fecha_hora_creacion)

