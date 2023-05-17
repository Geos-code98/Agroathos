
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import cultivo
from apps.menu.models import fundo
from apps.menu.models import ProgramaProduccion
from apps.maestras.models import LaboresPlantaAthos
from apps.menu.models import ConfigurarDia
from apps.menu.models import AreaPlanta


# Create your models here.
class PersonalAthos(models.Model):
	cod_trab = models.CharField( max_length=10, null=True, blank=True)
	tipdoc = models.CharField( max_length=5, null=True, blank=True)
	NroDoc = models.CharField( max_length=10, null=True, blank=True)
	ApellidoPat = models.CharField( max_length=30, null=True, blank=True)
	ApellidoMat = models.CharField( max_length=30, null=True, blank=True)
	Nombres = models.CharField( max_length=30, null=True, blank=True)
	FecNac = models.CharField( max_length=10, null=True, blank=True)
	PaisNacionalidad = models.CharField( max_length=20, null=True, blank=True)
	Nacionalidad = models.CharField( max_length=20, null=True, blank=True)
	Sexo = models.CharField( max_length=10, null=True, blank=True)
	EstadoCivil = models.CharField( max_length=10, null=True, blank=True)
	Posicion = models.CharField( max_length=30, null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionPersonalAthos", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPersonalAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Personal  Athos'
		verbose_name_plural = 'Personal  Athos'

	def __str__(self):
		return "%s-%s-%s" % (self.ApellidoPat, self.ApellidoMat, self.Nombres)


class TipoDocumentos(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Tipo Documentos'
        verbose_name_plural = 'Tipo Documentos'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)

class EstadoCivil(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)

class GradoInstruccion(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Grado de Instruccion'
        verbose_name_plural = 'Grado de Instruccion'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)

class SelectorPareja(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Selector Parejas'
        verbose_name_plural = 'Selector Parejas'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)

class RespuestasRrhh(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Selector Respuestas SI/NO RRHH'
        verbose_name_plural = 'Selector Respuestas SI/NO RRHH'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)



class GeneroPersonas(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Genero Personas'
        verbose_name_plural = 'Genero Personas'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)

class AreaEmpresa(models.Model):
    
    desc = models.CharField( max_length=30, null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Area Empresa'
        verbose_name_plural = 'Area Empresas'

    def __str__(self):
        return "%s-%s" % (self.id, self.desc)


class IngresoPersonalAthos(models.Model):
    
    anexo_documentos = models.ForeignKey(TipoDocumentos, on_delete=models.CASCADE, related_name="AnexoIngresoTipoDoc", blank=True, null=True)
    nro_documento = models.CharField( max_length=15, null=True, blank=True)
    ApellidoPat = models.CharField( max_length=30, null=True, blank=True)
    ApellidoMat = models.CharField( max_length=30, null=True, blank=True)
    Nombres = models.CharField( max_length=30, null=True, blank=True)
    anexo_genero = models.ForeignKey(GeneroPersonas, on_delete=models.CASCADE, related_name="AnexoIngresoGenero", blank=True, null=True)
    FecNac = models.CharField( max_length=10, null=True, blank=True)
    fecha_nacimiento=models.DateField(null=True, blank=True)

    observacion=models.CharField( max_length=200, null=True, blank=True)

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionIngresoPersonalAthos", blank=True, null=True)
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionIngresoPersonalAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Ingreso Personal  Athos'
        verbose_name_plural = 'Ingreso Personal  Athos'

    def __str__(self):
        return "%s-%s-%s-%s" % (self.nro_documento,self.ApellidoPat, self.ApellidoMat, self.Nombres)


class FiltroPersonalAthos(models.Model):
    
    apellidos = models.CharField( max_length=30, null=True, blank=True)
    nombres = models.CharField( max_length=30, null=True, blank=True)
    nombre_completo= models.CharField( max_length=50, null=True, blank=True)
    nro_documento = models.CharField( max_length=15, null=True, blank=True)
    sancion = models.CharField( max_length=15, null=True, blank=True)
    motivo= models.CharField( max_length=50, null=True, blank=True)
    empresa=models.CharField( max_length=50, null=True, blank=True)
    sede = models.CharField( max_length=15, null=True, blank=True)
    descripcion_falta=models.CharField( max_length=100, null=True, blank=True)
    anio_falta=models.IntegerField(null=True, blank=True)


    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionFiltroPersonalAthos", blank=True, null=True)
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionFiltroPersonalAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = ' Personal Filtro-  Athos'
        verbose_name_plural = ' Personal Filtro-  Athos'

    def __str__(self):
        return "%s-%s-%s" % (self.nro_documento,self.apellidos, self.nombres, self.sancion)


class FichaPersonalAthos(models.Model):
    
    
    nro_documento = models.CharField( max_length=15, null=True, blank=True)
    ApellidoPat = models.CharField( max_length=30, null=True, blank=True)
    ApellidoMat = models.CharField( max_length=30, null=True, blank=True)
    Nombres = models.CharField( max_length=30, null=True, blank=True)
    fecha_nacimiento=models.DateField(null=True, blank=True)
    anexo_estadocivil=models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, related_name="AnexoFichaEstadoCivil", blank=True, null=True)
    anexo_grado=models.ForeignKey(GradoInstruccion, on_delete=models.CASCADE, related_name="AnexoFichaGradoInstruccion", blank=True, null=True)
    celular=models.BigIntegerField(null=True, blank=True)
    celular_emergencia=models.BigIntegerField(null=True, blank=True)
    
    anexo_pareja=models.ForeignKey(SelectorPareja, on_delete=models.CASCADE, related_name="AnexoFichaSelectorPareja", blank=True, null=True)
    nombre_pareja = models.CharField( max_length=100, null=True, blank=True)
    direccion_pareja = models.CharField( max_length=100, null=True, blank=True)
    celular_pareja=models.BigIntegerField(null=True, blank=True)
    cant_hijos=models.IntegerField(null=True, blank=True)

    empresa_experiencia=models.CharField( max_length=50, null=True, blank=True)
    tiempo_experiencia=models.IntegerField(null=True, blank=True)
    cargo_experiencia=models.CharField( max_length=50, null=True, blank=True)

    lugar_nacimiento = models.CharField( max_length=50, null=True, blank=True)
    direccion = models.CharField( max_length=200, null=True, blank=True)
    observacion=models.CharField( max_length=200, null=True, blank=True)

    anexo_antecedentes=models.ForeignKey(RespuestasRrhh, on_delete=models.CASCADE, related_name="AnexoFichaRespuesta", blank=True, null=True)
    antecedente=models.CharField( max_length=100, null=True, blank=True)

    anexo_alcohol=models.ForeignKey(RespuestasRrhh, on_delete=models.CASCADE, related_name="AnexoFichaRespuestaAlcohol", blank=True, null=True)
    anexo_tabaco=models.ForeignKey(RespuestasRrhh, on_delete=models.CASCADE, related_name="AnexoFichaRespuestaTabaco", blank=True, null=True)
    anexo_farmaco=models.ForeignKey(RespuestasRrhh, on_delete=models.CASCADE, related_name="AnexoFichaRespuestaFarmaco", blank=True, null=True)
    anexo_sustancia=models.ForeignKey(RespuestasRrhh, on_delete=models.CASCADE, related_name="AnexoFichaRespuestaSustancia", blank=True, null=True)
    otra_sustancia=models.CharField( max_length=100, null=True, blank=True)

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionFichaPersonalAthos", blank=True, null=True)
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionFichaPersonalAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Ficha Personal  Athos'
        verbose_name_plural = 'Ficha Personal  Athos'

    def __str__(self):
        return "%s-%s-%s-%s" % (self.nro_documento,self.ApellidoPat, self.ApellidoMat, self.Nombres)




class RequerimientoPersonal(models.Model):
    anio = models.IntegerField(null=True, blank=True)
    semana = models.IntegerField( null=True, blank=True)
    anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoReqPersonalAthos", blank=True, null=True)
    anexo_fundo = models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoReqPersonalAthos", blank=True, null=True)
    anexo_area = models.ForeignKey(AreaEmpresa, on_delete=models.CASCADE, related_name="AnexoAreaEmpReqPersonalAthos", blank=True, null=True)
        
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionReqPersonalAthos", blank=True, null=True)
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionReqPersonalAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Requerimiento Personal  Athos'
        verbose_name_plural = 'Requerimiento Personal Athos'

    def __str__(self):
        return "%s-%s-%s" % (self.anio, self.semana, self.usuario_creacion)

class DetalleRequerimientoPersonal(models.Model):
    
    anexo_detalle = models.ForeignKey(RequerimientoPersonal, on_delete=models.CASCADE, related_name="AnexoDetRedPersonalAthos", blank=True, null=True)
    labor=models.CharField( max_length=100, null=True, blank=True)
    tiempo_contratacion = models.IntegerField(null=True, blank=True)
    rendimiento_esperado = models.IntegerField( null=True, blank=True)
    cantidad = models.IntegerField( null=True, blank=True)
    cantidad_aprobada = models.IntegerField( null=True, blank=True)
        
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionDetReqPersonalAthos", blank=True, null=True)
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionDetReqPersonalAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Detalle Requerimiento Personal  Athos'
        verbose_name_plural = 'Detalle Requerimiento Personal Athos'

    def __str__(self):
        return "%s-%s-%s" % (self.anexo_detalle, self.labor, self.usuario_creacion)



#PROYECCION SEMANAL MO
class ProyeccionSemanalPersonal(models.Model):
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoProyeccionSemanalPersonal",null=True, blank=True)
    anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoProyeccionSemanalPersonal", blank=True, null=True)
    anio= models.IntegerField(null=True, blank=True)
    semana= models.IntegerField(null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProyeccionSemanalPersonal")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProyeccionSemanalPersonal",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Proyeccion Semanal Personal'
        verbose_name_plural = 'Proyeccion Semanal Personal'

    def __str__(self):
        return "%s-%s" % ( self.anexo_fundo,self.anio)

class DetalleProyeccionSemanalPersonal(models.Model):
    anexo_detalle = models.ForeignKey(ProyeccionSemanalPersonal, on_delete=models.CASCADE, related_name="AnexoDetProyeccionSemanalPersonal")
    anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPepProyeccionSemanalPersonal",null=True, blank=True)
    anexo_labor= models.ForeignKey(LaboresPlantaAthos, on_delete=models.CASCADE, related_name="AnexoLaborProyeccionSemanalPersonal",null=True, blank=True)
    
    lunes_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    lunes_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    martes_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    martes_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    miercoles_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    miercoles_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    jueves_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    jueves_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    viernes_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    viernes_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    sabado_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    sabado_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    domingo_cantidad=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    domingo_avance=models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleProyeccionSemanalPersonal")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleProyeccionSemanalPersonal",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Detalle Proyeccion Semanal Personal'
        verbose_name_plural = 'Detalle Proyeccion Semanal Personal'

    def __str__(self):
        return "%s-%s" % (self.anexo_detalle.anexo_zona ,self.anexo_pep)

#PRODUCTIVIDAD PLANTA
class ProductividadPlanta(models.Model):
    zona=models.CharField(max_length=150, null=True, blank=True)
    nave=models.CharField(max_length=100, null=True, blank=True)
    cultivo=models.CharField(max_length=100, null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProduccionPlanta")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProduccionPlanta",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Produccion Planta'
        verbose_name_plural = 'Produccion Planta'

    def __str__(self):
        return "%s-%s-%s" % ( self.zona,self.nave,self.cultivo)

class DetalleProductividadPlanta(models.Model):
    anexo_detalle = models.ForeignKey(ProductividadPlanta, on_delete=models.CASCADE, related_name="AnexoDetProductividadPlanta")
    qr=models.CharField(max_length=100, null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleProductividadPlanta")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleProductividadPlanta",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Detalle Productividad Planta'
        verbose_name_plural = 'Detalle Productividad Planta'

    def __str__(self):
        return "%s - %s - %s - %s - %s" % (self.fecha_hora_creacion, self.usuario_creacion, self.anexo_detalle.zona, self.anexo_detalle.cultivo, self.qr)

#PRODUCTIVIDAD PLANTA ASISTENCIA
class LineaProductividadPlanta(models.Model):
    linea = models.CharField("Linea", max_length=40, null=True, blank=False)
    class Meta:
        verbose_name = 'Linea Productividad Planta'
        verbose_name_plural = 'Linea Productividad Planta'

    def __str__(self):
        return "%s" % (self.linea)

class MesaProductividadPlanta(models.Model):
    mesa = models.CharField("Mesa", max_length=40, null=True, blank=False)
    class Meta:
        verbose_name = 'Mesa Productividad Planta'
        verbose_name_plural = 'Mesa Productividad Planta'

    def __str__(self):
        return "%s" % (self.mesa)

class ProductividadPlantaAsistencia(models.Model):
    anexo_detalle = models.ForeignKey(ProductividadPlanta, on_delete=models.CASCADE, related_name="AnexoProducPlProductividadPlantaAsistencia", blank=True, null=True)
    anexo_fecha = models.ForeignKey(ConfigurarDia, on_delete=models.CASCADE, related_name="FechaProductividadPlantaAsistencia", blank=True, null=True)
    anexo_linea = models.ForeignKey(LineaProductividadPlanta, on_delete=models.CASCADE, related_name="LineaProductividadPlantaAsistencia", blank=True, null=True)
    anexo_actividad_labor = models.ForeignKey(AreaPlanta, on_delete=models.CASCADE, related_name="ActividadLaborProductividadPlantaAsistencia", blank=True, null=True)
    anexo_mesa = models.ForeignKey(MesaProductividadPlanta, on_delete=models.CASCADE, related_name="MesaProductividadPlantaAsistencia", blank=True, null=True)

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProduccionPlantaAsistencia")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProduccionPlantaAsistencia",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

    class Meta:
        verbose_name = 'Productividad Planta Asistencia'
        verbose_name_plural = 'Productividad Planta Asistencia'

    def __str__(self):
        return "%s-%s-%s" % (self.anexo_fecha.fecha,self.anexo_actividad_labor,self.anexo_mesa)

class DetalleProductividadPlantaAsistencia(models.Model):
    anexo_detalle = models.ForeignKey(ProductividadPlantaAsistencia, on_delete=models.CASCADE, related_name="IdDetalleProductividadPlantaAsistencia", blank=True, null=True)
    qr = models.CharField("QR", max_length=100, null=True, blank=False)

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="DetUsercreacionProduccionPlantaAsistencia")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="DetUserModProduccionPlantaAsistencia",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

    class Meta:
        verbose_name = 'Detalle Productividad Planta Asistencia'
        verbose_name_plural = 'Detalle Productividad Planta Asistencia'

    def __str__(self):
        return "%s-%s" % (self.anexo_detalle.id, self.qr)

