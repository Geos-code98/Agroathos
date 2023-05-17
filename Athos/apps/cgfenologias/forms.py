from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.cgfenologias.models import Macroproceso
from apps.cgfenologias.models import Proceso
from apps.cgfenologias.models import ObjetivoProceso
from apps.cgfenologias.models import Hitos
from apps.cgfenologias.models import SubHitos

class macroprocesoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(macroprocesoform, self).__init__(*args, **kwargs)
		
		self.fields['desc'].widget.attrs.update({"placeholder":"Macroproceso..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})


	class Meta:
		model = Macroproceso
		fields = [
			
			'desc',
			
		]

		labels={
			
			"desc":"Macroproceso",
			
		}

class procesoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(procesoform, self).__init__(*args, **kwargs)

		self.fields['abreviatura'].widget.attrs.update({"placeholder":"Abreviatura.","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Proceso.","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})


	class Meta:
		model = Proceso
		fields = [
			
			'abreviatura',
			'descripcion',
			
		]

		labels={

			"abreviatura":"Abreviatura",
			"descripcion":"Proceso",
			
		}


class objetivoprocesoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(objetivoprocesoform, self).__init__(*args, **kwargs)
		
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Objetivo..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})


	class Meta:
		model = ObjetivoProceso
		fields = [
			
			'descripcion',
			
		]

		labels={
			
			"descripcion":"Objetivo",
			
		}

class hitosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(hitosform, self).__init__(*args, **kwargs)
		
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})


	class Meta:
		model = Hitos
		fields = [
			
			'descripcion',
			
		]

		labels={
			
			"descripcion":"Hitos",
			
		}

class subhitosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexocultivo=kwargs.pop("cultivo")
		super(subhitosform, self).__init__(*args, **kwargs)
		
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['anexo_macro']=forms.ModelChoiceField(label="Macroproceso", queryset=Macroproceso.objects.filter(anexo_cultivo=anexocultivo))
		self.fields['anexo_macro'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['anexo_proceso'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['anexo_objetivos'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['anexo_estructura'].widget.attrs.update({"placeholder":"Hitos..","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})
		self.fields['valor'].widget.attrs.update({"placeholder":"Valor","required":"true","data-error-message":" Macroproceso requerido","class":"form-control"})

	class Meta:
		model = SubHitos
		fields = [
			
			'descripcion',
			'anexo_macro',
			'anexo_proceso',
			'anexo_objetivos',
			'anexo_estructura',
			'valor',
			
		]

		labels={
			
			"descripcion":"SubHitos",
			"anexo_macro":"Macroproceso",
			"anexo_proceso":"Proceso",
			"anexo_objetivos":"Objetivo",
			"anexo_estructura":"Estructura",
			"valor":"Valor",
		}

