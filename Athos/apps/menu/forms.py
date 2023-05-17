from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.menu.models import perfiles
from apps.menu.models import rol
from apps.menu.models import sub_item
from apps.menu.models import item
from apps.menu.models import menu_principal
from apps.menu.models import fundo
from apps.menu.models import cultivo
from apps.menu.models import fenologia
from apps.menu.models import campanas
from apps.menu.models import ejezona
from apps.menu.models import variedad
from apps.menu.models import Estado
from apps.menu.models import modulo
from apps.menu.models import lote
from apps.menu.models import ProgramaProduccion

from apps.menu.models import ProgramaProduccionFeno
from apps.menu.models import TurnoProgramaProduccion
from apps.menu.models import Flujo
from apps.menu.models import Acciones
from apps.menu.models import Procesos
from apps.menu.models import solicitud
from apps.menu.models import elementoPEP
from apps.menu.models import VariableAgronomica
from apps.menu.models import VersionAgronomica
from apps.menu.models import PproduccionVariable

from apps.menu.models import Planta
from apps.menu.models import Nave 
from apps.menu.models import PersonalPlanta
from apps.menu.models import Linea
from apps.menu.models import LPaletas
from apps.menu.models import LPaletasReal

from apps.menu.models import Materiales
from apps.menu.models import OrdenPedido
from apps.menu.models import Paletizado

from apps.menu.models import ZonaPaletizado
from apps.menu.models import OrdenPedidoMaterialf



from apps.menu.models import ConfAsistenciaPlanta


from apps.menu.models import IngresoAsistenciaPlanta
from apps.menu.models import SalidaAsistenciaPlanta

from apps.menu.models import AreaCapacitacion
from apps.menu.models import CompetenciaCapacitacion
from apps.menu.models import TemaCapacitacion
from apps.menu.models import CapacitacionCapacitacion
from apps.menu.models import AlcanceCapacitacion

from apps.menu.models import AsistenciaCapacitacion
from apps.menu.models import ConfAsistenciaPlanta

from apps.menu.models import AreaPlanta
from apps.menu.models import Turno
from apps.menu.models import LaborPlanta
from apps.menu.models import ConfigurarDia


from apps.menu.models import estadomaterial
from apps.menu.models import MaterialAcopio
from apps.menu.models import PlacasVehiculares
from apps.menu.models import DetallePlacasVehiculares
from apps.menu.models import ChoferesVehiculos
from apps.menu.models import UnidadMedida
from apps.menu.models import UnidadVehicular
from apps.menu.models import UbicacionFundo
from apps.menu.models import TipoLugarAthos
from apps.menu.models import LugarAthos
from apps.menu.models import UbicacionesAcopio
from apps.menu.models import CentrosAthos
from apps.menu.models import AlmacenesAthos
from apps.menu.models import GuiaAthos
from apps.menu.models import GuiaDetallesAthos
from apps.menu.models import InfoPalet
from apps.menu.models import MaterialMMPP
from apps.menu.models import MaterialTransporte

from apps.menu.models import TipoParihuela
from apps.menu.models import GaritaAthos
from apps.menu.models import RutasAthos
from apps.menu.models import SubVariableAgronomica

from apps.menu.models import HitosFenologicos

class perfilesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(perfilesform, self).__init__(*args, **kwargs)
		self.fields['cod_user'].widget.attrs.update({"placeholder":"Escribe tu codigo usuario","data-required":"true","data-error-message":"Tu codigo de usuario es requerido!","class":"form-control"})
		self.fields['celular'].widget.attrs.update({"placeholder":"Escribe tu N° de Celular","data-required":"true","data-error-message":"Tu N° de Celular es requerido!","class":"form-control"})
		self.fields['estado']=forms.ChoiceField(choices=rol.Eleccion_Estado,initial=0)
		self.fields['estado'].widget.attrs.update({"class":"form-control"})
		

	class Meta:
		model = perfiles
		fields = [
			'cod_user',
			'celular',
			'estado',
		]

		labels={
			"cod_user":"Código Usuario",
			"celular":"Celular",
			"estado":"ESTADO",
		}


class subitemform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(subitemform, self).__init__(*args, **kwargs)
		self.fields['cod_subitem'].widget.attrs.update({"placeholder":"Escribe tu codigo subitem","data-required":"true","data-error-message":"Tu codigo de subi item es requerido!","class":"form-control"})
		self.fields['nom_SubItem'].widget.attrs.update({"placeholder":"Escribe el nombre de subitem","data-required":"true","data-error-message":"Tu nombre de subitem es requerido!","class":"form-control"})
		self.fields['estado']=forms.ChoiceField(choices=rol.Eleccion_Estado,initial=0)
		self.fields['estado'].widget.attrs.update({"class":"form-control"})
	class Meta:
		model = sub_item
		fields = [
			'cod_subitem',
			'nom_SubItem',
			'estado',
		]

		labels={
			"cod_subitem":"CODIGO SUBITEM",
			"nom_SubItem":"NOMBRE SUBITEM",
			"estado":"ESTADO",
		}


class menuform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(menuform, self).__init__(*args, **kwargs)
		self.fields['cod_menu'].widget.attrs.update({"placeholder":"Escribe tu codigo Menu","data-required":"true","data-error-message":"Tu codigo de Menu es requerido!","class":"form-control"})
		self.fields['nom_menu'].widget.attrs.update({"placeholder":"Escribe el nombre de Menu","data-required":"true","data-error-message":"Tu nombre de Menu es requerido!","class":"form-control"})
		self.fields['estado']=forms.ChoiceField(choices=rol.Eleccion_Estado,initial=0)
		self.fields['estado'].widget.attrs.update({"class":"form-control"})

	class Meta:
		model = menu_principal
		fields = [
			'cod_menu',
			'nom_menu',
			'estado',
		]

		labels={
			"cod_menu":"CÓDIGO MENU",
			"nom_menu":"NOMBRE MENU",
			"estado":"ESTADO",
		}


class itemform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(itemform, self).__init__(*args, **kwargs)
		self.fields['cod_item'].widget.attrs.update({"placeholder":"Escribe tu codigo Item","data-required":"true","data-error-message":"Tu codigo de Item es requerido!","class":"form-control"})
		self.fields['nom_item'].widget.attrs.update({"placeholder":"Escribe el nombre de Item","data-required":"true","data-error-message":"Tu nombre de Item es requerido!","class":"form-control"})
		
		self.fields['estado']=forms.ChoiceField(choices=rol.Eleccion_Estado,initial=0)
		self.fields['estado'].widget.attrs.update({"class":"form-control"})
		
		self.fields['id_menu']=forms.ModelChoiceField(queryset=menu_principal.objects.all(),initial=0)
		self.fields['id_menu'].widget.attrs.update({"class":"form-control"})
	class Meta:
		model = item
		fields = [
			'cod_item',
			'nom_item',
			'estado',
			'id_menu',
			
		]

		labels={
			"cod_item":"CÓDIGO ITEM",
			"nom_item":"NOMBRE ITEM",
			"estado":"ESTADO",
			"id_menu":"MENU",
			
		}


class UserAthosForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserAthosForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({"placeholder":"Escribe tu Nombre","data-required":"true","data-error-message":"Tu nombre es requerido!","class":"form-control"})
		self.fields['last_name'].widget.attrs.update({"placeholder":"Escribe tus Apellidos","data-required":"true","data-error-message":"Tus apellidos son requeridos!","class":"form-control"})
		self.fields['username'].widget.attrs.update({"placeholder":"Escribe tu Nombre de Usuario", "data-required":"true", "data-error-message":"Tu Nombre de Usuario es requerido.","class":"form-control"})
		self.fields['password1'].widget.attrs.update({"placeholder":"Escribe tu Contraseña","data-required":"true","data-error-message":"Tu Contraseña es requerida.","class":"form-control"})
		self.fields['password2'].widget.attrs.update({"placeholder":"Escribe tu Contraseña", "data-required":"true", "data-error-message":"Tu Contraseña es requerida.","class":"form-control"})
		self.fields['email'].widget.attrs.update({"placeholder":"Escribe tu Correo Electrónico", "data-required":"true", "data-error-message":"Tu Correo Electrónico es requerido.","class":"form-control"})


	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		]

		labels={
			"username":"NOMBRE DE USUARIO",
			"first_name":"NOMBRES",
			"last_name":"APELLIDOS",
			"email":"CORREO ELECTRONICO",
			"password1":"CONTRASEÑA",
			"password2":"REPITE CONTRASEÑA",
		}


