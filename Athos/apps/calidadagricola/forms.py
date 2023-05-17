from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.menu.models import ProgramaProduccion
from apps.menu.models import variedad

from apps.calidadagricola.models import EvCalCosechaGr
from apps.calidadagricola.models import DetalleEvCalCosechaGrCat1

from apps.calidadagricola.models import DetalleEvCalCosechaGrCat2
from apps.calidadagricola.models import DetalleEvCalCosechaGrDescarte
from apps.calidadagricola.models import DetalleEvCalCosechaGrCampo

from apps.calidadagricola.models import EvCalidadMuestreoPlantaGr

class evcalcosechagrform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalcosechagrform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Ubicacion","required":"false","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['sector'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['qrsupervisor'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['anexo_supervisor'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=1))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		
	class Meta:
		model = EvCalCosechaGr
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'anexo_pep',
			'anexo_turno',
			'sector',
			'qrsupervisor',
			'anexo_supervisor',
			'anexo_variedad',
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_pep":"PEP",
			"anexo_turno":"Turno",
			"sector":"Sector",
			"qrsupervisor":"Qr-Supervisor",
			"anexo_supervisor":"Supervisor",
			
			"anexo_variedad":"Variedad",
		}

class detalleevcalcosechagrcat1form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	
		super(detalleevcalcosechagrcat1form, self).__init__(*args, **kwargs)
		
		self.fields['total_fruta'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fruta_rajada'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fruta_clara2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_clara3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_descarte'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['dano_tijera'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['sin_pedunculo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['con_pedunculo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		self.fields['fruta_deforme'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_deshidratada'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fruta_pquemada'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['qrevaluador'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})

		self.fields['queresa'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_hojas'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		self.fields['fruta_sana'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_cosechable_c3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['corona_deshidratada'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['corona_botritis'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		self.fields['anexo_guantes'].widget.attrs.update({"placeholder":"------","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
		self.fields['anexo_tijeras'].widget.attrs.update({"placeholder":"------","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_jabas_burbupack'].widget.attrs.update({"placeholder":"------","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_jabas_sinb'].widget.attrs.update({"placeholder":"------","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		self.fields['cochinilla'].widget.attrs.update({"placeholder":"------","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['color25'].widget.attrs.update({"placeholder":"------","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
	class Meta:
		model = DetalleEvCalCosechaGrCat1
		fields = [
			'total_fruta',
			'fruta_rajada',
			'fruta_clara2',
			'fruta_clara3',
			'fruta_descarte',
			'dano_tijera',
			'sin_pedunculo',
			'con_pedunculo',
			
			'fruta_deforme',
			'fruta_deshidratada',
			'fruta_pquemada',
			'queresa',
			'fruta_hojas',
			'fruta_sana',
			'qrevaluador',			
			'fruta_cosechable_c3',
			'corona_deshidratada',
			'corona_botritis',
			'anexo_guantes',
			'anexo_tijeras',
			'anexo_jabas_burbupack',
			'anexo_jabas_sinb',
			'cochinilla',
			'color25',

		]

		labels={
			"total_fruta":"Total Fruta",
			"fruta_rajada":"Fruta Rajada",
			"fruta_clara2":"Fruta Desviación-C2",
			"fruta_clara3":"Fruta Desviación-C3",
			"fruta_descarte":"Fruta Descarte",
			"dano_tijera":"Daño Tijera",
			"sin_pedunculo":"Sin Pedunculo",
			"con_pedunculo":"Pedunculo Largo",
			"fruta_deforme":"Fruta Deforme",
			"fruta_deshidratada":"Fruta Deshidratado",
			"fruta_pquemada":"Fruta Punta Quemada",
			"queresa":"Queresa",
			"fruta_hojas":"Fruta con Hojas",
			"fruta_sana":"Fruta Sana",
			"qrevaluador":"Qr-Cosechador",
			"fruta_cosechable_c3":"Fruta C3 Cosechable",
			"corona_deshidratada":"Corona Deshidratada",
			"corona_botritis":"Corona Botrytis",

			"anexo_guantes":"Estado de Guantes",
		    "anexo_tijeras":"Estado de Tijeras",
		    "anexo_jabas_burbupack":"Jabas con Burbupack",
		    "anexo_jabas_sinb":"Jabas sin Base",
		    "cochinilla":"Cochinilla",
		    "color25":"Color 2.5",

		}




class detalleevcalcosechagrcat2form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	
		super(detalleevcalcosechagrcat2form, self).__init__(*args, **kwargs)
		
		self.fields['total_fruta'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fruta_cat1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['qrevaluador'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_verde2'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		


	class Meta:
		model = DetalleEvCalCosechaGrCat2
		fields = [
			'total_fruta',
			'fruta_cat1',
			'qrevaluador',
			'fruta_verde2',
			
		]

		labels={
			"total_fruta":"Total Fruta",
			"fruta_cat1":"Fruta Cat.I",
			"qrevaluador":"Qr-Cosechador",
			"fruta_verde2":"Fruta Verde 2DA"
		}


class detalleevcalcosechagrdescarteform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	
		super(detalleevcalcosechagrdescarteform, self).__init__(*args, **kwargs)
		
		self.fields['total_fruta'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fruta_cat1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['qrevaluador'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})


	class Meta:
		model = DetalleEvCalCosechaGrDescarte
		fields = [
			'total_fruta',
			'fruta_cat1',
			'qrevaluador',
		]

		labels={
			"total_fruta":"Total Fruta",
			"fruta_cat1":"Fruta Cat.I",
			"qrevaluador":"Qr-Cosechador",
		}


class detalleevcalcosechagrcampoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	
		super(detalleevcalcosechagrcampoform, self).__init__(*args, **kwargs)
		
		self.fields['rajados'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['r3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['r35'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['r4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['r5'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['qrevaluador'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_verde_pl'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		

	class Meta:
		model = DetalleEvCalCosechaGrCampo
		fields = [
			'rajados',
			'r3',
			'r35',
			'r4',
			'r5',
			'qrevaluador',
			'fruta_verde_pl',
			
		]

		labels={
			"rajados":"Rajados",
			"r3":"Color 3",
			"r35":"Color 3.5",
			"r4":"Color 4",
			"r5":"Color 5",
			"qrevaluador":"Qr-Cosechador",
			"fruta_verde_pl":"Fruta Verde Planta",
		}




class evcalidadmuestreoplantagrform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	
		super(evcalidadmuestreoplantagrform, self).__init__(*args, **kwargs)
		
		self.fields['qrpalet'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['num_palet'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['variedad'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['guia_remision'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		

	class Meta:
		model = EvCalidadMuestreoPlantaGr
		fields = [
			'qrpalet',
			'num_palet',
			'variedad',
			'guia_remision',
			
		]

		labels={
			"qrpalet":"Qr Palet",
			"num_palet":"Numero Palet",
			"variedad":"Variedad",
			"guia_remision":"Guia Remision",
			
		}