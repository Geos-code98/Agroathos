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
class GuiaAthosHgPisco2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaHgPisco2021", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosHgPisco2021")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesHgPisco2021",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosHgPisco2021",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPHgPisco2021")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLHgPisco2021")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpHgPisco2021")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaHgPisco2021",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaHgPisco2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaHgPisco2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-HIGO-PIS-2021'
		verbose_name_plural = 'Guias Athos-HIGO-PIS-2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosHgPisco2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosHgPisco2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosHgPisco2021")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosHgPisco2021")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioHgPisco2021")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMHgPisco2021", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDHgPisco2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDHgPisco2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-HIGO-PIS-2021'
		verbose_name_plural = 'Guias  Detalles Athos-HIGO-PIS-2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosHgPisco2021.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletHgPisco2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosHgPisco2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosHgPisco2021")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenHgPisco2021", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaHgPisco2021", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsHgPisco2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsHgPisco2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-HIGO-PIS-2021'
		verbose_name_plural = 'Info Palets-HIGO-PIS-2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)



class AlmacenAcopioHgPisco2021(models.Model):
	
	codigoqr=models.CharField("Codigo Qr", max_length=200, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioHgPisco2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioHgPisco2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-HIGO-PIS-2021'
		verbose_name_plural = 'Almacen Acopio-HIGO-PIS-2021'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)

#CAMPAÑA HG 2022
class GuiaAthosHgPisco2022(models.Model):
	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaHgPisco2022", blank=True, null=True)
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosHgPisco2022")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesHgPisco2022",blank=True, null=True)
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosHgPisco2022",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPHgPisco2022")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLHgPisco2022")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpHgPisco2022")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaHgPisco2022",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaHgPisco2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaHgPisco2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-HIGO-PIS-2022'
		verbose_name_plural = 'Guias Athos-HIGO-PIS-2022'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)

class GuiaDetallesAthosHgPisco2022(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosHgPisco2022, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosHgPisco2022")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosHgPisco2022")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioHgPisco2022")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMHgPisco2022", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDHgPisco2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDHgPisco2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-HIGO-PIS-2022'
		verbose_name_plural = 'Guias  Detalles Athos-HIGO-PIS-2022'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosHgPisco2022.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets

class InfoPaletHgPisco2022(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosHgPisco2022, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosHgPisco2022")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenHgPisco2022", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaHgPisco2022", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsHgPisco2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsHgPisco2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-HIGO-PIS-2022'
		verbose_name_plural = 'Info Palets-HIGO-PIS-2022'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)

class AlmacenAcopioHgPisco2022(models.Model):	
	codigoqr=models.CharField("Codigo Qr", max_length=200, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioHgPisco2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioHgPisco2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-HIGO-PIS-2022'
		verbose_name_plural = 'Almacen Acopio-HIGO-PIS-2022'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)


#NEPEÑA 2021
class GuiaAthosHgNepena2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaHgNepena2021", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosHgNepena2021")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesHgNepena2021",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosHgNepena2021",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPHgNepena2021")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLHgNepena2021")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpHgNepena2021")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaHgNepena2021",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaHgNepena2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaHgNepena2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-HIGO-NEPEÑA-2021'
		verbose_name_plural = 'Guias Athos-HIGO-NEPEÑA-2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosHgNepena2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosHgNepena2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosHgNepena2021")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosHgNepena2021")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioHgNepena2021")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMHgNepena2021", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDHgNepena2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDHgNepena2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-HIGO-NEPEÑA-2021'
		verbose_name_plural = 'Guias  Detalles Athos- HIGO-NEPEÑA-2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosHgNepena2021.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletHgNepena2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosHgNepena2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosHgNepena2021")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenHgNepena2021", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaHgNepena2021", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsHgNepena2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsHgNepena2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-HIGO-NEPEÑA-2021'
		verbose_name_plural = 'Info Palets-HIGO-NEPEÑA-2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)



class AlmacenAcopioHgNepena2021(models.Model):
	
	codigoqr=models.CharField("Codigo Qr", max_length=200, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioHgNepena2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioHgNepena2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-HIGO-NEPEÑA-2021'
		verbose_name_plural = 'Almacen Acopio-HIGO-NEPEÑA-2021'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)


# CAMAPAÑA HG 2022
class GuiaAthosHgNepena2022(models.Model):
	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaHgNepena2022", blank=True, null=True)
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosHgNepena2022")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesHgNepena2022",blank=True, null=True)
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosHgNepena2022",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPHgNepena2022")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLHgNepena2022")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpHgNepena2022")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaHgNepena2022",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaHgNepena2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaHgNepena2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-HIGO-NEPEÑA-2022'
		verbose_name_plural = 'Guias Athos-HIGO-NEPEÑA-2022'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)

class GuiaDetallesAthosHgNepena2022(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosHgNepena2022, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosHgNepena2022")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosHgNepena2022")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioHgNepena2022")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMHgNepena2022", null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDHgNepena2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDHgNepena2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-HIGO-NEPEÑA-2022'
		verbose_name_plural = 'Guias  Detalles Athos- HIGO-NEPEÑA-2022'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosHgNepena2022.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets

class InfoPaletHgNepena2022(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosHgNepena2022, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosHgNepena2022")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenHgNepena2022", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaHgNepena2022", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsHgNepena2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsHgNepena2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-HIGO-NEPEÑA-2022'
		verbose_name_plural = 'Info Palets-HIGO-NEPEÑA-2022'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)

class AlmacenAcopioHgNepena2022(models.Model):
	codigoqr=models.CharField("Codigo Qr", max_length=200, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioHgNepena2022", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioHgNepena2022",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-HIGO-NEPEÑA-2022'
		verbose_name_plural = 'Almacen Acopio-HIGO-NEPEÑA-2022'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)