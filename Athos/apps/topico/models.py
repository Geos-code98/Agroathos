
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import LugarAthos
from apps.menu.models import DatosEmpresa


# Create your models here.


class MotivosJustificacion(models.Model):
	
	motivo= models.CharField("Motivo", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Motivo Justificacion Topico'
		verbose_name_plural = 'Motivo Justificacion Topico'

	def __str__(self):
		return "%s" % ( self.motivo)



class RespuestaTopico(models.Model):
    
    desc= models.CharField("Respuesta", max_length=50,null=True, blank=True)
    
    class Meta:
        verbose_name = 'Respuesta Topico'
        verbose_name_plural = 'Respuesta Topico'

    def __str__(self):
        return "%s" % ( self.desc)

class TipoDolor(models.Model):
    
    desc= models.CharField("Dolor", max_length=50,null=True, blank=True)
    
    class Meta:
        verbose_name = 'TIPO DE DOLOR'
        verbose_name_plural = 'TIPO DE DOLOR'

    def __str__(self):
        return "%s" % ( self.desc)



class DetalleMotivosJustificacion(models.Model):
	
	detalle= models.CharField("Detalle", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Detalle Motivo Justificacion Topico'
		verbose_name_plural = 'Detalle Motivo Justificacion Topico'

	def __str__(self):
		return "%s" % ( self.detalle)



class JustificacionTopico(models.Model):
	
	dni= models.CharField("Leer Dni", max_length=50,null=True, blank=True)
	fecha_justificacion= models.DateField("Fecha Justificacion",null=True, blank=True)
	fecha_inicio= models.DateField("Fecha Inicio",null=True, blank=True)
	fecha_fin= models.DateField("Fecha Fin",null=True, blank=True)

	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoJustificacionZona")
	anexo_lugar=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoJustificacionLugar")
	
	anexo_motivo = models.ForeignKey(MotivosJustificacion, on_delete=models.CASCADE, related_name="AnexoJustificacionZona")
	anexo_detallemotivo=models.ForeignKey(DetalleMotivosJustificacion, on_delete=models.CASCADE, related_name="AnexoDetalleJustificacionZona",null=True, blank=True)
	adjunta= models.CharField("Adjunta", max_length=250,null=True, blank=True)
	justificacion= models.CharField("Justificacion", max_length=250,null=True, blank=True)
	imagen_justificacion1=models.ImageField(upload_to="foto_topico" ,blank=True, null=True)
	imagen_justificacion2=models.ImageField(upload_to="foto_topico" ,blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionJustificacionTopico")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModJustificacionTopico",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Justificacion Topico'
		verbose_name_plural = 'Justificacion Topico'

	def __str__(self):
		return "%s" % ( self.dni)


class FichaEpidemiologica(models.Model):
    anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoFichaEpiZona")
    anexo_lugar=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoFichaEpiLugar")
    dni= models.CharField("Leer Dni", max_length=50,null=True, blank=True)
    fecha_evaluacion= models.DateField("Fecha Evaluacion",null=True, blank=True)
    nombre_completo= models.CharField("Nombre Completo", max_length=250,null=True, blank=True)
    edad=models.IntegerField(blank=True, null=True)
    genero=models.CharField("Genero", max_length=50, blank=True, null=True)
    anexo_preg1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta1")
    anexo_preg2_1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_1")
    anexo_preg2_2 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_2")
    anexo_preg2_3 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_3")
    anexo_preg2_4 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_4")
    anexo_preg2_5 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_5")
    anexo_preg2_6 = models.ForeignKey(TipoDolor, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_6")
    anexo_preg2_7 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta2_7")
    fecha_sintomas= models.DateField("Fecha Sintomas",null=True, blank=True)
    anexo_preg4_1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta4_1")
    lugar_visita= models.CharField("Lugar Visita", max_length=250,null=True, blank=True)
    anexo_preg5_1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta5_1")
    anexo_preg6_1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_1")
    trimestre_embarazo=models.IntegerField(blank=True, null=True)
    anexo_preg6_2 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_2")
    anexo_preg6_3 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_3")
    anexo_preg6_4 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_4")
    anexo_preg6_5 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_5")
    anexo_preg6_6 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_6")
    anexo_preg6_7 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_7")
    anexo_preg6_8 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_8")
    anexo_preg6_9 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_9")
    anexo_preg6_10 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichaepiRpta6_10")
    

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Usercreacionfichaepiuser")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModfichaepiuser",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    

    class Meta:
        verbose_name = 'Ficha epidemiologica  Topico'
        verbose_name_plural = 'Ficha epidemiologica  Topico'

    def __str__(self):
        return "%s" % ( self.dni)



class FichaSintomatologiaCovid(models.Model):
    anexo_empresa = models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoFichaSCovEmpresa")
    dni= models.CharField("Leer Dni", max_length=50,null=True, blank=True)
    nombre_completo= models.CharField("Nombre Completo", max_length=250,null=True, blank=True)
    area_trabajo=models.CharField("Area Trabajo", max_length=50, blank=True, null=True)
    direccion=models.CharField("Direccion", max_length=50, blank=True, null=True)
    celular=models.IntegerField(blank=True, null=True)
    
    anexo_preg1 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta1")
    anexo_preg2 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta2_1")
    anexo_preg3 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta2_2")
    anexo_preg4 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta2_3")
    anexo_preg5 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta2_4")
    anexo_preg6 = models.ForeignKey(RespuestaTopico, on_delete=models.CASCADE, related_name="AnexoFichascovidRpta2_5")


    fecha= models.DateField("Fecha",null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Usercreacionfichascovuser")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModfichascovuser",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    

    class Meta:
        verbose_name = 'Ficha sintomatologica  Topico'
        verbose_name_plural = 'Ficha sintomatologica  Topico'

    def __str__(self):
        return "%s" % ( self.dni)


class MotivoAmonestacion(models.Model):
	
	detalle= models.CharField("Detalle", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Motivo Amonestacion- Topico'
		verbose_name_plural = 'Motivo Amonestacion- Topico'

	def __str__(self):
		return "%s" % ( self.detalle)


class AmonestacionTopico(models.Model):
	
	amonestado= models.CharField("Amonestado", max_length=100,null=True, blank=True)
	sap=models.IntegerField(blank=True, null=True)
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoAmonestacionZona")
	anexo_lugar=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoAmonestacionLugar")
	amonestador= models.CharField("Amonestador", max_length=100,null=True, blank=True)
	asunto= models.CharField("Asunto", max_length=250,null=True, blank=True)
	fecha_actual= models.DateField("Fecha Actual",null=True, blank=True)
	anexo_motivo = models.ForeignKey(MotivoAmonestacion, on_delete=models.CASCADE, related_name="AnexoMotivoAmonestacion")
	motivo= models.CharField("Motivacion", max_length=250,null=True, blank=True)
	fecha_amonestacion= models.DateField("Fecha Amonestacion",null=True, blank=True)
	fecha_inicio= models.DateField("Fecha Inicio",null=True, blank=True)
	fecha_fin= models.DateField("Fecha Fin",null=True, blank=True)
	articulos= models.CharField("Articulos", max_length=250,null=True, blank=True)
	antecedentes= models.CharField("Articulos", max_length=250,null=True, blank=True)
	otros= models.CharField("Otros", max_length=250,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionAmonestacionTopico")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModAmonestacionTopico",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Amonestacion Topico'
		verbose_name_plural = 'Amonestacion Topico'

	def __str__(self):
		return "%s" % ( self.dni)