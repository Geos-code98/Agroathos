from django.db import models
from django.contrib.auth.models import User
from apps.menu.models import ejezona
from apps.menu.models import AlmacenesAthos
from apps.menu.models import ChoferesVehiculos
from apps.menu.models import PlacasVehiculares
from apps.menu.models import LugarAthos
from apps.menu.models import DatosEmpresa
from apps.menu.models import ProgramaProduccion
from apps.menu.models import MaterialAcopio
from apps.menu.models import CalidadProducto
from apps.menu.models import TipoParihuela
from apps.menu.models import fundo
from apps.menu.models import MaterialTransporte
from apps.acopio_athos.granada.models import TipoCalidadFruta
# Create your models here.

class GuiaAthosAgCaraz2022(models.Model):
	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaAthosAgCaraz2022", blank=True, null=True)
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaGuiaAthosAgCaraz2022")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGuiaAthosAgCaraz2022",blank=True, null=True)
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGuiaAthosAgCaraz2022",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi1GuiaAthosAgCaraz2022")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi2GuiaAthosAgCaraz2022")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosGuiaAthosAgCaraz2022")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaAthosAgCaraz2022",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaAthosAgCaraz2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaAthosAgCaraz2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos Caraz Aguaymanto 2022'
		verbose_name_plural = 'Guias Athos Caraz Aguaymanto 2022'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)

class GuiaDetallesAthosAgCaraz2022(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosAgCaraz2022, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosAgCaraz2022")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosAgCaraz2022")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioAgCaraz2022")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMAgCaraz2022", null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDAgCaraz2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDAgCaraz2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos Caraz Aguaymanto 2022'
		verbose_name_plural = 'Guias  Detalles Athos Caraz  Aguaymanto 2022'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosAgCaraz2022.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets

class InfoPaletAgCaraz2022(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosAgCaraz2022, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosAgCaraz2022")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenAgCaraz2022", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaAgCaraz2022", blank=True, null=True)
	cant_clamshell=models.DecimalField(max_digits=5, decimal_places=0)
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatEnvaseAgCaraz2022", blank=True, null=True)
	anexo_tipocalidadfruta=models.ForeignKey(TipoCalidadFruta, on_delete=models.CASCADE, related_name="AnexoTIpoCalFrutaAgCaraz2022", blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsAgCaraz2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsAgCaraz2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet Aguaymanto Caraz 2022'
		verbose_name_plural = 'Info Palets Aguaymanto Caraz 2022'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)