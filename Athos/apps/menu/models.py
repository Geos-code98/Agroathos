
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from apps.programaproduccion.models import Grupos
from apps.programaproduccion.models import SubGrupos
from apps.programaproduccion.models import Hitos
from apps.programaproduccion.models import SubHitos

from apps.programaproduccion.models import PlanSanidad
from apps.programaproduccion.models import PlanRiego
from apps.programaproduccion.models import PlanFertilizacion
from apps.programaproduccion.models import PlanManoObra
from apps.programaproduccion.models import AreaAthos
from apps.programaproduccion.models import TipoHitos

from apps.capacitaciones.models import RespuestaAprobacion
from apps.capacitaciones.models import RespuestaEncuesta





class menu_principal(models.Model):
	Eleccion_Estado = (
		("activo","activo"),
		("inactivo","inactivo"),
		("suspendido","suspendido"),
	)

	cod_menu = models.CharField("Codigo de menu", max_length=20)#varchar
	nom_menu = models.CharField("Nombre de menu", max_length=30)#varchar
	estado = models.CharField("Estado de Menu", choices=Eleccion_Estado, max_length=15)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'menu principal'
		verbose_name_plural = 'menu principal'

	def __str__(self):
		return "%s" % (self.nom_menu)


class item(models.Model):
	cod_item= models.CharField("Codigo de item", max_length=20)
	nom_item = models.CharField("Nombre de Item", max_length=30)#varchar
	estado = models.CharField("Estado de Item", choices=menu_principal.Eleccion_Estado, max_length=15)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion2")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion2",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	estado = models.CharField("Estado de Menu", choices=menu_principal.Eleccion_Estado, max_length=15)
	id_menu = models.ForeignKey(menu_principal, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'item'
		verbose_name_plural = 'items'

	def __str__(self):
		return "%s" % (self.nom_item)

class sub_item(models.Model):
	cod_subitem= models.CharField("Codigo de Sub-Item", max_length=20)
	nom_SubItem = models.CharField("Nombre de Sub-Item", max_length=30)#varchar
	estado = models.CharField("Estado de Sub-Item", choices=menu_principal.Eleccion_Estado, max_length=15)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion4")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion4",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	id_item=models.ForeignKey(item, on_delete=models.CASCADE)

	def __str__(self):
		return "%s-%s" % (self.cod_subitem, self.nom_SubItem)

class rol(models.Model):
	Eleccion_Estado = (
		("activo","activo"),
		("inactivo","inactivo"),
		("suspendido","suspendido"),
	)
	estado= None
	nombre_rol = models.CharField("Nombre de Rol",max_length=30, null= True, blank= True)
	estado = models.CharField("Estado Rol", choices=Eleccion_Estado, max_length=15, null=True,blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion7")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion7",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	def __str__(self):
		return "%s" % (self.nombre_rol)
	class Meta:
		verbose_name = 'rol'
		verbose_name_plural = 'roles'

class perfiles(models.Model):
	usuario=models.ForeignKey(User, on_delete=models.CASCADE)
	cod_user = models.CharField("Codigo de Usuario",max_length=30, null= True, blank= True)
	celular=models.CharField("Celular",max_length=30, blank=False, null= False)
	estado = models.CharField("Estado", choices=rol.Eleccion_Estado, max_length=15, null=True,blank=True)

	class Meta:
		verbose_name = 'perfil'
		verbose_name_plural = 'perfiles'

	def __str__(self):
		return "%s" % (self.usuario)

class Usuario_Roles(models.Model):
	Eleccion_Estado = (
		("activo","activo"),
		("inactivo","inactivo"),
		("suspendido","suspendido"),
	)
	estado= None
	id_rol=models.ForeignKey(rol, on_delete=models.CASCADE, related_name="roles")
	asignar_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="asignar_usuario")

	estado = models.CharField("Estado Rol", choices=Eleccion_Estado, max_length=15, null=True,blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion47",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion8",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Usuario-Rol'
		verbose_name_plural = 'Usuario-Roles'

	def __str__(self):
		return "%s-%s" % (self.id_rol.nombre_rol,self.asignar_usuario)


class Estado(models.Model):
	
	nom_estado=models.CharField("estado", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Estado'
		verbose_name_plural = 'Estados'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_estado)

class EstadoCampana(models.Model):
	
	nom_estado=models.CharField("Estado Campaña", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Estado Campaña'
		verbose_name_plural = 'Estados Campañas'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_estado)

class ejezona(models.Model):
	cod_zona_eje=models.CharField("Codigo Zona", max_length=15,null=True, blank=True)
	nombre_eje=models.CharField("Nombre del Eje", max_length=15)
	class Meta:
		verbose_name = 'Eje'
		verbose_name_plural = 'Ejes'

	def __str__(self):
		return "%s-%s" % (self.id,self.nombre_eje)


class fundo(models.Model):
	nom_fundo=None
	abreviatura=models.CharField("Abreviatura", max_length=10, blank=True, null=True, unique=True)
	nom_fundo=models.CharField("Nombre de Fundo",max_length=30,blank=False, null=False, unique=True)
	nom_zona=models.CharField("Nombre de la zona", max_length=30, blank=True, null=True)
	zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="ejezona", null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado5", null=True)
	
	empresa=models.CharField("Empresa", max_length=50, blank=True, null=True)
	responsable=models.CharField("Responsable", max_length=50, blank=True, null=True)


	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion9")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	class Meta:
		verbose_name = 'Fundo'
		verbose_name_plural = 'Fundos'

	def __str__(self):
		return "%s-%s" % (self.id, self.nom_fundo)

class modulo(models.Model):
	nombremodulo=models.CharField("Modulo",max_length=30,blank=False, null=False)
	idfundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="fundo1", null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado9", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion21")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	class Meta:
		verbose_name = 'Modulo'
		verbose_name_plural = 'Modulos'

	def __str__(self):
		return "%s-%s" % (self.idfundo.nom_fundo, self.nombremodulo)

class tiposuelo(models.Model):
	suelo=models.CharField("Suelo",max_length=30,blank=True, null=True)
	
	class Meta:
		verbose_name = 'Tipo Suelo'
		verbose_name_plural = 'Tipo Suelo'

	def __str__(self):
		return "%s" % (self.suelo)

class lote(models.Model):
	mod=models.ForeignKey(modulo, on_delete=models.CASCADE, related_name="fundo", null=True)
	nom_lote=models.CharField("Nombre del lote",max_length=30,blank=False, null=False)
	longitud=models.CharField("Longitud",max_length=30,blank=True, null=True)
	latitud=models.CharField("Latitud",max_length=30,blank=True, null=True)
	cod_alterno1 = models.CharField("Codigo Alterno 1", max_length=30, blank=True, null=True)
	cod_alterno2 = models.CharField("Codigo Alterno 2", max_length=30, blank=True, null=True)
	
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado7", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion8")
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion20")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)

	class Meta:
		verbose_name = 'Lote'
		verbose_name_plural = 'Lotes'

	def __str__(self):
		return "%s-%s" % ( self.nom_lote, self.mod)

