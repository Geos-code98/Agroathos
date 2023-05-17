from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.programaproduccion.models import Grupos
from apps.programaproduccion.models import SubGrupos
from apps.programaproduccion.models import Hitos
from apps.programaproduccion.models import SubHitos



class gruposform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(gruposform, self).__init__(*args, **kwargs)
		
		self.fields['desc'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = Grupos
		fields = [
			
			'desc',
				
		]

		labels={
			
			"desc":"Descripcion",
			
			
		}

class subgruposform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(subgruposform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_grupo'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['desc'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = SubGrupos
		fields = [
			
			'anexo_grupo',
			'desc',
				
		]

		labels={
			
			"anexo_grupo":"Grupo",
			"desc":"Descripcion",
			
			
		}


class hitosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(hitosform, self).__init__(*args, **kwargs)

		self.fields['anexo_subgrupo'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['desc'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = Hitos
		fields = [
			
			'anexo_subgrupo',
			'desc',
				
		]

		labels={
			
			"anexo_subgrupo":"SubGrupo",
			"desc":"Descripcion",
			
			
		}


class subhitosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(subhitosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_hito'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['desc'].widget.attrs.update({"required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = SubHitos
		fields = [
			
			'anexo_hito',
			'desc',
				
		]

		labels={
			
			"anexo_hito":"Grupo Variable",
			"desc":"Descripcion",
			
			
		}
