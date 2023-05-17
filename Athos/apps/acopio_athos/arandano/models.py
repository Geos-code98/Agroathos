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
from apps.maestras.models import AuxiliaresCampoAthos
from apps.acopio.models import LadosTunel
from apps.acopio_athos.granada.models import TipoCalidadFruta

# Create your models here.

class GuiaAthosArCaraz2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaAthosArCaraz2021", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaGuiaAthosArCaraz2021")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGuiaAthosArCaraz2021",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGuiaAthosArCaraz2021",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi1GuiaAthosArCaraz2021")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi2GuiaAthosArCaraz2021")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosGuiaAthosArCaraz2021")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaAthosArCaraz2021",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaAthosArCaraz2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaAthosArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-Caraz Arandanos 2021'
		verbose_name_plural = 'Guias Athos-Caraz Arandanos 2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)


class GuiaDetallesAthosArCaraz2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosArCaraz2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosArCaraz2021")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosArCaraz2021")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioArCaraz2021")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMArCaraz2021", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDArCaraz2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Caraz Arandanos 2021'
		verbose_name_plural = 'Guias  Detalles Athos-Caraz  Arandanos 2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosArCaraz2021.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_clamshell
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets


class InfoPaletArCaraz2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosArCaraz2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosArCaraz2021")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenArCaraz2021", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaArCaraz2021", blank=True, null=True)

	cant_clamshell=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatEnvaseArCaraz2021", blank=True, null=True)
	anexo_tipocalidadfruta=models.ForeignKey(TipoCalidadFruta, on_delete=models.CASCADE, related_name="AnexoTIpoCalFrutaArCaraz2021", blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsArCaraz2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsArCaraz2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-Arandanos Caraz 2021'
		verbose_name_plural = 'Info Palets-Arandanos Caraz 2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)


class GuiaAthosArIca2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaAthosArIca2021", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaGuiaAthosArIca2021")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGuiaAthosArIca2021",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGuiaAthosArIca2021",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi1GuiaAthosArIca2021")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi2GuiaAthosArIca2021")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosGuiaAthosArIca2021")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaAthosArIca2021",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaAthosArIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaAthosArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-Ica Arandanos 2021'
		verbose_name_plural = 'Guias Athos-Ica Arandanos 2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)


class GuiaDetallesAthosArIca2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosArIca2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosArIca2021")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosArIca2021")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioArIca2021")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMArIca2021", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDArIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Ica Arandanos 2021'
		verbose_name_plural = 'Guias  Detalles Athos-Ica  Arandanos 2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosArIca2021.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_clamshell
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets


class InfoPaletArIca2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosArIca2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosArIca2021")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenArIca2021", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaArIca2021", blank=True, null=True)

	cant_clamshell=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatEnvaseArIca2021", blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsArIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-Arandanos Ica 2021'
		verbose_name_plural = 'Info Palets-Arandanos Ica 2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)




#campaña2021-1-ENFRIADO ICA 
class ModEnfriadoArIca2021(models.Model):
	fecha=models.DateField("Fecha de Enfriado")
	cod_termometro= models.CharField("Codigo de termometro", max_length=30,null=True, blank=True)
	cod_vac1= models.CharField("Codigo de Vacuometro 1", max_length=30,null=True, blank=True)
	cod_vac2= models.CharField("Codigo de Vacuometro 2", max_length=30,null=True, blank=True)
	cod_vac3= models.CharField("Codigo de Vacuometro 3", max_length=30,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionEnfriadoArIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModEnfriadoArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	

	class Meta:
		verbose_name = 'Modulo Enfriado-Arandano Ica 2021'
		verbose_name_plural = 'Modulo de Enfriado-Arandano Ica 2021'

	def __str__(self):
		return "%s-%s" % (self.fecha, self.cod_termometro)


class DistribucionEnfriadoArIca2021(models.Model):
	anexo_enfriado=models.ForeignKey(ModEnfriadoArIca2021, on_delete=models.CASCADE, related_name="AnexoEnfriadoDistribucionArIca2021",null=True, blank=True)
	anexo_lado=models.ForeignKey(LadosTunel, on_delete=models.CASCADE, related_name="AnexoLadoTunelDArIca2021",null=True, blank=True)
	tunel=models.IntegerField(null=True, blank=True)
	#n_tunel es numero de compartimento
	n_tunel= models.CharField(max_length=100,null=True, blank=True)

	lectura_qr= models.CharField("Lectura QR", max_length=100, unique=True)
	n_palet= models.DecimalField(max_digits=5, decimal_places=0)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDistribucionArIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDistribucionArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Distribucion Enfriado-Arandano Ica 2021'
		verbose_name_plural = 'Distribucion Enfriado-Arandano Ica 2021'

	def __str__(self):
		return "%s-%s" % (self.n_palet, self.n_tunel)
		

class TemperaturaEnfriadoArIca2021(models.Model):
	anexo_temperatura=models.ForeignKey(DistribucionEnfriadoArIca2021, on_delete=models.CASCADE, related_name="AnexoTemperaturaEnfriadoArIca2021",null=True, blank=True)
	m_tempambiente= models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
	m_tempinterna= models.DecimalField(max_digits=5, decimal_places=2)
	m_tempexterna= models.DecimalField(max_digits=5, decimal_places=2)
	

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTemperaturaArIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTemperaturaArIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Temperatura Enfriado-Arandanos Ica 2021'
		verbose_name_plural = 'Temperatura Enfriado-Arandanos Ica 2021'

	def __str__(self):
		return "%s-%s" % (self.id, self.anexo_temperatura) 


#CAMPAÑA 2022-2 PALET AR CARAZ
class GuiaAthosArCaraz202202(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaAthosArCaraz202202", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaGuiaAthosArCaraz202202")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGuiaAthosArCaraz202202",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGuiaAthosArCaraz202202",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi1GuiaAthosArCaraz202202")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi2GuiaAthosArCaraz202202")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosGuiaAthosArCaraz202202")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaAthosArCaraz202202",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaAthosArCaraz202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaAthosArCaraz202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-Caraz Arandanos 2022-02'
		verbose_name_plural = 'Guias Athos-Caraz Arandanos 2022-02'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)