class cultivo(models.Model):
	
	nom_cultivo= models.CharField("Nombre del cultivo",max_length=30,blank=False, null=False, unique=True)
	abreviatura_cultivo=models.CharField("Abreviatura Cultivo",max_length=30,blank=True, null=True, unique=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado1", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion10")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	class Meta:
		verbose_name = 'cultivo'
		verbose_name_plural = 'cultivos'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_cultivo)


class variedad(models.Model):
	nom_variedad= models.CharField("Nombre de Variedad",max_length=30,blank=False, null=False)
	abreviatura_variedad=models.CharField("Abreviatura de Variedad",max_length=30,blank=True, null=True, unique=True)
	cul = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="cutivo1")
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado2" ,null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion11")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	tipo_fruta= models.CharField("Tipo Fruta",max_length=30,blank=True, null=True)
	class Meta:
		verbose_name = 'variedad'
		verbose_name_plural = 'variedades'
		ordering = ['cul']

	def __str__(self):
		return "%s-%s" % (self.cul.nom_cultivo, self.nom_variedad)


class fenologia(models.Model):
	fecha_hora_creacion=None
	id_cultivo=models.ForeignKey(cultivo,on_delete=models.CASCADE, related_name="cultivo", null=True)
	indice=models.CharField("Indice",max_length=30,blank=True, null=True)
	nom_feno=models.CharField("Fenología",max_length=30,blank=False, null=False)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado3", null= True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion12", default="")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, null=True)
	class Meta:
		verbose_name = 'Fenología'
		verbose_name_plural = 'Fenologías'

	def __str__(self):
		return "%s-%s" % (self.id_cultivo.nom_cultivo,self.nom_feno)



