from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.planificacion.models import MaestraRegion
from apps.planificacion.models import MaestraClientes
from apps.planificacion.models import CategoriaCultivo
from apps.planificacion.models import MarcaPT
from apps.planificacion.models import MaterialPT
from apps.planificacion.models import PlanVentas
from apps.planificacion.models import DetallePlanVentas

from apps.planificacion.models import OrdenProceso
from apps.planificacion.models import ProgramaProduccionPlanta
from apps.planificacion.models import PlanVentas2021



class maestraregionform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(maestraregionform, self).__init__(*args, **kwargs)
		
		
		self.fields['desc'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = MaestraRegion
		fields = [
			'desc',
			
		]

		labels={
			"desc":"Region",
			
		}


class maestraclientesform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(maestraclientesform, self).__init__(*args, **kwargs)
		
		
		self.fields['cliente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['anexo_region'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = MaestraClientes
		fields = [
			'cliente',
			'anexo_region',
			


		]

		labels={
			"cliente":"Cliente",
			"anexo_region":"Region",
		}



class categoriacultivoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(categoriacultivoform, self).__init__(*args, **kwargs)
		
		
		self.fields['desc'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = CategoriaCultivo
		fields = [
			'desc',
			'anexo_cultivo',
			


		]

		labels={
			"desc":"Categoria",
			"anexo_cultivo":"Cultivo",
		}

class marcaptform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(marcaptform, self).__init__(*args, **kwargs)
		
		
		self.fields['desc'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = MarcaPT
		fields = [
			'desc',
			'anexo_cultivo',
			


		]

		labels={
			"desc":"Marca",
			"anexo_cultivo":"Cultivo",
		}


class materialptform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialptform, self).__init__(*args, **kwargs)
		
		
		
		self.fields['cod_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['desc_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['grupo_art'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_categoria'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cod_sap'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_unidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['anexo_marca'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_envase'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['peso_neto'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['calibre'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = MaterialPT
		fields = [
			
			'cod_material',
			'desc_material',
			'grupo_art',
			'anexo_cultivo',
			'anexo_categoria',
			'anexo_unidad',
			'cod_sap',
		

			'anexo_marca',
			'anexo_envase',
			'peso_neto',
			'calibre',

		]

		labels={
		
			"cod_material":"Codigo Material",
			"desc_material":"Descripcion Material",
			"grupo_art":"Grupo Articulo",
			"anexo_cultivo":"Cultivo",
			"anexo_categoria":"Categoria",
			"anexo_unidad":"Unidad Material",
			"cod_sap":"Codigo SAP Material",
		
			
			"anexo_marca":"Marca",
			"anexo_envase":"Envase",
			"peso_neto":"Peso Neto",
			"calibre":"Calibre",


		}


class planventasform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(planventasform, self).__init__(*args, **kwargs)
		
		
		self.fields['fecha_despacho'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['fecha_produccion'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['num_pedido'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['anexo_cliente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_transporte'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		
		
		self.fields['num_semana'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = PlanVentas
		fields = [
			'fecha_despacho',
			'fecha_produccion',
			'num_pedido',
			'anexo_cultivo',
			
			'anexo_cliente',
			'anexo_estado',
			'anexo_transporte',

			'num_semana',
		]

		labels={
			"fecha_despacho":"Fecha Despacho",
			"fecha_produccion":"Fecha Produccion",
			"num_pedido":"Numero Pedido",
			"anexo_cultivo":"Cultivo",
			
			"anexo_cliente":"Cliente",
			"anexo_estado":"Estado",
			"anexo_transporte":"Transporte",
			
			
			"num_semana":"Numero Semana",
		}


class detalleplanventasform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleplanventasform, self).__init__(*args, **kwargs)
		
		
		
		self.fields['pos_pedido'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['desc_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['un_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['peso_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		self.fields['cant_cajas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['kpg'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_categoria'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_calibre'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cajas_palet'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cant_palet'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = DetallePlanVentas
		fields = [
			
			'pos_pedido',
			
			'anexo_material',
			'desc_material',
			'un_material',
			'peso_material',

			'cant_cajas',
			'kpg',
			'anexo_categoria',
			'anexo_calibre',
			'anexo_variedad',
			'cajas_palet',
			'cant_palet',
			
		]

		labels={
		
			"pos_pedido":"Numero Pedido Ventas",
			
			
			"anexo_material":"Material",
			"desc_material":"Desc. Material",
			"un_material":"Unidad Material",
			"peso_material":"Peso Material",

			"cant_cajas":"Cant. Cajas",
			"kpg":"KPG",
			"anexo_categoria":"Categoria",
			"anexo_calibre":"Calibre",
			"anexo_variedad":"Variedad",
			"cajas_palet":"Cajas x Palet",
			"cant_palet":"Cant. Palet",
		}


class ordenprocesoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ordenprocesoform, self).__init__(*args, **kwargs)
		
		self.fields['nro_orden'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
		
		self.fields['desc_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
	
		self.fields['cant_cajas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['kpg'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['consumo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = OrdenProceso
		fields = [
			
			'nro_orden',
		
			
			'desc_material',
			
	

			'cant_cajas',
			'kpg',
			'consumo',
			
		]

		labels={
		
			"nro_orden":"Numero Orden",
			
		

			"desc_material":"Desc. Material",
		

			"cant_cajas":"Cant. Cajas",
			"kpg":"KPG",
			"consumo":"Consumo Cajas",
		}



class programaproduccionplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(programaproduccionplantaform, self).__init__(*args, **kwargs)
		self.fields['anexo_orden'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['pos_orden'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['desc_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})	
		self.fields['cant_cajas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['kpg'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['consumo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['fecha_programada'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		
	class Meta:
		model = ProgramaProduccionPlanta
		fields = [
			'anexo_orden',
			'pos_orden',
			'desc_material',
			'cant_cajas',
			'kpg',
			'consumo',
			'fecha_programada',
			
		]

		labels={
			"anexo_orden":"Orden",
			"pos_orden":"Posicion Orden",
			"desc_material":"Desc. Material",
			"cant_cajas":"Cant. Cajas",
			"kpg":"KPG",
			"consumo":"Consumo Cajas",
			"fecha_programada":"Fecha Programada",
		}




class planventas2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(planventas2021form, self).__init__(*args, **kwargs)
		
		
		self.fields['anio_campana'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['anio'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['trimestre'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['mes'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['semana'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['fecha_inicio'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['codigo_cliente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['nombre_cliente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cod_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['desc_material'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['um'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['kgt'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['tipo_despacho'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['destino'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['pais'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['region'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		self.fields['continente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Temp requerido!!","class":"form-control"})
		

	class Meta:
		model = PlanVentas2021
		fields = [
			'anio_campana',
			'cultivo',
			'anio',
			'trimestre',
			'mes',
			'semana',
			'fecha_inicio',
			'codigo_cliente',
			'nombre_cliente',
			'cod_material',
			'desc_material',
			'um',
			'cantidad',
			'kgt',
			'tipo_despacho',
			'destino',
			'pais',
			'region',
			'continente',
			
			
		]

		labels={
			"anio_campana":"Año Campaña",
			"cultivo":"Cultivo",
			"anio":"Año",
			"trimestre":"Trimestre",
			"mes":"Mes",
			"semana":"Semana",
			"fecha_inicio":"Fecha Inicio",
			"codigo_cliente":"Codigo Cliente",
			"nombre_cliente":"Nombre Cliente",
			"cod_material":"Codigo Material",
			"desc_material":"Desc. Material",
			"um":"Unidad de Medida",
			"cantidad":"Cantidad",
			"kgt":"KGT",
			"tipo_despacho":"Tipo Despacho",
			"destino":"Destino",
			"pais":"Pais",
			"region":"Region",
			"continente":"Continente",
			
			
		}
