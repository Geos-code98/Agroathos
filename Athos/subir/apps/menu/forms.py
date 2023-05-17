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
from apps.menu.models import Flujo
from apps.menu.models import Acciones
from apps.menu.models import Procesos
from apps.menu.models import solicitud
from apps.menu.models import elementoPEP

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
		
		
	class Meta:
		model = fundo
		fields = [
			'abreviatura',
			'nom_fundo',
			'nom_zona',
			
			'zona',
			
			'estado',

		]

		labels={
			"abreviatura":" ABREVIATURA",
			"nom_fundo":" NOMBRE DEL FUNDO",
			"nom_zona":" NOMBRE DE LA ZONA ",
			"zona":" EJE",
			"estado":" ESTADO",

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
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Ingresa tu estado","class":"form-control"})
		
		
		
		
	class Meta:
		model = variedad
		fields = [
			'nom_variedad',
			'abreviatura_variedad',
			'cul',
			'estado',
			
		]

		labels={
			"nom_variedad":"NOMBRE VARIEDAD",
			"abreviatura_variedad":"ABREVIATURA VARIEDAD",
			"cul":"CULTIVO",
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
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad", "data-required":"true", "data-error-message":"Variedad requerido!","class":"form-control"})
		self.fields['area'].widget.attrs.update({"placeholder":"Area", "data-required":"true", "data-error-message":"Area requerido!","class":"form-control"})
		self.fields['cierre_campana'].widget.attrs.update({"placeholder":"cierre_campana", "data-required":"true", "data-error-message":"Ingrese Cierre de Campaña","class":"form-control"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Estado requerido!","class":"form-control"})

	class Meta:
		model = ProgramaProduccion
		fields = [

			'anexo_fundo',
			
			'anexo_campana',
			'ano_campana',
			'anexo_variedad',
			'area',
			'cierre_campana',
			'estado',	
			
		]

		labels={
			
			"anexo_fundo":"FUNDO",
			
			"anexo_campana":"N° CAMPAÑA",
			"ano_campana":"AÑO CAMPAÑA",
			"anexo_variedad":"VARIEDAD",			
			"area":"AREA",
			"cierre_campana":"CIERRE CAMPAÑA",
			"estado":"ESTADO",
		}


class ProduccionFenoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ProduccionFenoform, self).__init__(*args, **kwargs)
		self.fields['anexo_fenologia'].widget.attrs.update({"placeholder":"Fenologias", "data-required":"true", "data-error-message":"fenologiasrequerido!"})
		self.fields['fecha'].widget.attrs.update({"placeholder":"Fecha", "data-required":"true", "data-error-message":"fecha requerida!"})
		self.fields['estado'].widget.attrs.update({"placeholder":"Estado", "data-required":"true", "data-error-message":"Estado requerido!"})
		
	class Meta:
		model = ProgramaProduccionFeno
		fields = [

			'anexo_fenologia',
			'fecha',
			'estado',	
			
		]

		labels={
			
			
			"anexo_fenologia":"Fenologias",
			"Fecha":"Fecha",
			"estado":"Estado",
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
		self.fields['elementopep'].widget.attrs.update({"placeholder":"Elemento PEP","data-required":"true","data-error-message":"Solicitud requerida"})
				
	class Meta:
		model = elementoPEP
		fields = [
			'elementopep',
		]

		labels={
			"elementopep":"Elemento PEP",			
		}
