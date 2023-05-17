from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import Planta
from apps.menu.models import Nave
from apps.menu.models import MaterialMMPP
from apps.menu.models import Turno
from apps.menu.models import fundo

from apps.menu.models import cultivo


# Create your models here.
class ModEnfriado(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	cod_termometro= models.CharField("Codigo de termometro", max_length=30,null=True, blank=True)
	cod_vac1= models.CharField("Codigo de Vacuometro 1", max_length=30,null=True, blank=True)
	cod_vac2= models.CharField("Codigo de Vacuometro 2", max_length=30,null=True, blank=True)
	cod_vac3= models.CharField("Codigo de Vacuometro 3", max_length=30,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEnfriado")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEnfriado",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Modulo Enfriado'
		verbose_name_plural = 'Modulo de Enfriado'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.cod_termometro)

class TipoModEnfriado(models.Model):
	tipo= models.CharField("Tipo", max_length=50)

	class Meta:
		verbose_name = 'Tipo Enfriado'
		verbose_name_plural = 'Tipo Enfriado'

	def __str__(self):
		return "%s-%s" % (self.id, self.tipo)

class LadosTunel(models.Model):
	lados= models.CharField("Lados Tunel", max_length=50)

	class Meta:
		verbose_name = 'Lados Tunel'
		verbose_name_plural = 'Lados Tunel'

	def __str__(self):
		return "%s-%s" % (self.id, self.lados)

class ModEnfriado2022(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoPlantaEnfriado2022",null=True, blank=True)
	anexo_tipo=models.ForeignKey(TipoModEnfriado, on_delete=models.CASCADE, related_name="AnexoTipoModEnfriado2022",null=True, blank=True)
	n_tunel=models.IntegerField(null=True, blank=True)
	n_batch=models.IntegerField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEnfriado2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEnfriado2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Modulo Enfriado 2022'
		verbose_name_plural = 'Modulo de Enfriado 2022'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.anexo_planta)

class ConfirmacionModEnfriado2022(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriado2022, on_delete=models.CASCADE, related_name="AnexoEnfriadoConfirmacionPalet",null=True, blank=True)
	n_palet= models.IntegerField(null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionConfirmacionPaletEnfriado2022",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserConfirmacionPaletModEnfriado2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Confirmacion Mod Enfriado 2022'
		verbose_name_plural = 'Confirmacion Mod Enfriado 2022'

	def __str__(self):
		return "%s-%s" % (self.id, self.n_palet)

class ConfirmacionTicketModEnfriado2022(models.Model):
	anexo_palet=models.ForeignKey(ConfirmacionModEnfriado2022, on_delete=models.CASCADE, related_name="AnexoEnfriadoConfirmacionTicket",null=True, blank=True)
	n_ticket = models.CharField("N° Ticket", max_length=150)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionConfirmacionTicketEnfriado2022",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserConfirmacionTicketModEnfriado2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Confirmacion Mod Ticket Enfriado 2022'
		verbose_name_plural = 'Confirmacion Mod Ticket Enfriado 2022'

	def __str__(self):
		return "%s-%s" % (self.id, self.n_ticket)

class RegistroTemperaturaModEnfriado2022(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriado2022, on_delete=models.CASCADE, related_name="AnexoEnfriadoRTemperatura",null=True, blank=True)
	m_tempambiente= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionRTemperaturaEnfriado2022",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserRTemperaturaModEnfriado2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Registro de Temperaturas Mod Enfriado 2022'
		verbose_name_plural = 'Registro de Temperaturas Mod Enfriado 2022'

	def __str__(self):
		return "%s-%s" % (self.id, self.m_tempambiente)

class TomaDatosModEnfriado2022(models.Model):
	anexo_temperatura=models.ForeignKey(RegistroTemperaturaModEnfriado2022, on_delete=models.CASCADE, related_name="AnexoEnfriadoTomaDatos",null=True, blank=True)
	n_palet= models.IntegerField(null=True, blank=True)
	anexo_lado=models.ForeignKey(LadosTunel, on_delete=models.CASCADE, related_name="AnexoLadoTunelTomaDatosModEnfriado2022",null=True, blank=True)
	m_tempinterna= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	m_tempexterna= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTomaDatosEnfriado2022",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserTomaDatosModEnfriado2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Toma de Datos Mod Enfriado 2022'
		verbose_name_plural = 'Toma de Datos Mod Enfriado 2022'

	def __str__(self):
		return "%s-%s" % (self.id, self.m_tempinterna)

class DistribucionEnfriado(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriado, on_delete=models.CASCADE, related_name="AnexoEnfriadoDistribucion",null=True, blank=True)
	anexo_lado=models.ForeignKey(LadosTunel, on_delete=models.CASCADE, related_name="AnexoLadoTunelD",null=True, blank=True)
	tunel=models.IntegerField(null=True, blank=True)
	#n_tunel es numero de compartimento
	n_tunel= models.CharField(max_length=100,null=True, blank=True)

	lectura_qr= models.CharField("Lectura QR", max_length=100, unique=True)
	n_palet= models.DecimalField(max_digits=5, decimal_places=0)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDistribucion")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDistribucion",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Distribucion Enfriado'
		verbose_name_plural = 'Distribucion Enfriado'

	def __str__(self):
		return "%s-%s" % (self.n_palet, self.n_tunel)
		

class TemperaturaEnfriado(models.Model):
	anexo_temperatura=models.ForeignKey(DistribucionEnfriado, on_delete=models.CASCADE, related_name="AnexoTemperaturaEnfriado",null=True, blank=True)
	m_tempambiente= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	m_tempinterna= models.DecimalField(max_digits=5, decimal_places=2)
	m_tempexterna= models.DecimalField(max_digits=5, decimal_places=2)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTemperatura")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTemperatura",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Temperatura Enfriado'
		verbose_name_plural = 'Temperatura Enfriado'

	def __str__(self):
		return "%s-%s" % (self.id, self.anexo_temperatura)








#campaña2021-1
class ModEnfriadoArCaraz2021(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	cod_termometro= models.CharField("Codigo de termometro", max_length=30,null=True, blank=True)
	cod_vac1= models.CharField("Codigo de Vacuometro 1", max_length=30,null=True, blank=True)
	cod_vac2= models.CharField("Codigo de Vacuometro 2", max_length=30,null=True, blank=True)
	cod_vac3= models.CharField("Codigo de Vacuometro 3", max_length=30,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEnfriadoArCaraz2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEnfriadoArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Modulo Enfriado-Arandano Caraz 2021'
		verbose_name_plural = 'Modulo de Enfriado-Arandano Caraz 2021'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.cod_termometro)


class DistribucionEnfriadoArCaraz2021(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriadoArCaraz2021, on_delete=models.CASCADE, related_name="AnexoEnfriadoDistribucionArCaraz2021",null=True, blank=True)
	anexo_lado=models.ForeignKey(LadosTunel, on_delete=models.CASCADE, related_name="AnexoLadoTunelDArCaraz2021",null=True, blank=True)
	tunel=models.IntegerField(null=True, blank=True)
	#n_tunel es numero de compartimento
	n_tunel= models.CharField(max_length=100,null=True, blank=True)

	lectura_qr= models.CharField("Lectura QR", max_length=100, unique=True)
	n_palet= models.DecimalField(max_digits=5, decimal_places=0)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDistribucionArCaraz2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDistribucionArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Distribucion Enfriado-Arandano Caraz 2021'
		verbose_name_plural = 'Distribucion Enfriado-Arandano Caraz 2021'

	def __str__(self):
		return "%s-%s" % (self.n_palet, self.n_tunel)
		

class TemperaturaEnfriadoArCaraz2021(models.Model):
	anexo_temperatura=models.ForeignKey(DistribucionEnfriadoArCaraz2021, on_delete=models.CASCADE, related_name="AnexoTemperaturaEnfriadoArCaraz2021",null=True, blank=True)
	m_tempambiente= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	m_tempinterna= models.DecimalField(max_digits=5, decimal_places=2)
	m_tempexterna= models.DecimalField(max_digits=5, decimal_places=2)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTemperaturaArCaraz2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTemperaturaArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Temperatura Enfriado-Arandanos Caraz 2021'
		verbose_name_plural = 'Temperatura Enfriado-Arandanos Caraz 2021'

	def __str__(self):
		return "%s-%s" % (self.id, self.anexo_temperatura)



#CAMPAÑA 2021-2
class ModEnfriadoArCaraz202102(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoPlantaEnfriado",null=True, blank=True)
	cod_termometro= models.CharField("Codigo de termometro", max_length=30,null=True, blank=True)
	cod_vac1= models.CharField("Codigo de Vacuometro 1", max_length=30,null=True, blank=True)
	cod_vac2= models.CharField("Codigo de Vacuometro 2", max_length=30,null=True, blank=True)
	cod_vac3= models.CharField("Codigo de Vacuometro 3", max_length=30,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEnfriadoArCaraz202102")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEnfriadoArCaraz202102",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Modulo Enfriado-Arandano Caraz 2021 02'
		verbose_name_plural = 'Modulo de Enfriado-Arandano Caraz 2021 02'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.cod_termometro)


class DistribucionEnfriadoArCaraz202102(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriadoArCaraz202102, on_delete=models.CASCADE, related_name="AnexoEnfriadoDistribucionArCaraz202102",null=True, blank=True)
	anexo_lado=models.ForeignKey(LadosTunel, on_delete=models.CASCADE, related_name="AnexoLadoTunelDArCaraz202102",null=True, blank=True)
	tunel=models.IntegerField(null=True, blank=True)
	#n_tunel es numero de compartimento
	n_tunel= models.CharField(max_length=100,null=True, blank=True)

	lectura_qr= models.CharField("Lectura QR", max_length=100, unique=True)
	n_palet= models.DecimalField(max_digits=5, decimal_places=0)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDistribucionArCaraz202102")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDistribucionArCaraz202102",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Distribucion Enfriado-Arandano Caraz 2021 02'
		verbose_name_plural = 'Distribucion Enfriado-Arandano Caraz 2021 02'

	def __str__(self):
		return "%s-%s" % (self.n_palet, self.n_tunel)
		

class TemperaturaEnfriadoArCaraz202102(models.Model):
	anexo_temperatura=models.ForeignKey(DistribucionEnfriadoArCaraz202102, on_delete=models.CASCADE, related_name="AnexoTemperaturaEnfriadoArCaraz202102",null=True, blank=True)
	m_tempambiente= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	m_tempinterna= models.DecimalField(max_digits=5, decimal_places=2)
	m_tempexterna= models.DecimalField(max_digits=5, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTemperaturaArCaraz202102")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTemperaturaArCaraz202102",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Temperatura Enfriado-Arandanos Caraz 2021 02'
		verbose_name_plural = 'Temperatura Enfriado-Arandanos Caraz 2021 02'

	def __str__(self):
		return "%s-%s" % (self.id, self.anexo_temperatura)


class TipoDescarteAthos(models.Model):
	descarte= models.CharField("TipoDescarte", max_length=50)

	class Meta:
		verbose_name = 'Tipo Descarte'
		verbose_name_plural = 'Tipo Descarte'

	def __str__(self):
		return "%s-%s" % (self.id, self.descarte)

class DescarteAthos(models.Model):
	anexo_eje=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoDescarteEje",null=True, blank=True)
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoDescartePlanta",null=True, blank=True)
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="AnexoDescarteNave",null=True, blank=True)
	anexo_material=models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, related_name="AnexoDescarteMMPP",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoDescarteTurno",null=True, blank=True)

	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoDescarteFundo",null=True, blank=True)
	cant_jabas=models.IntegerField(null=True, blank=True)
	peso_bruto=models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	fecha_lanzado=models.DateField("Fecha Lanzado")

	peso_descarte= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	merma_maquina= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	merma_proceso= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	merma_recepcion= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	descarte_mini= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	recuperable= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	norecuperable= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDescarte")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDescarte",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Descarte Planta Athos'
		verbose_name_plural = 'Descarte Planta Athos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.fecha_lanzado, self.anexo_nave, self.anexo_material,self.fecha_hora_creacion)


class TipoSalidaDescarte(models.Model):
	
	desc= models.CharField("Tipo Salida Descarte", max_length=100,blank=True, null= True)

	
	


	class Meta:
		verbose_name = 'Tipo Salidad Descarte'
		verbose_name_plural = 'Tipo Salida Descarte'

	def __str__(self):
		return "%s-%s" % (self.id, self.desc)





class SalidaDescarte(models.Model):
	
	anexo_eje= models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeSalidaDescarte" ,null=True, blank=True)
	cantidad= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoSalidaDescarte" ,null=True, blank=True)
	anexo_tipo = models.ForeignKey(TipoSalidaDescarte, on_delete=models.CASCADE, related_name="AnexoCultivoSalidaDescarte" ,null=True, blank=True)
	nroguia= models.CharField("Nro Guia", max_length=100,blank=True, null= True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSalidaDescarte")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSalidaDescarte",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Salida Descarte'
		verbose_name_plural = 'Salida Descarte'

	def __str__(self):
		return "%s-%s" % (self.anexo_tipo, self.cantidad)

#DESCARTE PL HG 2022
class DescartePlantaHgAthos(models.Model):
	fecha_proceso = models.DateField("Fecha Proceso")
	anexo_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoDescarteTurnoHg2022",null=True, blank=True)
	anexo_planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoDescartePlantaHg2022",null=True, blank=True)
	anexo_material = models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, related_name="AnexoDescarteMMPPHg2022",null=True, blank=True)

	descarte1 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte2 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte3 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte4 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte5 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte6 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte7 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte8 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte9 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte10 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte11 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte12 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte13 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte14 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte15 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte16 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte17 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	descarte18 = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
	total_descarte = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDescarteHg2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDescarteHg2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Descarte Planta Hg Athos 2022'
		verbose_name_plural = 'Descarte Planta Hg Athos 2022'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.fecha_proceso, self.anexo_turno, self.anexo_planta,self.anexo_material)