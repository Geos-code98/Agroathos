from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.menu.models import ProgramaProduccion
from apps.sanidad.models import ProductosSanidad
from apps.sanidad.models import IngredientesSanidad 
from apps.sanidad.models import ToxicologiaSanidad
from apps.sanidad.models import PlagasEnfermedadesSanidad
from apps.sanidad.models import TipoMetodoSanidad
from apps.sanidad.models import EquiposSanidad
from apps.sanidad.models import TipoDosisSanidad
from apps.sanidad.models import LugaresAplicacionSanidad
from apps.sanidad.models import TractoresAthos
from apps.sanidad.models import BoquillasSanidadAthos
from apps.sanidad.models import OperadoresSanidadAthos

from apps.sanidad.models import UbicacionProductosAutorizados
from apps.sanidad.models import ProductosAutorizados

from apps.sanidad.models import UbicacionRegistroAplicacion

from apps.sanidad.models import MaestraLMR

from apps.sanidad.models import DetalleProductosAutorizados

from apps.sanidad.models import RegistroAplicacion
from apps.sanidad.models import DetalleLmrPa

from apps.sanidad.models import DetalleRegistroAplicacion

from apps.sanidad.models import ProyeccionSemanalSanidad
from apps.sanidad.models import DetalleProyeccionSemanalSanidad
from apps.sanidad.models import RegistroProyeccionSemanalSanidad

from apps.sanidad.models import ConfirmativaRegistroAplicacion

class productossanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(productossanidadform, self).__init__(*args, **kwargs)
		
		self.fields['subgrupo'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['partidarc'].widget.attrs.update({"placeholder":"Partida RC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['producto'].widget.attrs.update({"placeholder":"Familia..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = ProductosSanidad
		fields = [
			'subgrupo',
			'partidarc',
			'producto',
		]

		labels={
			"subgrupo":"SubGrupo",
			"partidarc":"Partida RC",
			"producto":"Familia",
		}

class ingredientessanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ingredientessanidadform, self).__init__(*args, **kwargs)
		
		
		
		self.fields['ingrediente'].widget.attrs.update({"placeholder":"Ingredientes..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = IngredientesSanidad
		fields = [
			
			'ingrediente',
			
			
			
		]

		labels={
			
			"ingrediente":"Ingredientes",
		
		}

class toxicologiasanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(toxicologiasanidadform, self).__init__(*args, **kwargs)
		
		
		
		self.fields['toxico'].widget.attrs.update({"placeholder":"Toxicologia..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = ToxicologiaSanidad
		fields = [
			
			'toxico',
			
			
			
		]

		labels={
			
			"toxico":"Toxicologia",
		
		}

class plagasenfermedadessanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(plagasenfermedadessanidadform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Tipo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tipo'].widget.attrs.update({"placeholder":"Tipo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nombre_comun'].widget.attrs.update({"placeholder":"Nombre Comun","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nombre_cientifico'].widget.attrs.update({"placeholder":"Nombre Especifico","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = PlagasEnfermedadesSanidad
		fields = [
			
			'anexo_cultivo',
			'tipo',
			'nombre_comun',
			'nombre_cientifico',			
		]

		labels={
			
			"anexo_cultivo":"Cultivo",
			"tipo":"Tipo(PLAGAS/ENFERMEDADES)",
			"nombre_comun":"Nombre Comun",
			"nombre_cientifico":"Nombre Cientifico",		
		}

class tipometodosanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tipometodosanidadform, self).__init__(*args, **kwargs)

		
		self.fields['metodo'].widget.attrs.update({"placeholder":"Metodo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	class Meta:
		model = TipoMetodoSanidad
		fields = [
			
			'metodo',			
		]

		labels={
			
			"metodo":"Metodo",
			
		}

class equipossanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(equipossanidadform, self).__init__(*args, **kwargs)

		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tequipo'].widget.attrs.update({"placeholder":"Tipo de Equipo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['equipo'].widget.attrs.update({"placeholder":"Equipo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['equipo_sap'].widget.attrs.update({"placeholder":"Equipo SAP","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['implemento'].widget.attrs.update({"placeholder":"Implemento","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['factor'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

	class Meta:
		model = EquiposSanidad
		fields = [
			
			'anexo_zona',
			'tequipo',
			'equipo',
			'equipo_sap',
			'implemento',
			'factor',
			'anexo_estado',			
		]

		labels={
			
			"anexo_zona":"Zona",
			"tequipo":"Tipo de Equipo",
			"equipo":"Equipo",
			"equipo_sap":"Equipos SAP",
			"implemento":"Implemento",
			"factor":"Factor",
			"anexo_estado":"Estado",
		}

class tipodosissanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tipodosissanidadform, self).__init__(*args, **kwargs)

		
		self.fields['tipo'].widget.attrs.update({"placeholder":"Tipo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	class Meta:
		model = TipoDosisSanidad
		fields = [
			
			'tipo',			
		]

		labels={
			
			"tipo":"Tipo Dosis",
			
		}

class lugaresaplicacionsanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(lugaresaplicacionsanidadform, self).__init__(*args, **kwargs)

		
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['lugar'].widget.attrs.update({"placeholder":"Lugar","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

	class Meta:
		model = LugaresAplicacionSanidad
		fields = [
			
			'codigo',	
			'lugar',			
		]

		labels={
			
			"codigo":"Codigo",
			"lugar":"Lugar",

			
		}

class tractoresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tractoresathosform, self).__init__(*args, **kwargs)

		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['marca'].widget.attrs.update({"placeholder":"Marca","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['modelo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['placa'].widget.attrs.update({"placeholder":"Codigo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Marca","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

	class Meta:
		model = TractoresAthos
		fields = [

			'anexo_zona',
			'codigo',	
			'marca',	
			'modelo',
			'placa',
			'anexo_estado',

		]

		labels={
		
			"anexo_zona":"Zona",
			"codigo":"Codigo",
			"marca":"Marca",
			"modelo":"Modelo",
			"placa":"Placa",
			"anexo_estado":"Estado",

			
		}


class boquillassanidadathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(boquillassanidadathosform, self).__init__(*args, **kwargs)

		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['boquilla'].widget.attrs.update({"placeholder":"Boquilla","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = BoquillasSanidadAthos
		fields = [
			
			'anexo_zona',
			'codigo',	
			'boquilla',	
		

		]

		labels={

			"anexo_zona":"Zona",	
			"codigo":"Codigo",
			"boquilla":"Boquilla",

			
		}

class operadoressanidadathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(operadoressanidadathosform, self).__init__(*args, **kwargs)

		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo_sap'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['funcion'].widget.attrs.update({"placeholder":"Funcion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

	class Meta:
		model = OperadoresSanidadAthos
		fields = [
			
			'anexo_zona',
			'codigo_sap',
			'dni',	
			'descripcion',	
			'funcion',	
			'anexo_estado',	

		]

		labels={
			
			"anexo_zona":"Zona",
			"codigo_sap":"Codigo SAP",
			"dni":"DNI",
			"descripcion":"Descripcion",
			"funcion":"Funcion",
			"anexo_estado":"Estado",

			
		}

class ubicacionproductosautorizadosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ubicacionproductosautorizadosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = UbicacionProductosAutorizados
		fields = [

			'anexo_cultivo',
			
			
		]

		labels={

			"anexo_cultivo":"Cultivo",
			
			
		}



class productosautorizadosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(productosautorizadosform, self).__init__(*args, **kwargs)
		
	#	self.fields['anexo_producto']=forms.ModelChoiceField(label="Cliente", queryset=ProductosSanidad.objects.all().partidarc	
		self.fields['anexo_producto'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['codigo_material'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nom_comercial'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_ingrediente'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_toxico'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['um'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pr'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['uac'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['equivalencia'].widget.attrs.update({"placeholder":"Equivalencia","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['nroaplicaciones'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['concentracion_ia'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['formulacion'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pc'].widget.attrs.update({"placeholder":"Pc","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo_senasa'].widget.attrs.update({"placeholder":"Codigo Senasa","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_permitido'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_versiones'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
	class Meta:
		model = ProductosAutorizados
		fields = [

			'anexo_producto',
			'codigo_material',
			'nom_comercial',
			'anexo_ingrediente',
			'anexo_toxico',
			'um',
			'pr',
			'uac',
			'equivalencia',
			
			'nroaplicaciones',
		
			
			'concentracion_ia',
			'formulacion',
			'pc',
			'codigo_senasa',
			'anexo_permitido',
			'anexo_versiones',
			'anexo_estado',
		]

		labels={

			"anexo_producto":"Familia",
			"codigo_material":"Codigo Material",
			"nom_comercial":"Nombre Comercial",
			"anexo_ingrediente":"Ingredientes Activo",
			"anexo_toxico":"Toxico",
			"um":"UM",
			"pr":"PR(Horas)",
			"uac":"UAC(dias)",
			"equivalencia":"Equivalencia",
			"nroaplicaciones":"Nro de Aplicaciones (Campaña)",
			
			
			"concentracion_ia":"Concentracion IA",
			"formulacion":"Formulacion",
			"pc":"PC",
			"codigo_senasa":"Codigo Senasa",
			"anexo_permitido":"Permitido",
			"anexo_versiones":"Versiones",
			"anexo_estado":"Estado",
		}

class ubicacionregistroaplicacionform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ubicacionregistroaplicacionform, self).__init__(*args, **kwargs)
		
		self.fields['nroreserva'].widget.attrs.update({"placeholder":"Nro Reserva..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['anexo_permitido'].widget.attrs.update({"placeholder":"Permitidos","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_produccion']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.all()[:1])
		self.fields['anexo_produccion'].widget.attrs.update({"placeholder":"PEP","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_metodo'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_equipo']=forms.ModelChoiceField(label="Equipo", queryset=EquiposSanidad.objects.all()[:1])
		self.fields['anexo_equipo'].widget.attrs.update({"multiple":"multiple","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['idequipo'].widget.attrs.update({"readonly":"readonly","placeholder":"Area","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['codigo_boquilla'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['num_boquilla'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['presion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_tanque'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['area_aplicada'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['vol_agua'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['numero_tanque'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['anexo_tractor']=forms.ModelChoiceField(label="Tractor", queryset=TractoresAthos.objects.all()[:1])
		self.fields['anexo_tractor'].widget.attrs.update({"multiple":"multiple","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['marcha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})			
		self.fields['rpm'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['velocidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fecha_aplicacion'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['fecha_premezcla'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_operario']=forms.ModelChoiceField(label="Supervisor", queryset=OperadoresSanidadAthos.objects.filter(funcion="SUPERVISOR DE APLICACIONES")[:1])
		self.fields['anexo_operario'].widget.attrs.update({"multiple":"multiple","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['observacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['idoperario'].widget.attrs.update({"readonly":"readonly","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['idtractor'].widget.attrs.update({"readonly":"readonly","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
	class Meta:
		model = UbicacionRegistroAplicacion
		fields = [
			'nroreserva',
			'anexo_permitido',
			'anexo_fecha',
			'anexo_cultivo',
			'anexo_zona',
			'anexo_fundo',
			'anexo_produccion',
			'anexo_metodo',	
			'anexo_equipo',
			'codigo_boquilla',
			'num_boquilla',
			'presion',
			'capacidad_tanque',
			'area_aplicada',
			'vol_agua',
			'numero_tanque',	
			'anexo_tractor',
			'rpm',
			'velocidad',
			'marcha',
			'fecha_aplicacion',
			'fecha_premezcla',
			'anexo_operario',
			'anexo_lugar',
			'observacion',
			'idequipo',
			'idoperario',
			'idtractor',
		]

		labels={
			"nroreserva":"Nro Reserva",
			"anexo_permitido":"Permitido",
			"anexo_fecha":"Fecha Registro",
			"anexo_cultivo":"Cultivo",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_produccion":"PEP",
			"anexo_metodo":"Metodo de Aplic.",
			"anexo_equipo":"Equipo",
			"codigo_boquilla":"Codigo Boquilla",
			"num_boquilla":"Numero Boquilla",
			"presion":"Presion",
			"capacidad_tanque":"Capacidad Tanque",
			"area_aplicada":"Area Aplicada",
			"vol_agua":"Volumen Agua(Lt/Ha)",
			"numero_tanque":"Numero Tanque",
			"anexo_tractor":"Tractor",
			"marcha":"Marcha",
			"rpm":"RPM",
			"velocidad":"Velocidad",
			"fecha_aplicacion":"Fecha Aplicacion",
			"fecha_premezcla":"Fecha Pre Mezcla",
			"anexo_operario":"Supervisor",
			"anexo_lugar":"Lugar",
			"observacion":"Observacion",
			"idequipo":"Equipos Multiples",
			"idoperario":"Operarios Multiples",
			"idtractor":"Tractor Multiples",
		}

class editarubicacionregistroaplicacionform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(editarubicacionregistroaplicacionform, self).__init__(*args, **kwargs)
		
		self.fields['nroreserva'].widget.attrs.update({"placeholder":"Nro Reserva..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_permitido'].widget.attrs.update({"placeholder":"Permitidos","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['anexo_produccion']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.none())
		self.fields['anexo_produccion'].widget.attrs.update({"placeholder":"PEP","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_metodo'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_equipo'].widget.attrs.update({"multiple":"multiple","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['idequipo'].widget.attrs.update({"readonly":"readonly","placeholder":"Area","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo_boquilla'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['num_boquilla'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['presion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_tanque'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['area_aplicada'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['vol_agua'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['numero_tanque'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_tractor'].widget.attrs.update({"multiple":"multiple","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['marcha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['rpm'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['velocidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fecha_aplicacion'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fecha_premezcla'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_operario'].widget.attrs.update({"multiple":"multiple","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['idoperario'].widget.attrs.update({"readonly":"readonly","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['idtractor'].widget.attrs.update({"readonly":"readonly","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = UbicacionRegistroAplicacion
		fields = [
			'nroreserva',
			'anexo_permitido',
			'anexo_fecha',
			'anexo_cultivo',
			'anexo_zona',
			'anexo_fundo',
			'anexo_produccion',
			'anexo_metodo',	
			'anexo_equipo',
			'codigo_boquilla',
			'num_boquilla',
			'presion',
			'capacidad_tanque',
			'area_aplicada',
			'vol_agua',
			'numero_tanque',	
			'anexo_tractor',
			'rpm',
			'velocidad',
			'marcha',
			'fecha_aplicacion',
			'fecha_premezcla',
			'anexo_operario',
			'anexo_lugar',
			'observacion',
			'idequipo',
			'idoperario',
			'idtractor',
		]

		labels={
			"nroreserva":"Nro Reserva",
			"anexo_permitido":"Permitido",
			"anexo_fecha":"Fecha Registro",
			"anexo_cultivo":"Cultivo",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_produccion":"PEP",
			"anexo_metodo":"Metodo de Aplic.",
			"anexo_equipo":"Equipo",
			"codigo_boquilla":"Codigo Boquilla",
			"num_boquilla":"Numero Boquilla",
			"presion":"Presion",
			"capacidad_tanque":"Capacidad Tanque",
			"area_aplicada":"Area Aplicada",
			"vol_agua":"Volumen Agua(Lt/Ha)",
			"numero_tanque":"Numero Tanque",
			"anexo_tractor":"Tractor",
			"marcha":"Marcha",
			"rpm":"RPM",
			"velocidad":"Velocidad",
			"fecha_aplicacion":"Fecha Aplicacion",
			"fecha_premezcla":"Fecha Pre Mezcla",
			"anexo_operario":"Supervisor",
			"anexo_lugar":"Lugar",
			"observacion":"Observacion",
			"idequipo":"Equipos Multiples",
			"idoperario":"Operarios Multiples",
			"idtractor":"Tractor Multiples",	
		}


class maestralmrform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(maestralmrform, self).__init__(*args, **kwargs)

		
		self.fields['destino'].widget.attrs.update({"placeholder":"Destino","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = MaestraLMR
		fields = [
			
			'destino',	
		
		

		]

		labels={
			
			"destino":"Destino",
		
			
		}


class detalleproductosautorizadosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("variable_cultivo")
		super(detalleproductosautorizadosform, self).__init__(*args, **kwargs)

		self.fields['anexo_plagas']=forms.ModelChoiceField(label="Plagas", queryset=variablecultivo.AnexoCultivoPlagasEnfSanidad.filter(anexo_cultivo=variablecultivo))
		self.fields['anexo_plagas'].widget.attrs.update({"placeholder":"Codigo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_dosis'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dosis_min'].widget.attrs.update({"placeholder":"Dosis Min","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dosis_max'].widget.attrs.update({"placeholder":"Dosis Max","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['por_concentracion_min'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['por_concentracion_max'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['factor_premezcla'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = DetalleProductosAutorizados
		fields = [
			
			'anexo_plagas',	
			'dosis_min',
			'dosis_max',
			'por_concentracion_min',
			'por_concentracion_max',
			'anexo_dosis',
			'factor_premezcla',
			
		]

		labels={
			
			"anexo_plagas":"Plaga",
			"dosis_min":"Dosis Min",
			"dosis_max":"Dosis Max",
			"por_concentracion_min":"% Concentracion (minimo)",
			"por_concentracion_max":"% Concentracion (maximo)",
			"anexo_dosis":"Dosis",
			"factor_premezcla":"Factor Premezcla",
		
		}

class registroaplicacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")
		variablezona=kwargs.pop("anexo_zona")
		super(registroaplicacionform, self).__init__(*args, **kwargs)

		

		self.fields['anexo_listas']=forms.ModelChoiceField(label="Productos Autorizados", queryset=ProductosAutorizados.objects.filter(anexo_detalle__anexo_cultivo=variablecultivo))

		self.fields['anexo_listas'].widget.attrs.update({"placeholder":"Listas..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dosis'].widget.attrs.update({"readonly":"readonly","placeholder":"Dosis..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dosis_real'].widget.attrs.update({"placeholder":"Dosis..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	
		self.fields['factor'].widget.attrs.update({"readonly":"readonly","placeholder":"Factor..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['total_producto'].widget.attrs.update({"readonly":"true","placeholder":"Total Producto..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"readonly":"readonly","placeholder":"Tipo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tipo_dosis_real'].widget.attrs.update({"placeholder":"Tipo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	
		self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"....","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cod_aplicador'].widget.attrs.update({"placeholder":"....","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta'].widget.attrs.update({"placeholder":"Consumo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

		#self.fields['anexo_objetivo']=forms.ModelChoiceField(label="Objetivo", queryset=variablecultivo.AnexoCultivoPlagasEnfSanidad.filter(anexo_cultivo=variablecultivo))
		self.fields['anexo_objetivo'].widget.attrs.update({"placeholder":"Objetivo..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
			

	class Meta:
		model = RegistroAplicacion
		fields = [
			
		

			'anexo_listas',
			'dosis',
			'dosis_real',	
			'factor',
			'total_producto',	
			'anexo_tipo',
			'tipo_dosis_real',
			'anexo_objetivo',

			'hora_inicio',	
			'hora_final',	
			'cod_aplicador',	
			'anexo_rpta',
			

		]

		labels={
			
		

			"anexo_listas":"Productos Autorizados",
			"dosis":"Dosis Etiqueta",
			"dosis_real":"Dosis Real",
			"factor":"Factor",
			"total_producto":"Total Producto",
			"anexo_tipo":"Tipo Dosis Etiqueta(No Tocar)",
			"tipo_dosis_real":"Tipo Dosis Real",
			"anexo_objetivo":"Objetivo",
			
			"hora_inicio":"Hora Inicio",
			"Hora Final":"Hora Final",
			"cod_aplicador":"Codigo Aplicador",
			"anexo_rpta":"Premezcla?",
		}

class detallelmrpaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detallelmrpaform, self).__init__(*args, **kwargs)

		
		self.fields['anexo_lmr'].widget.attrs.update({"placeholder":"Destino","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dato_lmr'].widget.attrs.update({"placeholder":"Datos LMR","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = DetalleLmrPa
		fields = [
			
			'anexo_lmr',
			'dato_lmr',	

		]

		labels={
			
			"anexo_lmr":"LMR",
			"dato_lmr":"DATO LMR",
		
		}




class detalleregistroaplicacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")
		super(detalleregistroaplicacionform, self).__init__(*args, **kwargs)
		
		
		self.fields['consumo_detalle'].widget.attrs.update({"placeholder":"Consumo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['fecha_consumo'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control","id":"datepicker"})
		
		
	class Meta:
		model = DetalleRegistroAplicacion
		fields = [
			
			'consumo_detalle',
			
			'fecha_consumo',
			
		]

		labels={
			
			"consumo_detalle":"Consumo",
			
			"fecha_consumo":"Fecha Consumo",
			
		}


class confirmativaregistroaplicacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		
		super(confirmativaregistroaplicacionform, self).__init__(*args, **kwargs)
		
		
	
		self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"Hora de Inicio","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"Hora de Finalizacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_aplicador']=forms.ModelChoiceField(label="Operario", queryset=OperadoresSanidadAthos.objects.filter(funcion ="APLICADOR"))
		self.fields['anexo_aplicador'].widget.attrs.update({"multiple":"multiple","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['cod_aplicador'].widget.attrs.update({"readonly":"readonly","placeholder":"Codigo Aplicador","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['temperatura'].widget.attrs.update({"placeholder":"Temperatura..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hr'].widget.attrs.update({"placeholder":"HR..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['vv'].widget.attrs.update({"placeholder":"VV..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['ph_antes'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_antes'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['ph_despues'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_despues'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['observaciones'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	
		
	class Meta:
		model = ConfirmativaRegistroAplicacion
		fields = [
			
		
			'hora_inicio',
			'hora_final',
			'anexo_aplicador',
			'cod_aplicador',
			
			'temperatura',
			'hr',
			'vv',
		
			'ph_antes',
			'ce_antes',
			'ph_despues',
			'ce_despues',
			'observaciones',
		
			
		]

		labels={
			
			
			"hora_inicio":"Hora Inicio",
			"hora_final":"Hora Final",
			"anexo_aplicador":"Aplicador",
			"cod_aplicador":"Cod. Aplicador",
			"temperatura":"Temperatura",
			"hr":"HR",
			"vv":"VV",

			"ph_antes":"PH Agua",
			"ce_antes":"CE Agua",
			"ph_despues":"PH Solucion",
			"ce_despues":"CE Solucion",
			"observaciones":"Observaciones",
			
			
		}

class proyeccionsemanalsanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proyeccionsemanalsanidadform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Codigo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Nro Pozo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = ProyeccionSemanalSanidad
		fields = [

			'anio',
			'semana',
			'anexo_cultivo',
			'anexo_zona',
			'anexo_fundo',
			
		]

		labels={

			"anio":"Año",
			"semana":"Semana",
			"anexo_cultivo":"Cultivo",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			
		}

class detalleproyeccionsemanalsanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")

		super(detalleproyeccionsemanalsanidadform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_producto']=forms.ModelChoiceField(label="Productos Autorizados", queryset=ProductosAutorizados.objects.filter(anexo_detalle__anexo_cultivo=variablecultivo))
		self.fields['anexo_producto'].widget.attrs.update({"placeholder":"Producto","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		


	
		
		






		
	class Meta:
		model = DetalleProyeccionSemanalSanidad
		fields = [

			'anexo_producto',
			'cantidad',
			
		]

		labels={

			"anexo_producto":"Producto",
			"cantidad":"Cantidad",
			
		}


class registroproyeccionsemanalsanidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(registroproyeccionsemanalsanidadform, self).__init__(*args, **kwargs)
		
		self.fields['sem2'].widget.attrs.update({"placeholder":"Semana 2","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sem3'].widget.attrs.update({"placeholder":"Semana 3","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sem4'].widget.attrs.update({"placeholder":"Semana 4","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = RegistroProyeccionSemanalSanidad
		fields = [

			'sem2',
			'sem3',
			'sem4',
			
		]

		labels={

			"sem2":"Semana2",
			"sem3":"Semana3",
			"sem4":"Semana4",
		}