class campanas(models.Model):
	camp=models.CharField("Campaña",max_length=30,blank=False, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion22")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, null= True)
	class Meta:
		verbose_name = 'Campaña'
		verbose_name_plural = 'Campañas'

	def __str__(self):
		return "%s" % (self.camp)

class siembra(models.Model):
	boolsiembra=models.CharField("Siembra",max_length=30,blank=False, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserCreacionSiembra")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, null= True)
	class Meta:
		verbose_name = 'Siembra'
		verbose_name_plural = 'Siembras'

	def __str__(self):
		return "%s" % (self.boolsiembra)


class ProgramaProduccionManager(models.Manager):

    def get_by_fundo(self, variablefundo):
        return self.filter(anexo_fundo=variablefundo).filter(estado_id=1)

class ProgramaProduccion(models.Model):

	anexo_fundo=models.ForeignKey(fundo,on_delete=models.CASCADE, related_name="fundo3", null=True)
	anexo_modulo=models.ForeignKey(modulo,on_delete=models.CASCADE, related_name="lote1", null= True)
	anexo_lote=models.ForeignKey(lote,on_delete=models.CASCADE, related_name="lote1")
	anexo_campana=models.ForeignKey(campanas,on_delete=models.CASCADE, related_name="campanas1")
	ano_campana=models.CharField("Año Campaña", max_length=10, null=True, blank=True)
	organos_campana=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	anexo_variedad=models.ForeignKey(variedad,on_delete=models.CASCADE, related_name="variedad1")
	area=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	inicio_campana=models.DateField("Inicio de Campaña", max_length=30, blank=True, null=True)
	cierre_campana=models.DateField("Cierre de Campaña", max_length=30, blank=True, null=True)
	anio_cosecha=models.CharField("Año Cosecha", max_length=10, null=True, blank=True)
	var_pep=models.CharField("Variedad_PEP", max_length=20, null=True, blank=True)
	anexo_siembra=models.ForeignKey(siembra,on_delete=models.CASCADE, related_name="AnexoSiembra" , null=True, blank=True)
	etapa=models.CharField("Etapa", max_length=10, null=True, blank=True)
	responsable=models.CharField("Responsable", max_length=50, null=True, blank=True)
	estado = models.ForeignKey(EstadoCampana, on_delete=models.CASCADE, related_name="estado10", null= True)
	
	inicio_cosecha_clp = models.DateField("Fecha cosecha CLP", null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionPP", null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	objects = ProgramaProduccionManager()

	class Meta:
		verbose_name = 'Programa Produccion'
		verbose_name_plural = 'Programas de Produccion'
		ordering = ['anexo_variedad']

	def __str__(self):
		#return "%s%s%s" % (self.anexo_fundo.abreviatura,self.anexo_modulo.nombremodulo,self.anexo_lote.nom_lote)
		return "%s%s%s-%s" % (self.anexo_fundo.abreviatura,self.anexo_modulo.nombremodulo,self.anexo_lote.nom_lote,self.ano_campana)

class ProgramaProduccionFeno(models.Model):
	programa_produccion=models.ForeignKey(ProgramaProduccion,on_delete=models.CASCADE, related_name="Programa")
	indice=models.CharField("Indice",max_length=30,blank=True, null=True)
	anexo_fenologia=models.ForeignKey(fenologia,on_delete=models.CASCADE, related_name="fenologia1")
	fecha=models.DateField("Fecha y Hora de Creación", null=True)
	
	class Meta:
		verbose_name = 'Programa Produccion -Fases Fenologicas'
		verbose_name_plural = 'Programa Produccion -Fases Fenologicas'

	def __str__(self):
		return "%s-%s-%s" % ( self.programa_produccion,self.anexo_fenologia.nom_feno,self.fecha)


class VariableAgronomica(models.Model):
	anexo_cultivo=models.ForeignKey(cultivo,on_delete=models.CASCADE, related_name="fen", null=True, blank=True)
	Variable=models.CharField("Variable Agronomica", max_length=30, blank=True, null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado39", null= True)
	class Meta:
		verbose_name = 'Variable Agronomica'
		verbose_name_plural = 'Variable Agronomica'

	def __str__(self):
		return "%s-%s" % (self.anexo_cultivo, self.Variable)



class HitosFenologicos(models.Model):
	anexo_detalle=models.ForeignKey(ProgramaProduccionFeno,on_delete=models.CASCADE, related_name="AnexoHitosFenologicos")
	semana=models.IntegerField(blank=True, null=True)
	anexo_grupo=models.ForeignKey(Grupos,on_delete=models.CASCADE, related_name="AnexoHitosFenologicosGrupos",null=True, blank=True)
	anexo_subgrupo=models.ForeignKey(SubGrupos,on_delete=models.CASCADE, related_name="AnexoHitosFenologicosSubGrupos",null=True, blank=True)
	anexo_hito=models.ForeignKey(Hitos,on_delete=models.CASCADE, related_name="AnexoHitosFenologicosHitos",null=True, blank=True)
	anexo_subhito=models.ForeignKey(SubHitos,on_delete=models.CASCADE, related_name="AnexoSubHitosFenologicos",null=True, blank=True)
	anexo_area=models.ForeignKey(AreaAthos,on_delete=models.CASCADE, related_name="AnexoAreaAthosHF",null=True, blank=True)
	anexo_tipo=models.ForeignKey(TipoHitos,on_delete=models.CASCADE, related_name="AnexoTipoAthosHF",null=True, blank=True)
	
	valor=models.DecimalField(max_digits=9, decimal_places=4,blank=True, null=True)
	valor_max=models.DecimalField(max_digits=9, decimal_places=4,blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionHitosFen")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModHitosFen",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'PP FENO-Hitos Fenológico'
		verbose_name_plural = 'PP FENO-Hitos Fenológico'

	def __str__(self):
		return "%s-%s-%s-%s-%s" % ( self.anexo_detalle,self.anexo_detalle.programa_produccion.anexo_campana,self.anexo_detalle.programa_produccion.estado, self.semana, self.anexo_subhito)





class TurnoProgramaProduccion(models.Model):
	anexo_programa=models.ForeignKey(ProgramaProduccion,on_delete=models.CASCADE, related_name="AnexoProgramaTurnoPP")
	anexo_suelo=models.ForeignKey(tiposuelo,on_delete=models.CASCADE, related_name="AnexoSueloTurnoPP",blank=True, null=True)
	turno=models.CharField("Turno",max_length=30,blank=True, null=True)
	hectareaje=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	densidad=models.IntegerField(blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado,on_delete=models.CASCADE, related_name="AnexoTurnoPPEstado")
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionTurnoPP")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModTurnoPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Turno-Programa de Produccion'
		verbose_name_plural = 'Turno-Programa de Produccion'

	def __str__(self):
		return "%s-%s" % ( self.anexo_programa,self.turno)








class Flujo(models.Model):
	nom_flujo=models.CharField("Nombre de Flujo",max_length=30,blank=False, null=False)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion42")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacio42",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	
	class Meta:
		verbose_name = 'Flujo'
		verbose_name_plural = 'Flujos'

	def __str__(self):
		return "%s-%s" % ( self.id,self.nom_flujo)

class Acciones(models.Model):
	nom_accion= models.CharField("Acción", max_length=30, blank=False, null=False)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion43")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion43",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	
	class Meta:
		verbose_name = 'Acción'
		verbose_name_plural = 'Acciones'

	def __str__(self):
		return "%s-%s" % ( self.id,self.nom_accion)

class TipoRespuesta(models.Model):
	Tipo_Respuesta=models.CharField("Respuesta",max_length=30,blank=False, null=False)
		
	class Meta:
		verbose_name = 'Respuesta'
		verbose_name_plural = 'Respuestas'

	def __str__(self):
		return "%s-%s" % ( self.id,self.Tipo_Respuesta)	


class Procesos(models.Model):
	idflujo=models.ForeignKey(Flujo, on_delete=models.CASCADE, related_name="flujos3")
	accion_inicio=models.ForeignKey(Acciones, on_delete=models.CASCADE, related_name="acciones1")
	usuario_asignacion=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion44",null=True, blank=True)
	respuesta=models.ForeignKey(TipoRespuesta, on_delete=models.CASCADE, related_name="TipoRespuesta1",null=True, blank=True)
	accion_siguiente=models.ForeignKey(Acciones, on_delete=models.CASCADE, related_name="TipoRespuesta1",null=False, blank=False)
	tiempo_atencion=models.DecimalField(max_digits=5, decimal_places=2)
	url=models.CharField("URL DE PROCEDIMIENTO",max_length=30,blank=False, null=False)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion40")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion40",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Proceso'
		verbose_name_plural = 'Procesos'

	def __str__(self):
		return "%s-%s-%s" % ( self.id,self.accion_inicio.nom_accion, self.accion_siguiente.nom_accion)	


class solicitud(models.Model):
	cod_solicitud=models.CharField("Código de solicitud", max_length=30,blank= False, null= False)
	idflujo=models.ForeignKey(Flujo, on_delete=models.CASCADE, related_name="flujos2")
	id_accion=models.ForeignKey(Acciones, on_delete=models.CASCADE, related_name="Acciones2")
	descripcion=models.TextField("Código de solicitud", max_length=300,blank= False, null= False)
	respuesta_solicitud=models.ForeignKey(TipoRespuesta, on_delete=models.CASCADE, related_name="TipoRespuesta2",null=False, blank=False)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion45")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion45",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Solicitud'
		verbose_name_plural = 'Solicitudes'

	def __str__(self):
		return "%s-%s-%s" % ( self.cod_solicitud,self.idflujo.nom_flujo, self.id_accion.nom_accion)		


class elementoPEP(models.Model):
	programa_produccion=models.ForeignKey(ProgramaProduccion,on_delete=models.CASCADE, related_name="Programa1", null=True, blank=True)
	elementopep=models.CharField("Elemento PEP", max_length=30, blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado,on_delete=models.CASCADE, related_name="AnexoEstadoElementoPEP", null=True, blank=True)
	
	anexo_sanidad=models.CharField("Plan de Sanidad", max_length=30, blank=True, null=True)
	anexo_riego=models.CharField("Plan de Riego", max_length=30, blank=True, null=True)
	anexo_fertilizacion=models.CharField("Plan de Fertilizacion", max_length=30, blank=True, null=True)
	anexo_obra=models.CharField("Plan de Obra", max_length=30, blank=True, null=True)


	class Meta:
		verbose_name = 'Etapas-Programa Produccion'
		verbose_name_plural = 'Etapas-Programa Produccion'

	def __str__(self):
		return "%s-%s-%s" % ( self.elementopep, self.programa_produccion, self.programa_produccion.anexo_campana)




class SubVariableAgronomica(models.Model):
	anexo_variable=models.ForeignKey(VariableAgronomica,on_delete=models.CASCADE, related_name="AnexoSubVariable", null=True, blank=True)
	sub_variable=models.CharField("SubVariable", max_length=30, blank=True, null=True)
	descripcion=models.CharField("Descripcion", max_length=30, blank=True, null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoVariable", null= True)
	class Meta:
		verbose_name = 'Sub Variable Agronomica'
		verbose_name_plural = 'Sub Variable Agronomica'

	def __str__(self):
		return "%s-%s" % (self.sub_variable, self.descripcion)



class VersionAgronomica(models.Model):
	version=models.CharField("N° de Version", max_length=30, blank=True, null=True, unique=True)
	
	class Meta:
		verbose_name = 'Version Agronomica'
		verbose_name_plural = 'Version Agronomica'

	def __str__(self):
		return "%s" % ( self.version)


class PproduccionVariable(models.Model):
	programa_produccion=models.ForeignKey(ProgramaProduccion,on_delete=models.CASCADE, related_name="Programa3", null=True, blank=True)
	
	anexo_subvariable=models.ForeignKey(SubVariableAgronomica,on_delete=models.CASCADE, null=True, blank=True)
	anexo_versiones=models.ForeignKey(VersionAgronomica,on_delete=models.CASCADE, related_name="versiones", null=True, blank=True)
	
	cantidad=models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	
	class Meta:
		verbose_name = 'PP-variable Agronomica'
		verbose_name_plural = 'PP-variable Agronomica'

	def __str__(self):
		return "%s-%s-%s-%s-%s" % ( self.programa_produccion,self.programa_produccion.anexo_campana,self.programa_produccion.estado, self.anexo_subvariable, self.anexo_versiones)

class Planta(models.Model):
	
	nom_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="ejezona20")
	nom_planta=models.CharField("Planta", max_length=30, blank=True, null=True, unique=True)
	estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="uestado_planta",null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion74")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion74",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Planta'
		verbose_name_plural = 'Planta'

	def __str__(self):
		return "%s" % ( self.nom_planta)

class Nave(models.Model):
	
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="Planta")
	nom_nave=models.CharField("Nave", max_length=30, blank=True, null=True, unique=True)
	estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado_nave",null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion75")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion75",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Nave'
		verbose_name_plural = 'Nave'

	def __str__(self):
		return "%s" % ( self.nom_nave)

class Linea(models.Model):
	
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="nave2")
	nom_linea=models.CharField("Linea", max_length=30, blank=True, null=True, unique=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion77")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion77",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Linea'
		verbose_name_plural = 'Lineas'

	def __str__(self):
		return "%s" % ( self.nom_linea)

class PersonalPlanta(models.Model):
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="ejezona21")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="planta2")
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="nave1")
	linea=models.ForeignKey(Linea, on_delete=models.CASCADE, related_name="linea1", blank=True, null=True)
	trab_empa=models.DecimalField(max_digits=5, decimal_places=0)
	trab_term=models.DecimalField(max_digits=5, decimal_places=0)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion76")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion76",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Personal Planta'
		verbose_name_plural = 'Personal Planta'

	def __str__(self):
		return "%s-%s" % ( self.anexo_nave,self.linea)

