from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from apps.planta.granada_planta.models import UbicacionPlanta
from apps.planta.granada_planta.models import LanzadoPaletasGrIca2021
#Campana granada ica 2023
from apps.planta.granada_planta.models import LanzadoPaletasGrIca2023

#campaña arandano ar ica 2022
from apps.planta.granada_planta.models import LanzadoPaletasArIca2022

from apps.planta.granada_planta.models import PrePaletizadoGrIca2020
from apps.planta.granada_planta.models import DetallePrePaletizadoGrIca2020


class ubicacionplantaform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ubicacionplantaform ,self).__init__(*args, **kwargs)
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Cultivo requerido","class":"form-control"})
		
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado ","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})		
		
		

	class Meta:
		model = UbicacionPlanta
		fields = [
			'anexo_zona',
			'anexo_planta',
			'anexo_nave',
			'anexo_cultivo',
			'anexo_estado',
			
			
			
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_planta":"Planta",
			"anexo_nave":"Nave",
			"anexo_cultivo":"Cultivo",
			"anexo_estado":"Estado",
			
						
		}

class lanzadopaletasgrica2020form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lanzadopaletasgrica2020form ,self).__init__(*args, **kwargs)
		self.fields['anexo_linea'].widget.attrs.update({"maxlength":"100","autocomplete":"off","required":"True","data-required":"true","data-error-message":"Linea requerido","class":"form-control"})
		self.fields['linea'].widget.attrs.update({"maxlength":"100","autocomplete":"off","required":"True","data-required":"true","data-error-message":"Linea requerido","class":"form-control"})
		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Fecha","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control", "id":"datepicker"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})	
		self.fields['leerqr'].widget.attrs.update({"autofocus":"autofocus","placeholder":"QR","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"placeholder":"N° Palet","readonly":"readonly","data-required":"true","data-error-message":"N° de Palet requerido","class":"form-control"})
		self.fields['njabas'].widget.attrs.update({"placeholder":"N° jabas","readonly":"readonly","data-required":"true","data-error-message":"N° de javas requerido","class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Peso","readonly":"readonly","data-required":"true","data-error-message":"Peso requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","readonly":"readonly","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})	
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})
		self.fields['fecha_hora_creacion'].widget.attrs.update({"placeholder":"Fecha Hora Creacion ","readonly":"readonly","data-required":"false","data-error-message":"Estado requerido","class":"form-control","id":"datepickercreacion"})	
		self.fields['trazabilidad'].widget.attrs.update({"placeholder":"Trazabilidad","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})

		self.fields['pep'].widget.attrs.update({"placeholder":"PEP","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control","readonly":"readonly"})
		self.fields['material'].widget.attrs.update({"placeholder":"Material","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control","readonly":"readonly"})


	class Meta:
		model = LanzadoPaletasArIca2022
		fields = [
			'anexo_linea',
			'linea',
			'fecha_lanzado',
			'anexo_turno',
			'leerqr',
			'npalet',
			'njabas',
			'peso',
			'estado',
			'fecha_cosecha',
			'fecha_hora_creacion',
			'trazabilidad',	
			'pep',
			'material',
				
		]

		labels={
			"anexo_linea":"Linea",
			"linea":"QR Linea",
			"fecha_lanzado":"Fecha Lanzado",
			"anexo_turno":"Turno",
			"leerqr":"Codigo Qr",
			"npalet":"N° de Palet",
			"njabas":"N° de Jabas",
			"peso":"Peso",
			"estado":"estado",
			"fecha_cosecha":"Fecha Cosecha",
			"fecha_hora_creacion":"Fecha Creacion",
			"trazabilidad":"Trazabilidad",	
			"pep":"PEP",
			"material":"Material",		
		}

#campaña granada ica 2023
class lanzadopaletasgrica2023form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lanzadopaletasgrica2023form ,self).__init__(*args, **kwargs)
		self.fields['linea'].widget.attrs.update({"maxlength":"100","autocomplete":"off","required":"True","data-required":"true","data-error-message":"Linea requerido","class":"form-control"})
		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Fecha","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control", "id":"datepicker"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})	
		self.fields['leerqr'].widget.attrs.update({"autofocus":"autofocus","placeholder":"QR","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"placeholder":"N° Palet","readonly":"readonly","data-required":"true","data-error-message":"N° de Palet requerido","class":"form-control"})
		self.fields['njabas'].widget.attrs.update({"placeholder":"N° jabas","readonly":"readonly","data-required":"true","data-error-message":"N° de javas requerido","class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Peso","readonly":"readonly","data-required":"true","data-error-message":"Peso requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","readonly":"readonly","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})	
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})
		self.fields['fecha_hora_creacion'].widget.attrs.update({"placeholder":"Fecha Hora Creacion ","readonly":"readonly","data-required":"false","data-error-message":"Estado requerido","class":"form-control","id":"datepickercreacion"})	
		self.fields['trazabilidad'].widget.attrs.update({"placeholder":"Trazabilidad","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})

		self.fields['pep'].widget.attrs.update({"placeholder":"PEP","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control","readonly":"readonly"})
		self.fields['material'].widget.attrs.update({"placeholder":"Material","data-required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control","readonly":"readonly"})


	class Meta:
		model = LanzadoPaletasGrIca2023
		fields = [
			
			'linea',
			'fecha_lanzado',
			'anexo_turno',
			'leerqr',
			'npalet',
			'njabas',
			'peso',
			'estado',
			'fecha_cosecha',
			'fecha_hora_creacion',
			'trazabilidad',	
			'pep',
			'material',
				
		]

		labels={
			
			"linea":"QR Linea",
			"fecha_lanzado":"Fecha Lanzado",
			"anexo_turno":"Turno",
			"leerqr":"Codigo Qr",
			"npalet":"N° de Palet",
			"njabas":"N° de Jabas",
			"peso":"Peso",
			"estado":"estado",
			"fecha_cosecha":"Fecha Cosecha",
			"fecha_hora_creacion":"Fecha Creacion",
			"trazabilidad":"Trazabilidad",	
			"pep":"PEP",
			"material":"Material",		
		}







class prepaletizadogrica2020form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(prepaletizadogrica2020form ,self).__init__(*args, **kwargs)
		self.fields['anexo_produccion'].widget.attrs.update({"placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['cantidad_cajas'].widget.attrs.update({"placeholder":" ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":" ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		
	class Meta:
		model = PrePaletizadoGrIca2020
		fields = [
			'anexo_produccion',
			'fecha_lanzado',
			'anexo_turno',
			'cantidad_cajas',
			'anexo_estado',
			'observacion',
			
			
		]

		labels={
			"anexo_produccion":"Produccion",
			"fecha_lanzado":"Fecha Lanzado",
			"anexo_turno":"Turno",
			"cantidad_cajas":"Cantidad de Cajas",
			"anexo_estado":"Estado",
			"observacion":"Observacion",
						
		}

class detalleprepaletizadogrica2020form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(detalleprepaletizadogrica2020form ,self).__init__(*args, **kwargs)
		self.fields['traza'].widget.attrs.update({"autofocus":"autofocus","placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		
	class Meta:
		model = DetallePrePaletizadoGrIca2020
		fields = [
			'traza',
		
				
		]

		labels={
			"traza":"Trazabilidad",
			
						
		}