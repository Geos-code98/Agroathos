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
from apps.menu.models import Planta
from apps.menu.models import Nave
from apps.menu.models import Turno
from apps.menu.models import MaterialMMPP
from apps.menu.models import cultivo
from apps.planta.granada_planta.models import LineasPlanta

# Create your models here.
class TipoCalidadFruta(models.Model):
	
	desc= models.CharField("Tipo Calidad Fruta", max_length=100,blank=True, null= True)

	class Meta:
		verbose_name = 'Tipo  Calidad de fruta'
		verbose_name_plural = 'Tipo Calidad de fruta'

	def __str__(self):
		return "%s-%s" % (self.id, self.desc)

#campaña granada 2020
class GuiaAthosGr2020(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaGr2020", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosGr2020")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGr2020",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGr2020",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPGr2020")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLGr2020")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpGr2020")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaGr2020",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaGr2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-GRANADA 2020'
		verbose_name_plural = 'Guias Athos-GRANADA 2020'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosGr2020(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosGr2020, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosGr2020")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosGr2020Athos")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioGr2020")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMGr2020", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDGr2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Granada 2020'
		verbose_name_plural = 'Guias  Detalles Athos- Granada 2020'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosGr2020.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletGr2020(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosGr2020, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosGr2020")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenGr2020", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaGr2020", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsGr2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-GRANADA 2020'
		verbose_name_plural = 'Info Palets-GRANADA 2020'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)



class AlmacenAcopioGr2020(models.Model):
	
	codigoqr=models.CharField("Codigo Qr", max_length=30, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioGr2020", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioGr2020",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-GRANADA 2020'
		verbose_name_plural = 'Almacen Acopio-GRANADA 2020'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)


#campaña granada 2021-Acopio
class GuiaAthosGrIca2021(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaGrIca2021", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosGrIca2021")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGrIca2021",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGrIca2021",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPGrIca2021")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLGrIca2021")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpGrIca2021")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaGrIca2021",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaGrIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-GRANADA 2021'
		verbose_name_plural = 'Guias Athos-GRANADA 2021'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosGrIca2021(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosGrIca2021, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosGrIca2021")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosGrIca2021")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioGrIca2021")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMGrIca2021", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDGrIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Granada 2021'
		verbose_name_plural = 'Guias  Detalles Athos- Granada 2021'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosGrIca2021.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletGrIca2021(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosGrIca2021, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosGrIca2021")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenGrIca2021", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaGrIca2021", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsGrIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-GRANADA ICA 2021'
		verbose_name_plural = 'Info Palets-GRANADA ICA 2021'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)