class EstadoPlanta(models.Model):
	
	nom_estado=models.CharField("Estado", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Estado Planta'
		verbose_name_plural = 'Estados Plantas'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_estado)


class LPaletas(models.Model):
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="ejezona24")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="planta6")
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="nave5")
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoPaletasCultivo", blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoPaletas", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion83")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion83",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'ATHOS Lanzado Paleta'
		verbose_name_plural = 'ATHOS Lanzado Paletas'

	def __str__(self):
		return "%s-%s-%s" % ( self.anexo_zona,self.anexo_planta,self.anexo_nave)

class Turno(models.Model):
	
	nom_turno=models.CharField("Turno", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Turno'
		verbose_name_plural = 'Turnos'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_turno)

class LPaletasReal(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="linea7", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzado", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njavas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="estado101", blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion84")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación")
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion84",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado'
		verbose_name_plural = ' Lanzado'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)

class Materiales(models.Model):
	codigo=models.CharField("codigo", max_length=30, blank=True, null=True, unique=True)
	descripcion=models.CharField("descripcion", max_length=200, blank=True, null=True, unique=True)
	codigosap=models.CharField("codigo sap", max_length=200, blank=True, null=True, unique=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="eplanta1", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion82")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion82",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Materiales'
		verbose_name_plural = 'Materiales'

	def __str__(self):
		return "%s-%s" % ( self.id ,self.codigosap)

class OrdenPedido(models.Model):
	npedido=models.CharField("N° OrdenPedido", max_length=30, blank=True, null=True, unique=True)
	ordenfabricacion=models.CharField("Orden de Fabricacion", max_length=200)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="eplanta2", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion183")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion183",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Orden Pedido'
		verbose_name_plural = 'Orden Pedido'

	def __str__(self):
		return "%s-%s" % ( self.npedido,self.ordenfabricacion)

class OrdenPedidoMaterialf(models.Model):
	anexo_orden=models.ForeignKey(OrdenPedido, on_delete=models.CASCADE, related_name="orden3")
	cod_material=models.ForeignKey(Materiales, on_delete=models.CASCADE, related_name="material9")
	anexo_descripcion=models.ForeignKey(Materiales, on_delete=models.CASCADE, related_name="descripcion2")
	cantidad=models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
	estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado97", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion90")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion90",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Orden Pedido Material'
		verbose_name_plural = 'Orden Pedido Material'

	def __str__(self):
		return "%s-%s" % ( self.cod_material,self.cantidad)

class ZonaPaletizado(models.Model):
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="ejezona31")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="planta7")
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="nave7")
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion186")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion186",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Zona Paletizado'
		verbose_name_plural = 'Zona Paletizado'

	def __str__(self):
		return "%s-%s-%s" % ( self.anexo_zona,self.anexo_planta,self.anexo_nave)

