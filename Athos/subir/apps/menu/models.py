
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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
	class Meta:
		verbose_name = 'variedad'
		verbose_name_plural = 'variedades'

	def __str__(self):
		return "%s-%s" % (self.nom_variedad,self.cul.nom_cultivo)


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

class ProgramaProduccion(models.Model):

	anexo_fundo=models.ForeignKey(fundo,on_delete=models.CASCADE, related_name="fundo3", null=True)
	anexo_modulo=models.ForeignKey(modulo,on_delete=models.CASCADE, related_name="lote1", null= True)
	anexo_lote=models.ForeignKey(lote,on_delete=models.CASCADE, related_name="lote1")
	anexo_campana=models.ForeignKey(campanas,on_delete=models.CASCADE, related_name="campanas1")
	ano_campana=models.CharField("Año Campaña", max_length=10, null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad,on_delete=models.CASCADE, related_name="variedad1")
	area=models.CharField("Area",max_length=30,blank=False, null=False)
	cierre_campana=models.DateField("Cierre de Campaña", max_length=30, blank=True, null=True)
	estado = models.ForeignKey(EstadoCampana, on_delete=models.CASCADE, related_name="estado10", null= True)
	class Meta:
		verbose_name = 'Programa Produccion'
	class Meta:
		verbose_name_plural = 'Programas de Produccion'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.anexo_fundo.nom_fundo,self.anexo_modulo.nombremodulo,self.anexo_lote.nom_lote,self.anexo_campana.camp)

class ProgramaProduccionFeno(models.Model):
	programa_produccion=models.ForeignKey(ProgramaProduccion,on_delete=models.CASCADE, related_name="Programa")
	anexo_fenologia=models.ForeignKey(fenologia,on_delete=models.CASCADE, related_name="fenologia1")
	fecha=models.DateField("Fecha y Hora de Creación", null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="estado30", null= True)
	class Meta:
		verbose_name = 'Produccion Fenologias'
		verbose_name_plural = 'Produccion Fenologias'

	def __str__(self):
		return "%s-%s" % ( self.anexo_fenologia.nom_feno,self.fecha)


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
	elementopep=models.CharField("Elemento PEP", max_length=30, blank=True, null=True, unique=True)

	class Meta:
		verbose_name = 'Elemento PEP'
		verbose_name_plural = 'Elementos PEP'

	def __str__(self):
		return "%s" % ( self.elementopep)



class RegistroPersonal(models.Model):
	Apellidos=models.CharField("Apellidos", max_length=30, blank=True, null=True, unique=True)
	Nombres= models.CharField("Nombres", max_length=30, blank=True, null=True, unique=True)
	DNI=models.CharField("DNI", max_length=30, blank=True, null=True, unique=True)

	class Meta:
		verbose_name = 'Registro de Personal'
		verbose_name_plural = 'Registros de Personal'

	def __str__(self):
		return "%s-%s" % ( self.DNI, self.Apellidos)