class GuiaDetallesAthosArCaraz202202(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosArCaraz202202, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosArCaraz202202")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosArCaraz202202")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioArCaraz202202")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMArCaraz202202", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDArCaraz202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDArCaraz202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Caraz Arandanos 2022-02'
		verbose_name_plural = 'Guias  Detalles Athos-Caraz  Arandanos 2022-02'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosArCaraz202202.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets

class InfoPaletArCaraz202202(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosArCaraz202202, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosArCaraz202202")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenArCaraz202202", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaArCaraz202202", blank=True, null=True)

	cant_clamshell=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatEnvaseArCaraz202202", blank=True, null=True)
	anexo_tipocalidadfruta=models.ForeignKey(TipoCalidadFruta, on_delete=models.CASCADE, related_name="AnexoTIpoCalFrutaArCaraz202202", blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsArCaraz202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsArCaraz202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-Arandanos Caraz 2022-02'
		verbose_name_plural = 'Info Palets-Arandanos Caraz 2022-02'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)




#CAMPAÑANA 2022-2 PALET AR ICA
class GuiaAthosArIca202202(models.Model):
	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaAthosArIca202202", blank=True, null=True)
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaGuiaAthosArIca202202")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGuiaAthosArIca202202",blank=True, null=True)
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGuiaAthosArIca202202",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi1GuiaAthosArIca202202")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbi2GuiaAthosArIca202202")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosGuiaAthosArIca202202")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaAthosArIca202202",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaAthosArIca202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaAthosArIca202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-Ica Arandanos 2022 - 02'
		verbose_name_plural = 'Guias Athos-Ica Arandanos 2022 - 02'

	def __str__(self):
		return "%s-%s" % ( self.id,self.NroGuia)

class GuiaDetallesAthosArIca202202(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosArIca202202, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosArIca202202")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosArIca202202")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioArIca202202")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMArIca202202", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDArIca202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDArIca202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Ica Arandanos 2022 - 02'
		verbose_name_plural = 'Guias  Detalles Athos-Ica  Arandanos 2022 - 02'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosArIca202202.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets

class InfoGuiaAthosArIca202202(models.Model):
	anexo_guia = models.ForeignKey(GuiaAthosArIca202202, on_delete=models.CASCADE, related_name="AnexoInfoGuiaAthosArIca202202")
	anexo_auxiliar = models.ForeignKey(AuxiliaresCampoAthos, on_delete=models.CASCADE, related_name="AnexoAuxCampoAthosArIca202202")
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioInfoGuiaArIca202202", blank=True, null=True)
	sub_lote = models.CharField("SUB LOTE", max_length=10, blank=True, null=True)
	cant_envases = models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioInfoGuiaArIca202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionInfoGuiaArIca202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Guia Athos-Ica Arandano 2022 - 02'
		verbose_name_plural = 'Infos de Guias Athos-Ica Arandanos 2022 - 02'

	def __str__(self):
		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_auxiliar)

class InfoPaletArIca202202(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosArIca202202, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosArIca202202")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenArIca202202", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaArIca202202", blank=True, null=True)
	cant_clamshell=models.DecimalField(max_digits=5, decimal_places=0)
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0,blank=True, null=True)
	anexo_envase=models.ForeignKey(MaterialTransporte, on_delete=models.CASCADE, related_name="AnexoMatEnvaseArIca202202", blank=True, null=True)
	anexo_tipocalidadfruta=models.ForeignKey(TipoCalidadFruta, on_delete=models.CASCADE, related_name="AnexoTIpoCalFrutaArIca202202", blank=True, null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsArIca202202", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsArIca202202",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-Arandanos Ica 2022 - 02'
		verbose_name_plural = 'Info Palets-Arandanos Ica 2022 - 02'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)