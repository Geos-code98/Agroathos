from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.menu.models import ProgramaProduccion
from apps.riego.models import ProductosRiego

from apps.riego.models import MetodoRiego
from apps.riego.models import EquiposRiego
from apps.riego.models import PozosRiego
from apps.riego.models import LeyNutricionRiego

from apps.riego.models import ProyeccionSemanalRiego
from apps.riego.models import DetalleProyeccionSemanalRiego
from apps.riego.models import SemDetalleProyeccionSemanalRiego

from apps.riego.models import RegistroRiegoFertilizacion
from apps.riego.models import RegistroProyeccionSemanalRiego
from apps.riego.models import DetalleRegistroRiegoFertilizacion
from apps.riego.models import DetalleRequerimientoRiegot

from apps.riego.models import DetRequerimientoRiegoFert

from apps.riego.models import ConsumoRequerimientoRiegoFert
from apps.riego.models import ExplotacionPozos

from apps.riego.models import DetalleExplotacionPozos
from apps.riego.models import OperadoresRiegoAthos

from apps.riego.models import EstacionMeteorologica

from apps.riego.models import SolucionesMadres
from apps.riego.models import DetalleSolucionesMadres
from apps.maestras.models import TanquesAthos

class productosriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(productosriegoform, self).__init__(*args, **kwargs)
		
		self.fields['subgrupo'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['partidarc'].widget.attrs.update({"placeholder":"Partida RC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['familia'].widget.attrs.update({"placeholder":"Familia..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = ProductosRiego
		fields = [
			'subgrupo',
			'partidarc',
			'familia',
			
		]

		labels={
			"subgrupo":"SubGrupo",
			"partidarc":"Partida RC",
			"familia":"Familia",
		
		}

class metodoriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(metodoriegoform, self).__init__(*args, **kwargs)
		
		self.fields['metodo'].widget.attrs.update({"placeholder":"Metodo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
	class Meta:
		model = MetodoRiego
		fields = [
			'metodo',
			
		]

		labels={
			"metodo":"Metodo",
			
		}

class equiposriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(equiposriegoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Partida RC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['equipo'].widget.attrs.update({"placeholder":"Equipo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['reservorio'].widget.attrs.update({"placeholder":"Reservorio","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['factor_correccion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['centro_costo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = EquiposRiego
		fields = [
			'anexo_zona',
			'anexo_cultivo',
			'equipo',
			'descripcion',
			'reservorio',
			'anexo_estado',
			'factor_correccion',
			'centro_costo',
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_cultivo":"Cultivo",
			"equipo":"Equipo",
			"descripcion":"Descripcion",
			"reservorio":"Reservorio",
			"anexo_estado":"Estado",
			"factor_correccion":"Factor Correccion",
			"centro_costo":"Centro Costo",
		}



class operadoresriegoathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(operadoresriegoathosform, self).__init__(*args, **kwargs)

		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['codigo_sap'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['funcion'].widget.attrs.update({"placeholder":"Funcion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

	class Meta:
		model = OperadoresRiegoAthos
		fields = [
			
			'anexo_zona',
			'anexo_fundo',
			'codigo_sap',
			'dni',	
			'descripcion',	
			'funcion',	
			'anexo_estado',	

		]

		labels={
			
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"codigo_sap":"Codigo SAP",
			"dni":"DNI",
			"descripcion":"Descripcion",
			"funcion":"Funcion",
			"anexo_estado":"Estado",

			
		}

class pozosriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(pozosriegoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['npozo'].widget.attrs.update({"placeholder":"Nro Pozo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_real'].widget.attrs.update({"placeholder":"Capacidad Real..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_ene'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_feb'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_mar'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_abr'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_may'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_jun'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_jul'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_ago'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_sep'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_oct'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_nov'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['capacidad_dic'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['caudal_autorizado'].widget.attrs.update({"placeholder":"Caudal Autorizado","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['factor_correccion'].widget.attrs.update({"placeholder":"Factor Correcion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = PozosRiego
		fields = [
			'anexo_zona',
			'anexo_fundo',
			'nombre',
			'anio',
			'codigo',
			'npozo',
			'capacidad',
			'capacidad_real',
			'capacidad_ene',
			'capacidad_feb',
			'capacidad_mar',
			'capacidad_abr',
			'capacidad_may',
			'capacidad_jun',
			'capacidad_jul',
			'capacidad_ago',
			'capacidad_sep',
			'capacidad_oct',
			'capacidad_nov',
			'capacidad_dic',
			'caudal_autorizado',
			'factor_correccion',

		]

		labels={
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anio":"Año",
			"nombre":"Nombre",
			"codigo":"Codigo",
			"npozo":"Nro Pozo",
			"capacidad":"Capacidad",
			"capacidad_real":"Capacidad Real",
			
			"capacidad_ene":"Capacidad Enero",
			"capacidad_feb":"Capacidad Febrero",
			"capacidad_mar":"Capacidad Marzo",
			"capacidad_abr":"Capacidad Abril",
			"capacidad_may":"Capacidad Mayo",
			"capacidad_jun":"Capacidad Junio",
			"capacidad_jul":"Capacidad Julio",
			"capacidad_ago":"Capacidad Agosto",
			"capacidad_sep":"Capacidad Septiembre",
			"capacidad_oct":"Capacidad Octubre",
			"capacidad_nov":"Capacidad Noviembre",
			"capacidad_dic":"Capacidad Diciembre",
			"caudal_autorizado":"Caudal Autorizado",
			"factor_correccion":"Factor de Correccion",



		}


class leynutricionriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(leynutricionriegoform, self).__init__(*args, **kwargs)
		
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_producto'].widget.attrs.update({"placeholder":"Producto","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['um'].widget.attrs.update({"placeholder":"UM","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['n'].widget.attrs.update({"placeholder":"N","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['p2o5'].widget.attrs.update({"placeholder":"P205..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['k2o'].widget.attrs.update({"placeholder":"K2O","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cao'].widget.attrs.update({"placeholder":"CAO","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['mgo'].widget.attrs.update({"placeholder":"MGO..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['s'].widget.attrs.update({"placeholder":"S","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fe'].widget.attrs.update({"placeholder":"FE","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['mn'].widget.attrs.update({"placeholder":"MN..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['b'].widget.attrs.update({"placeholder":"B","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['zn'].widget.attrs.update({"placeholder":"ZN","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['mo'].widget.attrs.update({"placeholder":"MO..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ci'].widget.attrs.update({"placeholder":"CI","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cu'].widget.attrs.update({"placeholder":"CU","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['h2o'].widget.attrs.update({"placeholder":"H2O..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['kc'].widget.attrs.update({"placeholder":"KC..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = LeyNutricionRiego
		fields = [
			'codigo',
			'anexo_producto',
			'nombre',
			'um',
			'n',
			'p2o5',
			'k2o',
			'cao',
			'mgo',
			's',
			'fe',
			'mn',
			'b',
			'zn',
			'mo',
			'ci',
			'cu',
			'h2o',
			'kc',
			
		]

		labels={
			"codigo":"Codigo",
			"anexo_producto":"Productos",
			"nombre":"Nombre",
			"um":"UM",
			"n":"N",
			"p2o5":"P2O5",
			"k2o":"K2O",
			"cao":"CAO",
			"mgo":"MGO",
			"s":"S",
			"fe":"FE",
			"mn":"MN",
			"b":"B",
			"zn":"ZN",
			"mo":"MO",
			"ci":"CI",
			"cu":"CU",
			"h2o":"H2O",
			"kc":"KC",
		}


class proyeccionsemanalriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proyeccionsemanalriegoform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Codigo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Nro Pozo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = ProyeccionSemanalRiego
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

class detalleproyeccionsemanalriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):

		variablefundo=kwargs.pop("variable_fundo")
		super(detalleproyeccionsemanalriegoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_ley'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Data requerida","class":"form-control"})
		
		self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.filter(anexo_fundo=variablefundo, estado_id=1))
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Data requerida","class":"form-control"})
		
		self.fields['semana_1'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['semana_2'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['semana_3'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['semana_4'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
		
	class Meta:
		model = DetalleProyeccionSemanalRiego
		fields = [

			'anexo_ley',
			'anexo_pep',
			'semana_1',
			'semana_2',
			'semana_3',
			'semana_4',			
		]

		labels={

			"anexo_ley":"Descripcion de Producto",
			"anexo_pep":"PEP",
			"semana_1":"Semana 1",
			"semana_2":"Semana 2",
			"semana_3":"Semana 3",
			"semana_4":"Semana 4",
		}

class semdetalleproyeccionsemanalriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):

		super(semdetalleproyeccionsemanalriegoform, self).__init__(*args, **kwargs)
		
		self.fields['sem2'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['sem3'].widget.attrs.update({"placeholder":"SubGrupo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['sem4'].widget.attrs.update({"placeholder":"Cantidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = SemDetalleProyeccionSemanalRiego
		fields = [

			'sem2',
			'sem3',
			'sem4',
			
		]

		labels={

			"sem2":"Semana 2",
			"sem3":"Semana 3",
			"sem4":"semana 4",
			
		}

class registroproyeccionsemanalriegoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(registroproyeccionsemanalriegoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_ley'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['sem2'].widget.attrs.update({"placeholder":"Semana 2","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sem3'].widget.attrs.update({"placeholder":"Semana 3","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sem4'].widget.attrs.update({"placeholder":"Semana 4","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sem5'].widget.attrs.update({"placeholder":"Semana 5","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = RegistroProyeccionSemanalRiego
		fields = [

			'anexo_ley',
			'sem2',
			'sem3',
			'sem4',
			'sem5',
		]

		labels={

			"anexo_ley":"Productos",
			"sem2":"Semana2",
			"sem3":"Semana3",
			"sem4":"Semana4",
			"sem5":"Semana5",
		}






class registroriegofertilizacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(registroriegofertilizacionform, self).__init__(*args, **kwargs)
		
		self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Producto","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Nombre..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"UM","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.filter(estado_id=1))
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"N","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_metodo'].widget.attrs.update({"placeholder":"P205..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_equipo'].widget.attrs.update({"placeholder":"K2O","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nroreserva'].widget.attrs.update({"placeholder":"Nro Reserva","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['area'].widget.attrs.update({"placeholder":"Area","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
		
	class Meta:
		model = RegistroRiegoFertilizacion
		fields = [
		
			
			'anexo_cultivo',
			'anexo_zona',
			'anexo_fundo',
			'anexo_pep',
			'anexo_metodo',
			'anexo_equipo',
			'nroreserva',
			'anio',
			'semana',
			'area',		
			
		]

		labels={

		
			"anexo_cultivo":"Cultivo",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_pep":"PEP",
			"anexo_metodo":"Metodo",
			"anexo_equipo":"Equipo",
		
		
			"nroreserva":"Nro Reserva",
			"anio":"Año",
			"semana":"Semana",
			
		
		}


class detalleregistroriegofertilizacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		
		super(detalleregistroriegofertilizacionform, self).__init__(*args, **kwargs)
		
		
		self.fields['anexo_fecha'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['turno'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

		self.fields['hectareaje'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['kc'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['m3'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_tanque'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['eto_acu'].widget.attrs.update({"placeholder":"Eto-Acumulado","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['valvula'].widget.attrs.update({"placeholder":"Valvula","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pulso1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['pulso2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pulso3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pulso4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['pulso5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['proporcion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['solucion_madre'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
	
	class Meta:
		model = DetalleRegistroRiegoFertilizacion
		fields = [

			'anexo_fecha',
			'turno',
			'hectareaje',
			'kc',
			'm3',
			'anexo_tanque',
			'eto_acu',

			'pulso1',

			'pulso2',
			'pulso3',
			'pulso4',
			'pulso5',
			'valvula',
			'proporcion',
			'solucion_madre',
			
		]

		labels={

			"anexo_fecha":"Fecha",
			"turno":"Turno",
			"hectareaje":"Ha.",
			"kc":"KC",
			"m3":"M3",
			"anexo_tanque":"Tanque",
			"eto_acu":"ETO-Acumulado",

			"pulso1":"Pulso 1",
			"pulso2":"Pulso 2",
			"pulso3":"Pulso 3",
			"pulso4":"Pulso 4",
			"pulso5":"Pulso 5",
			"valvula":"Valvula Asociada",
			"proporcion":"Proporcion",
			"solucion_madre":"Solucion Madre",
		}




class detrequerimientoriegofertform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detrequerimientoriegofertform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_ley'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['total_producto'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
		self.fields['lunes'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['martes'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['miercoles'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['jueves'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['viernes'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['sabado'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['domingo'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
#anexo_ley es producto

	class Meta:
		model = DetRequerimientoRiegoFert
		fields = [
			'anexo_ley',
			'total_producto',
			
			'lunes',
			'martes',
			'miercoles',
			'jueves',
			'viernes',
			'sabado',
			'domingo',
			
		]

		labels={
			"anexo_ley":"Producto",
			"total_producto":"Total Producto",
			
			"lunes":"Lunes",
			"martes":"Martes",
			"miercoles":"Miercoles",
			"jueves":"Jueves",
			"viernes":"Viernes",
			"sabado":"Sabado",
			"domingo":"Domingo",
		}


class consumorequerimientoriegofertform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablefundo=kwargs.pop("anexo_fundo")
		super(consumorequerimientoriegofertform, self).__init__(*args, **kwargs)
		
		self.fields['consumo'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fecha_consumo'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
		self.fields['anexo_riego']=forms.ModelChoiceField(label="Riego", queryset=DetalleRequerimientoRiegot.objects.filter(anexo_detalle__anexo_detalle__anexo_pep=variablefundo).order_by("-fecha_hora_creacion"))
		self.fields['anexo_riego'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		#self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['volumen'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['codigo'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['ph_agua'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['ce_agua'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['ph_solucion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['ce_solucion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['tensio20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['tensio40'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['tensio60'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['tensio90'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['caudal_inicial'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['caudal_final'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['paf'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		#self.fields['pdf'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		#self.fields['pdvr'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})#

		#self.fields['observacion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		


	class Meta:
		model = ConsumoRequerimientoRiegoFert
		fields = [
			'consumo',
			'fecha_consumo',
			'anexo_riego',
			
			#'hora_inicio',
			#'hora_final',
			#'volumen',
			#'codigo',
			#'ph_agua',
			#'ce_agua',
			#'ph_solucion',
			#'ce_solucion',
			#'tensio20',
			#'tensio40',
			#'tensio60',
			#'tensio90',
			#'caudal_inicial',
			#'caudal_final',
			#'paf',
			#'pdf',
			#'pdvr',
			#'observacion',
			
		]

		labels={
			"consumo":"Consumo",
			"fecha_consumo":"Fecha Consumo",
			"anexo_riego":"Riego",
			
			#"hora_inicio":"Hora Inicio",
			#"hora_final":"Hora Final",
			#"volumen":"Volumen M3",
			#"codigo":"Codigo Regador",
			#"ph_agua":"PH Agua",
			#"ce_agua":"CE Agua",
			#"ph_solucion":"PH Solucion",
			#"ce_solucion":"CE Solucion",
			#"tensio20":"Tensiometro 20",
			#"tensio40":"Tensiometro 40",
			#"tensio60":"Tensiometro 60",
			##"tensio90":"Tensiometro 90",
			##"caudal_inicial":"Hidrometro Inicial",
			##"caudal_final":"Hidrometro final",
			#"paf":"PAF",
			#"pdf":"PDF",
			#"pdvr":"PDVR",
			#"observacion":"Observacion",
			
		}

class detallerequerimientoriegotform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detallerequerimientoriegotform, self).__init__(*args, **kwargs)
		
		self.fields['fecha_consumo'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['consumo'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"...","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['anexo_pulso'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_operador'].widget.attrs.update({"multiple":"multiple","placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

		self.fields['codigo'].widget.attrs.update({"readonly":"readonly","placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ph_agua'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_agua'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['ph_solucion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_solucion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tensio20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['tensio30'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
		self.fields['tensio40'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tensio60'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['tensio90'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		

		self.fields['caudal_inicial'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['caudal_final'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		
		
		
		self.fields['paf'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['pdf'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})		
		self.fields['pdvr'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})#

		self.fields['observacion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		


	class Meta:
		model = DetalleRequerimientoRiegot
		fields = [
			
			'fecha_consumo',
			'consumo',
			'anexo_pulso',
			'hora_inicio',
			'hora_final',
			
			'codigo',
			'ph_agua',
			'ce_agua',
			'ph_solucion',
			'ce_solucion',
			'tensio20',
			'tensio30',
			'tensio40',
			'tensio60',
			'tensio90',
			'caudal_inicial',
			'caudal_final',
			'paf',
			'pdf',
			'pdvr',
			'observacion',

			'anexo_operador',
			
		]

		labels={
			
			"fecha_consumo":"Fecha Consumo",
			"consumo":"Consumo",
			"anexo_pulso":"Pulso",
			"hora_inicio":"Hora Inicio",
			"hora_final":"Hora Final",
			
			"codigo":"Codigo Regador",
			"ph_agua":"PH Agua",
			"ce_agua":"CE Agua",
			"ph_solucion":"PH Solucion",
			"ce_solucion":"CE Solucion",
			"tensio20":"Tensiometro 20",
			"tensio30":"Tensiometro 30",
			"tensio40":"Tensiometro 40",
			"tensio60":"Tensiometro 60",
			"tensio90":"Tensiometro 90",
			"caudal_inicial":"Hidrometro Inicial",
			"caudal_final":"Hidrometro final",
			"paf":"PAF",
			"pdf":"PDF",
			"pdvr":"PDVR",
			"observacion":"Observacion",
			
			"anexo_operador":"Operador",
			
		}






class explotacionpozosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(explotacionpozosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"placeholder":"Fecha","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"anexo_zona","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_pozo'].widget.attrs.update({"placeholder":"anexo_pozo","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = ExplotacionPozos
		fields = [

			'fecha',
			'anexo_zona',
			'anexo_pozo',
			
		]

		labels={

			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_pozo":"Pozo",
		}



class detalleexplotacionpozosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleexplotacionpozosform, self).__init__(*args, **kwargs)
		
		self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hidro_inicial'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hidro_final'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nivel_estatico'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nivel_dinamico'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ph'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_rpta8'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		
		
	class Meta:
		model = DetalleExplotacionPozos
		fields = [

			'hora_inicio',
			'hora_final',
			'hidro_inicial',
			'hidro_final',
			'nivel_estatico',
			'nivel_dinamico',
			'ce',
			'ph',
			'anexo_rpta1',
			'anexo_rpta2',
			'anexo_rpta3',
			'anexo_rpta4',
			'anexo_rpta5',
			'anexo_rpta6',
			'anexo_rpta7',
			'anexo_rpta8',
		]

		labels={

			"hora_inicio":"Hora Inicio",
			"hora_final":"Hora Final",
			"hidro_inicial":"Hidrometro Inicial",
			"hidro_final":"Hidrometro Final",
			"nivel_estatico":"Nivel Estatico",
			"nivel_dinamico":"Nivel Dinamico",
			"ce":"Conductividad Electrica",
			"ph":"PH",
			"anexo_rpta1":"Nivel de Aceite en el Deposito",
			"anexo_rpta2":"Dosificador de Aceite(12-15 gotas)",
			"anexo_rpta3":"No existe fugas en el sistema de lubricacion",
			"anexo_rpta4":"No presenta vibracion o temperatura alta en su funcionamiento",
			"anexo_rpta5":"Limpieza del equipo",
			"anexo_rpta6":"No presenta averias imprevistas en el equipo",
			"anexo_rpta7":"FUncionamiento del caudalimetro",
			"anexo_rpta8":"Infraestructura del caseta de riego o pozo",

		}


class estacionmeteorologicaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(estacionmeteorologicaform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fecha_hora'].widget.attrs.update({"placeholder":"Nombre","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['eto_mm'].widget.attrs.update({"placeholder":"Codigo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tem_min'].widget.attrs.update({"placeholder":"Nro Pozo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tem_max'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tem_pro'].widget.attrs.update({"placeholder":"Capacidad Real..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['rad_min'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['rad_max'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['vel_min'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['vel_max'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hr'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['precipitacion'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hmen18'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['h18'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['hmay18'].widget.attrs.update({"placeholder":"Capacidad","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = EstacionMeteorologica
		fields = [
			'anexo_zona',
			'anexo_fundo',
			'fecha_hora',
			'eto_mm',
			'tem_min',
			'tem_max',
			'tem_pro',
			'rad_min',
			'rad_max',
			'vel_min',
			'vel_max',
			'hr',
			'precipitacion',
			'hmen18',
			'h18',
			'hmay18',
			
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"fecha_hora":"Fecha Hora",
			"eto_mm":"ETO(MM)",
			"tem_min":"Temp. Minima",
			"tem_max":"Temp. Maxima",
			"tem_pro":"Temp. Promedio",
			"rad_min":"Radiacion Minima",
			"rad_max":"Radiacion Maxima",
			"vel_min":"Velocidad Minima",
			"vel_max":"Velocidad Maxima",
			"hr":"Humedad Relativa",
			"precipitacion":"Precipitacion",
			"hmen18":"Horas menor a 18 °C",
			"h18":"Horas entre 18 y 20 °C",
			"hmay18":"Horas mayores a 20 °C",
			
		}

#SOLUCIONES MADRES FORM
class solucionesmadresform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(solucionesmadresform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anio'].widget.attrs.update({"placeholder":"Año","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['semana'].widget.attrs.update({"placeholder":"Semana","required":"true","data-error-message":"Data requerida","class":"form-control"})
        
        self.fields['numero_tanque'].widget.attrs.update({"placeholder":"Número de Tanque","required":"true","data-error-message":"Data requerida","class":"form-control"})

    class Meta:
        model = SolucionesMadres
        fields = [
            'anexo_zona',
            'anexo_fundo',
            'anio',
            'semana',
            'numero_tanque',
        ]

        labels={
            "anexo_zona":"Zona",
            "anexo_fundo":"Fundo",
            "anio":"Año",
            "semana":"Semana",
            "numero_tanque":"Número de Tanque",
        }

class detallesolucionesmadresform(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(detallesolucionesmadresform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_fertilizante'].widget.attrs.update({"placeholder":"Fertilizante","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","required":"true","data-error-message":"Data requerida","class":"form-control"})

    class Meta:
        model = DetalleSolucionesMadres
        fields = [
            'anexo_fertilizante',
            'cantidad',
        ]

        labels={
            "anexo_fertilizante":"Fertilizante",
            "cantidad":"Cantidad",
        }
