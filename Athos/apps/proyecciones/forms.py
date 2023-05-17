from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.proyecciones.models import ProyeccionArandano
from apps.proyecciones.models import DetalleProyeccionArandano

from apps.menu.models import fundo
from apps.proyecciones.models import ProyeccionSemanalArandano
from apps.proyecciones.models import VariableAgronomica
from apps.proyecciones.models import ProyeccionDiariaArandano
from apps.proyecciones.models import DetProyeccionDiariaArandano
from apps.proyecciones.models import ProyeccionAnualArandano
from apps.proyecciones.models import DetalleProyeccionAnualArandano


class proyeccionarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proyeccionarandanoform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Eje","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		#self.fields['anexo_fundo']=forms.ModelChoiceField(queryset=fundo.objects.filter(zona_id=2).order_by("nom_fundo"),initial=0)
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['anexo_variable']=forms.ModelChoiceField(label="Variable", queryset=VariableAgronomica.objects.all())
		self.fields['anexo_variable'].widget.attrs.update({"placeholder":"Variable","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		
	class Meta:
		model = ProyeccionArandano
		fields = [
			'anio',
			'semana',
			'anexo_cultivo',
			'anexo_eje',
			'anexo_fundo',
			'anexo_variable',
			
			
		]

		labels={
			"anio":"Año",
			"semana":"Semana",
			"anexo_cultivo":"Cultivo",
			"anexo_eje":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_variable":"Variable",
			
		}


class detalleproyeccionarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexofundo=kwargs.pop("anexo_fundo")
		variableagronomica=kwargs.pop("anexo_subvariable")
		anexocultivo=kwargs.pop("anexo_cultivo")
		
		super(detalleproyeccionarandanoform, self).__init__(*args, **kwargs)
	
		
	

		self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=anexofundo.fundo3.filter(estado_id=1,anexo_variedad__cul=anexocultivo))
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"PEP","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		
		self.fields['anexo_subvariable']=forms.ModelChoiceField(label="SubVariable", queryset=variableagronomica.AnexoSubVariable.all())
		self.fields['anexo_subvariable'].widget.attrs.update({"placeholder":"SubVariable","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=anexocultivo.cutivo1.all())
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"SubVariable","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		
		self.fields['lunes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['martes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['miercoles'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['jueves'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['viernes'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['sabado'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['domingo'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})

		self.fields['semana2'].widget.attrs.update({"readonly":"True","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana3'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana4'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})

		self.fields['lunes_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['martes_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['miercoles_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['jueves_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['viernes_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['sabado_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['domingo_sem2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})

	class Meta:
		model = DetalleProyeccionArandano
		fields = [
			'anexo_pep',
			'anexo_subvariable',
			'anexo_variedad',
			'lunes',
			'martes',
			'miercoles',
			'jueves',
			'viernes',
			'sabado',
			'domingo',

			'semana2',
			'semana3',
			'semana4',

			'lunes_sem2',
			'martes_sem2',
			'miercoles_sem2',
			'jueves_sem2',
			'viernes_sem2',
			'sabado_sem2',
			'domingo_sem2',

			
		]

		labels={
			"anexo_pep":"PEP",
			"anexo_subvariable":"SubVariable",
			"anexo_variedad":"Variedad",
			"lunes":"Lunes",
			"martes":"Martes",
			"miercoles":"Miercoles",
			"jueves":"Jueves",
			"viernes":"Viernes",
			"sabado":"Sabado",
			"domingo":"Domingo",

			"semana2":"Semana2",
			"semana3":"Semana3",
			"semana4":"Semana4",
			
			"lunes_sem2":"Lunes - Semana 2",
			"martes_sem2":"Martes - Semana 2",
			"miercoles_sem2":"Miercoles - Semana 2",
			"jueves_sem2":"Jueves - Semana 2",
			"viernes_sem2":"Viernes - Semana 2",
			"sabado_sem2":"Sabado - Semana 2",
			"domingo_sem2":"Domingo - Semana 2",		
		}

class proyeccionsemanalarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		
		
		super(proyeccionsemanalarandanoform, self).__init__(*args, **kwargs)

		self.fields['lunes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['martes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['miercoles'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['jueves'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['viernes'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['sabado'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['domingo'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana1'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana2'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})


	class Meta:
		model = ProyeccionSemanalArandano
		fields = [
			
			'lunes',
			'martes',
			'miercoles',
			'jueves',
			'viernes',
			'sabado',
			'domingo',
			'semana1',
			'semana2',

			
		]

		labels={
			
			"lunes":"Lunes",
			"martes":"Martes",
			"miercoles":"Miercoles",
			"jueves":"Jueves",
			"viernes":"Viernes",
			"sabado":"Sabado",
			"domingo":"Domingo",
			"semana1":"Semana3",
			"semana2":"Semana4",
		}



class proyecciondiariaarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proyecciondiariaarandanoform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Eje","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		
	class Meta:
		model = ProyeccionDiariaArandano
		fields = [
			'anio',
			'semana',
			'anexo_cultivo',
			'anexo_eje',
			'anexo_fundo',
			
			
			
		]

		labels={
			"anio":"Año",
			"semana":"Semana",
			"anexo_cultivo":"Cultivo",
			"anexo_eje":"Zona",
			"anexo_fundo":"Fundo",
			
		}


class detalleproyecciondiariaarandanoform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		anexofundo1=kwargs.pop("anexo_fundo1")
		anexocultivo=kwargs.pop("anexo_cultivo")
		super(detalleproyecciondiariaarandanoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=anexofundo1.fundo3.filter(estado_id=1))
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"PEP","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})	
		
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=anexocultivo.cutivo1.all())
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"SubVariable","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		
		self.fields['lunes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['martes'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['miercoles'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['jueves'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['viernes'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['sabado'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['domingo'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})


	class Meta:
		model = DetProyeccionDiariaArandano
		fields = [
			'anexo_pep',
			'anexo_variedad',
			'lunes',
			'martes',
			'miercoles',
			'jueves',
			'viernes',
			'sabado',
			'domingo',
		]

		labels={
			"anexo_pep":"PEP",
			"anexo_variedad":"Variedad",
			"lunes":"Lunes",
			"martes":"Martes",
			"miercoles":"Miercoles",
			"jueves":"Jueves",
			"viernes":"Viernes",
			"sabado":"Sabado",
			"domingo":"Domingo",
		
		}


class proyeccionanualarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proyeccionanualarandanoform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Eje","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		#self.fields['anexo_fundo']=forms.ModelChoiceField(queryset=fundo.objects.filter(zona_id=2).order_by("nom_fundo"),initial=0)
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		
		self.fields['anexo_variable'].widget.attrs.update({"placeholder":"Variable","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['anexo_version'].widget.attrs.update({"placeholder":"Variable","data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		

	class Meta:
		model = ProyeccionAnualArandano
		fields = [
			'anio',
		
			'anexo_cultivo',
			'anexo_eje',
			'anexo_fundo',
			'anexo_variable',
			'anexo_version',

			
		]

		labels={
			"anio":"Año",
			"anexo_cultivo":"Cultivo",
			"anexo_eje":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_variable":"Variable",
			"anexo_version":"Version",
		}

class detalleproyeccionanualarandanoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		anexofundo=kwargs.pop("anexo_fundo")
		variableagronomica=kwargs.pop("anexo_subvariable")
		
		super(detalleproyeccionanualarandanoform, self).__init__(*args, **kwargs)
	
		
	

		self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=anexofundo.fundo3.all())
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"PEP","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		
		self.fields['anexo_subvariable']=forms.ModelChoiceField(label="SubVariable", queryset=variableagronomica.AnexoSubVariable.all())
		self.fields['anexo_subvariable'].widget.attrs.update({"placeholder":"SubVariable","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		
		self.fields['anexo_aniocampana'].widget.attrs.update({"placeholder":"Campaña","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['anexo_varpep'].widget.attrs.update({"placeholder":"Campaña","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['anexo_aniocosecha'].widget.attrs.update({"placeholder":"Campaña","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})






		self.fields['semana1'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana2'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana3'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana4'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana5'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana6'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana7'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana8'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana9'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana10'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana11'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana12'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana13'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana14'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana15'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana16'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana17'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana18'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana19'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana20'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana21'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana22'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana23'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana24'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana25'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana26'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana27'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana28'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana29'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana30'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana31'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana32'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana33'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana34'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana35'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana36'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana37'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana38'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana39'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana40'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana41'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana42'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana43'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana44'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['semana45'].widget.attrs.update({"data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		self.fields['semana46'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana47'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana48'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana49'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana50'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana51'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana52'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})
		self.fields['semana53'].widget.attrs.update({"data-required":"true","data-error-message":"Hora requerida","class":"form-control"})




	class Meta:
		model = DetalleProyeccionAnualArandano
		fields = [
			'anexo_pep',
			'anexo_subvariable',
			
			'anexo_aniocampana',
			'anexo_aniocosecha',
			'anexo_varpep',
			'semana1',
			'semana2',
			'semana3',
			'semana4',
			'semana5',
			'semana6',
			'semana7',
			'semana8',
			'semana9',
			'semana10',
			'semana11',
			'semana12',
			'semana13',
			'semana14',
			'semana15',
			'semana16',
			'semana17',
			'semana18',
			'semana19',
			'semana20',
			'semana21',
			'semana22',
			'semana23',
			'semana24',
			'semana25',
			'semana26',
			'semana27',
			'semana28',
			'semana29',
			'semana30',
			'semana31',
			'semana32',
			'semana33',
			'semana34',
			'semana35',
			'semana36',
			'semana37',
			'semana38',
			'semana39',
			'semana40',
			'semana41',
			'semana42',
			'semana43',
			'semana44',
			'semana45',
			'semana46',
			'semana47',
			'semana48',
			'semana49',
			'semana50',
			'semana51',
			'semana52',
			'semana53',
		]

		labels={
			"anexo_pep":"PEP",
			"anexo_subvariable":"SubVariable",
			
			"anexo_aniocampana":"Año Campaña",
			"anexo_aniocosecha":"Año Cosecha",
			"anexo_varpep":"VAR PEP",
			"semana1":"Semana1",
			"semana2":"Semana2",
			"semana3":"Semana3",
			"semana4":"Semana4",
			"semana5":"Semana5",
			"semana6":"Semana6",
			"semana7":"Semana7",
			"semana8":"Semana8",
			"semana9":"Semana9",
			"semana10":"Semana10",
			"semana11":"Semana11",
			"semana12":"Semana12",
			"semana13":"Semana13",
			"semana14":"Semana14",
			"semana15":"Semana15",
			"semana16":"Semana16",
			"semana17":"Semana17",
			"semana18":"Semana18",
			"semana19":"Semana19",
			"semana20":"Semana20",
			"semana21":"Semana21",
			"semana22":"Semana22",
			"semana23":"Semana23",
			"semana24":"Semana24",
			"semana25":"Semana25",
			"semana26":"Semana26",
			"semana27":"Semana27",
			"semana28":"Semana28",
			"semana29":"Semana29",
			"semana30":"Semana30",
			"semana31":"Semana31",
			"semana32":"Semana32",
			"semana33":"Semana33",
			"semana34":"Semana34",
			"semana35":"Semana35",
			"semana36":"Semana36",
			"semana37":"Semana37",
			"semana38":"Semana38",
			"semana39":"Semana39",
			"semana40":"Semana40",
			"semana41":"Semana41",
			"semana42":"Semana42",
			"semana43":"Semana43",
			"semana44":"Semana44",
			"semana45":"Semana45",
			"semana46":"Semana46",
			"semana47":"Semana47",
			"semana48":"Semana48",
			"semana49":"Semana49",
			"semana50":"Semana50",
			"semana51":"Semana51",
			"semana52":"Semana52",
			"semana53":"Semana53",
		}