class Paletizado(models.Model):
	anexo_lanzado=models.ForeignKey(ZonaPaletizado, on_delete=models.CASCADE, related_name="linea8", blank=True, null=True)
	npalet=models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
	anexo_ordenpe=models.ForeignKey(OrdenPedido, on_delete=models.CASCADE, related_name="orden6",blank=True, null=True)
	anexo_codigo=models.ForeignKey(OrdenPedidoMaterialf, on_delete=models.CASCADE, related_name="codigo3",blank=True, null=True)
	anexo_descripcion=models.ForeignKey(OrdenPedidoMaterialf, on_delete=models.CASCADE, related_name="material6",blank=True, null=True)
	anexo_qr=models.ForeignKey(LPaletasReal, on_delete=models.CASCADE, related_name="lanzado2",blank=True, null=True)
	trazabilidad=models.CharField("trazabilidad", max_length=200)
	cantidad=models.DecimalField(max_digits=8, decimal_places=0,blank=True, null=True)
	calibre=models.DecimalField(max_digits=8, decimal_places=0,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="eplanta4", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_creacion185")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_modificacion185",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Paletizado'
		verbose_name_plural = 'Paletizados'

	def __str__(self):
		return "%s-%s" % ( self.npalet,self.cantidad)

class DescartePlanta(models.Model):
	anexo_lanzado=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="Ubicacion_Lanzado",blank=True, null=True)
	
	anexo_linea=models.ForeignKey(Linea, on_delete=models.CASCADE, related_name="Linea_Descarte",blank=True, null=True)
	cantidad=models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacion3")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacion3",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	
	
	class Meta:
		verbose_name = 'Descarte Planta'
		verbose_name_plural = 'Descarte Planta'

	def __str__(self):
		
	
		return "%s" % ( self.id)



class ConfigurarDia(models.Model):
	fecha = models.DateField("Fecha",null=True, blank=True)
	Turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="Turno_Configuracion", blank=True, null=True)
	fecha_hora_inicio = models.TimeField("Fecha y Hora de Inicio",null=True, blank=True)
	fecha_hora_fin = models.TimeField("Fecha y Hora de Fin",null=True, blank=True)

	anexo_ubicacion=models.ForeignKey(LPaletas, on_delete=models.CASCADE, related_name="Ubicacion_Configuracion", blank=True, null=True)
	


	class Meta:
		verbose_name = 'Configurar Dia'
		verbose_name_plural = 'Configurar Dias'

	def __str__(self):

		return "%s-%s-%s-%s" % ( self.fecha,self.Turno, self.fecha_hora_inicio, self.fecha_hora_fin)

class LaborPlanta(models.Model):
	
	labor=models.CharField("Labor Planta Configurar", max_length=40, null=True, blank=False)
	class Meta:
		verbose_name = 'Labor Planta'
		verbose_name_plural = 'LaborPlanta'

	def __str__(self):
		return "%s" % (self.labor)


class AreaPlanta(models.Model):
	
	area=models.CharField("Area Planta", max_length=40, null=True, blank=False)
	anexo_labor=models.ForeignKey(LaborPlanta, on_delete=models.CASCADE, related_name="area_labor", blank=True, null=True)
	class Meta:
		verbose_name = 'Area Planta'
		verbose_name_plural = 'Area Planta'

	def __str__(self):
		return "%s-%s" % (self.area, self.anexo_labor)

class ConfAsistenciaPlanta(models.Model):
	
	anexo_configuracion=models.ForeignKey(ConfigurarDia, on_delete=models.CASCADE, related_name="ConfAsistencia", blank=True, null=True)
	anexo_areaplanta=models.ForeignKey(AreaPlanta, on_delete=models.CASCADE, related_name="ConfAreaPlanta", blank=True, null=True)
	class Meta:
		verbose_name = 'Configurar Asistencia Planta'
		verbose_name_plural = 'Configurar Asistencia Planta'

	def __str__(self):
		return "%s-%s" % (self.anexo_configuracion.fecha,self.anexo_areaplanta)

class IngresoAsistenciaPlanta(models.Model):
	
	anexo_asistencia=models.ForeignKey(ConfAsistenciaPlanta, on_delete=models.CASCADE, related_name="AsistenciaIngreso", blank=True, null=True)
	dni=models.CharField("DniAsistencia", max_length=40, null=True, blank=False)
	fecha_ingreso = models.DateTimeField("Fecha y Hora de Inicio",null=True, blank=True, auto_now_add=True)
	class Meta:
		verbose_name = 'Ingreso Asistencia Planta'
		verbose_name_plural = 'Ingreso Asistencia Planta'

	def __str__(self):
		return "%s" % (self.dni)

class SalidaAsistenciaPlanta(models.Model):
	
	anexo_asistencia=models.ForeignKey(ConfAsistenciaPlanta, on_delete=models.CASCADE, related_name="AsistenciaSalida", blank=True, null=True)
	dni=models.CharField("DniAsistencia", max_length=40, null=True, blank=False)
	fecha_salida = models.DateTimeField("Fecha y Hora de Salida",null=True, blank=True, auto_now_add=True)
	class Meta:
		verbose_name = 'Salida Asistencia Planta'
		verbose_name_plural = 'Salida Asistencia Planta'

	def __str__(self):
		return "%s" % (self.dni)




class AreaCapacitacion(models.Model):
	
	nom_area=models.CharField("Area", max_length=100, null=True, blank=False)
	class Meta:
		verbose_name = 'Area Capacitacion'
		verbose_name_plural = 'Area Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_area)

class CompetenciaCapacitacion(models.Model):
	
	anexo_area=models.ForeignKey(AreaCapacitacion, on_delete=models.CASCADE, related_name="Area_Competencia", blank=True, null=True)
	codigo=models.CharField("Codigos", max_length=100, null=True, blank=False)
	nom_capacitacion=models.CharField("Competencias", max_length=100, null=True, blank=False)
	class Meta:
		verbose_name = 'Competencia Capacitacion'
		verbose_name_plural = 'Competencia Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_capacitacion)

class TemaCapacitacion(models.Model):
	
	anexo_competencia=models.ForeignKey(CompetenciaCapacitacion, on_delete=models.CASCADE, related_name="Competencia_Tema", blank=True, null=True)
	codigo=models.CharField("Codigos", max_length=100, null=True, blank=False)
	nom_tema=models.CharField("Tema", max_length=100, null=True, blank=False)
	class Meta:
		verbose_name = 'Tema Capacitacion'
		verbose_name_plural = 'Tema Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_tema)

class AlcanceCapacitacion(models.Model):
	
	nom_alcance=models.CharField("Alcance", max_length=40, null=True, blank=False)
	class Meta:
		verbose_name = 'Alcance Capacitacion'
		verbose_name_plural = 'Alcance Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.id,self.nom_alcance)

