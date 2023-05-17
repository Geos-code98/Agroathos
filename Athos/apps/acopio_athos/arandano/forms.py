from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from apps.acopio_athos.arandano.models import GuiaAthosArCaraz2021
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArCaraz2021
from apps.acopio_athos.arandano.models import InfoPaletArCaraz2021

from apps.acopio_athos.arandano.models import GuiaAthosArIca2021
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArIca2021
from apps.acopio_athos.arandano.models import InfoPaletArIca2021

from apps.menu.models import PlacasVehiculares
from apps.menu.models import ProgramaProduccion
from apps.menu.models import MaterialAcopio
from apps.menu.models import MaterialTransporte

from apps.acopio_athos.arandano.models import ModEnfriadoArIca2021
from apps.acopio_athos.arandano.models import DistribucionEnfriadoArIca2021
from apps.acopio_athos.arandano.models import TemperaturaEnfriadoArIca2021


#CAMPAÑA AR 2022 - 02 CARAZ
from apps.acopio_athos.arandano.models import GuiaAthosArCaraz202202
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArCaraz202202
from apps.acopio_athos.arandano.models import InfoPaletArCaraz202202

#CAMAPAÑA AR 2022 - 02 ICA
from apps.acopio_athos.arandano.models import GuiaAthosArIca202202
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArIca202202
from apps.acopio_athos.arandano.models import InfoGuiaAthosArIca202202
from apps.acopio_athos.arandano.models import InfoPaletArIca202202
from apps.maestras.models import AuxiliaresCampoAthos

from apps.menu.models import ChoferesVehiculos

class guiaathosarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiaathosarcaraz2021form, self).__init__(*args, **kwargs)

		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Codigo QR", "data-required":"true", "data-error-message":"Ingrese Codigo","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		
		
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})

		#self.fields['anexo_vehiculo']=forms.ModelChoiceField(label="Vehiculo",queryset=PlacasVehiculares.objects.filter(anexo_tipotransporte=1)[:1])
		self.fields['anexo_vehiculo'].widget.attrs.update({"placeholder":"Vehiculo", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})		
		
		self.fields['ubic_partida'].widget.attrs.update({"placeholder":"Partida", "data-required":"true", "data-error-message":"Ingrese Partida","class":"form-control"})
		self.fields['ubic_llegada'].widget.attrs.update({"placeholder":"Llegada", "data-required":"true", "data-error-message":"Ingrese Llegada","class":"form-control"})
		self.fields['anexo_sociedad'].widget.attrs.update({"placeholder":"Sociedad", "data-required":"true", "data-error-message":"Ingrese Sociedad","class":"form-control"})		
		self.fields['NroGuia'].widget.attrs.update({"placeholder":"Nro Guia", "data-required":"true", "data-error-message":"Ingrese NroGuia","class":"form-control"})
		self.fields['fecha_transporte'].widget.attrs.update({"placeholder":"Fecha Transporte", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control","id":"datepicker"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo", "required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['nroprecinto'].widget.attrs.update({"placeholder":"Nro Precinto", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		
		self.fields['longitud'].widget.attrs['readonly'] = True
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs['readonly'] = True
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})


	class Meta:
		model = GuiaAthosArCaraz2021
		fields = [
			
			'codigoqr',
			'anexo_zona',
			'anexo_almacen',
			
			'anexo_chofer',
			'anexo_vehiculo',
			
			'ubic_partida',
			'ubic_llegada',
			'anexo_sociedad',
			'NroGuia',
			'fecha_transporte',
			"anexo_fundo",
			'nroprecinto',
			'longitud',
			'latitud',

		
		]

		labels={

			"codigoqr":"Codigo QR",
			"anexo_zona":"Zona",
			"anexo_almacen":"Almacen",
			"anexo_chofer":"Chofer",
			"anexo_vehiculo":"Placa",
	
			"ubic_partida":"Ubicación Partida",
			"ubic_llegada":"Ubicación llegada",
			"anexo_sociedad":"Sociedad",
			"NroGuia":"Nro Guia",
			"fecha_transporte":"Fecha Transporte",
			"anexo_fundo":"Fundo",
			"nroprecinto":"Numero de Precinto",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}


class guiadetallesathosarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosarcaraz2021form, self).__init__(*args, **kwargs)



		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=2))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosArCaraz2021
		fields = [
			

			'anexo_ubi_mmpp',
			'cant_jabas',
			'peso_jabas',
			'anexo_material',
			'fecha_cosecha',
			'anexo_calidad',
		
		]

		labels={

			"anexo_ubi_mmpp":"PEP",
			"cant_jabas":"Cantidad de Jabas",
			"peso_jabas":"Peso Campo",
			"anexo_material":"Material Compuesto",
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_calidad":"Calidad",
		}

class infopaletarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(infopaletarcaraz2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_clamshell'].widget.attrs.update({"placeholder":"Cantidad de clamshell", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
		self.fields['pesova_jabas'].widget.attrs.update({"placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Cajas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['anexo_envase'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['anexo_tipocalidadfruta'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
		
	class Meta:
		model = InfoPaletArCaraz2021
		fields = [
			
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_clamshell',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',

			'cant_jabas',
			'anexo_envase',
			'anexo_tipocalidadfruta',
				
		]

		labels={

			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_clamshell":"Cantidad de Clamshell",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Clamshell Vacias",
			"pesonet_palet":"Peso Neto Palet",
			
			"cant_jabas":"Cantidad de Jabas",
			"anexo_envase":"Envase-Jabas",
			"anexo_tipocalidadfruta":"Tipo Calidad de Fruta",

		}











#CAMPAÑA 2022 - 02 AR CARAZ
class guiaathosarcaraz202202form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiaathosarcaraz202202form, self).__init__(*args, **kwargs)

		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Codigo QR", "data-required":"true", "data-error-message":"Ingrese Codigo","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['anexo_vehiculo']=forms.ModelChoiceField(label="Vehiculo",queryset=PlacasVehiculares.objects.filter(anexo_tipotransporte=1))
		self.fields['anexo_vehiculo'].widget.attrs.update({"placeholder":"Vehiculo", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})		
		self.fields['ubic_partida'].widget.attrs.update({"placeholder":"Partida", "data-required":"true", "data-error-message":"Ingrese Partida","class":"form-control"})
		self.fields['ubic_llegada'].widget.attrs.update({"placeholder":"Llegada", "data-required":"true", "data-error-message":"Ingrese Llegada","class":"form-control"})
		self.fields['anexo_sociedad'].widget.attrs.update({"placeholder":"Sociedad", "data-required":"true", "data-error-message":"Ingrese Sociedad","class":"form-control"})		
		self.fields['NroGuia'].widget.attrs.update({"placeholder":"Nro Guia", "data-required":"true", "data-error-message":"Ingrese NroGuia","class":"form-control"})
		self.fields['fecha_transporte'].widget.attrs.update({"placeholder":"Fecha Transporte", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control","id":"datepicker"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo", "required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['nroprecinto'].widget.attrs.update({"placeholder":"Nro Precinto", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['longitud'].widget.attrs['readonly'] = True
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs['readonly'] = True
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})

	class Meta:
		model = GuiaAthosArCaraz202202
		fields = [
			'codigoqr',
			'anexo_zona',
			'anexo_almacen',
			'anexo_chofer',
			'anexo_vehiculo',
			'ubic_partida',
			'ubic_llegada',
			'anexo_sociedad',
			'NroGuia',
			'fecha_transporte',
			"anexo_fundo",
			'nroprecinto',
			'longitud',
			'latitud',
		]

		labels={
			"codigoqr":"Codigo QR",
			"anexo_zona":"Zona",
			"anexo_almacen":"Almacen",
			"anexo_chofer":"Chofer",
			"anexo_vehiculo":"Placa",
			"ubic_partida":"Ubicación Partida",
			"ubic_llegada":"Ubicación llegada",
			"anexo_sociedad":"Sociedad",
			"NroGuia":"Nro Guia",
			"fecha_transporte":"Fecha Transporte",
			"anexo_fundo":"Fundo",
			"nroprecinto":"Numero de Precinto",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class guiadetallesathosarcaraz202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosarcaraz202202form, self).__init__(*args, **kwargs)

		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=2))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosArCaraz202202
		fields = [
			'anexo_ubi_mmpp',
			'cant_jabas',
			'peso_jabas',
			'anexo_material',
			'fecha_cosecha',
			'anexo_calidad',
		]

		labels={
			"anexo_ubi_mmpp":"PEP",
			"cant_jabas":"Cantidad de Jabas",
			"peso_jabas":"Peso Campo",
			"anexo_material":"Material Compuesto",
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_calidad":"Calidad",
		}