class UserAthosForm2(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserAthosForm2, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({"placeholder":"Escribe tu Nombre","data-required":"true","data-error-message":"Tu nombre es requerido!","class":"form-control"})
		self.fields['last_name'].widget.attrs.update({"placeholder":"Escribe tus Apellidos","data-required":"true","data-error-message":"Tus apellidos son requeridos!","class":"form-control"})
		self.fields['username'].widget.attrs.update({"placeholder":"Escribe tu Nombre de Usuario", "data-required":"true", "data-error-message":"Tu Nombre de Usuario es requerido.","class":"form-control"})
		self.fields['email'].widget.attrs.update({"placeholder":"Escribe tu Correo Electrónico", "data-required":"true", "data-error-message":"Tu Correo Electrónico es requerido.","class":"form-control"})


	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels={
			"username":"NOMBRE DE USUARIO",
			"first_name":"NOMBRES",
			"last_name":"APELLIDOS",
			"email":"CORREO ELECTRONICO",
		}
class Fundoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Fundoform, self).__init__(*args, **kwargs)

		self.fields['abreviatura'].widget.attrs.update({"placeholder":"Abreviatura","data-required":"true","data-error-message":"Escribe la abreviatura", "class":"form-control"})
		self.fields['nom_fundo'].widget.attrs.update({"placeholder":"Nombre del Fundo","data-required":"true","data-error-message":"Escribe el nombre del fundo!","class":"form-control"})
		self.fields['nom_zona'].widget.attrs.update({"placeholder":"zona","data-required":"true","data-error-message":"Escribe la zona","class":"form-control"})
		self.fields['zona'].widget.attrs.update({"placeholder":"eje","data-required":"true","data-error-message":"Escribe el eje","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		self.fields['empresa'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		self.fields['responsable'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
	class Meta:
		model = fundo
		fields = [
			'abreviatura',
			'nom_fundo',
			'nom_zona',
			
			'zona',
			
			'estado',
			'empresa',
			'responsable',

		]

		labels={
			"abreviatura":" ABREVIATURA",
			"nom_fundo":" NOMBRE DEL FUNDO",
			"nom_zona":" ZONA-CODIGO SAP ",
			"zona":" EJE",
			"estado":" ESTADO",
			"empresa":"Empresa",
			"responsable":"Responsable",
		}

class Moduloform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Moduloform, self).__init__(*args, **kwargs)
		self.fields['nombremodulo'].widget.attrs.update({"placeholder":"Nombre del Modulo","data-required":"true","data-error-message":"Escribe el nombre del modulo!","class":"form-control"})
		
		self.fields['idfundo'].widget.attrs.update({"placeholder":"Fundo","data-required":"true","data-error-message":"Escribe el fundo","class":"form-control"})
		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
	class Meta:
		model = modulo
		fields = [
			'nombremodulo',
			'idfundo',
			'estado',


		]

		labels={
			"nombremodulo": " NOMBRE MODULO",
			"idfundo": " FUNDO",
			"estado": " ESTADO",

		}

class Loteform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Loteform, self).__init__(*args, **kwargs)
		self.fields['mod'].widget.attrs.update({"placeholder":"modulo","data-required":"true","data-error-message":"Escribe el modulo","class":"form-control"})
		self.fields['nom_lote'].widget.attrs.update({"placeholder":"Lote","data-required":"true","data-error-message":"Ingresa Lote","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","data-required":"false","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","data-required":"false","data-error-message":"Ingresa Latitud","class":"form-control"})
		self.fields['cod_alterno1'].widget.attrs.update({"placeholder":"Codigo 1","data-required":"false","data-error-message":"Ingresa codigo 1","class":"form-control"})
		self.fields['cod_alterno2'].widget.attrs.update({"placeholder":"Codigo 2","data-required":"false","data-error-message":"Ingresa Codigo 2","class":"form-control"})
		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		

	class Meta:
		model = lote
		fields = [
			'mod',
			'nom_lote',
			'longitud',
			'latitud',
			'cod_alterno1',
			'cod_alterno2',
		
			'estado',
			
		]

		labels={
			"mod":"MODULO",
			"nom_lote":"NOMBRE LOTE",
			"longitud":"LONGITUD",
			"latitud":"LATITUD",
			"cod_alterno1":"COD ALTERNO 1",
			"cod_alterno2":"COD ALTERNO 2",
		
			"estado":"ESTADO",
			

		}



class Cultivoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Cultivoform, self).__init__(*args, **kwargs)
		self.fields['nom_cultivo'].widget.attrs.update({"placeholder":"Nombre del Cultivo","data-required":"true","data-error-message":"Escribe el nombre del Cultivo!","class":"form-control"})
		self.fields['abreviatura_cultivo'].widget.attrs.update({"placeholder":"Abreviatura","data-required":"true","data-error-message":"Ingresa la abreviatura","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
	class Meta:
		model = cultivo
		fields = [
			'nom_cultivo',
			'abreviatura_cultivo',
			'estado',
			
		]

		labels={
			"nom_cultivo":"NOMBRE DE CULTIVO",
			"abreviatura_cultivo":"ABREVIATURA CULTIVO",
			"estado":"ESTADO",
			

		}
class Variedadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Variedadform, self).__init__(*args, **kwargs)
		self.fields['nom_variedad'].widget.attrs.update({"placeholder":"Nombre del Variedad","data-required":"true","data-error-message":"Escribe el nombre del Variedad!","class":"form-control"})
		self.fields['abreviatura_variedad'].widget.attrs.update({"placeholder":"Abreviatura de  Variedad","data-required":"true","data-error-message":"Escribe el nombre del Variedad!","class":"form-control"})
		self.fields['cul'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Escribe  Cultivo!","class":"form-control"})
		self.fields['tipo_fruta'].widget.attrs.update({"placeholder":"Tipo Fruta..","data-required":"true","data-error-message":"Escribe  Cultivo!","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
		
	class Meta:
		model = variedad
		fields = [
			'nom_variedad',
			'abreviatura_variedad',
			'cul',
			'tipo_fruta',
			'estado',
			
		]

		labels={
			"nom_variedad":"NOMBRE VARIEDAD",
			"abreviatura_variedad":"ABREVIATURA VARIEDAD",
			"cul":"CULTIVO",
			'tipo_fruta':"TIPO DE FRUTA(DULCE/ACIDA)",
			"estado":"ESTADO",
			

		}

class Fenologiaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Fenologiaform, self).__init__(*args, **kwargs)
		self.fields['id_cultivo'].widget.attrs.update({"placeholder":"Cultivo", "data-required":"true", "data-error-message":"Tu Cultivo es requerido","class":"form-control"})
		self.fields['indice'].widget.attrs.update({"placeholder":"Indice", "data-required":"true", "data-error-message":"El indice es requerido","class":"form-control"})
		self.fields['nom_feno'].widget.attrs.update({"placeholder":"Escribe la Fenologia", "data-required":"true", "data-error-message":"Tu nombre de fenologia es requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
	class Meta:
		model = fenologia
		fields = [
			'id_cultivo',
			'indice',
			'nom_feno',
			'estado',
			
		]

		labels={
			"id_cultivo": "CULTIVO",
			"indice":"INDICE",
			"nom_feno":"NOMBRE FENOLOGIA",
			"estado":"ESTADO"
			

		}
class Campanaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Campanaform, self).__init__(*args, **kwargs)
		
		self.fields['camp'].widget.attrs.update({"placeholder":"Ingresa la Campaña", "data-required":"true", "data-error-message":"Tu Correo Electrónico es requerido.","class":"form-control"})
		
		
		
		
		
	class Meta:
		model = campanas
		fields = [
			
			'camp',
			
			
		]

		labels={
			
			"camp":"N° CAMPAÑA",
			
			

		}


class Produccionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Produccionform, self).__init__(*args, **kwargs)
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo", "data-required":"true", "data-error-message":"Fundo requerido!", "id":"fundo","name":"fundo" ,"class":"form-control"})
		#self.fields['anexo_modulo'].widget.attrs.update({"placeholder":"Modulo", "data-required":"true", "data-error-message":"modulo requerido!","class":"form-control"})
		#self.fields['anexo_lote'].widget.attrs.update({"placeholder":"Lote", "data-required":"true", "data-error-message":"Lote requerido!","class":"form-control"})
		self.fields['anexo_campana'].widget.attrs.update({"placeholder":"Campaña", "data-required":"true", "data-error-message":"Campaña requerido!","class":"form-control"})
		self.fields['ano_campana'].widget.attrs.update({"placeholder":"Año Campaña", "data-required":"true", "data-error-message":"Año Campaña requerido!","class":"form-control"})
		self.fields['organos_campana'].widget.attrs.update({"placeholder":"Organos por Planta", "data-required":"true", "data-error-message":"Año Campaña requerido!","class":"form-control"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="VARIEDAD",queryset=variedad.objects.all().order_by("cul"),initial=0)
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad", "data-required":"true", "data-error-message":"Variedad requerido!","class":"form-control"})
		self.fields['area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area requerido!","class":"form-control"})
		#self.fields['cierre_campana'].widget.attrs['readonly'] = True
		self.fields['inicio_campana'].widget.attrs.update({"placeholder":"Inicio_campana", "data-required":"true", "data-error-message":"Ingrese Inicio de Campaña","class":"form-control","id":"datepicker1"})
		self.fields['cierre_campana'].widget.attrs.update({"placeholder":"cierre_campana", "data-required":"true", "data-error-message":"Ingrese Cierre de Campaña","class":"form-control","id":"datepicker2"})
		
		self.fields['anio_cosecha'].widget.attrs.update({"placeholder":"Año Cosecha", "data-required":"true", "data-error-message":"Año Cosecha requerido!","class":"form-control"})
		self.fields['var_pep'].widget.attrs.update({"placeholder":"Variedad PEP", "data-required":"true", "data-error-message":"Variedad PEP requerido!","class":"form-control"})
		self.fields['anexo_siembra'].widget.attrs.update({"placeholder":"Siembra", "data-required":"true", "data-error-message":"Anexo Suelo requerido!","class":"form-control"})
		self.fields['responsable'].widget.attrs.update({"placeholder":"Responsable..", "data-required":"true", "data-error-message":"Responsable requerido!","class":"form-control"})
		
		self.fields['inicio_cosecha_clp'].widget.attrs.update({"placeholder":"Fecha..", "data-required":"true", "data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Estado requerido!","class":"form-control"})


	class Meta:
		model = ProgramaProduccion
		fields = [

			'anexo_fundo',
			
			'anexo_campana',
			'ano_campana',
			'organos_campana',
			'anexo_variedad',
			'area',
			'inicio_campana',
			'cierre_campana',
			
			'anio_cosecha',
			'var_pep',
			'anexo_siembra',
			'responsable',
			'inicio_cosecha_clp',

			'estado',	
			
		]

		labels={
			
			"anexo_fundo":"FUNDO",
			"anexo_campana":"N° CAMPAÑA",
			"ano_campana":"AÑO CAMPAÑA",
			"organos_campana":"ORGANOS POR PLANTA",
			"anexo_variedad":"VARIEDAD",	
			"area":"AREA",
			"inicio_campana":"INICIO CAMPAÑA",
			"cierre_campana":"CIERRE CAMPAÑA",
			"anio_cosecha":"AÑO COSECHA",
			"var_pep":"VARIEDAD PEP",
			"anexo_siembra":"SIEMBRA",
			"responsable":"RESPONSABLE",
			"inicio_cosecha_clp":"INICIO COSECHA CLP",
			"estado":"ESTADO",
		}


class ProduccionFenoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")
		super(ProduccionFenoform, self).__init__(*args, **kwargs)
		self.fields['indice'].widget.attrs.update({"placeholder":"Indice", "data-required":"true", "data-error-message":"Indice requerido","class":"form-control"})
		
		self.fields['anexo_fenologia']=forms.ModelChoiceField(label="Fenologias", queryset=variablecultivo.cultivo.all())
		self.fields['anexo_fenologia'].widget.attrs.update({"placeholder":"Fenologias", "data-required":"true", "data-error-message":"fenologiasrequerido!","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha", "data-required":"true", "data-error-message":"fecha requerida!","class":"form-control","id":"datepicker"})
		
		
	class Meta:
		model = ProgramaProduccionFeno
		fields = [

			'indice',
			'anexo_fenologia',
			'fecha',
				
			
		]

		labels={
			
			"indice":"indice",
			"anexo_fenologia":"Fenologias",
			"fecha":"Fecha de Inicio Fenología",
			
		}	

class turnoprogramaproduccionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(turnoprogramaproduccionform, self).__init__(*args, **kwargs)
		self.fields['turno'].widget.attrs.update({"placeholder":"Valvula", "data-required":"true", "data-error-message":"Indice requerido","class":"form-control"})
		self.fields['anexo_suelo'].widget.attrs.update({"placeholder":"Suelo", "data-required":"true", "data-error-message":"Indice requerido","class":"form-control"})
		
		self.fields['hectareaje'].widget.attrs.update({"placeholder":"hectareaje", "data-required":"true", "data-error-message":"fenologiasrequerido!","class":"form-control"})
		self.fields['densidad'].widget.attrs.update({"placeholder":"densidad", "data-required":"true", "data-error-message":"Indice requerido","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"estado", "required":"true", "data-error-message":"fenologiasrequerido!","class":"form-control"})
	
		
	class Meta:
		model = TurnoProgramaProduccion
		fields = [

			'turno',
			'anexo_suelo',
			'hectareaje',
			'densidad',
			'anexo_estado',
			
		]

		labels={
			
			"turno":"Valvula",
			"anexo_suelo":"Suelo",
			"hectareaje":"Hectareaje",
			"densidad":"Densidad",
			"anexo_estado":"Estado",
			
		}	

class Flujoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Flujoform, self).__init__(*args, **kwargs)
		self.fields['nom_flujo'].widget.attrs.update({"placeholder":"Nombre del Flujo","data-required":"true","data-error-message":"Escribe el nombre del Flujo!","class":"form-control"})
		
		
		
		
	class Meta:
		model = Flujo
		fields = [
			'nom_flujo',
			
			
		]

		labels={
			"nom_flujo":"Nombre de flujo",
			

		}

class Accionesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Accionesform, self).__init__(*args, **kwargs)
		self.fields['nom_accion'].widget.attrs.update({"placeholder":"Nombre de la Accion","data-required":"true","data-error-message":"Escribe el nombre de la Accion!","class":"form-control"})
		
		
		
		
	class Meta:
		model = Acciones
		fields = [
			'nom_accion',
			
			
		]

		labels={
			"nom_accion":"Nombre de Accion",
			

		}

class Procesosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Procesosform, self).__init__(*args, **kwargs)
		self.fields['idflujo'].widget.attrs.update({"placeholder":"Flujo","data-required":"true","data-error-message":"Selecciona el Flujo","class":"form-control"})
		self.fields['accion_inicio'].widget.attrs.update({"placeholder":"Accion Inicio","data-required":"true","data-error-message":"Selecciona Accion Inicio","class":"form-control"})
		self.fields['usuario_asignacion'].widget.attrs.update({"placeholder":"Usuario Asignacion","data-required":"true","data-error-message":"Selecciona Usuario Asignacion","class":"form-control"})
		self.fields['respuesta'].widget.attrs.update({"placeholder":"Respuesta","data-required":"true","data-error-message":"Ingrese la Respuesta","class":"form-control"})
		self.fields['accion_siguiente'].widget.attrs.update({"placeholder":"Accion Siguiente","data-required":"true","data-error-message":"Selecciona Accion Siguiente","class":"form-control"})
		self.fields['tiempo_atencion'].widget.attrs.update({"placeholder":"Tiempo Atención","data-required":"true","data-error-message":"Ingrese Tiempo de Atención","class":"form-control"})
		self.fields['url'].widget.attrs.update({"placeholder":"URL","data-required":"true","data-error-message":"Ingrese URL","class":"form-control"})
		
		
		
	class Meta:
		model = Procesos
		fields = [
			'idflujo',
			'accion_inicio',
			'usuario_asignacion',
			'respuesta',
			'accion_siguiente',
			'tiempo_atencion',
			'url',
			
		]



		labels={
			"idflujo":"FLUJO",
			"accion_inicio":"ACCION INICIO",
			"usuario_asignacion":"USUARIO ASIGNACION",
			"respuesta":"RESPUESTA",
			"accion_siguiente":"ACCION SIGUIENTE",
			"tiempo_atencion":"TIEMPO DE ATENCIÓN",
			"url":"URL",

		}


class Solicitudform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Solicitudform, self).__init__(*args, **kwargs)
		self.fields['cod_solicitud'].widget.attrs.update({"placeholder":"Solicitud","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		self.fields['idflujo'].widget.attrs.update({"placeholder":"Flujo","data-required":"true","data-error-message":"Flujo requerido","class":"form-control"})
		self.fields['id_accion'].widget.attrs.update({"placeholder":"Accion","data-required":"true","data-error-message":"Accion Requerida","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion..","data-required":"true","data-error-message":"Ingrese Descripcion","class":"form-control"})
		self.fields['respuesta_solicitud'].widget.attrs.update({"placeholder":"Respuesta","data-required":"true","data-error-message":"Selecciona Respuesta","class":"form-control"})
		
		
		
		
	class Meta:
		model = solicitud
		fields = [
			'cod_solicitud',
			'idflujo',
			'id_accion',
			'descripcion',
			'respuesta_solicitud',
			
		]



		labels={
			"cod_solicitud":"CODIGO SOLICITUD",
			"idflujo":"FLUJO",
			"id_accion":"ACCION",
			"descripcion":"DESCRIPCION",
			"respuesta_solicitud":"RESPUESTA SOLICITUD",
			

		}

class elementoPEPform(forms.ModelForm):
	def __init__(self, *args, **kwargs):

		super(elementoPEPform, self).__init__(*args, **kwargs)
		self.fields['elementopep'].widget.attrs.update({"placeholder":"Elemento PEP","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		
		self.fields['anexo_sanidad'].widget.attrs.update({"placeholder":"Plan Sanidad","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		self.fields['anexo_riego'].widget.attrs.update({"placeholder":"Plan Riego","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		self.fields['anexo_fertilizacion'].widget.attrs.update({"placeholder":"Plan Fertilizacion","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
		self.fields['anexo_obra'].widget.attrs.update({"placeholder":"Plan Mano de Obra","data-required":"true","data-error-message":"Solicitud requerida","class":"form-control"})
				
	class Meta:
		model = elementoPEP
		fields = [
			'elementopep',
			'anexo_estado',

			'anexo_sanidad',
			'anexo_riego',
			'anexo_fertilizacion',
			'anexo_obra',
		]	

		labels={
			"elementopep":"Etapa- PEP",
			"anexo_estado":"Estado"	,

			"anexo_sanidad":"Plan Sanidad",
			"anexo_riego":"Plan Riego",
			"anexo_fertilizacion":"Plan Fertilizacion",
			"anexo_obra":"Plan Mano de Obra",		
		}

class Variableform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Variableform, self).__init__(*args, **kwargs)
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Cultivo requerido","class":"form-control"})
				
		self.fields['Variable'].widget.attrs.update({"placeholder":"Variable Agronómica","data-required":"true","data-error-message":"Variable  requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})
	class Meta:
		model = VariableAgronomica
		fields = [
			'anexo_cultivo',
			
			'Variable',
			'estado'
		]

		labels={
			"anexo_cultivo":"Cultivo",
			
			"Variable":"Variable",
			"estado":"estado",			
		}


class subvariableform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(subvariableform, self).__init__(*args, **kwargs)
		self.fields['anexo_variable'].widget.attrs.update({"placeholder":"Variable","data-required":"true","data-error-message":"Cultivo requerido","class":"form-control"})	
		self.fields['sub_variable'].widget.attrs.update({"placeholder":"Sub Variable Agronómica","data-required":"true","data-error-message":"Sub Variable  requerido","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Descripcion","data-required":"true","data-error-message":"Descripcion  requerido","class":"form-control"})
		
	class Meta:
		model = SubVariableAgronomica
		fields = [
			'anexo_variable',
			'sub_variable',
			'descripcion',

		]

		labels={
			"anexo_variable":"Variable",			
			"sub_variable":"Sub-Variable",
			"descripcion":"Descripcion",			
		}

class VersionAgroform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(VersionAgroform, self).__init__(*args, **kwargs)
		
		self.fields['version'].widget.attrs.update({"placeholder":"Ingresa Version", "data-required":"true", "data-error-message":"Ingresa tu Version","class":"form-control"})
		
	class Meta:
		model = VersionAgronomica
		fields = [
			
			'version',
		]

		labels={
			
			"version":"version",
		}


class ProduccionVariableform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")

		super(ProduccionVariableform, self).__init__(*args, **kwargs)
		

		self.fields['anexo_subvariable']=forms.ModelChoiceField(label="Subvariable",queryset=SubVariableAgronomica.objects.filter(anexo_variable__anexo_cultivo=variablecultivo))
		self.fields['anexo_subvariable'].widget.attrs.update({"placeholder":"Anexo Variable","data-required":"true","data-error-message":"Anexo Variable","class":"form-control"})		
		self.fields['anexo_versiones'].widget.attrs.update({"placeholder":"Anexo Version","data-required":"true","data-error-message":"Version  requerido","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","data-required":"true","data-error-message":"Cantidad requerido","class":"form-control"})

	class Meta:
		model = PproduccionVariable
		fields = [
		
			'anexo_subvariable',
			'anexo_versiones',
	
			'cantidad',
		
		]

		labels={
		
			"anexo_subvariable":"SubVariable",
			"anexo_versiones":"Versiones",
			
			"cantidad":"cantidad",
				
		}

class plantaform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(plantaform, self).__init__(*args, **kwargs)
		self.fields['nom_zona'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['nom_planta'].widget.attrs.update({"placeholder":"Planta ","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})

	class Meta:
		model = Planta
		fields = [
			'nom_zona',
			'nom_planta',
			'estado',
		]

		labels={
			"nom_zona":"Zona",
			"nom_planta":"Planta",
			"estado":"Estado",			
		}

class naveform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(naveform ,self).__init__(*args, **kwargs)
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['nom_nave'].widget.attrs.update({"placeholder":"Planta ","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado ","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})		
		

	class Meta:
		model = Nave
		fields = [
			'anexo_planta',
			'nom_nave',
			'estado',
		]

		labels={
			"anexo_planta":"Planta",
			"nom_nave":"Nave",
			"estado":"Estado",			
		}


class lineaform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lineaform ,self).__init__(*args, **kwargs)
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Nave","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['nom_linea'].widget.attrs.update({"placeholder":"Linea ","data-required":"true","data-error-message":"Linea requerido","class":"form-control"})		
		

	class Meta:
		model = Linea
		fields = [
			'anexo_nave',
			'nom_linea',
			
		]

		labels={
			"anexo_nave":"Nave",
			"nom_linea":"Linea",
						
		}

class personalplantaform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(personalplantaform ,self).__init__(*args, **kwargs)
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})		
		self.fields['linea'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['trab_empa'].widget.attrs.update({"placeholder":"Trabajador empaque ","data-required":"true","data-error-message":"Campo requerido","class":"form-control"})
		self.fields['trab_term'].widget.attrs.update({"placeholder":"Trabajador terminado ","data-required":"true","data-error-message":"Campo requerido","class":"form-control"})
		

	class Meta:
		model = PersonalPlanta
		fields = [
			'anexo_zona',
			'anexo_planta',
			'anexo_nave',
			'linea',
			'trab_empa',
			'trab_term'
			
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_planta":"Planta",
			"anexo_nave":"Nave",
			"linea":"Linea",
			"trab_empa":"Trabajador empacado",
			"trab_term":"Trabajador terminado",
						
		}
class lanzadopaletasform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lanzadopaletasform ,self).__init__(*args, **kwargs)
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"Cultivo requerido","class":"form-control"})
		
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado ","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})		
		
		

	class Meta:
		model = LPaletas
		fields = [
			'anexo_zona',
			'anexo_planta',
			'anexo_nave',
			'anexo_cultivo',
			'anexo_estado',
			
			
			
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_planta":"Planta",
			"anexo_nave":"Nave",
			"anexo_cultivo":"Cultivo",
			"anexo_estado":"Estado",
			
						
		}

class lanzadopaletasrealform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(lanzadopaletasrealform ,self).__init__(*args, **kwargs)
		self.fields['linea'].widget.attrs.update({"maxlength":"100","autocomplete":"off","required":"True","data-required":"true","data-error-message":"Linea requerido","class":"form-control"})
		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Fecha","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control", "id":"datepicker"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})	
		self.fields['leerqr'].widget.attrs.update({"autofocus":"autofocus","placeholder":"QR","required":"True","autocomplete":"off","data-error-message":"QR requerido","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"placeholder":"N° Palet","readonly":"readonly","data-required":"true","data-error-message":"N° de Palet requerido","class":"form-control"})
		self.fields['njavas'].widget.attrs.update({"placeholder":"N° jabas","readonly":"readonly","data-required":"true","data-error-message":"N° de javas requerido","class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Peso","readonly":"readonly","data-required":"true","data-error-message":"Peso requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","readonly":"readonly","data-required":"true","data-error-message":"Estado requerido","class":"form-control"})	
		self.fields['fecha_hora_creacion'].widget.attrs.update({"placeholder":"Fecha Hora Creacion ","readonly":"readonly","data-required":"true","data-error-message":"Estado requerido","class":"form-control","id":"datepickercreacion"})	

	class Meta:
		model = LPaletasReal
		fields = [
			'linea',
			'fecha_lanzado',
			'anexo_turno',
			'leerqr',
			'npalet',
			'njavas',
			'peso',
			'estado',
			'fecha_hora_creacion',
			
			
		]

		labels={
			"linea":"QR Linea",
			"fecha_lanzado":"Fecha Lanzado",
			"anexo_turno":"Turno",
			"leerqr":"Codigo Qr",
			"npalet":"N° de Palet",
			"njavas":"N° de Javas",
			"peso":"Peso",
			"estado":"estado",
			"fecha_hora_creacion":"Fecha Creacion"
						
		}

class materialesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialesform, self).__init__(*args, **kwargs)
		self.fields['codigo'].widget.attrs.update({"placeholder":"codigo", "data-required":"true", "data-error-message":"Tu Codigo es requerido","class":"form-control"})
		self.fields['descripcion'].widget.attrs.update({"placeholder":"descripcion", "data-required":"true", "data-error-message":"descripcion es requerido","class":"form-control"})
		self.fields['codigosap'].widget.attrs.update({"placeholder":"Escribe tu codigo sap", "data-required":"true", "data-error-message":"Tu codigo sap es requerido","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
	class Meta:
		model = Materiales
		fields = [
			'codigo',
			'descripcion',
			'codigosap',
			'estado',
			
		]

		labels={
			"codigo": "Codigo",
			"descripcion":"Descripcion",
			"codigosap":"Codigo Sap",
			"estado":"Estado"
			
		}

class ordenpedidoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ordenpedidoform, self).__init__(*args, **kwargs)
		self.fields['npedido'].widget.attrs.update({"placeholder":"N° Pedido", "data-required":"true", "data-error-message":"Tu N° de Pedido es requerido","class":"form-control"})
		self.fields['ordenfabricacion'].widget.attrs.update({"placeholder":"Orden de Fabricación", "data-required":"true", "data-error-message":"Orden de Fabricación requerida!","class":"form-control"})
		
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
	class Meta:
		model = OrdenPedido
		fields = [
			'npedido',
			'ordenfabricacion',
			
			'estado',
			
		]

		labels={
			"npedido": "N° pedido",
			"ordenfabricacion":"Orden de Fabricacion",
			
			"estado":"Estado",
			
		}

class ordenpedidomaterialfform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ordenpedidomaterialfform, self).__init__(*args, **kwargs)
		
		self.fields['cod_material'].widget.attrs.update({"placeholder":"Codigo Material SAP", "data-required":"true", "data-error-message":"Codigo SAP requerido","class":"form-control"})
		self.fields['cod_material'].choices = [(m.id, m.codigosap) for m in Materiales.objects.all()]
		self.fields['anexo_descripcion'].widget.attrs.update({"placeholder":"Descripcion", "data-required":"true", "data-error-message":"Tu Descripcion es requerida","class":"form-control"})
		self.fields['anexo_descripcion'].choices = [(m.id, m.descripcion) for m in Materiales.objects.all()]
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","data-required":"true","data-error-message":"Ingrese Cantidad","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
	class Meta:
		model = OrdenPedidoMaterialf
		fields = [
			
			'cod_material',
			'anexo_descripcion',
			'cantidad',
			'estado',
			
		]

		labels={
			
			"cod_material":"Codigo Material",
			"anexo_descripcion":"Anexo Descripcion",
			"cantidad":"Cantidad",
			"estado":"Estado",
			
		}



class zonapaletizadoform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(zonapaletizadoform ,self).__init__(*args, **kwargs)
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona ","id":"zona","data-required":"true","data-error-message":"Zona requerido","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Planta requerido","class":"form-control"})
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Nave ","data-required":"true","data-error-message":"Nave requerido","class":"form-control"})		
		
		

	class Meta:
		model = ZonaPaletizado
		fields = [
			'anexo_zona',
			'anexo_planta',
			'anexo_nave',
			
			
			
		]

		labels={
			"anexo_zona":"Zona",
			"anexo_planta":"Planta",
			"anexo_nave":"Nave",
			
						
		}



class paletizadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(paletizadoform, self).__init__(*args, **kwargs)
		
		self.fields['npalet'].widget.attrs.update({"placeholder":"N° Palet", "data-required":"true", "data-error-message":"Tu N° de Palet requerido","class":"form-control"})
		self.fields['anexo_ordenpe'].widget.attrs.update({"placeholder":"Orden Pedido", "data-required":"true", "data-error-message":"Tu Orden Pedido es requerido","class":"form-control"})
		self.fields['anexo_codigo'].widget.attrs.update({"placeholder":"Anexo Codigo", "data-required":"true", "data-error-message":"Anexo Codigo requerida!","class":"form-control"})
		self.fields['anexo_descripcion'].widget.attrs.update({"placeholder":"Anexo Descripcion", "data-required":"true", "data-error-message":"Anexo Descripcion requerida!","class":"form-control"})
		self.fields['anexo_qr'].widget.attrs.update({"placeholder":"Anexo QR", "data-required":"true", "data-error-message":"Anexo QR requerido!","class":"form-control"})
		self.fields['trazabilidad'].widget.attrs.update({"placeholder":"Trazabilidad", "data-required":"true", "data-error-message":"Trazabilidad requerido!","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad", "data-required":"true", "data-error-message":"Cantidad requerida!","class":"form-control"})
		self.fields['calibre'].widget.attrs.update({"placeholder":"Calibre", "data-required":"true", "data-error-message":"Calibre requerida!","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
	class Meta:
		model = Paletizado
		fields = [
				
			'npalet',
			'anexo_ordenpe',
			'anexo_codigo',
			'anexo_descripcion',
			'anexo_qr',
			'trazabilidad',
			'cantidad',
			'calibre',
			'estado',
			
		]

		labels={
			
			"npalet": "N° Palet",
			"anexo_ordenpe":"Orden Pedido",
			"anexo_codigo":"Anexo Codigo",
			"anexo_descripcion":"Descripcion",
			"trazabilidad":"Trazabilidad",
			"cantidad":"Cantidad",
			"calibre":"Calibre",
			"estado":"Estado",
			
		}







class configurarasistenciaplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(configurarasistenciaplantaform, self).__init__(*args, **kwargs)
		self.fields['anexo_configuracion']=forms.ModelChoiceField(label="Configuracion",queryset=ConfigurarDia.objects.all().order_by("-fecha"))
		self.fields['anexo_configuracion'].widget.attrs.update({"placeholder":"CONFIGURACION", "data-required":"true", "data-error-message":"INGRESO Requerida","class":"form-control"})
		self.fields['anexo_areaplanta'].widget.attrs.update({"placeholder":"AREA PLANTA", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		
	class Meta:
		model = ConfAsistenciaPlanta
		fields = [
				
			
			'anexo_configuracion',
			'anexo_areaplanta',	
		]

		labels={
			
			"anexo_configuracion":"Configuracion",
			"anexo_areaplanta":"AreaPlanta",			
		}

class ingresoplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ingresoplantaform, self).__init__(*args, **kwargs)
		
		self.fields['dni'].widget.attrs.update({"autofocus":"autofocus","maxlength":"8","autocomplete":"off","required":"True","placeholder":"Codigo", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		
	class Meta:
		model = IngresoAsistenciaPlanta
		fields = [
				
			
			
			'dni',	
		]

		labels={
			
			
			"dni":"CODIGO SAP",			
		}

class salidaplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(salidaplantaform, self).__init__(*args, **kwargs)
		
		self.fields['dni'].widget.attrs.update({"autofocus":"autofocus","maxlength":"8","autocomplete":"off","required":"True","placeholder":"Codigo", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		
	class Meta:
		model = SalidaAsistenciaPlanta
		fields = [
				
			
			
			'dni',	
		]

		labels={
			
			
			"dni":"CODIGO SAP",			
		}


class areaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(areaform, self).__init__(*args, **kwargs)
		self.fields['nom_area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area Requerida","class":"form-control"})
				

	class Meta:
		model = AreaCapacitacion
		fields = [
				
			
			'nom_area',
		
			
		]

		labels={
			
			
			"nom_area":"Area",
						
		}



class alcancecapacitacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(alcancecapacitacionform, self).__init__(*args, **kwargs)
		self.fields['nom_alcance'].widget.attrs.update({"placeholder":"Alcance", "data-required":"true", "data-error-message":"Area Requerida","class":"form-control"})
				

	class Meta:
		model = AlcanceCapacitacion
		fields = [
				
			
			'nom_alcance',
		
			
		]

		labels={
			
			
			"nom_alcance":"Alcance",
						
		}
class competenciaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(competenciaform, self).__init__(*args, **kwargs)
		self.fields['anexo_area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area Requerida","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		self.fields['nom_capacitacion'].widget.attrs.update({"placeholder":"Capacitacion", "data-required":"true", "data-error-message":"Competencia Requerida","class":"form-control"})
	class Meta:
		model = CompetenciaCapacitacion
		fields = [
				
			
			'anexo_area',
			'codigo',
			'nom_capacitacion',
		
			
		]

		labels={
			
			
			"anexo_area":"Area",
			"codigo":"Codigo",
			"nom_capacitacion":"Competencia",
						
		}

class temaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(temaform, self).__init__(*args, **kwargs)
		self.fields['anexo_competencia'].widget.attrs.update({"placeholder":"Competencia", "data-required":"true", "data-error-message":"Competencia Requerida","class":"form-control"})
		self.fields['codigo'].widget.attrs.update({"placeholder":"Codigo", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		self.fields['nom_tema'].widget.attrs.update({"placeholder":"Tema", "data-required":"true", "data-error-message":"Tema Requerida","class":"form-control"})
		
	class Meta:
		model = TemaCapacitacion
		fields = [
				
			
			'anexo_competencia',
			'codigo',
			'nom_tema',
			
			
		]

		labels={
			
			"anexo_competencia":"Competencia",
			"codigo":"Codigo",
			"nom_tema":"Tema",
						
		}

class capacitacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(capacitacionform, self).__init__(*args, **kwargs)
		self.fields['codigoacta'].widget.attrs.update({"placeholder":"Codigo Acta", "data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})
		self.fields['anexo_datos'].widget.attrs.update({"placeholder":"Datos", "data-required":"true", "data-error-message":"Datos Requerida","class":"form-control"})		
		self.fields['anexo_area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area Requerida","class":"form-control"})
		self.fields['anexo_competencia'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Competencia Requerida","class":"form-control"})
	

		self.fields['anexo_tema'].widget.attrs.update({"multiple":"multiple","type":"CheckBox","placeholder":"Tema", "data-required":"true", "data-error-message":"Tema Requerida","class":"form-control"})
		


		self.fields['fecha_hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Inicio", "data-required":"true", "data-error-message":"Inicio Requerida","class":"form-control","id":"datepicker"})
		self.fields['fecha_hora_fin'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Fin", "data-required":"true", "data-error-message":"Fin Requerida","class":"form-control","id":"datepicker1"})
		self.fields['lugar'].widget.attrs.update({"placeholder":"Lugar", "data-required":"true", "data-error-message":"Lugar Requerida","class":"form-control"})
		self.fields['lugar_especifico'].widget.attrs.update({"placeholder":"Lugar Especifico", "data-required":"true", "data-error-message":"Lugar Requerida","class":"form-control"})
		self.fields['dniexpositor'].widget.attrs.update({"placeholder":"Dni Expositor..", "data-required":"true", "data-error-message":"Lugar Requerida","class":"form-control"})
		self.fields['empresaexpositor'].widget.attrs.update({"placeholder":"Empresa..", "data-required":"true", "data-error-message":"Lugar Requerida","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad", "data-required":"true", "data-error-message":"Cantidad Requerida","class":"form-control"})
		self.fields['tipo_participante'].widget.attrs.update({"placeholder":"Tipo de Participante", "data-required":"true", "data-error-message":"Tipo participante Requerida","class":"form-control"})
		self.fields['tipo_capacitacion'].widget.attrs.update({"placeholder":"Tipo de Capacitacion", "data-required":"true", "data-error-message":"Capacitacion Requerida","class":"form-control"})
		self.fields['expositor'].widget.attrs.update({"placeholder":"Expositor", "data-required":"true", "data-error-message":" Expositor Requerida","class":"form-control"})
		self.fields['puestoexpositor'].widget.attrs.update({"placeholder":"Puesto Expositor", "data-required":"true", "data-error-message":" Expositor Requerida","class":"form-control"})
		
		self.fields['imagen_capacitacion'].widget.attrs.update({"capture":"camera","placeholder":"Imagen Capacitacion", "data-required":"true", "data-error-message":"Imagen Requerida","class":"form-control"})
		self.fields['imagen_acta'].widget.attrs.update({"capture":"camera","placeholder":"Imagen Acta", "data-required":"true", "data-error-message":"Imagen Requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Imagen Requerida","class":"form-control"})
		self.fields['idtema'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Imagen Requerida","class":"form-control"})
		

	class Meta:
		model = CapacitacionCapacitacion
		fields = [
				
			
			'codigoacta',
			'anexo_datos',
			'anexo_area',
			'anexo_competencia',
			'anexo_tema',
			
			"fecha_hora_inicio",
			'fecha_hora_fin',
			'lugar',
			'lugar_especifico',
			'cantidad',
			'tipo_participante',
			'tipo_capacitacion',
			'expositor',
			'dniexpositor',
			'empresaexpositor',
			'puestoexpositor',
			'imagen_capacitacion',
			'imagen_acta',
			'anexo_estado',
			'idtema',
		]

		labels={
			
			"codigoacta":"Codigo Acta",
			"anexo_datos":"Razon Social",
			"anexo_area":"Area",
			"anexo_competencia":"Competencia",
			"anexo_tema":"Tema",
		
			"fecha_hora_inicio":"Fecha Inicio",
			"fecha_hora_fin":"Fecha Fin",
			"lugar":"Eje",
			"lugar_especifico":"Lugar",
			"cantidad":"Cantidad de Horas",
			"tipo_participante":"Tipo Participante",
			"tipo_capacitacion":"Tipo de Capacitacion",	
			"expositor":"Expositor",
			"dniexpositor":"DNI Expositor",
			"empresaexpositor":"Empresa del Expositor",
			"puestoexpositor":"Puesto del Expositor",
			"imagen_capacitacion":"Imagen Capacitacion",
			"imagen_acta":"Autenticacion Expositor",
			"anexo_estado":"Estado",
			"idtema":"",				
		}



class asistenciacapacitacionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(asistenciacapacitacionform, self).__init__(*args, **kwargs)
		
		self.fields['dni'].widget.attrs.update({"placeholder":"Ingrese DNI...", "required":"True","maxlength":"8","autofocus":"autofocus","data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Ingrese DNI...", "data-required":"True","maxlength":"8","autofocus":"autofocus","data-required":"true", "data-error-message":"Codigo Requerida","class":"form-control"})		
		
	class Meta:
		model = AsistenciaCapacitacion
		fields = [
				
			
			
			'dni',	
			'anexo_estado',
		]

		labels={
			
			
			"dni":"DNI",	
			"anexo_estado":"Estado",		
		}

class turnoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(turnoform, self).__init__(*args, **kwargs)
		
		self.fields['nom_turno'].widget.attrs.update({"placeholder":"Turno", "data-required":"true", "data-error-message":"Turno Requerida","class":"form-control"})		
		
	class Meta:
		model = Turno
		fields = [
				
			
			
			'nom_turno',	
		]

		labels={
			
		
			"nom_turno":"Turno",			
		}

class arealaborform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(arealaborform, self).__init__(*args, **kwargs)
		
		self.fields['area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area Requerida","class":"form-control"})
		self.fields['anexo_labor'].widget.attrs.update({"placeholder":"Labor", "data-required":"true", "data-error-message":"Labor Requerida","class":"form-control"})		
		
	class Meta:
		model = AreaPlanta
		fields = [
				
			
			
			'area',	
			'anexo_labor',
		]

		labels={
			
		
			"area":"Area",	
			'anexo_labor':"Labor",
		}

class laborform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(laborform, self).__init__(*args, **kwargs)
		
		
		self.fields['labor'].widget.attrs.update({"placeholder":"Labor", "data-required":"true", "data-error-message":"Labor Requerida","class":"form-control"})		
		
	class Meta:
		model = LaborPlanta
		fields = [
				
			
	
			'labor',
		]

		labels={

			'labor':"Labor",
		}
class configurarfechaform(forms.ModelForm):
		def __init__(self, *args, **kwargs):
			super(configurarfechaform, self).__init__(*args, **kwargs)
			self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha", "data-required":"true", "data-error-message":"Linea Requerida","class":"form-control", "id":"datepicker"})
			self.fields['Turno'].widget.attrs.update({"placeholder":"Turno", "data-required":"true", "data-error-message":"Linea Requerida","class":"form-control"})
			self.fields['fecha_hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Inicio", "data-required":"true", "data-error-message":"Linea Requerida","id":"some_class_1","class":"form-control" })
			self.fields['fecha_hora_fin'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Fin", "data-required":"true", "data-error-message":"Cantidad requerida!","id":"some_class_2","class":"form-control"})
			self.fields['anexo_ubicacion'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Cantidad requerida!","class":"form-control"})
		

		class Meta:
			model = ConfigurarDia
			fields = [
					
				'fecha',
				'Turno',
				'fecha_hora_inicio',
				'fecha_hora_fin',
				'anexo_ubicacion',
				
			]

			labels={
				
				"fecha":"Fecha",
				"Turno":"Turno",
				"fecha_hora_inicio":"Inicio",
				"fecha_hora_fin":"Fin",
				"anexo_ubicacion":"Ubicacion",
			}

class estadomaterialform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(estadomaterialform, self).__init__(*args, **kwargs)
		
		self.fields['estado_material'].widget.attrs.update({"placeholder":"Estado Material", "data-required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		
	class Meta:
		model = estadomaterial
		fields = [
			
			'estado_material',
		]

		labels={
			
			"estado_material":"Estado Material",
		}



class unidadmedidaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(unidadmedidaform, self).__init__(*args, **kwargs)
		
		self.fields['unidad_medida'].widget.attrs.update({"placeholder":"Unidad Medida", "data-required":"true", "data-error-message":"Ingrese Unidad de Medida","class":"form-control"})
		
	class Meta:
		model = UnidadMedida
		fields = [
			
			'unidad_medida',
		]

		labels={
			
			"unidad_medida":"Unidad de Medida",
		}



class tipoparihuelaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tipoparihuelaform, self).__init__(*args, **kwargs)
		
		
		self.fields['nom_parihuela'].widget.attrs.update({"placeholder":" Desc. Parihuela", "data-required":"true", "data-error-message":"Ingrese Desc. Parihuela","class":"form-control"})
		self.fields['peso_parihuela'].widget.attrs.update({"placeholder":"Peso Parihuela", "data-required":"true", "data-error-message":"Ingrese Peso Parihuela","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Peso Material", "data-required":"true", "data-error-message":"Ingrese peso  Material","class":"form-control"})


	class Meta:
		model = TipoParihuela
		fields = [
			
			'nom_parihuela',
			'peso_parihuela',
			'anexo_estado',
			
	
		]

		labels={
			
			"nom_parihuela":"Desc. Parihuela",
			"peso_parihuela":"Peso Parihuela",
			"anexo_estado":"Estado",
			
		}


class materialacopioform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialacopioform, self).__init__(*args, **kwargs)
		
		
		self.fields['anexo_matmmpp'].widget.attrs.update({"placeholder":" Estado Material", "data-required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		self.fields['anexo_mattransporte'].widget.attrs.update({"placeholder":"Unidad  Material", "data-required":"true", "data-error-message":"Ingrese Unidad Material","class":"form-control"})
		self.fields['pesommpp_estimado'].widget.attrs.update({"placeholder":"Peso Material", "data-required":"true", "data-error-message":"Ingrese Peso","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":" Cultivo", "data-required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})		
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Peso Material", "data-required":"true", "data-error-message":"Ingrese peso  Material","class":"form-control"})


	class Meta:
		model = MaterialAcopio
		fields = [
			
			'anexo_matmmpp',
			'anexo_mattransporte',
			'anexo_cultivo',
			'anexo_estado',
			'pesommpp_estimado',
			
	
		]

		labels={
			
			"anexo_matmmpp":"Materia Prima",
			"anexo_mattransporte":"Materia Transporte",
			"anexo_cultivo":"Cultivo",
			"anexo_estado":"Estado",
			"pesommpp_estimado":"Peso Estimado Material",
			
			
		}



class materialmmppform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialmmppform, self).__init__(*args, **kwargs)
		
		self.fields['codigo_sap'].widget.attrs.update({"placeholder":" Codigo SAP", "data-required":"true", "data-error-message":"Ingrese CODIGO SAP","class":"form-control"})
		self.fields['desc_material'].widget.attrs.update({"placeholder":"Descripcion Material", "data-required":"true", "data-error-message":"Ingrese Descripcion Material","class":"form-control"})
		self.fields['desc_sap'].widget.attrs.update({"placeholder":"Descripcion SAP", "data-required":"true", "data-error-message":"Ingrese Descripcion Material","class":"form-control"})
		self.fields['var_pep'].widget.attrs.update({"placeholder":"VAR PEP", "data-required":"true", "data-error-message":"Ingrese Descripcion Material","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":" Estado Material", "required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":" Cultivo", "required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		self.fields['tipo_fruto'].widget.attrs.update({"placeholder":" Cultivo", "data-required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		
		self.fields['anexo_unidad'].widget.attrs.update({"placeholder":"Unidad  Material", "data-required":"true", "data-error-message":"Ingrese Unidad Material","class":"form-control"})
		


	class Meta:
		model = MaterialMMPP
		fields = [
			'codigo_sap',
			'desc_material',
			'desc_sap',
			'var_pep',
			'anexo_estado',
			'anexo_cultivo',
			'anexo_unidad',
			'tipo_fruto',
		]

		labels={
			"codigo_sap":"Codigo SAP",
			"desc_material":"Descripcion Material",
			"desc_sap":"Descripcion SAP",
			"var_pep":"VAR PEP",
			"anexo_estado":"Estado",
			"anexo_cultivo":"Cultivo",
			"anexo_unidad":"Unidad",
			"tipo_fruto":"Tipo fruto(DULCE/ACIDA)",
		}

class materialtransporteform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialtransporteform, self).__init__(*args, **kwargs)
		self.fields['codigo_sap'].widget.attrs.update({"placeholder":" Codigo SAP", "data-required":"true", "data-error-message":"Ingrese CODIGO SAP","class":"form-control"})		
		self.fields['desc_material'].widget.attrs.update({"placeholder":"Descripcion Material", "data-required":"true", "data-error-message":"Ingrese Descripcion Material","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":" Estado Material", "data-required":"true", "data-error-message":"Ingrese Estado Material","class":"form-control"})
		self.fields['anexo_unidad'].widget.attrs.update({"placeholder":"Unidad  Material", "data-required":"true", "data-error-message":"Ingrese Unidad Material","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo", "required":"true", "data-error-message":"Ingrese Unidad Material","class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Peso Material", "data-required":"true", "data-error-message":"Ingrese peso  Material","class":"form-control"})


	class Meta:
		model = MaterialTransporte
		fields = [
			'codigo_sap',
			'desc_material',
			'anexo_estado',
			'anexo_unidad',
			'anexo_cultivo',
			'peso',
		]

		labels={
			
			"codigo_sap":"Codigo SAP",
			"desc_material":"Descripcion Material",
			"anexo_estado":"Estado",
			"anexo_unidad":"Unidad",
			"anexo_cultivo":"Cultivo",
			"peso":"Peso",
		}


#maestra vehiculos 
class placasvehicularesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(placasvehicularesform, self).__init__(*args, **kwargs)
		
		self.fields['placas'].widget.attrs.update({"placeholder":"Placas Vehiculares", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})
		self.fields['placas2'].widget.attrs.update({"placeholder":"Placas Vehiculares 2", "data-required":"true", "data-error-message":"Ingrese Placas volquete","class":"form-control"})
		self.fields['anexo_tipovehiculo'].widget.attrs.update({"placeholder":"Tipo Vehiculo", "data-required":"true", "data-error-message":"Ingrese Vehiculo","class":"form-control"})
		self.fields['n_soat'].widget.attrs.update({"placeholder":"SOAT", "data-required":"true", "data-error-message":"Ingrese SOAT","class":"form-control"})
		self.fields['vencimiento_soat'].widget.attrs.update({"autocomplete":"off","placeholder":"Vencimiento Soat", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})
		self.fields['vencimiento_rtecnica'].widget.attrs.update({"autocomplete":"off","placeholder":"Vencimiento Rev.", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})

		self.fields['anexo_tipounidad'].widget.attrs.update({"placeholder":"Tipo Unidad", "data-required":"true", "data-error-message":"Ingrese Tipo Unidad","class":"form-control"})

		self.fields['capacidad_jabas'].widget.attrs.update({"placeholder":"Capacidad...", "data-required":"true", "data-error-message":"Ingrese Capacidad","class":"form-control"})
		self.fields['razon_social'].widget.attrs.update({"placeholder":"Empresa-Razon Social", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Estado", "required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado", "required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})

	class Meta:
		model = PlacasVehiculares
		fields = [
			
			'placas',
			'placas2',
			'anexo_tipovehiculo',
			'n_soat',
			'vencimiento_soat',
			'vencimiento_rtecnica',
			'anexo_tipounidad',
			'capacidad_jabas',
			'anexo_tipotransporte',
			'razon_social',
			'anexo_zona',
			'anexo_estado'
		]

		labels={
			
			"placas":"Placa del Vehiculo",
			"placas2":"Segunda Placa",
			"anexo_tipovehiculo":"Tipo Vehiculo",
			"n_soat":"N° Soat",
			"vencimiento_soat":"Vencimiento SOAT",
			"vencimiento_rtecnica":"Venc. Revisión Técnica",
			"anexo_tipounidad":"Unidad",
			"capacidad_jabas":"Capacidad",
			"anexo_tipotransporte":"Tipo de Transporte",
			"razon_social":"Razon Social-Empresa",
			"anexo_zona":"Zona",
			"anexo_estado":"Estado",
		}

class detalleplacasvehicularesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleplacasvehicularesform, self).__init__(*args, **kwargs)
		
		self.fields['rutas'].widget.attrs.update({"placeholder":"Placas Vehiculares", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})
		self.fields['tarifa'].widget.attrs.update({"placeholder":"Placas Vehiculares 2", "data-required":"true", "data-error-message":"Ingrese Placas volquete","class":"form-control"})
		
	class Meta:
		model = DetallePlacasVehiculares
		fields = [
			
			'rutas',
			'tarifa',
			
		]

		labels={
			
			"rutas":"Rutas",
			"tarifa":"Tarifas",
			
		}

class choferesvehiculosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(choferesvehiculosform, self).__init__(*args, **kwargs)
		
		self.fields['ApellidoPat'].widget.attrs.update({"placeholder":"Apellido Paterno", "data-required":"true", "data-error-message":"Ingrese Apellido Paterno","class":"form-control"})
		self.fields['ApellidoMat'].widget.attrs.update({"placeholder":"Apellido Materno", "data-required":"true", "data-error-message":"Ingrese Apellido Materno","class":"form-control"})
		self.fields['Nombres'].widget.attrs.update({"placeholder":"Nombres", "data-required":"true", "data-error-message":"Ingrese Nombres","class":"form-control"})
		self.fields['Dni'].widget.attrs.update({"placeholder":"DNI", "data-required":"true", "data-error-message":"Ingrese DNI","class":"form-control"})
		self.fields['Brevete'].widget.attrs.update({"placeholder":"Brevete", "data-required":"true", "data-error-message":"Ingrese Brevete","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado..", "data-required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})


	class Meta:
		model = ChoferesVehiculos
		fields = [
			
			'ApellidoPat',
			'ApellidoMat',
			'Nombres',
			'Dni',
			'Brevete',
			'anexo_zona',
			'anexo_estado',
		]

		labels={
			
			"ApellidoPat":"Apellido Paterno",
			"ApellidoMat":"Apellido Materno",
			"Dni":"DNI",
			"Brevete":"Brevete",
			"anexo_zona":"Eje",
			"anexo_estado":"Estado",
		}

class unidadvehicularform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(unidadvehicularform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_placas'].widget.attrs.update({"placeholder":"Placas", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Chofer","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})
		



	class Meta:
		model = UnidadVehicular
		fields = [
			
			'anexo_placas',
			'anexo_chofer',
			'anexo_zona',
			'anexo_estado',
		]

		labels={
			
			"anexo_placas":"Placas",
			"anexo_chofer":"Chofer",
			"anexo_zona":"Zona",
			"anexo_estado":"Estado",
		}

class ubicacionfundoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ubicacionfundoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"Fundo", "data-required":"true", "data-error-message":"Ingrese Fundo","class":"form-control"})
		


	class Meta:
		model = UbicacionFundo
		fields = [
			
			'anexo_pep',
			
		
		]

		labels={
			
			"anexo_pep":"PEP",
			
		}

class tipolugarathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(tipolugarathosform, self).__init__(*args, **kwargs)
		
		self.fields['tipo'].widget.attrs.update({"placeholder":"Tipo", "data-required":"true", "data-error-message":"Ingrese Placas","class":"form-control"})
		



	class Meta:
		model = TipoLugarAthos
		fields = [
			
			'tipo',
			
		]

		labels={
			
			"tipo":"Tipo",
		}


class lugarathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(lugarathosform, self).__init__(*args, **kwargs)
		
		self.fields['Lugar'].widget.attrs.update({"placeholder":"Lugar", "data-required":"true", "data-error-message":"Ingrese Lugar","class":"form-control"})
		self.fields['anexo_tipolugar'].widget.attrs.update({"placeholder":"Tipo Lugar", "data-required":"true", "data-error-message":"Ingrese Tipo Lugar","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})



	class Meta:
		model = LugarAthos
		fields = [
			
	
			'Lugar',
			'anexo_tipolugar',
			'anexo_zona',
			'anexo_estado',
			'longitud',
			'latitud',

		
		]

		labels={
			
			
			"Lugar":"Lugar",
			"anexo_tipolugar":"Tipo Lugar",
			"anexo_zona":"Zona",
			"anexo_estado":"Estado",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class ubicacioneacopioform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ubicacionesacopioform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"Lugar", "data-required":"true", "data-error-message":"Ingrese Lugar","class":"form-control"})
		

	class Meta:
		model = UbicacionesAcopio
		fields = [
			

			'anexo_zona',
			'anexo_lugar',
		
		]

		labels={

			"anexo_zona":"Zona",
			"anexo_lugar":"Lugar",
			
			
		}

class centrosathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(centrosathosform, self).__init__(*args, **kwargs)

		self.fields['centro'].widget.attrs.update({"placeholder":"Centros", "data-required":"true", "data-error-message":"Ingrese Centros","class":"form-control"})	
		self.fields['desc_centro'].widget.attrs.update({"placeholder":"Descripcion Centros", "data-required":"true", "data-error-message":"Ingrese Descr. Centros","class":"form-control"})		
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		
		

	class Meta:
		model = CentrosAthos
		fields = [
			

			'centro',
			'desc_centro',
			'anexo_zona',
		
		]

		labels={

			"centro":"Centro",
			"desc_centro":"Descripcion Centro",
			"anexo_zona":"Zona",
	
		}


class almacenesathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(almacenesathosform, self).__init__(*args, **kwargs)

		self.fields['almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['desc_almacen'].widget.attrs.update({"placeholder":"Descripcion Almacen", "data-required":"true", "data-error-message":"Ingrese Desc- Almacen","class":"form-control"})	
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centros", "required":"true", "data-error-message":"Ingrese Centros","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado..", "required":"true", "data-error-message":"Ingrese Estado","class":"form-control"})
		
		

	class Meta:
		model = AlmacenesAthos
		fields = [
			

			'almacen',
			'desc_almacen',
			'anexo_centro',
			'anexo_zona',
			'anexo_estado',
		
		]

		labels={

			"almacen":"Almacen",
			"desc_almacen":"Descripcion Almacen",
			"anexo_centro":"Centro",
			"anexo_zona":"Zona",
			"anexo_estado":"Estado",
		}

class guiaathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiaathosform, self).__init__(*args, **kwargs)

		self.fields['codigoqr'].widget.attrs.update({"placeholder":"Codigo QR", "data-required":"true", "data-error-message":"Ingrese Codigo","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		
		
		self.fields['anexo_chofer'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})

		self.fields['anexo_vehiculo']=forms.ModelChoiceField(queryset=PlacasVehiculares.objects.filter(anexo_tipotransporte=1))
		self.fields['anexo_vehiculo'].widget.attrs.update({"placeholder":"Vehiculo", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})		
		
		self.fields['ubic_partida'].widget.attrs.update({"placeholder":"Partida", "data-required":"true", "data-error-message":"Ingrese Partida","class":"form-control"})
		self.fields['ubic_llegada'].widget.attrs.update({"placeholder":"Llegada", "data-required":"true", "data-error-message":"Ingrese Llegada","class":"form-control"})
		self.fields['anexo_sociedad'].widget.attrs.update({"placeholder":"Sociedad", "data-required":"true", "data-error-message":"Ingrese Sociedad","class":"form-control"})		
		self.fields['NroGuia'].widget.attrs.update({"placeholder":"Nro Guia", "data-required":"true", "data-error-message":"Ingrese NroGuia","class":"form-control"})
		self.fields['fecha_transporte'].widget.attrs.update({"placeholder":"Fecha Transporte", "data-required":"true", "data-error-message":"Ingrese fecha cosecha","class":"form-control","id":"datepicker"})
		self.fields['longitud'].widget.attrs['readonly'] = True
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs['readonly'] = True
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})


	class Meta:
		model = GuiaAthos
		fields = [
			
			'codigoqr',
			'anexo_zona',
			'anexo_almacen',
			
			'anexo_chofer',
			'anexo_vehiculo',
			
			'ubic_partida',
			'ubic_llegada',
			'anexo_sociedad',
			'NroGuia',
			'fecha_transporte',
			'longitud',
			'latitud',

		
		]

		labels={

			"codigoqr":"Codigo QR",
			"anexo_zona":"Zona",
			"anexo_almacen":"Almacen",
			"anexo_chofer":"Chofer",
			"anexo_vehiculo":"Placa",
	
			"ubic_partida":"Ubicación Partida",
			"ubic_llegada":"Ubicación llegada",
			"anexo_sociedad":"Sociedad",
			"NroGuia":"Nro Guia",
			"fecha_transporte":"Fecha Transporte",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}


class guiadetallesathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(guiadetallesathosform, self).__init__(*args, **kwargs)

		self.fields['anexo_ubi_mmpp'].widget.attrs.update({"placeholder":"Ubicacion MMPP", "data-error-message":"Ingrese Ubicacion","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['peso_jabas'].widget.attrs.update({"placeholder":"Peso Campo", "data-required":"true", "data-error-message":"Ingrese Centro","class":"form-control"})
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material", "data-required":"true", "data-error-message":"Ingrese Transporte","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha", "data-required":"true", "data-error-message":"Ingrese fecha","class":"form-control","id":"datepicker"})			
		self.fields['anexo_calidad'].widget.attrs.update({"placeholder":"Calidad Material", "data-required":"true", "data-error-message":"Ingrese Calidad","class":"form-control"})		
	class Meta:
		model = GuiaDetallesAthos
		fields = [
			

			'anexo_ubi_mmpp',
			'cant_jabas',
			'peso_jabas',
			'anexo_material',
			'fecha_cosecha',
			'anexo_calidad',
		
		]

		labels={

			"anexo_ubi_mmpp":"PEP",
			"cant_jabas":"Cantidad de Jabas",
			"peso_jabas":"Peso Campo",
			"anexo_material":"Material Compuesto",
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_calidad":"Calidad",
		}

class infopaletform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(infopaletform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_tipoparihuela'].widget.attrs.update({"placeholder":"Tipo Parihuela", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['anexo_almacen'].widget.attrs.update({"placeholder":"Tipo Almacen", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})		
		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cantidad de Jabas", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['pesobr_palet'].widget.attrs.update({"placeholder":"Peso Bruto", "data-required":"true", "data-error-message":"Ingrese Peso Bruto","class":"form-control"})
		self.fields['anexo_envase2']=forms.ModelChoiceField(label="Segundo Material-Jaba",queryset=MaterialTransporte.objects.filter(anexo_cultivo=2))
		self.fields['anexo_envase2'].widget.attrs.update({"placeholder":"", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})
		self.fields['cant_jabas2'].widget.attrs.update({"placeholder":"", "data-required":"true", "data-error-message":"Ingrese Almacen","class":"form-control"})

		self.fields['pesova_jabas'].widget.attrs.update({"readonly":"true","placeholder":"Peso Jabas", "data-required":"true", "data-error-message":"Ingrese Peso Jabas","class":"form-control"})
		
		self.fields['pesonet_palet'].widget.attrs.update({"placeholder":"Peso Neto", "data-required":"true", "data-error-message":"Ingrese Peso Neto","class":"form-control"})
		
		
	class Meta:
		model = InfoPalet
		fields = [
			
			'anexo_tipoparihuela',
			'anexo_almacen',	
			'cant_jabas',
			'pesobr_palet',
			'pesova_jabas',
			'pesonet_palet',
			'anexo_envase2',
			'cant_jabas2',	
		]


		labels={

			"anexo_tipoparihuela":"Parihuela -Peso",
			"anexo_almacen":"Almacen",
			"cant_jabas":"Cantidad de Jabas",
			"pesobr_palet":"Peso Bruto Palet",
			"pesova_jabas":"Peso Jabas Vacias",
			"pesonet_palet":"Peso Neto Palet",
			"cant_jabas2":"Cantidad de 2do Material Envase(Jabas)",
			"anexo_envase2":"Segundo Material-Jaba",
		}



class rutasathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(rutasathosform, self).__init__(*args, **kwargs)
		
		self.fields['rutas'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['precio'].widget.attrs.update({"placeholder":"QR Placa", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"QR Campo Guia", "data-required":"true", "data-error-message":"Ingrese Qr Campo","class":"form-control"})
		
	class Meta:
		model = RutasAthos
		fields = [
		
			'rutas',
			'precio',
			'anexo_lugar',
			
		
		]

		labels={

			"rutas":"Rutas",
			"precio":"Precio",
			"anexo_lugar":"Lugar Athos",
			
		}


class garitaathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(garitaathosform, self).__init__(*args, **kwargs)
		self.fields['zona'].widget.attrs.update({"placeholder":"Zona", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['ruta'].widget.attrs.update({"placeholder":"Ubicacion", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['qrplaca'].widget.attrs.update({"placeholder":"QR Placa", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['qrcampo'].widget.attrs.update({"placeholder":"QR Campo Guia", "data-required":"true", "data-error-message":"Ingrese Qr Campo","class":"form-control"})
		self.fields['chofer_ref'].widget.attrs.update({"placeholder":"Chofer", "data-required":"true", "data-error-message":"Ingrese Chofer Referencial","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud", "data-required":"true", "data-error-message":"Ingrese Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud", "data-required":"true", "data-error-message":"Ingrese Latitud","class":"form-control"})
		self.fields['kilometraje'].widget.attrs.update({"placeholder":"Kilometraje", "data-required":"true", "data-error-message":"Ingrese Kilometraje","class":"form-control"})
		self.fields['cantpasajeros'].widget.attrs.update({"placeholder":"Cant. Pasajeros", "data-required":"true", "data-error-message":"Ingrese Cantidad Pasajeros","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Observacion..", "data-required":"true", "data-error-message":"Ingrese Observacion","class":"form-control"})
	
	class Meta:
		model = GaritaAthos
		fields = [
			'zona',
			'ubicacion',
			'ruta',
			'qrplaca',
			'qrcampo',
			'chofer_ref',
			'longitud',
			'latitud',
			'kilometraje',
			'cantpasajeros',
			'observacion',
		
		]

		labels={
			"zona":"Zona",
			"ubicacion":"Fundo",
			"ruta":"Rutas",
			"qrplaca":"QR Placas",
			"qrcampo":" QR Guia",
			"chofer_ref":"Chofer Referencial",
			"longitud":"Longitud",
			"latitud":"Latitud",
			"kilometraje":"Kilometraje",
			"cantpasajeros":"Cantidad de Pasajeros",
			"observacion":"Observaciones",
		}


class hitosfenologicosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablecultivo=kwargs.pop("anexo_cultivo")
		super(hitosfenologicosform, self).__init__(*args, **kwargs)
		self.fields['semana'].widget.attrs.update({"placeholder":"Semana..", "data-required":"true", "data-error-message":"Ingrese Zona","class":"form-control"})
		self.fields['anexo_grupo'].widget.attrs.update({"placeholder":"Numero Hito..", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['anexo_subgrupo'].widget.attrs.update({"placeholder":"Numero SubHito", "data-required":"true", "data-error-message":"Ingrese Ubicacion","class":"form-control"})
		self.fields['anexo_hito'].widget.attrs.update({"placeholder":"Descripcion Hito..", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['anexo_subhito'].widget.attrs.update({"placeholder":"Descripcion Hito..", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['anexo_area'].widget.attrs.update({"placeholder":"..", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"..", "data-required":"true", "data-error-message":"Ingrese Qr Placa","class":"form-control"})
	
		
		self.fields['valor'].widget.attrs.update({"placeholder":"Valor..", "data-required":"true", "data-error-message":"Ingrese Chofer Referencial","class":"form-control"})
		self.fields['valor_max'].widget.attrs.update({"placeholder":"Valor..", "data-required":"true", "data-error-message":"Ingrese Chofer Referencial","class":"form-control"})
		
	class Meta:
		model = HitosFenologicos
		fields = [
			'semana',
			'anexo_grupo',
			'anexo_subgrupo',
			'anexo_hito',
			'anexo_subhito',
			'anexo_area',
			'anexo_tipo',
			'valor',
			'valor_max',
			
		
		]

		labels={
			"semana":"Semana Cultivo",
			"anexo_grupo":"Grupo",
			"anexo_subgrupo":"SubGrupo",
			"anexo_hito":"Grupo Variable",
			"anexo_subhito":"Variable",
			"anexo_area":"Area",
			"anexo_tipo":"Tipo",
			"valor":"Valor Min",
			"valor_max":"Valor Max",
		}