class DatosEmpresa(models.Model):
	
	razon_social=models.CharField("razon_social", max_length=40, null=True, blank=False)
	ruc=models.CharField("ruc", max_length=40, null=True, blank=False)
	domicilio=models.CharField("domicilio", max_length=150, null=True, blank=False)
	class Meta:
		verbose_name = 'Datos empresa'
		verbose_name_plural = 'Datos Empresa'

	def __str__(self):
		return "%s-%s" % (self.id,self.razon_social)

class ParticipantesCapacitacion(models.Model):
	
	tip_participantes=models.CharField("Tipo_Participantes", max_length=40, null=True, blank=False)
	class Meta:
		verbose_name = 'Participantes Capacitacion'
		verbose_name_plural = 'Participantes Capacitaciones'

	def __str__(self):
		return "%s" % (self.tip_participantes)

class TipoCapacitacion(models.Model):
	
	tipo_capacitacion=models.CharField("tipo_capacitacion", max_length=40, null=True, blank=False)
	class Meta:
		verbose_name = 'Tipo Capacitacion'
		verbose_name_plural = 'Tipo Capacitaciones'

	def __str__(self):
		return "%s" % (self.tipo_capacitacion)

class EstadoCapacitacion(models.Model):
	estado=models.CharField("Estado", max_length=40, null=True, blank=True)
	
	class Meta:
		verbose_name = ' Estado Capacitacion'
		verbose_name_plural = ' Estado Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.id,self.estado)



class CapacitacionCapacitacion(models.Model):
	codigoacta=models.CharField("Codigo Acta", max_length=40, null=True, blank=False)
	anexo_datos=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="Datos_Empresa", blank=True, null=True)
	anexo_area=models.ForeignKey(AreaCapacitacion, on_delete=models.CASCADE, related_name="Area_CapacitacionA", blank=True, null=True)
	anexo_competencia=models.ForeignKey(CompetenciaCapacitacion, on_delete=models.CASCADE, related_name="Competencia_CapacitacionA", blank=True, null=True)
	anexo_tema=models.ManyToManyField(TemaCapacitacion)
	fecha_hora_inicio = models.DateTimeField("Fecha y Hora de Inicio",null=True, blank=True)
	fecha_hora_fin = models.DateTimeField("Fecha y Hora de Fin",null=True, blank=True)
	lugar=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="Zona_Capacitacion", blank=True, null=True)
	lugar_especifico=models.CharField("Lugar Especifico", max_length=60, null=True, blank=True)
	cantidad=models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
	tipo_participante=models.ForeignKey(ParticipantesCapacitacion, on_delete=models.CASCADE, related_name="Participantes_Capacitacion", blank=True, null=True)
	tipo_capacitacion=models.ForeignKey(TipoCapacitacion, on_delete=models.CASCADE, related_name="Tipo_Capacitacion", blank=True, null=True)
	expositor=models.CharField("Expositor", max_length=50, null=True, blank=False)
	dniexpositor=models.IntegerField(null=True, blank=False)
	empresaexpositor=models.CharField("Expositor", max_length=100, null=True, blank=False)
	puestoexpositor=models.CharField("Puesto Expositor", max_length=100, null=True, blank=False)
	
	imagen_capacitacion=models.ImageField(upload_to="foto_capacitacion" ,blank=True, null=True)
	imagen_acta=models.ImageField(upload_to="foto_acta_capacitacion" ,blank=True, null=True)
	anexo_estado=models.ForeignKey(EstadoCapacitacion, on_delete=models.CASCADE, related_name="AnexoEstadoCapacitacion", blank=True, null=True)	
	
	idtema=models.CharField("id tema", max_length=50, null=True, blank=False)

	class Meta:
		verbose_name = ' Conf. Capacitacion'
		verbose_name_plural = ' Conf. Capacitaciones'

	def __str__(self):
		return "%s-%s" % (self.codigoacta,self.fecha_hora_inicio)

class AsistenciaCapacitacion(models.Model):
	anexo_capacitacion=models.ForeignKey(CapacitacionCapacitacion, on_delete=models.CASCADE, related_name="Da", blank=True, null=True)
	dni=models.CharField("DNI", max_length=40, null=True, blank=False)
	fecha_hora_inicio = models.DateTimeField("Fecha y Hora de Inicio",null=True, blank=True, auto_now_add=True)
	anexo_estado=models.ForeignKey(RespuestaAprobacion, on_delete=models.CASCADE, related_name="AnexoAsisAprobacion", blank=True, null=True)	
	
	class Meta:
		verbose_name = 'Asistencia Capacitacion'
		verbose_name_plural = 'Asistencia Capacitacion'

	def __str__(self):
		return "%s" % (self.dni)
		
class MenuCapacitacioncapacitacionAnexoTema(models.Model):
    capacitacioncapacitacion = models.ForeignKey(CapacitacionCapacitacion, models.DO_NOTHING)
    temacapacitacion = models.ForeignKey(TemaCapacitacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_capacitacioncapacitacion_anexo_tema'
        unique_together = (('capacitacioncapacitacion', 'temacapacitacion'),)





class estadomaterial(models.Model):
	estado_material=models.CharField("Estado Material", max_length=30, blank=True, null=True)
	class Meta:
		verbose_name = 'Estado Material'
		verbose_name_plural = 'Estado Material'

	def __str__(self):

		return "%s-%s" % ( self.id,self.estado_material)

class UnidadMedida(models.Model):
	unidad_medida=models.CharField("Unidad de Medida", max_length=30, blank=True, null=True)
	class Meta:
		verbose_name = 'Unidad de Medida'
		verbose_name_plural = 'Unidad de Medida'

	def __str__(self):

		return "%s-%s" % ( self.id,self.unidad_medida)

class TipoSabor(models.Model):
	
	tipo=models.CharField("Tipo Sabor", max_length=30, blank=True, null=True)

	class Meta:
		verbose_name = 'Tipo Sabor'
		verbose_name_plural = 'Tipo Sabor'

	def __str__(self):

		return "%s-%s" % ( self.id,self.tipo)

class MaterialMMPP(models.Model):
	codigo_sap=models.CharField("Codigo SAP", max_length=50, blank=True, null=True)
	desc_material=models.CharField("Descripcion Material", max_length=50, blank=True, null=True)
	abr_material=models.CharField("Abreviatura  Material", max_length=50, blank=True, null=True)
	desc_sap=models.CharField("Descripcion Material SAP", max_length=50, blank=True, null=True)
	var_pep=models.CharField("VAR PEP", max_length=50, blank=True, null=True)
	anexo_estado=models.ForeignKey(estadomaterial, on_delete=models.CASCADE, related_name="AnexoEstadoMaterialMMPP")
	anexo_unidad=models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, related_name="AnexoUnidadMedidaMPPP")
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoMPPP",blank=True, null=True)
	tipo_fruto=models.CharField("Tipo Fruto", max_length=50, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacionmaterialMMPP", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacionmaterialMMPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Materiales Acopio MMPP'
		verbose_name_plural = 'Materiales Acopio MMPP'

	def __str__(self):

		return "%s-%s" % ( self.id,self.desc_material)

#ESTE ES EL MATERIAL ENVASE- material envase
class MaterialTransporte(models.Model):
	codigo_sap=models.CharField("Codigo SAP", max_length=50, blank=True, null=True)
	desc_material=models.CharField("Descripcion Material", max_length=50, blank=True, null=True)
	anexo_estado=models.ForeignKey(estadomaterial, on_delete=models.CASCADE, related_name="AnexoEstadoMaterialTrans")
	anexo_unidad=models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, related_name="AnexoUnidadMedidaTrans")
	peso=models.DecimalField(max_digits=8, decimal_places=3)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoEnvase",blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacionmaterialTrans", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacionmaterialTrans",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Materiales Acopio Transporte'
		verbose_name_plural = 'Materiales Acopio Transporte'

	def __str__(self):

		return "%s-%s" % ( self.desc_material,self.peso)


