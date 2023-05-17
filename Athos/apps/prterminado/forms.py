from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.prterminado.models import ProductoTerminado
from apps.prterminado.models import TempProductoTerminado



class prterminadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(prterminadoform, self).__init__(*args, **kwargs)
		
		
		self.fields['qr'].widget.attrs.update({"placeholder":"QR..","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['traza1'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['traza2'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['traza3'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['traza4'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['traza5'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['traza6'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['traza7'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['traza8'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['traza9'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['traza10'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['traza11'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['traza12'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['traza13'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['traza14'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['traza15'].widget.attrs.update({"placeholder":"Traza","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		
	class Meta:
		model = ProductoTerminado
		fields = [
			'qr',
			'traza1',
			'traza2',
			'traza3',
			'traza4',
			'traza5',
			'traza6',
			'traza7',
			'traza8',
			'traza9',
			'traza10',
			'traza11',
			'traza12',
			'traza13',
			'traza14',
			'traza15',
			


		]

		labels={
			"qr":"Lectura QR",
			"traza1":"Traza1",
			"traza2":"Traza2",
			"traza3":"Traza3",
			"traza4":"Traza4",
			"traza5":"Traza5",
			"traza6":"Traza6",
			"traza7":"Traza7",
			"traza8":"Traza8",
			"traza9":"Traza9",
			"traza10":"Traza10",
			"traza11":"Traza11",
			"traza12":"Traza12",
			"traza13":"Traza13",
			"traza14":"Traza14",
			"traza15":"Traza15",
		
		}



class tempprterminadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tempprterminadoform, self).__init__(*args, **kwargs)
		
		
		self.fields['temperatura'].widget.attrs.update({"placeholder":"Temperatura","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = TempProductoTerminado
		fields = [
			'temperatura',
			
			


		]

		labels={
			"temperatura":"Temperatura",
			
		}

