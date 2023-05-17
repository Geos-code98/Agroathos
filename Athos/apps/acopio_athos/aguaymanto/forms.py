from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.acopio_athos.aguaymanto.models import GuiaAthosAgCaraz2022
from apps.acopio_athos.aguaymanto.models import GuiaDetallesAthosAgCaraz2022
from apps.acopio_athos.aguaymanto.models import InfoPaletAgCaraz2022
from apps.menu.models import PlacasVehiculares
from apps.menu.models import ProgramaProduccion
from apps.menu.models import MaterialAcopio

class guiaathosagcaraz2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(guiaathosagcaraz2022form, self).__init__(*args, **kwargs)

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
		model = GuiaAthosAgCaraz2022
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

class guiadetallesathosagcaraz2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosagcaraz2022form, self).__init__(*args, **kwargs)

		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=6))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosAgCaraz2022
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

class infopaletagcaraz2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(infopaletagcaraz2022form, self).__init__(*args, **kwargs)
		
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
		model = InfoPaletAgCaraz2022
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