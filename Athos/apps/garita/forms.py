from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.garita.models import GaritaAthos
from apps.garita.models import DetalleGaritaBusAthos



class garitaathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(garitaathosform, self).__init__(*args, **kwargs)
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['anexo_ruta'].widget.attrs.update({"placeholder":"Ubicacion", "required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['anexo_traslado'].widget.attrs.update({"placeholder":"Traslado", "required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		
		self.fields['qrplaca'].widget.attrs.update({"placeholder":"QR Placa", "required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['qrcampo'].widget.attrs.update({"placeholder":"QR Campo Guia", "data-required":"true", "data-error-message":"Ingrese Qr Campo","class":"form-control"})
		self.fields['chofer_ref'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Chofer Referencial","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Latitud","class":"form-control"})
		self.fields['kilometraje'].widget.attrs.update({"placeholder":"Kilometraje", "data-required":"true", "data-error-message":"Ingrese Kilometraje","class":"form-control"})
		self.fields['cantpasajeros'].widget.attrs.update({"placeholder":"Cant. Pasajeros", "data-required":"true", "data-error-message":"Ingrese Cantidad Pasajeros","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Observacion..", "data-required":"true", "data-error-message":"Ingrese Observacion","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha..", "data-required":"true", "data-error-message":"Ingrese Observacion","class":"form-control"})
	
	class Meta:
		model = GaritaAthos
		fields = [
			'anexo_zona',
			'anexo_fundo',
			'anexo_ruta',
			'anexo_traslado',
			'qrplaca',
			'qrcampo',
			'chofer_ref',
			'longitud',
			'latitud',
			'kilometraje',
			'cantpasajeros',
			'observacion',
			'fecha',
		
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_ruta":"Rutas",
			"anexo_traslado":"Traslado",
			"qrplaca":"QR Placas",
			"qrcampo":" QR Guia",
			"chofer_ref":"Chofer Referencial",
			"longitud":"Longitud",
			"latitud":"Latitud",
			"kilometraje":"Kilometraje",
			"cantpasajeros":"Cantidad de Pasajeros",
			"observacion":"Observaciones",
			"fecha":"Fecha",
		}



class detallegaritabusathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detallegaritabusathosform, self).__init__(*args, **kwargs)
		
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI o SAP", "required":"true", "maxlength":"8","autofocus":"autofocus","data-error-message":"Ingrese Zona","class":"form-control"})
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		
	class Meta:
		model = DetalleGaritaBusAthos
		fields = [
			'dni',
			'anexo_zona',
			'anexo_fundo',
			
		
		]

		labels={
			"dni":"DNI o SAP",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
		}
