from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import CentrosAthos
from apps.menu.models import cultivo
from apps.menu.models import ejezona
from apps.menu.models import fundo
from apps.menu.models import Estado
# Create your models here.

class PresentacionesAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroPresentacionesG",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoPresentacionesG",null=True, blank=True)
	presentaciong= models.CharField("PresentacionG", max_length=30)
	presentacion= models.CharField("Presentacion", max_length=30)
	pesodestino= models.IntegerField(null=True, blank=True)
	pesomin= models.IntegerField(null=True, blank=True)
	pesomax= models.IntegerField(null=True, blank=True)
	por_pesomin= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	por_pesomax= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	cliente=models.CharField("Cliente", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMPresentacion")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMPresentacion",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Presentaciones G Athos'
		verbose_name_plural = '	Presentaciones G Athos'

	def __str__(self):
		return "%s" % ( self.presentaciong)


class ClientesAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroClientes",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoClientes",null=True, blank=True)
	cliente= models.CharField("Clientes", max_length=30)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMClientes")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMClientes",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Clientes Athos'
		verbose_name_plural = 'Clientes Athos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_centro,self.cliente)

#Presentaciones
class MaestraPresentacionesAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroPresentacionesA",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoPresentacionesA",null=True, blank=True)
	codigo= models.CharField("Codigo", max_length=30,null=True, blank=True)
	descripcion= models.CharField("Descripcion", max_length=100,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMPresentacionesAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMPresentacionesAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Presentaciones Athos'
		verbose_name_plural = 'Presentaciones Athos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_centro,self.descripcion)

class CalibresAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroCalibres",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoCalibres",null=True, blank=True)
	descripcion= models.CharField("Descripcion Calibre", max_length=100,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionCalibresAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCalibresAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Calibres Athos'
		verbose_name_plural = 'Calibres Athos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_centro,self.descripcion)


class AcomodoAthos(models.Model):
	
	selector= models.CharField("Selector", max_length=30)
	
	
	
	class Meta:
		verbose_name = 'Acomodo Athos'
		verbose_name_plural = 'Acomodo Athos'

	def __str__(self):
		return "%s" % ( self.selector)

class LineaEmpaqueAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCentroLinea",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoLinea",null=True, blank=True)
	descripcion= models.CharField("Descripcion Linea Empaque", max_length=100,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionLineaAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModLineaAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Linea Empaque Athos'
		verbose_name_plural = 'Linea Empaque Athos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_centro,self.descripcion)


class CartillasAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoCartillasCalibres",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoCartillas",null=True, blank=True)
	cartilla= models.CharField("Cartilla", max_length=100,null=True, blank=True)
	codigo= models.CharField("Codigo", max_length=100,null=True, blank=True)
	grupo= models.CharField("grupo", max_length=100,null=True, blank=True)
	subgrupo= models.CharField("subgrupo", max_length=100,null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionCartillasAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModCartillasAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Cartillas Athos'
		verbose_name_plural = 'Cartillas Athos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_centro,self.cartilla)


class LaboresAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoLaboresCalibres",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoLabores",null=True, blank=True)
	tipolabor= models.CharField("Tipo Labor", max_length=100,null=True, blank=True)
	descripcion= models.CharField("Descripcion Labor", max_length=100,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionLaboresAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModLaboresAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Labores Athos'
		verbose_name_plural = 'Labores Athos'

	def __str__(self):
		return "%s-%s" % ( self.tipolabor,self.descripcion)

class DescripcionLaboresAthos(models.Model):
	anexo_centro = models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoLDescaboresCalibres",null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoLaboresDesc",null=True, blank=True)
	codigo_labor= models.CharField("Codigo Labor", max_length=100,null=True, blank=True)
	anexo_tipolabor= models.ForeignKey(LaboresAthos, on_delete=models.CASCADE, related_name="AnexoLaboresDescLabot",null=True, blank=True)
	descripcion_labor= models.CharField("Descripcion Labor", max_length=200,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDescLaboresAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDescLaboresAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Desc. Labores Athos'
		verbose_name_plural = 'Desc. Labores Athos'

	def __str__(self):
		return "%s-%s" % ( self.codigo_labor,self.anexo_tipolabor)

class TipoAuxiliarCampoAthos(models.Model):
    descripcion = models.CharField("Descripcion", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Tipo Auxiliar Actividades Athos"
        verbose_name_plural = "Tipo Auxiliar Actividades Athos"

    def __str__(self):
        return (self.descripcion)

class AuxiliaresCampoAthos(models.Model):
	anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoAuxiliaresZona",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoAuxiliarFundo",null=True, blank=True)
	auxiliar= models.CharField("Auxiliar Campo", max_length=100,null=True, blank=True)
	dni= models.CharField("DNI",max_length=11, null=True, blank=True)
	anexo_estado= models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoAuxiliarEstado",null=True, blank=True)
	anexo_tipo= models.ForeignKey(TipoAuxiliarCampoAthos, on_delete=models.CASCADE, related_name="AnexoTipoAuxiliar",null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionAuxiliarCampo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModAuxiliarCampo",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Auxiliar Campo Athos'
		verbose_name_plural = 'Auxiliar Campo Athos'

	def __str__(self):
		return "%s-%s" % ( self.auxiliar,self.anexo_estado)


class TanquesAthos(models.Model):
    anexo_zona = models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoTanquesZona1",null=True, blank=True)
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoTanqueFundo1",null=True, blank=True)
    numero_tanque= models.IntegerField(null=True, blank=True)
    capacidad= models.IntegerField(null=True, blank=True)
    fundo_tanque=models.CharField("Fundo - Tanque", max_length=100,null=True, blank=True, unique=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTanquesAthos1")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTanquesAthos1",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Tanques Athos'
        verbose_name_plural = 'Tanques Athos'

    def __str__(self):
        return "%s-%s" % (self.anexo_fundo.nom_fundo, self.numero_tanque)


class ActividadesAthos(models.Model):
    descripcion = models.CharField("Descripcion", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Actividades Athos"
        verbose_name_plural = "Actividades Athos"

    def __str__(self):
        return (self.descripcion)

class LaboresPlantaAthos(models.Model):
    codigo=models.CharField("Codigo", max_length=100,null=True, blank=True)
    anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoLaboresPlantaAthos",null=True, blank=True)
    anexo_proceso= models.ForeignKey(ActividadesAthos, on_delete=models.CASCADE, related_name="AnexoProcesoLaboresPlantaAthos",null=True, blank=True)
    labor= models.CharField("Labor", max_length=100,null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionLaboresPlantaAthos")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModLaboresPlantaAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Labores Planta Athos'
        verbose_name_plural = 'Labores Planta Athos'

    def __str__(self):
        return "%s-%s-%s" % (self.codigo, self.labor, self.anexo_cultivo)

class MaestraFundoCultivo(models.Model):
	fundo = models.CharField("Nombre Fundo", max_length=100,null=True, blank=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoMaestraCultivo", null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMaestraFundoCultivo")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMaestraFundoCultivo", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Maestra Fundo Cultivos'
		verbose_name_plural = 'Maestra Fundo Cultivos'
		
	def __str__(self):
		return "%s" % (self.fundo)