class AlmacenAcopioGrIca2021(models.Model):
	
	codigoqr=models.CharField("Codigo Qr", max_length=100, blank=True, null=True, unique=True)
	posicion=models.IntegerField(blank=True, null=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionAlmacenAcopioGrIca2021", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionnAlmacenAcopioGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Almacen Acopio-GRANADA 2021'
		verbose_name_plural = 'Almacen Acopio-GRANADA 2021'

	def __str__(self):
		return "%s-%s" % ( self.codigoqr,self.posicion)


#Descarte
class DescarteAthosGrIca2021(models.Model):
	anexo_eje=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoDescarteEjeGrIca2021",null=True, blank=True)
	anexo_planta=models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="AnexoDescartePlantaGrIca2021",null=True, blank=True)
	anexo_material=models.ForeignKey(MaterialMMPP, on_delete=models.CASCADE, related_name="AnexoDescarteMatmpGrIca2021",null=True, blank=True)
	anexo_turno=models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="AnexoDescarteTurnoGrIca2021",null=True, blank=True)
	trazabilidad=models.CharField("Trazabilidad", max_length=30, blank=True, null=True, unique=True)
	
	anexo_linea=models.ForeignKey(LineasPlanta, on_delete=models.CASCADE,null=True, blank=True)
	alternaria=models.IntegerField(null=True, blank=True)
	bajo_peso=models.IntegerField(null=True, blank=True)
	cochinilla=models.IntegerField(null=True, blank=True)
	deformes=models.IntegerField(null=True, blank=True)
	danio_mecanico=models.IntegerField(null=True, blank=True)
	danio_mecanico_campo=models.IntegerField(null=True, blank=True)
	danio_roedor=models.IntegerField(null=True, blank=True)
	gelechidae=models.IntegerField(null=True, blank=True)
	hongo_corona=models.IntegerField(null=True, blank=True)
	inmadurez_verde=models.IntegerField(null=True, blank=True)
	insolacion_fuerte=models.IntegerField(null=True, blank=True)
	pudricion=models.IntegerField(null=True, blank=True)
	quereza=models.IntegerField(null=True, blank=True)
	rajadas_ae=models.IntegerField(null=True, blank=True)
	rajadas_golpe=models.IntegerField(null=True, blank=True)
	calibre18=models.IntegerField(null=True, blank=True)
	danio_industrial=models.IntegerField(null=True, blank=True)
	arilo_pardo=models.IntegerField(null=True, blank=True)
	hongo_industrial=models.IntegerField(null=True, blank=True)


	alternaria_linea2=models.IntegerField(null=True, blank=True)
	bajo_peso_linea2=models.IntegerField(null=True, blank=True)
	cochinilla_linea2=models.IntegerField(null=True, blank=True)
	deformes_linea2=models.IntegerField(null=True, blank=True)
	danio_mecanico_linea2=models.IntegerField(null=True, blank=True)
	danio_mecanico_campo_linea2=models.IntegerField(null=True, blank=True)
	danio_roedor_linea2=models.IntegerField(null=True, blank=True)
	gelechidae_linea2=models.IntegerField(null=True, blank=True)
	hongo_corona_linea2=models.IntegerField(null=True, blank=True)
	inmadurez_verde_linea2=models.IntegerField(null=True, blank=True)
	insolacion_fuerte_linea2=models.IntegerField(null=True, blank=True)
	pudricion_linea2=models.IntegerField(null=True, blank=True)
	quereza_linea2=models.IntegerField(null=True, blank=True)
	rajadas_ae_linea2=models.IntegerField(null=True, blank=True)
	rajadas_golpe_linea2=models.IntegerField(null=True, blank=True)
	calibre18_linea2=models.IntegerField(null=True, blank=True)
	danio_industrial_linea2=models.IntegerField(null=True, blank=True)
	arilo_pardo_linea2=models.IntegerField(null=True, blank=True)
	hongo_industrial_linea2=models.IntegerField(null=True, blank=True)

	alternaria_linea3=models.IntegerField(null=True, blank=True)
	bajo_peso_linea3=models.IntegerField(null=True, blank=True)
	cochinilla_linea3=models.IntegerField(null=True, blank=True)
	deformes_linea3=models.IntegerField(null=True, blank=True)
	danio_mecanico_linea3=models.IntegerField(null=True, blank=True)
	danio_mecanico_campo_linea3=models.IntegerField(null=True, blank=True)
	danio_roedor_linea3=models.IntegerField(null=True, blank=True)
	gelechidae_linea3=models.IntegerField(null=True, blank=True)
	hongo_corona_linea3=models.IntegerField(null=True, blank=True)
	inmadurez_verde_linea3=models.IntegerField(null=True, blank=True)
	insolacion_fuerte_linea3=models.IntegerField(null=True, blank=True)
	pudricion_linea3=models.IntegerField(null=True, blank=True)
	quereza_linea3=models.IntegerField(null=True, blank=True)
	rajadas_ae_linea3=models.IntegerField(null=True, blank=True)
	rajadas_golpe_linea3=models.IntegerField(null=True, blank=True)
	calibre18_linea3=models.IntegerField(null=True, blank=True)
	danio_industrial_linea3=models.IntegerField(null=True, blank=True)
	arilo_pardo_linea3=models.IntegerField(null=True, blank=True)
	hongo_industrial_linea3=models.IntegerField(null=True, blank=True)

	alternaria_linea4=models.IntegerField(null=True, blank=True)
	bajo_peso_linea4=models.IntegerField(null=True, blank=True)
	cochinilla_linea4=models.IntegerField(null=True, blank=True)
	deformes_linea4=models.IntegerField(null=True, blank=True)
	danio_mecanico_linea4=models.IntegerField(null=True, blank=True)
	danio_mecanico_campo_linea4=models.IntegerField(null=True, blank=True)
	danio_roedor_linea4=models.IntegerField(null=True, blank=True)
	gelechidae_linea4=models.IntegerField(null=True, blank=True)
	hongo_corona_linea4=models.IntegerField(null=True, blank=True)
	inmadurez_verde_linea4=models.IntegerField(null=True, blank=True)
	insolacion_fuerte_linea4=models.IntegerField(null=True, blank=True)
	pudricion_linea4=models.IntegerField(null=True, blank=True)
	quereza_linea4=models.IntegerField(null=True, blank=True)
	rajadas_ae_linea4=models.IntegerField(null=True, blank=True)
	rajadas_golpe_linea4=models.IntegerField(null=True, blank=True)
	calibre18_linea4=models.IntegerField(null=True, blank=True)
	danio_industrial_linea4=models.IntegerField(null=True, blank=True)
	arilo_pardo_linea4=models.IntegerField(null=True, blank=True)
	hongo_industrial_linea4=models.IntegerField(null=True, blank=True)
	
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoDescarteFundoGrIca2021",null=True, blank=True)
	cant_jabas=models.IntegerField(null=True, blank=True)
	peso_bruto=models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	fecha_lanzado=models.DateField("Fecha Lanzado")
	fecha_cosecha=models.DateField("Fecha Cosecha",null=True, blank=True)

	peso_descarte= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDescarteGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDescarteGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Descarte Planta Athos-Gr Ica 2021'
		verbose_name_plural = 'Descarte Planta Athos-Gr Ica 2021'

	def __str__(self):
		return "%s-%s" % (self.id, self.peso_descarte)


