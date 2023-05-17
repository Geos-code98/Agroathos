from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from apps.acopio_athos.granada.models import GuiaAthosGr2020
from apps.acopio_athos.granada.models import GuiaDetallesAthosGr2020
from apps.acopio_athos.granada.models import InfoPaletGr2020


from apps.acopio_athos.granada.models import GuiaAthosGrIca2021
from apps.acopio_athos.granada.models import GuiaDetallesAthosGrIca2021
from apps.acopio_athos.granada.models import InfoPaletGrIca2021
from apps.acopio_athos.granada.models import AlmacenAcopioGrIca2021


from apps.menu.models import PlacasVehiculares
from apps.menu.models import ProgramaProduccion
from apps.menu.models import MaterialAcopio
from apps.menu.models import MaterialMMPP
from apps.acopio_athos.granada.models import AlmacenAcopioGr2020

from apps.acopio_athos.granada.models import DescarteAthosGrIca2021
from apps.acopio_athos.granada.models import SalidaDescarteGrIca2021
from apps.acopio_athos.granada.models import DetalleSalidaDescarteGrIca2021

#campaña Granada Ica 2023
from apps.acopio_athos.granada.models import GuiaAthosGrIca2023
from apps.acopio_athos.granada.models import GuiaDetallesAthosGrIca2023
from apps.acopio_athos.granada.models import InfoPaletGrIca2023



class guiaathosgr2020form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiaathosgr2020form, self).__init__(*args, **kwargs)

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
		model = GuiaAthosGrIca2023
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


class guiadetallesathosgr2020form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexozona=kwargs.pop("anexo_zona")
		anexofundo=kwargs.pop("anexo_fundo")
		super(guiadetallesathosgr2020form, self).__init__(*args, **kwargs)



		self.fields['anexo_ubi_mmpp']=forms.ModelChoiceField(label="Ubicacion MMPP", queryset=anexofundo.fundo3.filter(estado_id=1))
		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialAcopio.objects.filter(anexo_cultivo=1))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	
	class Meta:
		model = GuiaDetallesAthosGrIca2023
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

