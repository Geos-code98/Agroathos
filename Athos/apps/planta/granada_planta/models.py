from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import Planta
from apps.menu.models import Nave
from apps.menu.models import cultivo
from apps.menu.models import Estado
from apps.menu.models import EstadoPlanta
from apps.menu.models import Turno

from apps.planificacion.models import ProgramaProduccionPlanta
# Create your models here.

class LineasPlanta(models.Model):
	
	desc= models.CharField("Lineas", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Lineas Planta '
		verbose_name_plural = 'Lineas Planta '

	def __str__(self):
		return "%s" % ( self.desc)

class LineasPlantaHG(models.Model):
	desc= models.CharField("Lineas", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Lineas Planta HG'
		verbose_name_plural = 'Lineas Planta HG'

	def __str__(self):
		return "%s" % ( self.desc)

class UbicacionPlanta(models.Model):
	
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoUbicacionZona")
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoUbicacionPlanta")
	anexo_nave=models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="AnexoNavePlanta")
	anexo_cultivo=models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoUbicacionCultivo", blank=True, null=True)
	anexo_estado=models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="AnexoEstadoUbicacion", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUserCreateUbicacionPlantaAthos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUserEditUbicacionPlantaAthos",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Ubicacion Planta Produccion'
		verbose_name_plural = 'Ubicacion Planta Produccion'

	def __str__(self):
		return "%s-%s-%s" % ( self.anexo_zona,self.anexo_planta,self.anexo_nave)



class LanzadoPaletasGrIca2020(models.Model):
	anexo_ubicacion=models.ForeignKey(UbicacionPlanta, on_delete=models.CASCADE, related_name="AnexoLanzadoUbicacion2020GrIca", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzadoGrIca2020", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="AnexoEstadoPlantaGr2020Ica", blank=True, null=True)
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad",max_length=255, blank=True, null=True)
	
	pep=models.CharField("PEP",max_length=255, blank=True, null=True)
	material=models.CharField("Material",max_length=255, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionLanzadoGr2020")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModLanzadoGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado Planta Granada 2020-Ica'
		verbose_name_plural = 'Lanzado Planta Granada 2020-Ica'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)

#CAMPAÑA GRANADA 2021
class LanzadoPaletasGrIca2021(models.Model):
	anexo_ubicacion=models.ForeignKey(UbicacionPlanta, on_delete=models.CASCADE, related_name="AnexoLanzadoUbicacionGrIca2021", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzadoGrIca2021", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="AnexoEstadoPlantaGrIca2021", blank=True, null=True)
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad",max_length=255, blank=True, null=True)
	
	pep=models.CharField("PEP",max_length=255, blank=True, null=True)
	material=models.CharField("Material",max_length=255, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionLanzadoGr2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModLanzadoGr2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado Planta Granada Ica 2022'
		verbose_name_plural = 'Lanzado Planta Granada Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)

class LanzadoPaletasArIca2022(models.Model):
	anexo_ubicacion=models.ForeignKey(UbicacionPlanta, on_delete=models.CASCADE, related_name="AnexoLanzadoUbicacionArIca202202", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzadoArIca202202", blank=True, null=True)
	anexo_linea=models.ForeignKey(LineasPlantaHG, on_delete=models.CASCADE, related_name="AnexoLineaLanzadoArIca202202", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="AnexoEstadoPlantaArIca202202", blank=True, null=True)
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad",max_length=255, blank=True, null=True)
	
	pep=models.CharField("PEP",max_length=255, blank=True, null=True)
	material=models.CharField("Material",max_length=255, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionLanzadoAr202202")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModLanzadoAr202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado Planta Arandano Ica 2022'
		verbose_name_plural = 'Lanzado Planta Arandano Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)

class EstadoPrePalet(models.Model):
	
	estado= models.CharField("Estado", max_length=50,null=True, blank=True)
	
	class Meta:
		verbose_name = 'Estado Pre Paletizado'
		verbose_name_plural = 'Estado Pre Paletizado'

	def __str__(self):
		return "%s" % ( self.estado)



class PrePaletizadoGrIca2020(models.Model):
	anexo_produccion=models.ForeignKey(ProgramaProduccionPlanta, on_delete=models.CASCADE, related_name="AnexoProgramaProduccion2020GrIca", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoPrepaGrIca2020", blank=True, null=True)
	cantidad_cajas=models.IntegerField(blank=True, null=True)
	anexo_estado=models.ForeignKey(EstadoPrePalet, on_delete=models.CASCADE, related_name="AnexoEstadoPrepaGrIca2020", blank=True, null=True)
	observacion= models.CharField("Observacion", max_length=150,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionPaletizadoGr2020")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModPaletizadoGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Pre Paletizado Planta Granada 2020-Ica'
		verbose_name_plural = 'Pre Paletizado Planta Granada 2020-Ica'

	def __str__(self):
		return "%s-%s" % ( self.fecha_lanzado,self.anexo_produccion)

	@property
	def suma_cajas(self):
		consumos = self.AnexoDetPrepalizado2020GrIca.all()
		cant = 0
		for con in consumos:
			cant = cant + 1
		return (cant)

	@property
	def resto_cajas(self):
		return self.cantidad_cajas - self.suma_cajas


class DetallePrePaletizadoGrIca2020(models.Model):
	anexo_detalle=models.ForeignKey(PrePaletizadoGrIca2020, on_delete=models.CASCADE, related_name="AnexoDetPrepalizado2020GrIca", blank=True, null=True)
	traza = models.CharField("Trazabilidad",null=True, blank=True, max_length=20)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionDetPaletizadoGr2020")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModDetPaletizadoGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Detalle Pre Paletizado Planta Granada 2020-Ica'
		verbose_name_plural = 'Detalle Pre Paletizado Planta Granada 2020-Ica'

	def __str__(self):
		return "%s-%s" % ( self.anexo_detalle,self.traza)




#CAMPAÑA GRANADA 2023
class LanzadoPaletasGrIca2023(models.Model):
	anexo_ubicacion=models.ForeignKey(UbicacionPlanta, on_delete=models.CASCADE, related_name="AnexoLanzadoUbicacionGrIca2023", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzadoGrIca2023", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="AnexoEstadoPlantaGrIca2023", blank=True, null=True)
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad",max_length=255, blank=True, null=True)
	
	pep=models.CharField("PEP",max_length=255, blank=True, null=True)
	material=models.CharField("Material",max_length=255, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionLanzadoGr2023")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModLanzadoGr2023",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado Planta Granada Ica 2023'
		verbose_name_plural = 'Lanzado Planta Granada Ica 2023'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)