class TipoSalidaDescarte(models.Model):
	
	desc= models.CharField("Tipo Salida Descarte", max_length=100,blank=True, null= True)

	class Meta:
		verbose_name = 'Tipo Salidad Descarte'
		verbose_name_plural = 'Tipo Salida Descarte'

	def __str__(self):
		return "%s-%s" % (self.id, self.desc)


class SalidaDescarteGrIca2021(models.Model):
	
	anexo_eje= models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeSalidaDescarteGrIca2021" ,null=True, blank=True)
	cantidad= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoSalidaDescarteGrIca2021" ,null=True, blank=True)
	anexo_tipo = models.ForeignKey(TipoSalidaDescarte, on_delete=models.CASCADE, related_name="AnexoTipoSalidaDescarteGrIca2021" ,null=True, blank=True)
	nroguia= models.CharField("Nro Guia", max_length=100,blank=True, null= True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionSalidaDescarteGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModSalidaDescarteGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Salida Descarte-Gr Ica 2021'
		verbose_name_plural = 'Salida Descarte- Gr Ica 2021'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_eje,self.anexo_tipo, self.cantidad)


class DetalleSalidaDescarteGrIca2021(models.Model):
	anexo_detalle= models.ForeignKey(SalidaDescarteGrIca2021, on_delete=models.CASCADE, related_name="AnexoDetSalidaDescarteGrIca2021" ,null=True, blank=True)
	anexo_palet= models.ForeignKey(DescarteAthosGrIca2021, on_delete=models.CASCADE, related_name="AnexoDetPaletDescarteGrIca2021" ,null=True, blank=True)
	cantidad= models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetSalidaDescarteGrIca2021")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetSalidaDescarteGrIca2021",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	

	class Meta:
		verbose_name = 'Detalle Salida Descarte-Gr Ica 2021'
		verbose_name_plural = 'Detalle Salida Descarte- Gr Ica 2021'

	def __str__(self):
		return "%s-%s-%s" % (self.anexo_detalle,self.anexo_palet,self.cantidad)


