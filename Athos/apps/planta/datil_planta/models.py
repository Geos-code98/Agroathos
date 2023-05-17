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


from apps.planta.granada_planta.models import UbicacionPlanta
# Create your models here.


class LanzadoPaletasDtIca2022(models.Model):
	anexo_ubicacion=models.ForeignKey(UbicacionPlanta, on_delete=models.CASCADE, related_name="AnexoLanzadoUbicacionDtIca2022", blank=True, null=True)
	fecha_lanzado = models.DateField("Fecha Lanzado",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoTurnoLanzadoDtIca2022", blank=True, null=True)
	linea=models.CharField("Linea",max_length=255, blank=True, null=True)
	leerqr=models.CharField("leer qr",max_length=255, blank=True, null=True, unique=True)
	npalet=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	njabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	peso=models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
	estado=models.ForeignKey(EstadoPlanta, on_delete=models.CASCADE, related_name="AnexoEstadoPlantaDtIca2022", blank=True, null=True)
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad",max_length=255, blank=True, null=True)
	
	pep=models.CharField("PEP",max_length=255, blank=True, null=True)
	material=models.CharField("Material",max_length=255, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioCreacionLanzadoDtIca2022")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuarioModLanzadoDtIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Lanzado Planta Datil Ica - 2022'
		verbose_name_plural = 'Lanzado Planta Datil Ica - 2022'

	def __str__(self):
		return "%s-%s" % ( self.leerqr,self.linea)