class TipoParihuela(models.Model):
	
	nom_parihuela=models.CharField("Descripcion Parihuela ", max_length=30, blank=True, null=True)
	peso_parihuela=models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	anexo_estado=models.ForeignKey(estadomaterial, on_delete=models.CASCADE, related_name="AnexoEstadoMaterialParihuela")
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreaciontipoparihuela", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificaciontipoparihuela",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Parihuelas'
		verbose_name_plural = 'Parihuelas'

	def __str__(self):

		return "%s-%s" % ( self.nom_parihuela,self.peso_parihuela)





class MaterialAcopio(models.Model):
	anexo_matmmpp=models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, related_name="AnexoMatMMPP", blank=True, null=True)
	anexo_mattransporte=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatTransporte", blank=True, null=True)
	pesommpp_estimado=models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoMaterial",null=True, blank=True)
	anexo_estado=models.ForeignKey(estadomaterial, on_delete=models.CASCADE, related_name="AnexoEstadoMaterial")
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacionmaterial", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacionmaterial",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Materiales Acopio'
		verbose_name_plural = 'Materiales Acopio'

	def __str__(self):

		return "%s-%s--%s" % ( self.anexo_matmmpp.desc_material,self.anexo_mattransporte.desc_material,self.pesommpp_estimado)

