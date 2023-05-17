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
# Create your models here.
class GuiaAthosDt2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaDt2020", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosDt2020")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesDt2020",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosDt2020",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPDt2020")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLDt2020")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpDt2020")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaDt2020",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaDt2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDt2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-DATIL 2021'
		verbose_name_plural = 'Guias Athos-DATIL 2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosDt2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosDt2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosDt2020")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosDt2020Athos")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioDt2020")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMDt2020", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDDt2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDDt2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Datil 2021'
		verbose_name_plural = 'Guias  Detalles Athos- Datil 2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosDt2020.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletDt2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosDt2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosDt2020")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenDt2020", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaDt2020", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsDt2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsDt2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-DATIL 2021'
		verbose_name_plural = 'Info Palets-DATIL 2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)



#CAMPAÑA DT - ICA - 2022
class GuiaAthosDtIca2022(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaDtIca2022", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosDtIca2022")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesDtIca2022",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosDtIca2022",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPDtIca2022")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLDtIca2022")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpDtIca2022")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaDtIca2022",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaDtIca2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDtIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-DATIL Ica 2022'
		verbose_name_plural = 'Guias Athos-DATIL Ica 2022'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosDtIca2022(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosDtIca2022, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosDtIca2022")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosDtIca2022Athos")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioDtIca2022")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMDtIca2022", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDDtIca2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDDtIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Datil Ica 2022'
		verbose_name_plural = 'Guias  Detalles Athos- Datil Ica 2022'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosDtIca2022.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletDtIca2022(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosDtIca2022, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosDtIca2022")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenDtIca2022", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaDtIca2022", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsDtIca2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsDtIca2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-DATIL Ica 2022'
		verbose_name_plural = 'Info Palets-DATIL Ica 2022'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)