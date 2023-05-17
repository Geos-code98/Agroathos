from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.maestras.models import PresentacionesAthos 
from apps.maestras.models import ClientesAthos
from apps.maestras.models import MaestraPresentacionesAthos
from apps.maestras.models import CalibresAthos
from apps.maestras.models import LineaEmpaqueAthos
from apps.maestras.models import CartillasAthos
from apps.maestras.models import LaboresAthos
from apps.maestras.models import DescripcionLaboresAthos
from apps.maestras.models import AuxiliaresCampoAthos
from apps.maestras.models import TanquesAthos
from apps.maestras.models import LaboresPlantaAthos


class presentacionesathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(presentacionesathosform, self).__init__(*args, **kwargs)
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['presentaciong'].widget.attrs.update({"placeholder":"Presentacion G","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['presentacion'].widget.attrs.update({"placeholder":"Presentacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pesodestino'].widget.attrs.update({"placeholder":"Peso Destino","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pesomin'].widget.attrs.update({"placeholder":"Peso Min","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pesomax'].widget.attrs.update({"placeholder":"Peso Max","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['por_pesomin'].widget.attrs.update({"placeholder":" % Peso Min","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['por_pesomax'].widget.attrs.update({"placeholder":"% Peso Max","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['cliente'].widget.attrs.update({"placeholder":"Cliente","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})		
	class Meta:
		model = PresentacionesAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'presentaciong',
			'presentacion',
			'pesodestino',
			'pesomin',
			'pesomax',
			'por_pesomin',
			'por_pesomax',	
			'cliente',
			
			
		]

		labels={
			"anexo_centro":"Centro",
			"anexo_cultivo":"Cultivo",
			"presentaciong":"Presentacion G",
			"presentacion":"Presentacion",
			"pesodestino":"Peso Destino",
			"pesomin":"Peso Minimo",
			"pesomax":"Peso Maximo",
			"por_pesomin":"% Peso Minimo",
			"por_pesomax":"% Peso Maximo",			
			"cliente":"Cliente",
			
		}

class clientesathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(clientesathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		self.fields['cliente'].widget.attrs.update({"placeholder":"Cliente","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		
	class Meta:
		model = ClientesAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'cliente',
			
			
			
		]

		labels={
			"anexo_centro":"Centro",
			"anexo_cultivo":"Cultivo",
			"cliente":"Cliente",
		
			
		}

class maestrapresentacionesathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(maestrapresentacionesathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		
	class Meta:
		model = MaestraPresentacionesAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'codigo',
			'descripcion',
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"codigo":"Codigo",
			"descripcion":"Descripcion",
		
		}

class calibresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(calibresathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		
	class Meta:
		model = CalibresAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'descripcion',
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"descripcion":"Descripcion",
		
		}


class lineaempaqueathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(lineaempaqueathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		
	class Meta:
		model = LineaEmpaqueAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'descripcion',
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"descripcion":"Descripcion",
		
		}

class cartillasathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(cartillasathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		self.fields['cartilla'].widget.attrs.update({"placeholder":"Cartilla","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['grupo'].widget.attrs.update({"placeholder":"Grupo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['subgrupo'].widget.attrs.update({"placeholder":"SubGrupo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		
	class Meta:
		model = CartillasAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'cartilla',
			'codigo',
			'grupo',
			'subgrupo'
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"cartilla":"Cartilla",
			"codigo":"Codigo",
			"grupo":"Grupo",
			"subgrupo":"SubGrupo",
		
		}

class laboresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(laboresathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})

		self.fields['tipolabor'].widget.attrs.update({"placeholder":"Tipo Labor","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = LaboresAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'tipolabor',
			'descripcion'
			
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"tipolabor":"Tipo Labor",
			"descripcion":"Descripcion",
			
		
		}



class descripcionlaboresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(descripcionlaboresathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['codigo_labor'].widget.attrs.update({"placeholder":"Codigo Labor","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['descripcion_labor'].widget.attrs.update({"placeholder":"Descripcion Labor","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_tipolabor'].widget.attrs.update({"placeholder":"Tipo Labor","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		
	class Meta:
		model = DescripcionLaboresAthos
		fields = [
			'anexo_centro',
			'anexo_cultivo',
			'codigo_labor',
			'anexo_tipolabor',
			'descripcion_labor',
			
		]

		labels={
			"anexo_centro":"Centro",
			'anexo_cultivo':"Cultivo",
			"codigo_labor":"Codigo Labor",
			"anexo_tipolabor":"Tipo Labor",
			"descripcion_labor":"Descripcion Labor",
		
		}

class auxiliarescampoathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(auxiliarescampoathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
		self.fields['auxiliar'].widget.attrs.update({"placeholder":"Auxiliar","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"Dni","data-required":"true","data-error-message":"Centro requerido","pattern":"[0-9]+","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		
	class Meta:
		model = AuxiliaresCampoAthos
		fields = [
			'anexo_zona',
			'anexo_fundo',
			'auxiliar',
			'dni',
			'anexo_estado',
			'anexo_tipo',
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"auxiliar":"Auxiliar",
			"dni":"DNI",
			"anexo_estado":"Estado",
			"anexo_tipo":"Tipo",
		}

class tanquesathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(tanquesathosform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Data requerida","class":"form-control"})        
        self.fields['numero_tanque'].widget.attrs.update({"placeholder":"N° Tanque","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['capacidad'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['fundo_tanque'].widget.attrs.update({"placeholder":"Fundo - Tanque","required":"true","data-error-message":"Data requerida","class":"form-control"})

    class Meta:
        model = TanquesAthos
        fields = [
            'anexo_zona',
            'anexo_fundo',
            'numero_tanque',
            'capacidad',
            'fundo_tanque',
        ]

        labels={
            "anexo_zona":"Zona",
            "anexo_fundo":"Fundo",
            "numero_tanque":"N° Tanque",
            "capacidad":"Capacidad",
            "fundo_tanque":"Fundo - N° Tanque",
        }

class laboresplantaathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(laboresplantaathosform, self).__init__(*args, **kwargs)
        
        self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['anexo_proceso'].widget.attrs.update({"placeholder":"Proceso","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['labor'].widget.attrs.update({"placeholder":"labor","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
        
        
    class Meta:
        model = LaboresPlantaAthos
        fields = [
            'codigo',
            'anexo_cultivo',
            'anexo_proceso',
            'labor'
        ]

        labels={
            "codigo":"Código",
            "anexo_cultivo":"Cultivo",
            "anexo_proceso":"Proceso / Actividad",
            "labor":"Labor",
        }