#campaña granada ica 2023 GrIca2023
class GuiaAthosGrIca2023(models.Model):

	codigoqr=models.CharField("Codigo QR", max_length=30, blank=True, null=True)
	anexo_zona=models.ForeignKey(ejezona, on_delete=models.CASCADE, related_name="AnexoEjeGuiaGrIca2023", blank=True, null=True)
	
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoAlmaAthosGrIca2023")
	anexo_chofer=models.ForeignKey(ChoferesVehiculos, on_delete=models.CASCADE, related_name="AnexoGuiaChoferesGrIca2023",blank=True, null=True)
	
	anexo_vehiculo=models.ForeignKey(PlacasVehiculares, on_delete=models.CASCADE, related_name="AnexoGuiaVehiculosGrIca2023",blank=True, null=True)
	ubic_partida=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaPGrIca2023")
	ubic_llegada=models.ForeignKey(LugarAthos, on_delete=models.CASCADE, related_name="AnexoUbiGuiaLLGrIca2023")
	anexo_sociedad=models.ForeignKey(DatosEmpresa, on_delete=models.CASCADE, related_name="AnexoDatosEmpGrIca2023")
	NroGuia=models.CharField("Nro Guia", max_length=30, blank=True, null=True, unique=True)
	fecha_transporte = models.DateField("Fecha trasnporte",null=True, blank=True)
	anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoGuiaGrIca2023",null=True, blank=True)
	nroprecinto=models.IntegerField(blank=True, null=True)
	
	longitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)
	latitud=models.DecimalField(max_digits=16, decimal_places=13,null=True, blank=True)

	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGuiaGrIca2023", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaGrIca2023",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Athos-Granada Ica 2023'
		verbose_name_plural = 'Guias Athos-Granada Ica 2023'

	def __str__(self):

		return "%s-%s" % ( self.id,self.NroGuia)



class GuiaDetallesAthosGrIca2023(models.Model):
	anexo_guia=models.ForeignKey(GuiaAthosGrIca2023, on_delete=models.CASCADE, related_name="AnexoGuiaDetAthosGrIca2023")
	anexo_ubi_mmpp=models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPPFundoAthosGrIca2023")
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	peso_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	anexo_material=models.ForeignKey(MaterialAcopio, on_delete=models.CASCADE, related_name="AnexoMaterialAcopioGrIca2023")
	fecha_cosecha = models.DateField("Fecha Cosecha",null=True, blank=True)
	anexo_calidad=models.ForeignKey(CalidadProducto, on_delete=models.CASCADE, related_name="AnexoCalidadMGrIca2023", null=True)
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioGuiaDGrIca2023", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionGuiaDGrIca2023",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Guia Detalle Athos-Granada Ica 2023'
		verbose_name_plural = 'Guias  Detalles Athos- Granada Ica 2023'

	def __str__(self):

		return "%s-%s-%s" % ( self.anexo_guia.NroGuia,self.anexo_ubi_mmpp,self.cant_jabas)
	@property
	def suma_jabas_palets(self):
		palets = self.AnexoGuiaDAthosGrIca2023.all()
		suma = 0
		for palet in palets:
			suma += palet.cant_jabas
		return int(suma)

	@property
	def resto_jabas(self):
		return self.cant_jabas - self.suma_jabas_palets




class InfoPaletGrIca2023(models.Model):
	anexo_guiad=models.ForeignKey(GuiaDetallesAthosGrIca2023, on_delete=models.CASCADE, related_name="AnexoGuiaDAthosGrIca2023")
	anexo_almacen=models.ForeignKey(AlmacenesAthos, on_delete=models.CASCADE, related_name="AnexoInfoAlmacenGrIca2023", blank=True, null=True)
	anexo_tipoparihuela=models.ForeignKey(TipoParihuela, on_delete=models.CASCADE, related_name="AnexoMaterialParihuelaGrIca2023", blank=True, null=True)
	cant_jabas=models.DecimalField(max_digits=5, decimal_places=0)
	
	pesobr_palet=models.DecimalField(max_digits=7, decimal_places=2)
	pesova_jabas=models.DecimalField(max_digits=7, decimal_places=2)
	pesonet_palet=models.DecimalField(max_digits=7, decimal_places=2)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacioPaletsGrIca2023", blank=True, null=True)
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True, blank=True, null=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModificacionPaletsGrIca2023",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)

	class Meta:
		verbose_name = 'Info Palet-Granada Ica 2023'
		verbose_name_plural = 'Info Palets-Granada Ica 2023'

	def __str__(self):
		return "%s-%s" % ( self.id,self.anexo_guiad)
