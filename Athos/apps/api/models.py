from django.db import models

#TIPOS DE USUARIOS ACCESO
class TipoUsuarioAccesoAthosMobile(models.Model):
	tipo = models.CharField("Tipo Usuario", max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Tipos de Usuarios Accesos Athos Mobile'
		verbose_name_plural = 'Tipo de Usuario Acceso Athos Mobile'

	def __str__(self):
		return "%s" % ( self.tipo)

class SedesAthosMobile(models.Model):
	sede = models.CharField("Sede Descripcion", max_length=30,null=True, blank=True)

	class Meta:
		verbose_name = 'Sedes Accesos Athos Mobile'
		verbose_name_plural = 'Sedes Acceso Athos Mobile'

	def __str__(self):
		return "%s" % ( self.sede)

#MAESTRAS
class MaestraAccesoAthosMobile(models.Model):
	usuario = models.CharField("Usuario", max_length=30,null=True, blank=True)
	dni = models.CharField("DNI", max_length=12,null=True, blank=True)
	tipo_usuario = models.ForeignKey(TipoUsuarioAccesoAthosMobile, on_delete=models.CASCADE, related_name="TipoUsuarioAccesoAthos",null=True, blank=True)

	class Meta:
		verbose_name = 'Maestras de Accesos Athos Mobile'
		verbose_name_plural = 'Maestra de Acceso Athos Mobile'

	def __str__(self):
		return "%s - %s - %s" % (self.dni,self.usuario,self.tipo_usuario)

#MAESTRA SEGURIDAD
class MaestraAccesoSeguridadAthosMobile(models.Model):
	usuario = models.CharField("Usuario", max_length=100,null=True, blank=True)
	posicion = models.CharField("Posicion", max_length=150,null=True, blank=True)
	dni = models.CharField("DNI", max_length=12,null=True, blank=True)
	sede = models.ForeignKey(SedesAthosMobile, on_delete=models.CASCADE, related_name="SedesAthos",null=True, blank=True)

	class Meta:
		verbose_name = 'Maestras de Accesos Seguridad Athos Mobile'
		verbose_name_plural = 'Maestra de Acceso Seguridad Athos Mobile'

	def __str__(self):
		return "%s - %s - %s" % (self.dni,self.usuario,self.sede)

#MODELO TAREO
#NIVEL 1 TAREO AR
class MobileNivelUno(models.Model):
	pep = models.CharField("Pep", max_length=50,null=True, blank=True)
	zona = models.CharField("Zona", max_length=30,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=30,null=True, blank=True)
	cultivo = models.CharField("Cultivo", max_length=30,null=True, blank=True)
	dni_supervisor = models.CharField("Supervisor", max_length=30,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Primer Nivel'
		verbose_name_plural = 'Tareo AR Primer Nivel'

	def __str__(self):
		return "%s - %s" % ( self.fundo,self.dni_supervisor)

#NIVEL 2 TAREO AR
class MobileNivelUnoMedio(models.Model):
	anexo_pep = models.CharField("Pep", max_length=50,null=True, blank=True)
	id_grupo = models.CharField("Id Grupo", max_length=50,null=True, blank=True)
	contador = models.CharField("Contador Grupo", max_length=50,null=True, blank=True)
	anexo_supervisor = models.CharField("Supervisor", max_length=50,null=True, blank=True)
	estado = models.CharField("Estado", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Segundo Nivel'
		verbose_name_plural = 'Tareo AR Segundo Nivel'

	def __str__(self):
		return "%s - %s" % ( self.anexo_supervisor,self.estado)

#NIVEL 3 TAREO AR
class MobileNivelDos(models.Model):
	anexo_grupo = models.CharField("Anexo Grupo", max_length=50,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=50,null=True, blank=True)
	modulo = models.CharField("Modulo", max_length=50,null=True, blank=True)
	lote = models.CharField("Lote", max_length=50,null=True, blank=True)
	labor = models.CharField("Labor", max_length=50,null=True, blank=True)
	personal = models.CharField("Personal", max_length=50,null=True, blank=True)
	anexo_supervisor = models.CharField("Supervisor", max_length=50,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=50,null=True, blank=True)
	hora_inicio = models.CharField("Hora Inicio", max_length=50,null=True, blank=True)
	hora_final = models.CharField("Hora Final", max_length=50,null=True, blank=True)
	estado = models.CharField("Estado", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Tercer Nivel'
		verbose_name_plural = 'Tareo AR Tercer Nivel'

	def __str__(self):
		return "%s - %s" % ( self.fundo,self.anexo_supervisor)

#-----------------------FIN MODELO TAREO V1-----------------------

#MODELO TAREO V2
class MobileTareoArNivelUno(models.Model):
	id_nivel_uno = models.CharField("Id Nivel 1", max_length=50,null=True, blank=True)
	zona = models.CharField("Zona", max_length=30,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=30,null=True, blank=True)
	cultivo = models.CharField("Cultivo", max_length=30,null=True, blank=True)
	dni_supervisor = models.CharField("Supervisor", max_length=30,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Nivel Uno'
		verbose_name_plural = 'Tareo AR Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.fundo,self.dni_supervisor)

class MobileTareoArNivelDos(models.Model):
	anexo_nivel1 = models.CharField("Anexo Nivel 1", max_length=50,null=True, blank=True)
	id_grupo = models.CharField("Id Grupo", max_length=50,null=True, blank=True)
	contador = models.CharField("Contador Grupo", max_length=50,null=True, blank=True)
	anexo_supervisor = models.CharField("Supervisor", max_length=50,null=True, blank=True)
	estado = models.CharField("Estado", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Nivel Dos'
		verbose_name_plural = 'Tareo AR Nivel Dos'

	def __str__(self):
		return "%s - %s" % ( self.anexo_supervisor,self.id_grupo)

class MobileTareoArNivelTres(models.Model):
	anexo_grupo = models.CharField("Anexo Grupo", max_length=50,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=50,null=True, blank=True)
	modulo = models.CharField("Modulo", max_length=50,null=True, blank=True)
	lote = models.CharField("Lote", max_length=50,null=True, blank=True)
	actividad = models.CharField("Actividad", max_length=50,null=True, blank=True)
	labor = models.CharField("Labor", max_length=50,null=True, blank=True)
	personal = models.CharField("Personal", max_length=150,null=True, blank=True)
	anexo_supervisor = models.CharField("Supervisor", max_length=50,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=50,null=True, blank=True)
	hora_inicio = models.CharField("Hora Inicio", max_length=50,null=True, blank=True)
	hora_final = models.CharField("Hora Final", max_length=50,null=True, blank=True)
	estado = models.CharField("Estado", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Nivel Tres'
		verbose_name_plural = 'Tareo AR Nivel Tres'

	def __str__(self):
		return "%s - %s" % ( self.fundo,self.anexo_supervisor)
#-----------------------FIN MODELO TAREO V2-----------------------

#MODELO DESTAJO - PRODUCTIVIDAD AR
#NIVEL 1 PRODUCTIVIDAD AR
class MobileProductividadAR(models.Model):
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	dni_personal = models.CharField("dni_personal", max_length=150,null=True, blank=True)
	dni = models.CharField("DNI", max_length=15,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Productividad AR Primer Nivel'
		verbose_name_plural = 'Productividad AR Primer Nivel'

	def __str__(self):
		return "%s - %s" % ( self.fecha,self.dni)

#-----------------------FIN MODELO DESTAJO-----------------------

#MODELO GARITA
#NIVEL 1 GARITA BUS
class MobileGaritaBusNivelUno(models.Model):
	placa = models.CharField("Placa", max_length=150,null=True, blank=True)
	zona = models.CharField("Zona", max_length=50,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=50,null=True, blank=True)
	personal = models.CharField("Personal", max_length=150,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=50,null=True, blank=True)
	hora = models.CharField("Hora", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Garita Bus Nivel Uno'
		verbose_name_plural = 'Garita Bus Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.fundo,self.placa)

#NIVEL 2 GARITA BUS
class MobileGaritaBusNivelDos(models.Model):
	personal = models.CharField("Personal", max_length=150,null=True, blank=True)
	contador = models.CharField("Contador", max_length=50,null=True, blank=True)
	anexo_placa = models.CharField("Placa", max_length=150,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Garita Bus Nivel Dos'
		verbose_name_plural = 'Garita Bus Nivel Dos'

	def __str__(self):
		return "%s - %s" % ( self.anexo_placa,self.personal)

#NIVEL 1 GARITA PERSONAL
class MobileGaritaPersonalNivelUno(models.Model):
	zona = models.CharField("Zona", max_length=50,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=50,null=True, blank=True)
	personal = models.CharField("Personal", max_length=150,null=True, blank=True)
	tipo_hora = models.CharField("Tipo Hora", max_length=50,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=50,null=True, blank=True)
	hora = models.CharField("Hora", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Garita Personal Nivel Uno'
		verbose_name_plural = 'Garita Personal Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.zona,self.fundo)

#NIVEL 1 GARITA UNIDAD
class MobileGaritaUnidadNivelUno(models.Model):
	zona = models.CharField("Zona", max_length=50,null=True, blank=True)
	fundo = models.CharField("Fundo", max_length=50,null=True, blank=True)
	personal = models.CharField("Personal", max_length=150,null=True, blank=True)
	tipo_hora = models.CharField("Tipo Hora", max_length=50,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=50,null=True, blank=True)
	hora = models.CharField("Hora", max_length=50,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Garita Unidad Nivel Uno'
		verbose_name_plural = 'Garita Unidad Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.zona,self.fundo)

#-----------------------FIN MODELO GARITA-----------------------

#MODELO TAREO PLANTA
class MobileTareoArPlantaNivelUno(models.Model):
	id_nivel_uno = models.CharField("Id Nivel 1", max_length=50,null=True, blank=True)
	nave = models.CharField("Nave", max_length=30,null=True, blank=True)
	linea = models.CharField("Linea", max_length=30,null=True, blank=True)
	turno = models.CharField("Turno", max_length=30,null=True, blank=True)
	dni = models.CharField("DNI", max_length=30,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Planta Nivel Uno'
		verbose_name_plural = 'Tareo AR Planta Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.nave,self.dni)

class MobileTareoArPlantaNivelDos(models.Model):
	anexo_nivel1 = models.CharField("Anexo Nivel 1", max_length=50,null=True, blank=True)
	id_grupo = models.CharField("Id Grupo", max_length=50,null=True, blank=True)
	contador = models.CharField("Contador Grupo", max_length=20,null=True, blank=True)
	dni = models.CharField("DNI", max_length=15,null=True, blank=True)
	estado = models.CharField("Estado", max_length=10,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Planta Nivel Dos'
		verbose_name_plural = 'Tareo AR Planta Nivel Dos'

	def __str__(self):
		return "%s - %s" % ( self.dni,self.id_grupo)

class MobileTareoArPlantaNivelTres(models.Model):
	anexo_grupo = models.CharField("Anexo Grupo", max_length=50,null=True, blank=True)
	proceso = models.CharField("Proceso", max_length=50,null=True, blank=True)
	actividad = models.CharField("Actividad", max_length=50,null=True, blank=True)
	labor = models.CharField("Labor", max_length=50,null=True, blank=True)
	mesa = models.CharField("Mesa", max_length=50,null=True, blank=True)
	dni = models.CharField("DNI", max_length=15,null=True, blank=True)
	qr_personal = models.CharField("QR Personal", max_length=150,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=15,null=True, blank=True)
	hora = models.CharField("Hora", max_length=15,null=True, blank=True)
	hora_inicio = models.CharField("Hora Inicio", max_length=50,null=True, blank=True)
	hora_final = models.CharField("Hora Final", max_length=50,null=True, blank=True)
	estado = models.CharField("Estado", max_length=10,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	class Meta:
		verbose_name = 'Tareo AR Planta Nivel Tres'
		verbose_name_plural = 'Tareo AR Planta Nivel Tres'

	def __str__(self):
		return "%s - %s" % ( self.proceso,self.dni)
#-----------------------FIN MODELO TAREO V2-----------------------

#-----------------------MODELO SEGURIDAD--------------------------
class MobileSeguridadNivelUno(models.Model):
	id_nivel_uno = models.CharField("Id Nivel 1", max_length=50,null=True, blank=True)
	dni = models.CharField("DNI", max_length=15,null=True, blank=True)
	usuario = models.CharField("Usuario", max_length=300,null=True, blank=True)
	sede = models.CharField("Sede", max_length=50,null=True, blank=True)
	unidad_operaria = models.CharField("Unidad Operativa", max_length=150,null=True, blank=True)
	area = models.CharField("Area", max_length=150,null=True, blank=True)
	tipo_reporte = models.CharField("Tipo Reporte", max_length=150,null=True, blank=True)
	nombre_reporte = models.CharField("Nombre Reporte", max_length=300,null=True, blank=True)
	descripcion = models.CharField("Descripcion", max_length=150,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)

	class Meta:
		verbose_name = 'Seguridad Nivel Uno'
		verbose_name_plural = 'Seguridad Nivel Uno'

	def __str__(self):
		return "%s - %s" % ( self.sede,self.dni)
#-----------------------FIN MODELO SEGURIDAD-----------------------

#-----------------------MODELO PRODUCTIVIDAD---------------------------
class MobileProductividadPlanta(models.Model):
	usuario = models.CharField("Usuario", max_length=300,null=True, blank=True)
	qr = models.CharField("QR", max_length=100,null=True, blank=True)
	fecha = models.CharField("Fecha", max_length=30,null=True, blank=True)
	hora = models.CharField("Hora", max_length=30,null=True, blank=True)
	sinc = models.CharField("Sincronizado", max_length=1,null=True, blank=True)

	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)

	class Meta:
		verbose_name = 'Productividad Planta Mobile'
		verbose_name_plural = 'Productividad Planta Mobile'

	def __str__(self):
		return "%s - %s - %s - %s" % (self.usuario,self.qr,self.fecha,self.hora)
#-----------------------FIN MODELO PRODUCTIVIDAD-----------------------