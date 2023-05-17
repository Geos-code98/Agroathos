from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import cultivo
from apps.menu.models import ejezona
from apps.menu.models import fundo
from apps.menu.models import VariableAgronomica
from apps.menu.models import ProgramaProduccion
from apps.menu.models import SubVariableAgronomica
from apps.menu.models import UbicacionFundo
from apps.menu.models import VersionAgronomica
from apps.menu.models import variedad



# Create your models here.
class ProyeccionArandano(models.Model):
	anio= models.CharField("Año", max_length=30,null=True, blank=True)
	semana= models.CharField("Semana", max_length=30,null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE)
	anexo_eje=models.ForeignKey(ejezona, on_delete=models.CASCADE,null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE,null=True, blank=True)
	anexo_variable=models.ForeignKey(VariableAgronomica, on_delete=models.CASCADE,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionProyeccionArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionProyeccionArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'EV. Proyeccion Arandano'
		verbose_name_plural = ' EV. Proyecciones Arandanos'

	def __str__(self):
		return "%s-%s-%s-%s-%s-%s" % (self.anexo_eje,self.anexo_fundo,self.anio, self.semana,self.anexo_cultivo,self.fecha_hora_creacion)

class DetalleProyeccionArandano(models.Model):
	anexo_detalle=models.ForeignKey(ProyeccionArandano, on_delete=models.CASCADE,null=True, blank=True)
	anexo_pep=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE,null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE,null=True, blank=True)
	anexo_subvariable=models.ForeignKey(SubVariableAgronomica, on_delete=models.CASCADE)
	lunes= models.IntegerField("Lunes",null=True, blank=True)
	martes= models.IntegerField("Martes",null=True, blank=True)
	miercoles= models.IntegerField("Miercoles",null=True, blank=True)
	jueves= models.IntegerField("Jueves",null=True, blank=True)
	viernes= models.IntegerField("Viernes",null=True, blank=True)
	sabado= models.IntegerField("Sabado",null=True, blank=True)
	domingo= models.IntegerField("Domingo",null=True, blank=True)

	semana2=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	semana3=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	semana4=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

	lunes_sem2= models.IntegerField("Lunes2",null=True, blank=True)
	martes_sem2= models.IntegerField("Martes2",null=True, blank=True)
	miercoles_sem2= models.IntegerField("Miercoles2",null=True, blank=True)
	jueves_sem2= models.IntegerField("Jueves2",null=True, blank=True)
	viernes_sem2= models.IntegerField("Viernes2",null=True, blank=True)
	sabado_sem2= models.IntegerField("Sabado2",null=True, blank=True)
	domingo_sem2= models.IntegerField("Domingo2",null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionDetProyeccionArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionDetProyeccionArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'EV. Detalle Proyeccion Arandano'
		verbose_name_plural = 'EV. Detalle Proyecciones Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_pep, self.anexo_subvariable, self.fecha_hora_creacion)

class ProyeccionSemanalArandano(models.Model):
	
	
	anexo_semanal=models.ForeignKey(ProyeccionArandano, on_delete=models.CASCADE)
	lunes= models.IntegerField("Lunes",null=True, blank=True)
	martes= models.IntegerField("Martes",null=True, blank=True)
	miercoles= models.IntegerField("Miercoles",null=True, blank=True)
	jueves= models.IntegerField("Jueves",null=True, blank=True)
	viernes= models.IntegerField("Viernes",null=True, blank=True)
	sabado= models.IntegerField("Sabado",null=True, blank=True)
	domingo= models.IntegerField("Domingo",null=True, blank=True)
	semana1=models.IntegerField("Semana 1",null=True, blank=True)
	semana2=models.IntegerField("Semana 2 ",null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionProyeccionSemArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionProyeccionSemArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	
	class Meta:
		verbose_name = ' Proyeccion Semanal Arandano'
		verbose_name_plural = ' Proyecciones  Semanales Arandanos'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_semanal, self.lunes, self.fecha_hora_creacion)

class ProyeccionDiariaArandano(models.Model):
	anio= models.CharField("Año", max_length=30,null=True, blank=True)
	semana= models.CharField("Semana", max_length=30,null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoArandano")
	anexo_eje=models.ForeignKey(ejezona, on_delete=models.CASCADE,null=True, blank=True, related_name="AnexoEjeArandano")
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE,null=True, blank=True,related_name="AnexoFundoArandano")
	
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionProyeccionDiariaArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionProyeccionDiariaArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'Proyeccion Arandano Diaria'
		verbose_name_plural = 'Proyecciones Arandanos Diarias'

	def __str__(self):
		return "%s-%s-%s-%s-%s-%s" % (self.anexo_eje,self.anexo_fundo,self.anexo_cultivo,self.anio, self.semana, self.fecha_hora_creacion)

class DetProyeccionDiariaArandano(models.Model):
	anexo_detalle=models.ForeignKey(ProyeccionDiariaArandano, on_delete=models.CASCADE,null=True, blank=True)
	anexo_pep=models.ForeignKey(ProgramaProduccion,related_name="AnexoDiariaFundoPep", on_delete=models.CASCADE,null=True, blank=True)
	anexo_variedad=models.ForeignKey(variedad, on_delete=models.CASCADE,null=True, blank=True)
	
	lunes= models.IntegerField("Lunes",null=True, blank=True)
	martes= models.IntegerField("Martes",null=True, blank=True)
	miercoles= models.IntegerField("Miercoles",null=True, blank=True)
	jueves= models.IntegerField("Jueves",null=True, blank=True)
	viernes= models.IntegerField("Viernes",null=True, blank=True)
	sabado= models.IntegerField("Sabado",null=True, blank=True)
	domingo= models.IntegerField("Domingo",null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserCreacionDetProyeccionDiariaArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModificacionDetProyeccionDiariaArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'Detalle Proyeccion Diaria Arandano'
		verbose_name_plural = 'Detalle Proyecciones Diarias Arandanos'

	def __str__(self):
		return "%s-%s-%s-%s" % (self.id,self.anexo_detalle,self.anexo_pep, self.fecha_hora_creacion)


class ProyeccionAnualArandano(models.Model):
	anio= models.CharField("Año", max_length=30,null=True, blank=True)
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE)
	anexo_eje=models.ForeignKey(ejezona, on_delete=models.CASCADE,null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE,null=True, blank=True)
	anexo_variable=models.ForeignKey(VariableAgronomica, on_delete=models.CASCADE,null=True, blank=True)
	anexo_version =models.ForeignKey(VersionAgronomica, on_delete=models.CASCADE,null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionProyeccionAnArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionProyeccionAnArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'Proyeccion Arandano Anuales'
		verbose_name_plural = 'Proyecciones Arandanos Anuales'

	def __str__(self):
		return "%s-%s-%s-%s-%s" % (self.anexo_eje,self.anexo_fundo , self.anio, self.anexo_cultivo, self.fecha_hora_creacion)

class DetalleProyeccionAnualArandano(models.Model):
	anexo_detalle=models.ForeignKey(ProyeccionAnualArandano, on_delete=models.CASCADE,null=True, blank=True)
	anexo_pep=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE,null=True, blank=True)
	anexo_subvariable=models.ForeignKey(SubVariableAgronomica, on_delete=models.CASCADE)
	anexo_aniocampana=models.CharField("Año Campaña", max_length=30,null=True, blank=True)
	anexo_varpep=models.CharField("VAR PEP", max_length=30,null=True, blank=True)
	anexo_aniocosecha=models.CharField("Año Cosecha", max_length=30,null=True, blank=True)
	
	semana1= models.IntegerField("Semana1",null=True, blank=True)
	semana2= models.IntegerField("Semana2",null=True, blank=True)
	semana3= models.IntegerField("Semana3",null=True, blank=True)
	semana4= models.IntegerField("Semana4",null=True, blank=True)
	semana5= models.IntegerField("Semana5",null=True, blank=True)
	semana6= models.IntegerField("Semana6",null=True, blank=True)
	semana7= models.IntegerField("Semana7",null=True, blank=True)
	semana8= models.IntegerField("Semana8",null=True, blank=True)
	semana9= models.IntegerField("Semana9",null=True, blank=True)
	semana10= models.IntegerField("Semana10",null=True, blank=True)
	semana11= models.IntegerField("Semana11",null=True, blank=True)
	semana12= models.IntegerField("Semana12",null=True, blank=True)
	semana13= models.IntegerField("Semana13",null=True, blank=True)
	semana14= models.IntegerField("Semana14",null=True, blank=True)
	semana15= models.IntegerField("Semana15",null=True, blank=True)
	semana16= models.IntegerField("Semana16",null=True, blank=True)
	semana17= models.IntegerField("Semana17",null=True, blank=True)
	semana18= models.IntegerField("Semana18",null=True, blank=True)
	semana19= models.IntegerField("Semana19",null=True, blank=True)
	semana20= models.IntegerField("Semana20",null=True, blank=True)
	semana21= models.IntegerField("Semana21",null=True, blank=True)
	semana22= models.IntegerField("Semana22",null=True, blank=True)
	semana23= models.IntegerField("Semana23",null=True, blank=True)
	semana24= models.IntegerField("Semana24",null=True, blank=True)
	semana25= models.IntegerField("Semana25",null=True, blank=True)
	semana26= models.IntegerField("Semana26",null=True, blank=True)
	semana27= models.IntegerField("Semana27",null=True, blank=True)
	semana28= models.IntegerField("Semana28",null=True, blank=True)
	semana29= models.IntegerField("Semana29",null=True, blank=True)
	semana30= models.IntegerField("Semana30",null=True, blank=True)
	semana31= models.IntegerField("Semana31",null=True, blank=True)
	semana32= models.IntegerField("Semana32",null=True, blank=True)
	semana33= models.IntegerField("Semana33",null=True, blank=True)
	semana34= models.IntegerField("Semana34",null=True, blank=True)
	semana35= models.IntegerField("Semana35",null=True, blank=True)
	semana36= models.IntegerField("Semana36",null=True, blank=True)
	semana37= models.IntegerField("Semana37",null=True, blank=True)
	semana38= models.IntegerField("Semana38",null=True, blank=True)
	semana39= models.IntegerField("Semana39",null=True, blank=True)
	semana40= models.IntegerField("Semana40",null=True, blank=True)
	semana41= models.IntegerField("Semana41",null=True, blank=True)
	semana42= models.IntegerField("Semana42",null=True, blank=True)
	semana43= models.IntegerField("Semana43",null=True, blank=True)
	semana44= models.IntegerField("Semana44",null=True, blank=True)
	semana45= models.IntegerField("Semana45",null=True, blank=True)
	semana46= models.IntegerField("Semana46",null=True, blank=True)
	semana47= models.IntegerField("Semana47",null=True, blank=True)
	semana48= models.IntegerField("Semana48",null=True, blank=True)
	semana49= models.IntegerField("Semana49",null=True, blank=True)
	semana50= models.IntegerField("Semana50",null=True, blank=True)
	semana51= models.IntegerField("Semana51",null=True, blank=True)
	semana52= models.IntegerField("Semana52",null=True, blank=True)
	semana53= models.IntegerField("Semana53",null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionDetProyeccionAnArandano",null=True, blank=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True,null=True, blank=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionDetProyeccionAnArandano",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)	

	class Meta:
		verbose_name = 'Detalle Proyeccion Anuales Arandano'
		verbose_name_plural = 'Detalle Proyecciones Anuales Arandanos'

	def __str__(self):
		return "%s-%s" % (self.anexo_pep, self.anexo_subvariable)