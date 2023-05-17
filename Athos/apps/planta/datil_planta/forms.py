from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from apps.planta.higo_planta.models import LanzadoPaletasDtIca2022



class lanzadopaletasdtica2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lanzadopaletasdtica2022form ,self).__init__(*args, **kwargs)
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
		model = LanzadoPaletasDtIca2022
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