class infopaletgr2020form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(infopaletgr2020form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		
		self.fields['pesova_jabas'].widget.attrs.update({"placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		
		
	class Meta:
		model = InfoPaletGrIca2023
		fields = [
			
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_jabas',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',
			

		
		]

		labels={

			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_jabas":"Cantidad de Jabas",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Jabas Vacias",
			"pesonet_palet":"Peso Neto Palet",
			
		}

class almacenacopiogr2020form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(almacenacopiogr2020form, self).__init__(*args, **kwargs)
		
		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Qr..", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['posicion'].widget.attrs.update({"placeholder":"..", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		
		
	class Meta:
		model = AlmacenAcopioGrIca2021
		fields = [
			
			'codigoqr',
			'posicion',	
			

		
		]

		labels={

			"codigoqr":"Qr.Palet",
			"posicion":"Posicion",
			
			
		}


#descarte
class descarteathosgrica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(descarteathosgrica2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material",queryset=MaterialMMPP.objects.filter(anexo_cultivo=1))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"VACIO requerida","class":"form-control"})

		self.fields['cant_jabas'].widget.attrs.update({"readonly":"true","placeholder":"Cant. Jabas","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['anexo_linea'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Fecha","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['trazabilidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['alternaria'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['bajo_peso'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cochinilla'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['deformes'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_campo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_roedor'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['gelechidae'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_corona'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['inmadurez_verde'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['insolacion_fuerte'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['pudricion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['quereza'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_ae'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_golpe'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['calibre18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_industrial'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['arilo_pardo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_industrial'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['alternaria_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['bajo_peso_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cochinilla_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['deformes_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_campo_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_roedor_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['gelechidae_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_corona_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['inmadurez_verde_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['insolacion_fuerte_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['pudricion_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['quereza_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_ae_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_golpe_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['calibre18_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_industrial_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['arilo_pardo_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_industrial_linea2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['alternaria_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['bajo_peso_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cochinilla_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['deformes_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_campo_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_roedor_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['gelechidae_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_corona_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['inmadurez_verde_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['insolacion_fuerte_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['pudricion_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['quereza_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_ae_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_golpe_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['calibre18_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_industrial_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['arilo_pardo_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_industrial_linea3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['alternaria_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['bajo_peso_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cochinilla_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['deformes_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_mecanico_campo_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_roedor_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['gelechidae_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_corona_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['inmadurez_verde_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['insolacion_fuerte_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['pudricion_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['quereza_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_ae_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['rajadas_golpe_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['calibre18_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['danio_industrial_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['arilo_pardo_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['hongo_industrial_linea4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
		self.fields['peso_bruto'].widget.attrs.update({"placeholder":"Peso Bruto","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['peso_descarte'].widget.attrs.update({"readonly":"true","placeholder":"Descarte Planta","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})

	class Meta:
		model = DescarteAthosGrIca2021
		fields = [
			
			'anexo_eje',
			'anexo_planta',
			'anexo_material',
			'anexo_turno',
			'fecha_lanzado',
			'peso_bruto',
			'peso_descarte',
			'cant_jabas',
			'anexo_fundo',
			'anexo_linea',
			'trazabilidad',
			'fecha_cosecha',
			'alternaria',
			'bajo_peso',
			'cochinilla',
			'deformes',
			'danio_mecanico',
			'danio_mecanico_campo',
			'danio_roedor',
			'gelechidae',
			'hongo_corona',
			'inmadurez_verde',
			'insolacion_fuerte',
			'pudricion',
			'quereza',
			'rajadas_ae',
			'rajadas_golpe',
			'calibre18',
			'danio_industrial',
			'arilo_pardo',
			'hongo_industrial',

			'alternaria_linea2',
			'bajo_peso_linea2',
			'cochinilla_linea2',
			'deformes_linea2',
			'danio_mecanico_linea2',
			'danio_mecanico_campo_linea2',
			'danio_roedor_linea2',
			'gelechidae_linea2',
			'hongo_corona_linea2',
			'inmadurez_verde_linea2',
			'insolacion_fuerte_linea2',
			'pudricion_linea2',
			'quereza_linea2',
			'rajadas_ae_linea2',
			'rajadas_golpe_linea2',
			'calibre18_linea2',
			'danio_industrial_linea2',
			'arilo_pardo_linea2',
			'hongo_industrial_linea2',

			'alternaria_linea3',
			'bajo_peso_linea3',
			'cochinilla_linea3',
			'deformes_linea3',
			'danio_mecanico_linea3',
			'danio_mecanico_campo_linea3',
			'danio_roedor_linea3',
			'gelechidae_linea3',
			'hongo_corona_linea3',
			'inmadurez_verde_linea3',
			'insolacion_fuerte_linea3',
			'pudricion_linea3',
			'quereza_linea3',
			'rajadas_ae_linea3',
			'rajadas_golpe_linea3',
			'danio_industrial_linea3',
			'arilo_pardo_linea3',
			'hongo_industrial_linea3',

			'calibre18_linea3',
			'alternaria_linea4',
			'bajo_peso_linea4',
			'cochinilla_linea4',
			'deformes_linea4',
			'danio_mecanico_linea4',
			'danio_mecanico_campo_linea4',
			'danio_roedor_linea4',
			'gelechidae_linea4',
			'hongo_corona_linea4',
			'inmadurez_verde_linea4',
			'insolacion_fuerte_linea4',
			'pudricion_linea4',
			'quereza_linea4',
			'rajadas_ae_linea4',
			'rajadas_golpe_linea4',
			'calibre18_linea4',
			'danio_industrial_linea4',
			'arilo_pardo_linea4',
			'hongo_industrial_linea4'
		]

		labels={
			
			"anexo_eje":"Zona",
			"anexo_planta":"Planta",
			"anexo_material":"Material",
			"anexo_turno":"Turno",
			"peso_bruto":"Peso Bruto",
			"peso_descarte":"´Descarte Planta",
			
			"cant_jabas":"Cantidad Jabas",
			"anexo_fundo":"Fundo",
			"anexo_linea":"Linea",
			"trazabilidad":"Trazabilidad",
			"fecha_cosecha":"Fecha Cosecha",
			"fecha_lanzado":"Fecha Lanzado",

			"alternaria":"Alternaria-Linea 1",
			"bajo_peso":"Bajo Peso-Linea 1",
			"cochinilla":"Cochinilla-Linea 1",
			"deformes":"Deformes-Linea 1",
			"danio_mecanico":"Daño Mecanico Planta-Linea 1",
			"danio_mecanico_campo":"Daño Mecanico Campo-Linea 1",
			"danio_roedor":"Daño Roedor-Linea 1",
			"gelechidae":"Gelechiidae-Linea 1",
			"hongo_corona":"Hongo Corona-Linea 1",
			"inmadurez_verde":"Inmadurez Verde-Linea 1",
			"insolacion_fuerte":"Insolacion Fuerte-Linea 1",
			"pudricion":"Pudricion-Linea 1",
			"quereza":"Quereza-Linea 1",
			"rajadas_ae":"Rajadas Arilo Expuesto-Linea 1",
			"rajadas_golpe":"Rajadas Golpe-Linea 1",
			"calibre18":"Calibre 18-Linea 1",
			"danio_industrial":"Daño Industrial-Linea 1",
			"arilo_pardo":"Arilo Pardo-Linea 1",
			"hongo_industrial":"Hongo Industrial-Linea 1",

			"alternaria_linea2":"Alternaria-Linea 2",
			"bajo_peso_linea2":"Bajo Peso-Linea 2",
			"cochinilla_linea2":"Cochinilla-Linea 2",
			"deformes_linea2":"Deformes-Linea 2",
			"danio_mecanico_linea2":"Daño Mecanico Planta-Linea 2",
			"danio_mecanico_campo_linea2":"Daño Mecanico Campo-Linea 2",
			"danio_roedor_linea2":"Daño Roedor-Linea 2",
			"gelechidae_linea2":"Gelechiidae-Linea 2",
			"hongo_corona_linea2":"Hongo Corona-Linea 2",
			"inmadurez_verde_linea2":"Inmadurez Verde-Linea 2",
			"insolacion_fuerte_linea2":"Insolacion Fuerte-Linea 2",
			"pudricion_linea2":"Pudricion-Linea 2",
			"quereza_linea2":"Quereza-Linea 2",
			"rajadas_ae_linea2":"Rajadas Arilo Expuesto-Linea 2",
			"rajadas_golpe_linea2":"Rajadas Golpe-Linea 2",
			"calibre18_linea2":"Calibre 18-linea 2",
			"danio_industrial_linea2":"Daño Industrial-Linea 2",
			"arilo_pardo_linea2":"Arilo Pardo-Linea 2",
			"hongo_industrial_linea2":"Hongo Industrial-Linea 2",
			
			"alternaria_linea3":"Alternaria-Linea 3",
			"bajo_peso_linea3":"Bajo Peso-Linea 3",
			"cochinilla_linea3":"Cochinilla-Linea 3",
			"deformes_linea3":"Deformes-Linea 3",
			"danio_mecanico_linea3":"Daño Mecanico Planta-Linea 3",
			"danio_mecanico_campo_linea3":"Daño Mecanico Campo-Linea 3",
			"danio_roedor_linea3":"Daño Roedor-Linea 3",
			"gelechidae_linea3":"Gelechiidae-Linea 3",
			"hongo_corona_linea3":"Hongo Corona-Linea 3",
			"inmadurez_verde_linea3":"Inmadurez Verde-Linea 3",
			"insolacion_fuerte_linea3":"Insolacion Fuerte-Linea 3",
			"pudricion_linea3":"Pudricion-Linea 3",
			"quereza_linea3":"Quereza-Linea 3",
			"rajadas_ae_linea3":"Rajadas Arilo Expuesto-Linea 3",
			"rajadas_golpe_linea3":"Rajadas Golpe-Linea 3",
			"calibre18_linea3":"Calibre 18-linea 3",
			"danio_industrial_linea3":"Daño Industrial-Linea 3",
			"arilo_pardo_linea3":"Arilo Pardo-Linea 3",
			"hongo_industrial_linea3":"Hongo Industrial-Linea 3",
			
			"alternaria_linea4":"Alternaria-Linea 4",
			"bajo_peso_linea4":"Bajo Peso-Linea 4",
			"cochinilla_linea4":"Cochinilla-Linea 4",
			"deformes_linea4":"Deformes-Linea 4",
			"danio_mecanico_linea4":"Daño Mecanico Planta-Linea 4",
			"danio_mecanico_campo_linea4":"Daño Mecanico Campo-Linea 4",
			"danio_roedor_linea4":"Daño Roedor-Linea 4",
			"gelechidae_linea4":"Gelechiidae-Linea 4",
			"hongo_corona_linea4":"Hongo Corona-Linea 4",
			"inmadurez_verde_linea4":"Inmadurez Verde-Linea 4",
			"insolacion_fuerte_linea4":"Insolacion Fuerte-Linea 4",
			"pudricion_linea4":"Pudricion-Linea 4",
			"quereza_linea4":"Quereza-Linea 4",
			"rajadas_ae_linea4":"Rajadas Arilo Expuesto-Linea 4",
			"rajadas_golpe_linea4":"Rajadas Golpe-Linea 4",
			"calibre18_linea4":"Calibre 18-linea 4",
			"danio_industrial_linea4":"Daño Industrial-Linea 4",
			"arilo_pardo_linea4":"Arilo Pardo-Linea 4",
			"hongo_industrial_linea4":"Hongo Industrial-Linea 4",
			
		}


class salidadescartegrica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(salidadescartegrica2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo Salida","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['nroguia'].widget.attrs.update({"placeholder":"Nro Guia","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = SalidaDescarteGrIca2021
		fields = [
			
			'anexo_eje',
			'cantidad',
			'anexo_cultivo',
			'anexo_tipo',
			'nroguia',
			
		]

		labels={
			"anexo_eje":"Zona",
			"cantidad":"Cantidad",
			"anexo_cultivo":"Cultivo",
			"anexo_tipo":"Tipo de Salida",
			"nroguia":"	Nro Guia"

		}


class detallesalidadescartegrica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detallesalidadescartegrica2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_palet'].widget.attrs.update({"placeholder":"Qr..", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cantidad'].widget.attrs.update({"placeholder":"..", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		
		
	class Meta:
		model = DetalleSalidaDescarteGrIca2021
		fields = [
			
			'anexo_palet',
			'cantidad',	
			

		
		]

		labels={

			"anexo_palet":"N° Palet- Peso",
			"cantidad":"Peso",
			
			
		}