class TipoVehiculo(models.Model):
	
	tipo_vehiculo=models.CharField("Tipo de Vehiculo", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Tipo Vehiculo'
		verbose_name_plural = 'Tipos Vehiculos'

	def __str__(self):
		return "%s-%s" % (self.id,self.tipo_vehiculo)


class TipoTransporte(models.Model):
	
	tipo_transporte=models.CharField("Tipo de Transporte", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Tipo Transporte'
		verbose_name_plural = 'Tipos de Transporte'

	def __str__(self):
		return "%s-%s" % (self.id,self.tipo_transporte)

class TipoUnidad(models.Model):
	
	tipo_unidad=models.CharField("Tipo de Unidad", max_length=15, null=True, blank=False)
	class Meta:
		verbose_name = 'Tipo Unidad'
		verbose_name_plural = 'Tipos de Unidades'

	def __str__(self):
		return "%s-%s" % (self.id,self.tipo_unidad)



#ahora es maestra vehiculos
class PlacasVehiculares(models.Model):
	placas=models.CharField("Placas Vehiculares ", max_length=30, blank=True, null=True)
	placas2=models.CharField("Placas Vehiculares Tolba ", max_length=30, blank=True, null=True)
	n_soat=models.CharField("Numero Soat ", max_length=30, blank=True, null=True)
	vencimiento_soat = models.DateField("Vencimiento soat",null=True, blank=True)
	vencimiento_rtecnica = models.DateField("Vc. Revision Tecnica",null=True, blank=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoVehiculos",blank=True, null=True)
	anexo_tipovehiculo=models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, related_name="AnexoPlacaTipoVehiculo",blank=True, null=True)
	anexo_tipounidad=models.ForeignKey(TipoUnidad, on_delete=models.CASCADE, related_name="AnexoPlacaTipoUnidad",blank=True, null=True)
	capacidad_jabas=models.DecimalField(max_digits=6, decimal_places=0,null=True, blank=True)
	anexo_tipotransporte=models.ForeignKey(TipoTransporte, on_delete=models.CASCADE, related_name="AnexoPlacaTipoTransporte",blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoPlacaZona",blank=True, null=True)
	razon_social=models.CharField("Razon Social", max_length=100, blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacionplacas", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacionplacas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Placas Vehiculares'
		verbose_name_plural = 'Placas Vehiculares'

	def __str__(self):

		return "%s-%s" % ( self.anexo_tipotransporte,self.placas)

class DetallePlacasVehiculares(models.Model):
	
	anexo_detalle=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoDetalleVehiculos",blank=True, null=True)
	rutas=models.CharField("Rutas", max_length=50, blank=True, null=True)
	tarifa=models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariocreacionDetplacas", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuariomodificacionDetplacas",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Detalle Placas Vehiculares'
		verbose_name_plural = 'Detalle Placas Vehiculares'

	def __str__(self):

		return "%s-%s" % ( self.anexo_detalle.placas,self.rutas)



class ChoferesVehiculos(models.Model):
	ApellidoPat=models.CharField("Apellido Paterno", max_length=30, blank=True, null=True)
	ApellidoMat=models.CharField("Apellido Materno ", max_length=30, blank=True, null=True)
	Nombres=models.CharField("Nombres ", max_length=30, blank=True, null=True)
	Dni=models.CharField("DNI ", max_length=30, blank=True, null=True)
	Brevete=models.CharField("N° BREVETE ", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaCH",blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoChoferes",blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionCH", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionCH",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	class Meta:
		verbose_name = 'Choferes'
		verbose_name_plural = 'Choferes'

	def __str__(self):

		return "%s-%s-%s" % ( self.ApellidoPat,self.ApellidoMat,self.Nombres)


class UnidadVehicular(models.Model):
	anexo_placas=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoPlacas")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoChofer")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZona")
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoUVehicular",blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionUV", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionUV",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Unidad Vehicular'
		verbose_name_plural = 'Unidades Vehiculares'

	def __str__(self):

		return "%s-%s" % (self.anexo_placas, self.anexo_chofer)


class UbicacionFundo(models.Model):
	anexo_pep=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoUbiProgramaProduccion",blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionUbiFU", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionUbiFU",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ubicacion Fundo'
		verbose_name_plural = 'UUbicacion Fundo'

	def __str__(self):

		return "%s%s%s" % ( self.anexo_pep.anexo_fundo.abreviatura,self.anexo_pep.anexo_modulo.nombremodulo,self.anexo_pep.anexo_lote.nom_lote)


class TipoLugarAthos(models.Model):
	tipo=models.CharField("TipoLugar", max_length=30, blank=True, null=True)
	
	class Meta:
		verbose_name = 'Tipo Lugar Athos'
		verbose_name_plural = 'Tipo Lugar Athos'

	def __str__(self):

		return "%s-%s" % ( self.id,self.tipo)

#ahora es UbicacionesAthos -- ubicaciones athos
class LugarAthos(models.Model):
	Lugar=models.CharField("Fundo", max_length=30, blank=True, null=True)
	anexo_tipolugar=models.ForeignKey(TipoLugarAthos, on_delete=models.CASCADE, related_name="AnexoTipoLug")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaLug")
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoLugar",blank=True, null=True)
	longitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)
	latitud=models.DecimalField(max_digits=18, decimal_places=15,null=True, blank=True)

	class Meta:
		verbose_name = 'Lugar Athos'
		verbose_name_plural = 'Lugar Athos'

	def __str__(self):

		return "%s-%s" % ( self.anexo_tipolugar.tipo, self.Lugar)



class UbicacionesAcopio(models.Model):
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaAco")
	anexo_lugar=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoTipoUbi")
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionUbiAco", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionUbiAco",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ubicacion Fundo'
		verbose_name_plural = 'Ubicacion Fundo'

	def __str__(self):

		return "%s-%s" % ( self.anexo_zona,self.anexo_lugar)



class CentrosAthos(models.Model):
	centro=models.CharField("Centros Athos", max_length=30, blank=True, null=True)
	desc_centro=models.CharField("Descripcion Centro", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaCentros")
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionCEN", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionCEN",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Centros Athos'
		verbose_name_plural = 'Centros Athos'

	def __str__(self):

		return "%s-%s" % ( self.centro,self.desc_centro)

class AlmacenesAthos(models.Model):
	almacen=models.CharField("Almacen", max_length=30, blank=True, null=True)
	desc_almacen=models.CharField("Descripcion Almacen", max_length=30, blank=True, null=True)
	anexo_centro=models.ForeignKey(CentrosAthos, on_delete=models.CASCADE, related_name="AnexoAlmacenCen")
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaAlmacen",blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoAlmacen",blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmaCEN", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionAlmaCEN",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacenes Athos'
		verbose_name_plural = 'Almacenes Athos'

	def __str__(self):

		return "%s-%s-%s-%s" % ( self.anexo_centro.centro, self.anexo_centro.desc_centro,self.almacen,self.desc_almacen)


class GuiaAthos(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuia", blank=True, null=True)
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthos")
	

	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferes",blank=True, null=True)
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculos",blank=True, null=True)


	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaP")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLL")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmp")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuia", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuia",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos'
		verbose_name_plural = 'Guias Athos'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)

class CalidadProducto(models.Model):
	calidad=models.CharField("Calidad Producto", max_length=30, blank=True, null=True)
	class Meta:
		verbose_name = 'Calidad Producto'
		verbose_name_plural = 'Calidad Producto'

	def __str__(self):

		return "%s-%s" % ( self.id,self.calidad)

class GuiaDetallesAthos(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthos, on_delete=models.CASCADE, related_name="AnexoGuiaAthos")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundo")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopio")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadM", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaD", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaD",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos'
		verbose_name_plural = 'Guias  Detalles Athos'

	def __str__(self):

		return "%s-%s" % ( self.anexo_guia,self.anexo_ubi_mmpp)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthos.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPalet(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthos, on_delete=models.CASCADE, related_name="AnexoGuiaDAthos")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacen", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuela", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	cant_jabas2=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase2=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMaterialEnvase2", blank=True, null=True)
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPalets", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPalets",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet'
		verbose_name_plural = 'Info Palets'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)


class RutasAthos(models.Model):
	rutas=models.CharField("Rutas Athos", max_length=50, blank=True, null=True)
	precio=models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	anexo_lugar=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoUbifundo" ,null=True, blank=True)

	class Meta:
		verbose_name = 'Rutas Athos'
		verbose_name_plural = 'Rutas Athos'

	def __str__(self):

		return "%s" % ( self.rutas)


class GaritaAthos(models.Model):
	zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoZonaGarita" ,null=True, blank=True)
	ubicacion=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFunGarita" ,null=True, blank=True)
	ruta=models.ForeignKey(RutasAthos, on_delete=models.CASCADE, related_name="AnexoRuta" ,null=True, blank=True)
	qrcampo=models.CharField("QR Campo", max_length=50, null=True, blank=True)
	qrplaca=models.CharField("QR Placas", max_length=50, null=True, blank=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	chofer_ref=models.CharField("Chofer Referencial", max_length=50, null=True, blank=True)
	kilometraje=models.DecimalField(max_digits=8, decimal_places=0,null=True, blank=True)
	cantpasajeros=models.DecimalField(max_digits=4, decimal_places=0,null=True, blank=True)
	observacion=models.CharField(max_length=300, null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGarita", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGarita",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Garita Athos'
		verbose_name_plural = 'Garita Athos'

	def __str__(self):
		return "%s-%s" % (self.id,self.qrcampo)


class personalplanta_athos(models.Model):
	cod_trab = models.CharField( max_length=10, null=True, blank=True)
	tipdoc = models.CharField( max_length=5, null=True, blank=True)
	NroDoc = models.CharField( max_length=10, null=True, blank=True)
	ApellidoPat = models.CharField( max_length=30, null=True, blank=True)
	ApellidoMat = models.CharField( max_length=30, null=True, blank=True)
	Nombres = models.CharField( max_length=27, null=True, blank=True)
	FecNac = models.CharField( max_length=10, null=True, blank=True)
	PaisNacionalidad = models.CharField( max_length=10, null=True, blank=True)
	Nacionalidad = models.CharField( max_length=15, null=True, blank=True)
	Sexo = models.CharField( max_length=6, null=True, blank=True)
	EstadoCivil = models.CharField( max_length=6, null=True, blank=True)

	class Meta:
		managed = False
		db_table = "personalplanta_athos" # your view name