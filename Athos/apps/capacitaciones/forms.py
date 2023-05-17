from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.capacitaciones.models import EncuestaCapacitacionNew




class encuestacapacitacionnewform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(encuestacapacitacionnewform, self).__init__(*args, **kwargs)
		
		self.fields['dni'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_capacitacion'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_rpta1'].widget.attrs.update({"placeholder":"RUC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta2'].widget.attrs.update({"placeholder":"Proveedor..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_rpta3'].widget.attrs.update({"placeholder":"RUC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta4'].widget.attrs.update({"placeholder":"Proveedor..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta5'].widget.attrs.update({"placeholder":"RUC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta6'].widget.attrs.update({"placeholder":"Proveedor..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

		self.fields['imagen_justificacion1'].widget.attrs.update({"capture":"camera","placeholder":"Estado","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EncuestaCapacitacionNew
		fields = [
			
			'dni',
			'anexo_zona',
			'anexo_capacitacion',		
			'anexo_rpta1',
			'anexo_rpta2',

			'anexo_rpta1',
			'anexo_rpta2',

			'anexo_rpta3',
			'anexo_rpta4',

			'anexo_rpta5',
			'anexo_rpta6',

					
			'imagen_justificacion1',			
		]

		labels={
			
			"dni":"DNI",
			"anexo_zona":"Zona",
			"anexo_capacitacion":"Capacitacion",
			"anexo_rpta1":"¿Comprendiste la capacitación?",
			"anexo_rpta2":"¿Te resultó util la capacitación?",

			"anexo_rpta3":"Mobiliario: Comenta tu experiencia con las sillas y mesas",
			"anexo_rpta4":" Horario: Califica el cumplimiento del horario",

			"anexo_rpta5":"Ponente: Califica el desenvolvimiento del ponente",
			"anexo_rpta6":"Material: Califica qué tan útil fue el material de capacitación",

			
			
			
		}