class infopaletarcaraz202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(infopaletarcaraz202202form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_clamshell'].widget.attrs.update({"placeholder":"Cantidad de clamshell", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['pesova_jabas'].widget.attrs.update({"placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Cajas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['anexo_envase'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['anexo_tipocalidadfruta'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
		
	class Meta:
		model = InfoPaletArCaraz202202
		fields = [
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_clamshell',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',
			'cant_jabas',
			'anexo_envase',
			'anexo_tipocalidadfruta',
		]

		labels={
			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_clamshell":"Cantidad de Clamshell",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Clamshell Vacias",
			"pesonet_palet":"Peso Neto Palet",
			"cant_jabas":"Cantidad de Jabas",
			"anexo_envase":"Envase-Jabas",
			"anexo_tipocalidadfruta":"Tipo Calidad de Fruta",
		}


#CAMPAÑA 2022 - 02 AR ICA
class guiaathosarica202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(guiaathosarica202202form, self).__init__(*args, **kwargs)

		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Codigo QR", "data-required":"true", "data-error-message":"Ingrese Codigo","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		#self.fields['anexo_chofer']=forms.ModelChoiceField(label="Chofer",queryset=ChoferesVehiculos.objects.all()[:1])
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		#self.fields['anexo_vehiculo']=forms.ModelChoiceField(label="Vehiculo",queryset=PlacasVehiculares.objects.filter(anexo_tipotransporte=1)[:1])
		self.fields['anexo_vehiculo'].widget.attrs.update({"placeholder":"Vehiculo", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['ubic_partida'].widget.attrs.update({"placeholder":"Partida", "data-required":"true", "data-error-message":"Ingrese Partida","class":"form-control"})
		self.fields['ubic_llegada'].widget.attrs.update({"placeholder":"Llegada", "data-required":"true", "data-error-message":"Ingrese Llegada","class":"form-control"})
		self.fields['anexo_sociedad'].widget.attrs.update({"placeholder":"Sociedad", "data-required":"true", "data-error-message":"Ingrese Sociedad","class":"form-control"})
		self.fields['NroGuia'].widget.attrs.update({"placeholder":"Nro Guia", "data-required":"true", "data-error-message":"Ingrese NroGuia","class":"form-control"})
		self.fields['fecha_transporte'].widget.attrs.update({"placeholder":"Fecha Transporte", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control","id":"datepicker"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo", "required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['nroprecinto'].widget.attrs.update({"placeholder":"Nro Precinto", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['longitud'].widget.attrs['readonly'] = True
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs['readonly'] = True
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})

	class Meta:
		model = GuiaAthosArIca202202
		fields = [
			'codigoqr',
			'anexo_zona',
			'anexo_almacen',
			'anexo_chofer',
			'anexo_vehiculo',
			'ubic_partida',
			'ubic_llegada',
			'anexo_sociedad',
			'NroGuia',
			'fecha_transporte',
			"anexo_fundo",
			'nroprecinto',
			'longitud',
			'latitud',
		]

		labels={
			"codigoqr":"Codigo QR",
			"anexo_zona":"Zona",
			"anexo_almacen":"Almacen",
			"anexo_chofer":"Chofer",
			"anexo_vehiculo":"Placa",
			"ubic_partida":"Ubicación Partida",
			"ubic_llegada":"Ubicación llegada",
			"anexo_sociedad":"Sociedad",
			"NroGuia":"Nro Guia",
			"fecha_transporte":"Fecha Transporte",
			"anexo_fundo":"Fundo",
			"nroprecinto":"Numero de Precinto",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class guiadetallesathosarica202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosarica202202form, self).__init__(*args, **kwargs)

		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		#self.fields['sub_lote'].widget.attrs.update({"placeholder":"Sub Lote", "data-error-message":"Ingresa sub lote","class":"form-control"})
		#self.fields['anexo_supervisor']=forms.ModelChoiceField(label="Supervisor",queryset=AuxiliaresCampoAthos.objects.filter(anexo_estado_id=1))
		#self.fields['anexo_supervisor'].widget.attrs.update({"placeholder":"Supervisor", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=2))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosArIca202202
		fields = [
			'anexo_ubi_mmpp',
			'cant_jabas',
			'peso_jabas',
			'anexo_material',
			'fecha_cosecha',
			'anexo_calidad',
		]

		labels={
			"anexo_ubi_mmpp":"PEP",
			"cant_jabas":"Cantidad de Jabas",
			"peso_jabas":"Peso Campo",
			"anexo_material":"Material Compuesto",
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_calidad":"Calidad",
		}

class infoguiaathosarica202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(infoguiaathosarica202202form, self).__init__(*args, **kwargs)

		self.fields['anexo_auxiliar']=forms.ModelChoiceField(label="Auxiliar",queryset=AuxiliaresCampoAthos.objects.filter(anexo_estado_id=1))
		self.fields['anexo_auxiliar'].widget.attrs.update({"placeholder":"Auxiliar", "data-error-message":"Error","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=2))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['sub_lote'].widget.attrs.update({"placeholder":"Sub Lote", "data-error-message":"Error","class":"form-control"})
		self.fields['cant_envases'].widget.attrs.update({"placeholder":"Cantidad de Envases", "data-required":"true", "data-error-message":"Error","class":"form-control"})
	
	class Meta:
		model = InfoGuiaAthosArIca202202
		fields = [
			'anexo_auxiliar',
			'anexo_material',
			'sub_lote',
			'cant_envases',
		]

		labels={
			"anexo_auxiliar":"AUXILIAR",
			"anexo_material":"MATERIAL",
			"sub_lote":"SUB LOTE",
			"cant_envases":"CANT. ENVASES",
		}

class infopaletarica202202form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(infopaletarica202202form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_clamshell'].widget.attrs.update({"placeholder":"Cantidad de clamshell", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['pesova_jabas'].widget.attrs.update({"placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Cajas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['anexo_envase']=forms.ModelChoiceField(label="Envase",queryset=MaterialTransporte.objects.filter(anexo_cultivo=2))
		self.fields['anexo_envase'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['anexo_tipocalidadfruta'].widget.attrs.update({"placeholder":"Tipo Calidad", "data-required":"true", "data-error-message":"Error","class":"form-control"})
		
	class Meta:
		model = InfoPaletArIca202202
		fields = [
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_clamshell',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',
			'cant_jabas',
			'anexo_envase',
			'anexo_tipocalidadfruta',
		]

		labels={
			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_clamshell":"Cantidad de Clamshell",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Clamshell Vacias",
			"pesonet_palet":"Peso Neto Palet",
			"cant_jabas":"Cantidad de Jabas",
			"anexo_envase":"Envase-Jabas",
			"anexo_tipocalidadfruta":"Tipo Calidad Fruta",
		}












class guiaathosarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiaathosarica2021form, self).__init__(*args, **kwargs)

		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Codigo QR", "data-required":"true", "data-error-message":"Ingrese Codigo","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		
		
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})

		self.fields['anexo_vehiculo']=forms.ModelChoiceField(label="Vehiculo",queryset=PlacasVehiculares.objects.filter(anexo_tipotransporte=1))
		self.fields['anexo_vehiculo'].widget.attrs.update({"placeholder":"Vehiculo", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})		
		
		self.fields['ubic_partida'].widget.attrs.update({"placeholder":"Partida", "data-required":"true", "data-error-message":"Ingrese Partida","class":"form-control"})
		self.fields['ubic_llegada'].widget.attrs.update({"placeholder":"Llegada", "data-required":"true", "data-error-message":"Ingrese Llegada","class":"form-control"})
		self.fields['anexo_sociedad'].widget.attrs.update({"placeholder":"Sociedad", "data-required":"true", "data-error-message":"Ingrese Sociedad","class":"form-control"})		
		self.fields['NroGuia'].widget.attrs.update({"placeholder":"Nro Guia", "data-required":"true", "data-error-message":"Ingrese NroGuia","class":"form-control"})
		self.fields['fecha_transporte'].widget.attrs.update({"placeholder":"Fecha Transporte", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control","id":"datepicker"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo", "required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		self.fields['nroprecinto'].widget.attrs.update({"placeholder":"Nro Precinto", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control"})
		
		self.fields['longitud'].widget.attrs['readonly'] = True
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs['readonly'] = True
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})


	class Meta:
		model = GuiaAthosArIca2021
		fields = [
			
			'codigoqr',
			'anexo_zona',
			'anexo_almacen',
			
			'anexo_chofer',
			'anexo_vehiculo',
			
			'ubic_partida',
			'ubic_llegada',
			'anexo_sociedad',
			'NroGuia',
			'fecha_transporte',
			"anexo_fundo",
			'nroprecinto',
			'longitud',
			'latitud',

		
		]

		labels={

			"codigoqr":"Codigo QR",
			"anexo_zona":"Zona",
			"anexo_almacen":"Almacen",
			"anexo_chofer":"Chofer",
			"anexo_vehiculo":"Placa",
	
			"ubic_partida":"Ubicación Partida",
			"ubic_llegada":"Ubicación llegada",
			"anexo_sociedad":"Sociedad",
			"NroGuia":"Nro Guia",
			"fecha_transporte":"Fecha Transporte",
			"anexo_fundo":"Fundo",
			"nroprecinto":"Numero de Precinto",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class guiadetallesathosarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosarica2021form, self).__init__(*args, **kwargs)



		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=2))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosArIca2021
		fields = [
			

			'anexo_ubi_mmpp',
			'cant_jabas',
			'peso_jabas',
			'anexo_material',
			'fecha_cosecha',
			'anexo_calidad',
		
		]

		labels={

			"anexo_ubi_mmpp":"PEP",
			"cant_jabas":"Cantidad de Jabas",
			"peso_jabas":"Peso Campo",
			"anexo_material":"Material Compuesto",
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_calidad":"Calidad",
		}

class infopaletarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(infopaletarica2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_clamshell'].widget.attrs.update({"placeholder":"Cantidad de clamshell", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
		self.fields['pesova_jabas'].widget.attrs.update({"placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Cajas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		
		self.fields['anexo_envase']=forms.ModelChoiceField(label="Envase",queryset=MaterialTransporte.objects.filter(anexo_cultivo=2))
		self.fields['anexo_envase'].widget.attrs.update({"placeholder":"Envase", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
	class Meta:
		model = InfoPaletArIca2021
		fields = [
			
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_clamshell',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',

			'cant_jabas',
			'anexo_envase',
				
		]

		labels={

			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_clamshell":"Cantidad de Clamshell",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Clamshell Vacias",
			"pesonet_palet":"Peso Neto Palet",
			
			"cant_jabas":"Cantidad de Jabas",
			"anexo_envase":"Envase-Jabas",

		}


#campaña2021ICAAr - ENFRIADO ICA AR 2021 1
class modenfriadoarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(modenfriadoarica2021form, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control", "id":"datepicker"})
		self.fields['cod_termometro'].widget.attrs.update({"placeholder":"Codigo Termometro","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['cod_vac1'].widget.attrs.update({"placeholder":"Codigo Vacuometro 1","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['cod_vac2'].widget.attrs.update({"placeholder":"Codigo Vacuometro 2","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['cod_vac3'].widget.attrs.update({"placeholder":"Codigo Vacuometro 3","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		
	class Meta:
		model = ModEnfriadoArIca2021
		fields = [
			'fecha',
			'cod_termometro',
			'cod_vac1',
			'cod_vac2',
			'cod_vac3',
			
		]

		labels={
			"fecha":"Fecha",
			"cod_termometro":"Codigo de Termometro",
			"cod_vac1":"Codigo Vacuometro 1",
			"cod_vac2":"Codigo Vacuometro 2",
			"cod_vac3":"Codigo Vacuometro 3",
			

		}

class distribucionenfriadoarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(distribucionenfriadoarica2021form, self).__init__(*args, **kwargs)
		
		self.fields['tunel'].widget.attrs.update({"placeholder":"N° de Tunel","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['n_tunel'].widget.attrs.update({"placeholder":"N° de Compartimento","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['anexo_lado'].widget.attrs.update({"placeholder":"Lado","data-required":"true","data-error-message":"Lado requerida","class":"form-control"})
		self.fields['lectura_qr'].widget.attrs.update({"placeholder":"Lectura QR","data-required":"true","data-error-message":"QR requerida","class":"form-control"})
		self.fields['n_palet'].widget.attrs.update({"placeholder":"N° Palet","data-required":"true","data-error-message":"N° palet requerida","class":"form-control"})
		
	class Meta:
		model = DistribucionEnfriadoArIca2021
		fields = [
			'tunel',
			'n_tunel',
			'anexo_lado',
			'lectura_qr',
			'n_palet',
			
		]

		labels={
			"tunel":"N° Tunel(Escribir 1 o 2 segun corresponda)",
			"n_tunel":"N° Compartimento",
			"anexo_lado":"Lado",
			"lectura_qr":"Lectura QR",
			"n_palet":"N° Palet",
			

		}

class temperaturaenfriadoarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(temperaturaenfriadoarica2021form, self).__init__(*args, **kwargs)
		
		self.fields['m_tempambiente'].widget.attrs.update({"placeholder":"Temperatura Ambiente","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['m_tempinterna'].widget.attrs.update({"placeholder":"Temperatura Interna","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['m_tempexterna'].widget.attrs.update({"placeholder":"Temperatura Externa","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = TemperaturaEnfriadoArIca2021
		fields = [
			
			'm_tempambiente',
			'm_tempinterna',
			'm_tempexterna',
			
		]

		labels={
			
			"m_tempambiente":"Temperatura Ambiente",
			"m_tempinterna":"Temperatura Interna",
			"m_tempexterna":"Temperatura Externa",
			
		}
