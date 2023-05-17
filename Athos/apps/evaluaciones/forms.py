from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.menu.models import ProgramaProduccion
from apps.evaluaciones.models import EvFenBrotesArandanos
from apps.evaluaciones.models import DetallePlantaEvFenBrotesArandanos
from apps.evaluaciones.models import BrotePlantaEvFenBrotesArandanos

from apps.evaluaciones.models import EvFenBrotesArandanosSem
from apps.evaluaciones.models import DetallePlantaEvFenBrotesArandanosSem
from apps.evaluaciones.models import BrotePlantaEvFenBrotesArandanosSem

from apps.evaluaciones.models import EvFenRaicesArandanos
from apps.evaluaciones.models import DetalleEvFenRaicesArandanos
from apps.evaluaciones.models import RaicesEvFenRaicesArandanos

from apps.evaluaciones.models import ControlProductoTerminado
from apps.evaluaciones.models import DetalleControlProductoTerminado

from apps.evaluaciones.models import EvSanPlagasArandanos
from apps.evaluaciones.models import GruposPlagasArandanos
from apps.evaluaciones.models import SubGruposPlagasArandanos
from apps.evaluaciones.models import VariablesPlagasArandanos

from apps.evaluaciones.models import EvFenFrutoArandanos
from apps.evaluaciones.models import DetalleEvFenFrutoArandanos

from apps.evaluaciones.models import EvFenPlanasa
from apps.evaluaciones.models import DetalleEvFenPlanasa

from apps.evaluaciones.models import EvCalDefectosCampo
from apps.evaluaciones.models import DetalleEvCalDefectosCampo
from apps.menu.models import variedad
from apps.menu.models import fundo
from apps.menu.models import TurnoProgramaProduccion
from apps.maestras.models import AuxiliaresCampoAthos

from apps.evaluaciones.models import EvCalAcopioPlantaArCaraz2021
from apps.evaluaciones.models import EvCalAcopioPlantaArCaraz202202
from apps.evaluaciones.models import EvCalAcopioPlantaArIca2021
from apps.evaluaciones.models import EvCalAcopioPlantaArIca202202
from apps.evaluaciones.models import EvCartillaDrenado

from apps.evaluaciones.models import DetalleEvCartillaDrenado

from apps.evaluaciones.models import SelTrabajadorEvCalPodaAr
from apps.evaluaciones.models import EvCalPodaAr
from apps.evaluaciones.models import DetalleEvCalPodaAr

from apps.evaluaciones.models import EvCalMuestreoCosechaHg2021
from apps.evaluaciones.models import DetalleEvCalMuestreoCosechaHg2021

from apps.evaluaciones.models import EvCalMuestreoPlantaHgIca2021
from apps.evaluaciones.models import DetalleEvCalMuestreoPlantaHgIca2021

from apps.evaluaciones.models import EvCalBrixGrIca2021
from apps.evaluaciones.models import DetalleEvCalBrixGrIca2021

from apps.evaluaciones.models import EvCalMmppGrIca2021
from apps.evaluaciones.models import DetalleEvCalMmppGrIca2021

from apps.evaluaciones.models import EvCalControlDescarteGrIca2022
from apps.evaluaciones.models import DetalleEvCalControlDescarteGrIca2022

from apps.evaluaciones.models import MaterialesCalidad

from apps.evaluaciones.models import EvCalControlPesosGrIca2022
from apps.evaluaciones.models import DetalleEvCalControlPesosGrIca2022

from apps.maestras.models import ClientesAthos
from apps.maestras.models import CalibresAthos

from apps.evaluaciones.models import EvPlantonesPlNaz2022
from apps.evaluaciones.models import DetalleEvPlantonesPlNaz2022

#CARTILLA EV MUESTRA CAJAS EMPACADAS GR2022
from apps.evaluaciones.models import EvMuestrasCajasEmpacadasGR2022
from apps.evaluaciones.models import DetalleEvMuestrasCajasEmpacadasGR2022

#CONTROL DESCARTE GR 2022
from apps.evaluaciones.models import EvControlDescarteGR2022
from apps.menu.models import MaterialMMPP

#EV RAMAS ARANDANOS
from apps.evaluaciones.models import EvFenRamasArandanos
from apps.evaluaciones.models import DetallePlantaEvFenRamasArandanos
from apps.evaluaciones.models import RamaPlantaEvFenRamasArandanos

#EV CALIDAD DESCARTE AR 2022
from apps.evaluaciones.models import EvCalControlDescarteAr2022
from apps.evaluaciones.models import DetalleEvCalControlDescarteAr2022
from apps.maestras.models import MaestraFundoCultivo

#EV CONTROL DESCARTE AR 2022
from apps.evaluaciones.models import EvControlDescarteAr2022
from apps.evaluaciones.models import DetalleEvControlDescarteAr2022
from apps.evaluaciones.models import EvControlDescarteAr202202
from apps.evaluaciones.models import DetalleEvControlDescarteAr202202

#EV CAMARAS HUMEDAS
from apps.evaluaciones.models import EvCamarasHumedas
from apps.evaluaciones.models import DetallePlantaEvCamarasHumedas
from apps.sanidad.models import ProductosAutorizados

#EV CALIDAD MUESTREO PLANTA HG ICA 2022
from apps.evaluaciones.models import EvCalMuestreoPlantaHgIca2022
#EV CALIDAD MUESTREO PLANTA HG NEP 2022
from apps.evaluaciones.models import EvCalMuestreoPlantaHgNep202202

#EV CALIDAD CONTROL DESCARTE HG 2022
from apps.evaluaciones.models import EvCalControlDescarteHg2022
from apps.evaluaciones.models import DetalleEvCalControlDescarteHg2022

#EV CALIDAD PRODUCTO TERMINADO HG 2022
from apps.evaluaciones.models import ControlProductoTerminadoHg
from apps.evaluaciones.models import DetalleControlProductoTerminadoHg

#EV EFICIENCIA SELECCION Y CALIBRADO 2022
from apps.evaluaciones.models import EvEficienciaSeleccionCalibrado

#EV PRODUCTO TERMINADO DESPACHO 2022
from apps.evaluaciones.models import EvProductoTerminadoDespacho
from apps.evaluaciones.models import DetalleEvProductoTerminadoDespacho

class evfenbrotesarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenbrotesarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['valvula'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EvFenBrotesArandanos
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			
			'valvula',
			'anexo_tipo',
			
			
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Fun-Mod-Lot",
			
			"valvula":"Valvula",
			"anexo_tipo":"Tipo Evaluacion",
			
		}

class evfenbrotedetalleplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenbrotedetalleplantaform, self).__init__(*args, **kwargs)
		
		self.fields['n_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['ancho'].widget.attrs.update({"placeholder":"Ancho","data-required":"true","data-error-message":"Ancho requerida","class":"form-control"})
		self.fields['largo'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Largo requerida","class":"form-control"})
		self.fields['cant_ramas'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
				
		
	class Meta:
		model = DetallePlantaEvFenBrotesArandanos
		fields = [
			
			'n_planta',
			'ancho',
			'largo',
			'cant_ramas',
			
			
		]

		labels={
			
			"n_planta":"N° Planta",
			"ancho":"Ancho",
			"largo":"Largo",
			"cant_ramas":"Cantidad de Ramas",
			
		}


class broteplantaevfenform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(broteplantaevfenform, self).__init__(*args, **kwargs)
		self.fields['anexo_diametro'].widget.attrs.update({"placeholder":"Diametro","required":"true","data-error-message":"Diametro requerida","class":"form-control"})
		self.fields['diametro'].widget.attrs.update({"placeholder":"Diametro","data-required":"true","data-error-message":"Diametro requerida","class":"form-control"})
		self.fields['anexo_brote'].widget.attrs.update({"placeholder":"Diametro","required":"true","data-error-message":"Diametro requerida","class":"form-control"})
		self.fields['anexo_yema'].widget.attrs.update({"placeholder":"Yemas","required":"true","data-error-message":"Yemas requerida","class":"form-control"})
		
		self.fields['altura'].widget.attrs.update({"placeholder":"Altura","data-required":"true","data-error-message":"Altura requerida","class":"form-control"})
		self.fields['diametrobrote'].widget.attrs.update({"placeholder":"diametrobrote","data-required":"true","data-error-message":"Diametro brote requerida","class":"form-control"})
		self.fields['nudos'].widget.attrs.update({"placeholder":"Nudo","data-required":"true","data-error-message":"Nudo requerida","class":"form-control"})
		self.fields['hojas'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['A1'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['L1'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['A2'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['L2'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['A3'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['L3'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['axilas'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		
		
		self.fields['yhinchada'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['yescamosa'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['ycargador'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})

		self.fields['botonfloral'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['botonrosado'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['flor'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['cuajado'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde1'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde2'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde3'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde4'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		
		
		self.fields['verderojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoverde'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoazul'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['azulrojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})		
		self.fields['maduro'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","readonly":"true","required":"false","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","readonly":"true","required":"false","data-error-message":"Ingresa Latitud","class":"form-control"})



	class Meta:
		model = BrotePlantaEvFenBrotesArandanos
		fields = [
			'anexo_diametro',
			'diametro',
			'anexo_brote',
			'anexo_yema',
			'altura',
			'diametrobrote',
			'nudos',
			'hojas',
			'A1',
			'L1',
			'A2',
			'L2',
			'A3',
			'L3',
			'axilas',
		
			
			'yhinchada',
			'yescamosa',
			'ycargador',
			'botonfloral',
			'botonrosado',
			'flor',
			'cuajado',
			'verde1',
			'verde2',
			'verde3',
			'verde4',
			
	
			'verderojo',
			'rojoverde',
			'rojoazul',
			'azulrojo',
			'maduro',

			'longitud',
			'latitud',
		]

		labels={
			"anexo_diametro": "N° Cuadrante",
			"diametro":"Diametro de Rama",
			"anexo_brote":"Brote",
			"anexo_yema":"Origen del Brote",
			"altura":"Altura",
			"diametrobrote":"Diametro Brote",
			"nudos":"Nudo",
			"hojas":"Hojas",
			"A1":"A1",
			"L1":"L1",
			"A2":"A2",
			"L2":"L2",
			"A3":"A3",
			"L3":"L3",
			"axilas":"# Axila Activa",
		
			
			"yhinchada":"#Yema Hinchada",
			"yescamosa":"#Yema Escamosa",
			"ycargador":"#Yema Cargador",
			'botonrosado':"#Boton Rosado",
			"flor":"#Flor",
			"cuajado":"#Numero Cuaja",
			"verde1":"#Verde 1 ",
			"verde2":"#Verde 2",
			"verde3":"#Verde 3",
			"verde4":"#Verde 4",		
			"verderojo":"#Verde Rojo",
			"rojoverde":"#Rojo Verde",
			"rojoazul":"#Rojo Azul",
			"azulrojo":"#Azul Rojo",
			"maduro":"#Maduro",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}



class evfenraicesarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenraicesarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['valvula'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Observacion","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EvFenRaicesArandanos
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
		
			'valvula',
			'observacion',
			
			
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Fun-Mod-Lot",
			"valvula":"Valvula",
			"observacion":"Observacion",
			
		}



class detalleevfenraicesarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevfenraicesarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['num_planta'].widget.attrs.update({"placeholder":"N° Planta","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['ancho'].widget.attrs.update({"placeholder":"Ancho","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['largo'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['alto'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['altura_molde'].widget.attrs.update({"placeholder":"Altura","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		

		
	class Meta:
		model = DetalleEvFenRaicesArandanos
		fields = [
			
			'num_planta',
			
			'ancho',
			'largo',
			'alto',
			'altura_molde',
	
			
		]

		labels={
#			
			"num_planta":"N° Planta",
			
			"ancho":"Ancho",
			"largo":"Largo",
			"alto":"Alto",
			"altura_molde":"Altura Molde",
			
			
		}


class raicesevfenraicesarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(raicesevfenraicesarandanosform, self).__init__(*args, **kwargs)
		self.fields['anexo_cuadrante'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['sr'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['re'].widget.attrs.update({"placeholder":"RE","data-required":"true","data-error-message":"Ancho requerida","class":"form-control"})
		self.fields['rfs'].widget.attrs.update({"placeholder":"RFS","data-required":"true","data-error-message":"Largo requerida","class":"form-control"})
		self.fields['rfj'].widget.attrs.update({"placeholder":"RFJ","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rfjb'].widget.attrs.update({"placeholder":"RFJB","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","readonly":"true","required":"true","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","readonly":"true","required":"true","data-error-message":"Ingresa Latitud","class":"form-control"})

	class Meta:
		model = RaicesEvFenRaicesArandanos
		fields = [
			'anexo_cuadrante',
			'anexo_zona',
			'sr',
			're',
			'rfs',
			'rfj',
			'rfjb',
			
			'longitud',
			'latitud',	
			
		]

		labels={
			"anexo_cuadrante":"#Cuadrante",
			"anexo_zona":"Zona",
			"sr":"SR",
			"re":"RE",
			"rfs":"RFS",
			"rfj":"RFJ",
			"rfjb":"RFJB",
			
			"longitud":"Longitud",
			"latitud":"Latitud",	
		}


class controlproductoterminadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(controlproductoterminadoform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_turno'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_centro'].widget.attrs.update({"autocomplete":"off","placeholder":"Centro","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"FECHA","required":"true","data-error-message":"N° Planta requerida","class":"form-control","id":"datepickercreacion1"})
		self.fields['anexo_linea'].widget.attrs.update({"autocomplete":"off","placeholder":"Linea","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_pagina'].widget.attrs.update({"autocomplete":"off","placeholder":"Pagina","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"autocomplete":"off","placeholder":"Obs..","required":"false","data-error-message":"Obs requerida","class":"form-control"})
		self.fields['fecha_hora_creacion'].widget.attrs.update({"autocomplete":"off","placeholder":"FECHA","required":"true","data-error-message":"N° Planta requerida","class":"form-control","id":"datepickercreacion"})
		
	class Meta:
		model = ControlProductoTerminado
		fields = [
			
			'anexo_turno',
			'anexo_centro',
			
			'fecha',
			'anexo_linea',
			'anexo_pagina',
			'observacion',
			'fecha_hora_creacion',
		
			
			
		]

		labels={
		
			"anexo_turno":"Turno",
			"anexo_centro":"Centro",
			
			'fecha':"Fecha",
			"anexo_linea":"Linea",
			"anexo_pagina":"Pagina",
			'observacion':"Observacion",
			"fecha_hora_creacion":"Fecha-Hora",
			
			
		}

class detallecontrolproductoterminadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):

		variablecliente=kwargs.pop("variable_cliente")
		variablevariedad=kwargs.pop("variable_variedad")
	
		print("aqiii")
		print(variablecliente)
		print(variablevariedad)
		print("lo que sea")
		super(detallecontrolproductoterminadoform, self).__init__(*args, **kwargs)
		self.fields['anexo_muestra'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","required":"true","data-error-message":"N° Palet","class":"form-control"})
		
		
	
		self.fields['anexo_cliente']=forms.ModelChoiceField(label="Cliente", queryset=variablecliente.AnexoCentroClientes.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_cliente'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
		self.fields['anexo_presentaciong']=forms.ModelChoiceField(label="PresentacionesG", queryset=variablecliente.AnexoCentroPresentacionesG.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_presentaciong'].widget.attrs.update({"autocomplete":"off","placeholder":"","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variablevariedad.cutivo1.all())
		self.fields['anexo_variedad'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
		self.fields['anexo_calibre']=forms.ModelChoiceField(label="Calibres", queryset=variablecliente.AnexoCentroCalibres.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_calibre'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
		self.fields['anexo_presentacion']=forms.ModelChoiceField(label="Presentaciones", queryset=variablecliente.AnexoCentroPresentacionesA.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_presentacion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['trazabilidad'].widget.attrs.update({"autocomplete":"off","placeholder":"Trazabilidad","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['tamano_pulpa'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso_neto'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['homogeneidad'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_acomodo'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['firme'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['sensitivo'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['blando'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['n1'].widget.attrs.update({"autocomplete":"off","placeholder":"n1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['n2'].widget.attrs.update({"autocomplete":"off","placeholder":"n2","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['n3'].widget.attrs.update({"autocomplete":"off","placeholder":"n3","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['n4'].widget.attrs.update({"autocomplete":"off","placeholder":"n4","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['pudricion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['micelio'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['heridas'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['deshidratacion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['desgarro'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['exudacion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['machucon'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['polvo'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['deforme'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['russet'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['presencia'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['restos'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['inmadura_verde'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['inmadura_rojo'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['bajo_calibre'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['material_extrano'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['cochinilla'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['mosca_fruta'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['arana_fruta'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['globito'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['decoloracion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['fruta_hinchada'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['p1'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p2'].widget.attrs.update({"autocomplete":"off","placeholder":"p2","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p3'].widget.attrs.update({"autocomplete":"off","placeholder":"p3","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p4'].widget.attrs.update({"autocomplete":"off","placeholder":"p4","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p5'].widget.attrs.update({"autocomplete":"off","placeholder":"p5","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p6'].widget.attrs.update({"autocomplete":"off","placeholder":"p6","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p7'].widget.attrs.update({"autocomplete":"off","placeholder":"p7","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p8'].widget.attrs.update({"autocomplete":"off","placeholder":"p8","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p9'].widget.attrs.update({"autocomplete":"off","placeholder":"p9","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p10'].widget.attrs.update({"autocomplete":"off","placeholder":"p10","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p11'].widget.attrs.update({"autocomplete":"off","placeholder":"p11","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p12'].widget.attrs.update({"autocomplete":"off","placeholder":"p12","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
	class Meta:
		model = DetalleControlProductoTerminado
		fields = [
			'anexo_muestra',
			'npalet',
			'anexo_cliente',
			'anexo_variedad',
			'anexo_calibre',
			'anexo_presentaciong',
			'anexo_presentacion',
			'trazabilidad',
			'tamano_pulpa',
			'peso_neto',
			'homogeneidad',
			'anexo_acomodo',
			'firme',
			'sensitivo',
			'blando',
			'n1',
			'n2',
			'n3',
			'n4',
			'pudricion',
			'micelio',
			'heridas',
			'deshidratacion',
			'desgarro',
			'exudacion',
			'machucon',
			'polvo',
			'deforme',
			'russet',
			'presencia',
			'restos',
			'inmadura_rojo',
			'inmadura_verde',
			'bajo_calibre',
			'material_extrano',
			'cochinilla',
			'mosca_fruta',
			'arana_fruta',
			'globito',
			'decoloracion',
			'fruta_hinchada',
			'p1',
			'p2',
			'p3',
			'p4',
			'p5',
			'p6',
			'p7',
			'p8',
			'p9',
			'p10',
			'p11',
			'p12',
		]

		labels={
			"anexo_muestra":"Muestra",
			"npalet":"N° Palet",
			"anexo_cliente":"Cliente",
			"anexo_variedad":"Variedad",
			"anexo_calibre":"Calibre",
			"anexo_presentaciong":"Presentacion G",
			"anexo_presentacion":"Presentacion",
			"trazabilidad":"Trazabilidad",
			"tamano_pulpa":"Temperatura Pulpa",
			"peso_neto":"Peso Neto",
			"homogeneidad":"Homogeneidad",
			"anexo_acomodo":"Acomodo",
			"firme":"% Firmeza",
			"sensitivo":"% Sensitivo",
			"blando":" % Blando",
			"n1":"% N1",
			"n2":"% N2",
			"n3":"% N3",
			"n4":"% N4",
			"blando":"% Blando",
			"pudricion":"% Pudricion",
			"micelio":"% Micelio",
			"heridas":"% Heridas",
			"deshidratacion":"% Deshidratacion",
			"desgarro":"% Desgarro",
			"exudacion":"% Exudacion",
			"machucon":"% Machucon",
			"polvo":"% Polvo",
			"deforme":"% Deforme",
			"russet":"% Russet",
			"presencia":"% Presencia",
			"restos":"% Restos",
			"inmadura_verde":"% Inmadura Verde",
			"inmadura_rojo":"% Inmadura Rojo",
			"bajo_calibre":"% Bajo Calibre",
			"material_extrano":"% Material Extraño",
			"cochinilla":"% Cochinilla",
			"mosca_fruta":"% Mosca Fruta",
			"arana_fruta":"% Araña Fruta",
			"globito":"% Globito",
			"decoloracion":"% Decoloracion",
			"fruta_hinchada":"% Fruta Hinchada",
			"p1":"P1",
			"p2":"P2",
			"p3":"P3",
			"p4":"P4",
			"p5":"P5",
			"p6":"P6",
			"p7":"P7",
			"p8":"P8",
			"p9":"P9",
			"p10":"P10",
			"p11":"P11",
			"p12":"P12",
			
		}



class evfenbrotesarandanossemform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenbrotesarandanossemform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['valvula'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EvFenBrotesArandanosSem
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			
			'valvula',
			
			
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Fun-Mod-Lot",
			
			"valvula":"Valvula",
			
		}

class evfenbrotedetalleplantasemform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenbrotedetalleplantasemform, self).__init__(*args, **kwargs)
		
		self.fields['n_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['nramas'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['nbrotes'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['verde1'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde2'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde3'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verde4'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['verderojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoverde'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoazul'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['azulrojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})		
		self.fields['maduro'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","readonly":"true","required":"true","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","readonly":"true","required":"true","data-error-message":"Ingresa Latitud","class":"form-control"})
	class Meta:
		model = DetallePlantaEvFenBrotesArandanosSem
		fields = [
			
			'n_planta',
			'nramas',
			'nbrotes',
			'verde1',
			'verde2',
			'verde3',
			'verde4',
			'verderojo',
			'rojoverde',
			'rojoazul',
			'azulrojo',
			'maduro',
			'longitud',
			'latitud',
			
			
		]

		labels={
			
			"n_planta":"N° Planta",
			"nramas":"N° Ramas",
			"nbrotes":"N° Brotes",
			"n_planta":"N° Planta",
			"verde1":"#Verde 1",
			"verde2":"#Verde 2",
			"verde3":"#Verde 3",
			"verde4":"#Verde 4",		
			"verderojo":"#Verde Rojo",
			"rojoverde":"#Rojo Verde",
			"rojoazul":"#Rojo Azul",
			"azulrojo":"#Azul Rojo",
			"maduro":"#Maduro",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}


class broteplantaevfensemform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(broteplantaevfensemform, self).__init__(*args, **kwargs)
		
		self.fields['verde4'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		
		
		self.fields['verderojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoverde'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['rojoazul'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['azulrojo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})		
		self.fields['maduro'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
	class Meta:
		model = BrotePlantaEvFenBrotesArandanosSem
		fields = [
			
			'verde4',
			'verderojo',
			'rojoverde',
			'rojoazul',
			'azulrojo',
			'maduro',
		]

		labels={
			
			"verde4":"#Verde 4",		
			"verderojo":"#Verde Rojo",
			"rojoverde":"#Rojo Verde",
			"rojoazul":"#Rojo Azul",
			"azulrojo":"#Azul Rojo",
			"maduro":"#Maduro",
			
		}


class evsanplagasarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evsanplagasarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_sector'].widget.attrs.update({"placeholder":"Sector","data-required":"true","data-error-message":"Sector requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_pagina'].widget.attrs.update({"placeholder":"Pagina","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['area_eval'].widget.attrs.update({"placeholder":"Area Eval.","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
	class Meta:
		model = EvSanPlagasArandanos
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'anexo_sector',
			'ubicacion',
			'anexo_pagina',
		
			'area_eval',
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_sector":"Sector",
			"ubicacion":"Fun-Mod-Lot",
			"anexo_pagina":"Pagina",
		
			"area_eval":"Area Evaluacion",
			
		}

class gruposplagasarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(gruposplagasarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['grupo'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		
		
	class Meta:
		model = GruposPlagasArandanos
		fields = [
			
			'grupo',
		
		]

		labels={
			
			"grupo":"Grupo",
			
			
		}

class subgruposplagasarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(subgruposplagasarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['subgrupo'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		
		
	class Meta:
		model = SubGruposPlagasArandanos
		fields = [
			
			'subgrupo',
		
		]

		labels={
			
			"subgrupo":"SubGrupo",
			
			
		}

class variablesplagasarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(variablesplagasarandanosform, self).__init__(*args, **kwargs)
		
		
		self.fields['acaro_hialino_nplanta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['arana_roja_nplanta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['argy_spha_nfrutos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['argy_spha_nlarvasgr'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['argy_spha_nlarvaspe'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['argy_spha_nplantas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cigarrita_individuos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_porplantas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_nadultos_corona'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_nadultos_planta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ninfas_corona'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ovisacos_corona'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ovisacos_planta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_adultos_brotes'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_adultos_ramas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ninfas_frutos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ninfas_brotes'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ninfas_ramas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ovisacos_brotes'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cochi_hari_ovisacos_ramas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['crypto_plantas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['diabro'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['gryllus'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['helio_plantas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['helio_frutos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['helio_larvasgr'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['helio_larvaspe'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['membracidos_nplanta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['mosca_blanca_ninfa'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['mosca_blanca_adulta'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['mosca_fruta_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['plecto_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['prosco_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['pulgones_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['pulgones_brotes'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['pulgones_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['queresas_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['queresas_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['spodo_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['spodo_larvargr'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['spodo_larvape'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['spodo_masa'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['trips_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['aranas_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cocci_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['crisopas_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['cryptola_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['otros_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['alternaria_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['antra_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['grado_infestacion'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['botritis_flores'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['botritis_frutos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['botritis_num'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['lasio_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['pestalo_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['pestalo_ramas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['phyto_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['planta_quemadas_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['planta_quemadas_ramas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['roya_por'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['roya_grado'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_ancha_hojas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_ancha_hojas2'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_ancha_cotiledones'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_angosta_focos'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_angosta_1'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['hoja_angosta_2'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		self.fields['abejas'].widget.attrs.update({"autocomplete":"off","data-required":"true","data-error-message":"Fecha requerida","class":"form-control","id":"datepicker"})
		
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","readonly":"true","required":"true","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","readonly":"true","required":"true","data-error-message":"Ingresa Latitud","class":"form-control"})
		
		
	class Meta:
		model = VariablesPlagasArandanos
		fields = [
			
			'acaro_hialino_nplanta',
			'arana_roja_nplanta',
			'argy_spha_nfrutos',
			'argy_spha_nlarvasgr',
			'argy_spha_nlarvaspe',
			'argy_spha_nplantas',
			'cigarrita_individuos',
			'cochi_hari_porplantas',
			'cochi_hari_nadultos_corona',
			'cochi_hari_nadultos_planta',
			'cochi_hari_ninfas_corona',
			'cochi_hari_ovisacos_corona',
			'cochi_hari_ovisacos_planta',
			'cochi_hari_adultos_brotes',
			'cochi_hari_adultos_ramas',
			'cochi_hari_ninfas_frutos',
			'cochi_hari_ninfas_brotes',
			'cochi_hari_ninfas_ramas',
			'cochi_hari_ovisacos_brotes',
			'cochi_hari_ovisacos_ramas',
			'crypto_plantas',
			'diabro',
			'gryllus',
			'helio_plantas',
			'helio_frutos',
			'helio_larvasgr',
			'helio_larvaspe',
			'membracidos_nplanta',
			'mosca_blanca_ninfa',
			'mosca_blanca_adulta',
			'mosca_fruta_num',
			'plecto_num',
			'prosco_num',
			'pulgones_por',
			'pulgones_brotes',
			'pulgones_num',
			'queresas_por',
			'queresas_num',
			'spodo_por',
			'spodo_larvargr',
			'spodo_larvape',
			'spodo_masa',
			'trips_num',
			'aranas_num',
			'cocci_num',
			'crisopas_num',
			'cryptola_num',
			'otros_num',
			'alternaria_por',
			'grado_infestacion',
			'antra_por',
			'botritis_flores',
			'botritis_frutos',
			'botritis_num',
			'lasio_por',
			'pestalo_por',
			'pestalo_ramas',
			'phyto_por',
			'planta_quemadas_por',
			'planta_quemadas_ramas',
			'roya_por',
			'roya_grado',
			'hoja_ancha_hojas',
			'hoja_ancha_hojas2',
			'hoja_ancha_cotiledones',
			'hoja_angosta_focos',
			'hoja_angosta_1',
			'hoja_angosta_2',
			'abejas',
			'longitud',
			'latitud'
		
		]

		labels={
			
			"acaro_hialino_nplanta":"Acaro Hialino /ind. x Planta",
			"arana_roja_nplanta":"Arañita Roja/ ind. x planta",
			"argy_spha_nfrutos":"Argyrotaenia sphaleropa /Frut. x planta",
			"argy_spha_nlarvasgr":"Argyrotaenia sphaleropa /Larv. Grande x planta",
			"argy_spha_nlarvaspe":"Argyrotaenia sphaleropa /Larv. Pequen x planta",
			"argy_spha_nplantas":"Argyrotaenia sphaleropa / N° Plantas Infectadas",
			"cigarrita_individuos":"Cigarrita/ Ind. x planta",
			"cochi_hari_porplantas":"Cochinilla Harinosa/% Plantas infectadas",
			"cochi_hari_nadultos_corona":"Cochinilla Harinosa/N° Adultos Corona-5cm SubSuelo ",
			"cochi_hari_nadultos_planta":"Cochinilla Harinosa/N° Adultos Planta-100 frutos",
			"cochi_hari_ninfas_corona":"Cochinilla Harinosa/N° Ninfas Corona-5cm SubSuelo ",
			"cochi_hari_ovisacos_corona":"Cochinilla Harinosa/N° Ovisacos Corona-5cm SubSuelo",
			"cochi_hari_ovisacos_planta":"Cochinilla Harinosa/N° Ovisacos Planta-100 frutos",
			"cochi_hari_adultos_brotes":"Cochinilla Harinosa/N° Adultos-brotes",
			"cochi_hari_adultos_ramas":"Cochinilla Harinosa/N° Adultos-Ramas",
			"cochi_hari_ninfas_frutos":"Cochinilla Harinosa/N° Ninfas - frutos",
			"cochi_hari_ninfas_brotes":"Cochinilla Harinosa/N° Ninfas - brotes",
			"cochi_hari_ninfas_ramas":"Cochinilla Harinosa/N° Ninfas - ramas",
			"cochi_hari_ovisacos_brotes":"Cochinilla Harinosa/N° Ovisacos - brotes",
			"cochi_hari_ovisacos_ramas":"Cochinilla Harinosa/N° Ovisacos - ramas",
			"crypto_plantas":"Cryptocephalus/Ind. x Planta",
			"diabro":"Diabrotica Viridula/Ind. x Planta",
			"gryllus":"Gryllus sp/Ind. x Planta",
			"helio_plantas":"Heliothis sp./ % - x planta",
			"helio_frutos":"Heliothis sp./Nro. Frutos Infectados",
			"helio_larvasgr":"Heliothis sp./Nro. Larvas Grandes",
			"helio_larvaspe":"Heliothis sp./Nro. Larvas Pequeñas",
			"membracidos_nplanta":"Membracidos /Nro Ind. x Planta",
			"mosca_blanca_ninfa":"Mosca Blanca/ N° Ninfas x Planta",
			"mosca_blanca_adulta":"Mosca Blanca/ N° Adultas x Planta",
			"mosca_fruta_num":"Mosca de la Fruta/ N° Frutos Infectados",
			"plecto_num":"Plectophoroides/ N° de Individuos x Planta",
			"prosco_num":"Proscópidos/N° de Individuos x Planta",
			"pulgones_por":"Pulgones/ % de Plantas Infectadas",
			"pulgones_brotes":"Pulgones/N° brotes infectados",
			"pulgones_num":"Pulgones/N° de Individuos x planta",
			"queresas_por":"Queresa/% plantas Infectadas",
			"queresas_num":"Queresa/N° Individuos x planta",
			"spodo_por":"Spodoptera/% de Plantas infectadas",
			"spodo_larvargr":"Spodoptera/ N° Larvas Grandes",
			"spodo_larvape":"Spodoptera/ N° Larvas Pequeñas",
			"spodo_masa":"Spodoptera/ N° Masa Huevo",
			"trips_num":"Trips/% Plantas Infectadas",
			"aranas_num":"Arañas/ N° Individuos x Plantas",
			"cocci_num":"Coccinelidos/N° Individuos x Plantas",
			"crisopas_num":"Crisopas/N° Individuos x Plantas",
			"cryptola_num":"Cryptolaemus/N° Individuos x Plantas",
			"otros_num":"Otros/ N° Individuos",
			"alternaria_por":"alternaria/ % Porcentaje Infectadas",
			"grado_infestacion":"Alternaria/ Grado de Infectación",
			"antra_por":"Antracnosis/% Porcentaje Infectadas",
			"botritis_flores":"Botritis/N° Flores Infectadas",
			"botritis_frutos":"Botritis/N° Frutos Infectadas",
			"botritis_num":"Botritis/N° Plantas Infectadas",
			"lasio_por":"Lasiodiplodia/% Porcentaje Infectadas",
			"pestalo_por":"Pestalotiopsis/% Porcentaje Infectadas",
			"pestalo_ramas":"Pestalotiopsis/ N° Ramas Infectadas",
			"phyto_por":"Phytophthora/% Porcentaje Infectadas",
			"planta_quemadas_por":"Planta quemadas//% Porcentaje quemadas",
			"planta_quemadas_ramas":"Planta quemadas/ N° Ramas quemadas",
			"roya_por":"Roya/% Plantas infectadas",
			"roya_grado":"Roya Grado de Infección",
			"hoja_ancha_hojas":"Hoja Ancha/N° plantas c/2 hojas /m2",
			"hoja_ancha_hojas2":"Hoja Ancha/N° plantas c/+2 hojas/m2",
			"hoja_ancha_cotiledones":"Hoja Ancha/N° plantas c/2 cotiledones",
			"hoja_angosta_focos":"Hoja Angosta/N° Focos de grama",
			"hoja_angosta_1":"Hoja Angosta/N° plantas c/+2 hojas /m2",
			"hoja_angosta_2":"Hoja Angosta/N° plantas c/2 hojas /m2",			
			"abejas":"Abejas/ N° Individuos x Planta",
			"latitud":"Latitud",
			"longitud":"Longitud",

		}


class evfenfrutoarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenfrutoarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['valvula'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EvFenFrutoArandanos
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			'valvula',
			
			
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Fun-Mod-Lot",
			
			"valvula":"Valvula",
			
		}

class detalleevfenfrutoarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevfenfrutoarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['nbaya'].widget.attrs.update({"autocomplete":"off","placeholder":"N Baya","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['calibre'].widget.attrs.update({"placeholder":"Calibre","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_selector'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Obs","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Longitud","readonly":"true","required":"true","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Latitud","readonly":"true","required":"true","data-error-message":"Ingresa Latitud","class":"form-control"})
		

	class Meta:
		model = DetalleEvFenFrutoArandanos
		fields = [
			
			'nbaya',
			'calibre',
			'anexo_selector',
			'observacion',
			'longitud',
			'latitud',
			
			
		]

		labels={
			
			"nbaya":"N° Baya",
			"calibre":"Calibre",
			"anexo_selector":"Tipo de Organo",
			"observacion":"Observacion",
			"latitud":"Latitud",
			"longitud":"Longitud",
			
			
		}

class evfenplanasaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenplanasaform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['valvula'].widget.attrs.update({"placeholder":"valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Observacion","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = EvFenPlanasa
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
		
			'valvula',
			'observacion',
			
			
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Fun-Mod-Lot",
			"valvula":"Valvula",
			"observacion":"Observacion",
			
		}

class detalleevfenplanasaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevfenplanasaform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_brote'].widget.attrs.update({"autocomplete":"off","placeholder":"Codigo Planta..","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['cod_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"Codigo Planta..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['altura_planta'].widget.attrs.update({"placeholder":"Alt. Planta","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cant.","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_selector'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['longitud1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['longitud2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['diametro'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['nro_hojas'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['observacion'].widget.attrs.update({"placeholder":"Obs..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Observacion","readonly":"true","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Observacion","readonly":"true","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = DetalleEvFenPlanasa
		fields = [
			'anexo_brote',
			'cod_planta',
			'altura_planta',
			'cantidad',
			'anexo_selector',
			'longitud1',
			'longitud2',
			'diametro',
			'nro_hojas',
			'observacion',
			'longitud',
			'latitud',
			
		]

		labels={
			"anexo_brote":"Brote",
			"cod_planta":"Codigo Planta",
			"altura_planta":"Altura Planta",
			"cantidad":"Cantidad",
			"anexo_selector":"Estado",
			"longitud1":"Longitud1",
			"longitud2":"Longitud2",
			"diametro":"Diametro",
			"nro_hojas":"Nro Hojas",
			"observacion":"Observacion",
			"longitud":"Longitud",
			"latitud":"Latitud",
			
		}

class evcaldefectoscampoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcaldefectoscampoform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		
	class Meta:
		model = EvCalDefectosCampo
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Pep",
		}

class detalleevcaldefectoscampoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablefundo=kwargs.pop("variable_fundo")
		super(detalleevcaldefectoscampoform, self).__init__(*args, **kwargs)
		
		self.fields['valvula'].widget.attrs.update({"autocomplete":"off","placeholder":"Valvula..","required":"true","data-error-message":"Fecha requerida","class":"form-control","onKeyDown":"validaciones()"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=2))
		self.fields['anexo_variedad'].widget.attrs.update({"autocomplete":"off","placeholder":"Variedad","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['densidad'].widget.attrs.update({"placeholder":"Densidad","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['reingreso'].widget.attrs.update({"placeholder":"Reingreso","required":"true","data-error-message":"Ubicacion requerida","class":"form-control","pattern":"[0-9]+","onKeyDown":"validaciones()"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['muestra'].widget.attrs.update({"placeholder":"Muestra","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control","pattern":"[0-9]+","onKeyDown":"validaciones()"})	
		self.fields['exportable'].widget.attrs.update({"placeholder":"Exportable","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['remanente'].widget.attrs.update({"placeholder":"Remanente","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['desgarro'].widget.attrs.update({"placeholder":"Desgarro","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['inmadurez'].widget.attrs.update({"placeholder":"Inmadurez","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['polvo'].widget.attrs.update({"placeholder":"Deshidratado","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['bayas'].widget.attrs.update({"placeholder":"Bayas","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['restos_florales'].widget.attrs.update({"placeholder":"Restos Florales","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['heridas'].widget.attrs.update({"placeholder":"Heridas","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['bajo_calibre'].widget.attrs.update({"placeholder":"Fuera de Calibre","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['pudricion'].widget.attrs.update({"placeholder":"Pudricion","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['cochinilla'].widget.attrs.update({"placeholder":"Cochinilla","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fruta_decolorada'].widget.attrs.update({"placeholder":"Fruta Decolorada","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI","required":"true","data-error-message":"Valvula requerida","class":"form-control","pattern":"[0-9]+","onKeyDown":"validaciones()"})
		self.fields['anexo_auxiliares']=forms.ModelChoiceField(label="Datos del Auxiliar", queryset=variablefundo.AnexoAuxiliarFundo.filter(anexo_estado=1))
		#self.fields['anexo_auxiliares']=forms.ModelChoiceField(label="Datos Auxiliar", queryset=AuxiliaresCampoAthos.objects.filter(anexo_estado=1))
		self.fields['anexo_auxiliares'].widget.attrs.update({"placeholder":"Auxiliar","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"placeholder":"Observacion","readonly":"true","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"Observacion","readonly":"true","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_caseta'].widget.attrs.update({"placeholder":"Caseta","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_tipo_envase'].widget.attrs.update({"placeholder":"Envase","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_evaluacion'].widget.attrs.update({"placeholder":"Evaluacion","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
	class Meta:
		model = DetalleEvCalDefectosCampo
		fields = [
			'valvula',
			'anexo_variedad',
			'densidad',
			'reingreso',
			'anexo_tipo',
			'muestra',
			'exportable',
			'remanente',
			'desgarro',
			'inmadurez',
			'polvo',
			'bayas',
			'restos_florales',
			'heridas',
			'bajo_calibre',
			'dni',
			'anexo_auxiliares',
			'longitud',
			'latitud',
			'anexo_caseta',
			'anexo_tipo_envase',
			'anexo_evaluacion',
			'pudricion',
			'cochinilla',
			'fruta_decolorada',
		]

#cambio de polvo por deshidratado
		labels={
			"valvula":"Valvula",
			"anexo_variedad":"Variedad",
			"densidad":"Densidad",
			"reingreso":"Reingreso",
			"anexo_tipo":"Tipo Calidad",
			"muestra":"Muestra(N° de bayas)",
			"exportable":"Exportable(N° de bayas)",
			"remanente":"Remanente(N° de bayas)",
			"desgarro":"Desgarro(N° de bayas)",
			"inmadurez":"Inmadurez(N° de bayas)",
			"polvo":"Deshidratado(N° de bayas)",
		
			"bayas":"Bayas en el Suelo",
			"restos_florales":"Restos Florales(N° de bayas)",
			"heridas":"Heridas(N° de bayas)",
			"bajo_calibre":"Fuera de Calibre",
			"dni":"Dni del Trabajador",
			"anexo_auxiliares":"Auxiliares",
			"longitud":"Longitud",
			"latitud":"Latitud",
			"anexo_caseta":"Caseta",
			"anexo_tipo_envase":"Tipo de Envase",
			"anexo_evaluacion":"Nro Evaluacion",
			"pudricion":"Pudricion",
			"cochinilla":"Cochinilla",
			"fruta_decolorada":"Fruta Decolorada",
		}


class evcalacopioplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalacopioplantaform, self).__init__(*args, **kwargs)
		
		self.fields['idacopio'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control"})
		self.fields['anexo_tipo_envase'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['tpulpa'].widget.attrs.update({"placeholder":"Tamaño Pulpa","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_mediano'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_grande'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_extra'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_jumbo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_partidura_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_partidura_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_partidura_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_partidura_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_fruta_hinchada_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_fruta_hinchada_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_fruta_hinchada_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_fruta_hinchada_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_globito_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_globito_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_globito_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_globito_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_picadura_ave_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_picadura_ave_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_picadura_ave_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_picadura_ave_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_cicatriz_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_cicatriz_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_cicatriz_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_cicatriz_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_decoloracion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_decoloracion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_decoloracion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_decoloracion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_pulgon_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_pulgon_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_pulgon_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_pulgon_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['fit_moscaf_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_prioridad'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		
		
	class Meta:
		model = EvCalAcopioPlantaArCaraz202202
		fields = [
			
		'idacopio',
		'fecha',
		'anexo_tipo_envase',
		'tpulpa',
		'dl_tamano1',
		'dl_tamano2',
		'dl_tamano3',
		'dl_tamano4',
		'dc_mediano',
		'dc_grande',
		'dc_extra',
		'dc_jumbo',
		'nb_n1_1',
		'nb_n1_2',
		'nb_n1_3',
		'nb_n1_4',
		'nb_n2_1',
		'nb_n2_2',
		'nb_n2_3',
		'nb_n2_4',
		'nb_n3_1',
		'nb_n3_2',
		'nb_n3_3',
		'nb_n3_4',
		'nb_n4_1',
		'nb_n4_2',
		'nb_n4_3',
		'nb_n4_4',
		'cd_pudricion_1',
		'cd_pudricion_2',
		'cd_pudricion_3',
		'cd_pudricion_4',
		'cd_blando_1',
		'cd_blando_2',
		'cd_blando_3',
		'cd_blando_4',
		'cd_micelio_1',
		'cd_micelio_2',
		'cd_micelio_3',
		'cd_micelio_4',
		'cd_herida_1',
		'cd_herida_2',
		'cd_herida_3',
		'cd_herida_4',
		'cd_deshidratacion_1',
		'cd_deshidratacion_2',
		'cd_deshidratacion_3',
		'cd_deshidratacion_4',
		'cd_desgarro_1',
		'cd_desgarro_2',
		'cd_desgarro_3',
		'cd_desgarro_4',
		'cd_exudacion_1',
		'cd_exudacion_2',
		'cd_exudacion_3',
		'cd_exudacion_4',
		'cd_machucon_1',
		'cd_machucon_2',
		'cd_machucon_3',
		'cd_machucon_4',
		'cd_partidura_1',
		'cd_partidura_2',
		'cd_partidura_3',
		'cd_partidura_4',
		'cd_fruta_hinchada_1',
		'cd_fruta_hinchada_2',
		'cd_fruta_hinchada_3',
		'cd_fruta_hinchada_4',
		'cd_globito_1',
		'cd_globito_2',
		'cd_globito_3',
		'cd_globito_4',
		'cal_polvo_1',
		'cal_polvo_2',
		'cal_polvo_3',
		'cal_polvo_4',
		'cal_deformes_1',
		'cal_deformes_2',
		'cal_deformes_3',
		'cal_deformes_4',
		'cal_picadura_ave_1',
		'cal_picadura_ave_2',
		'cal_picadura_ave_3',
		'cal_picadura_ave_4',
		'cal_russet_1',
		'cal_russet_2',
		'cal_russet_3',
		'cal_russet_4',
		'cal_cicatriz_1',
		'cal_cicatriz_2',
		'cal_cicatriz_3',
		'cal_cicatriz_4',
		'cal_presenciap_1',
		'cal_presenciap_2',
		'cal_presenciap_3',
		'cal_presenciap_4',
		'cal_restos_1',
		'cal_restos_2',
		'cal_restos_3',
		'cal_restos_4',
		'cal_frutaiv_1',
		'cal_frutaiv_2',
		'cal_frutaiv_3',
		'cal_frutaiv_4',
		'cal_frutair_1',
		'cal_frutair_2',
		'cal_frutair_3',
		'cal_frutair_4',
		'cal_bajoc_1',
		'cal_bajoc_2',
		'cal_bajoc_3',
		'cal_bajoc_4',
		'cal_materiale_1',
		'cal_materiale_2',
		'cal_materiale_3',
		'cal_materiale_4',
		'cal_decoloracion_1',
		'cal_decoloracion_2',
		'cal_decoloracion_3',
		'cal_decoloracion_4',
		'fit_cochinilla_1',
		'fit_cochinilla_2',
		'fit_cochinilla_3',
		'fit_cochinilla_4',

		'fit_pulgon_1',
		'fit_pulgon_2',
		'fit_pulgon_3',
		'fit_pulgon_4',

		'fit_moscaf_1',
		'fit_moscaf_2',
		'fit_moscaf_3',
		'fit_moscaf_4',
		'fit_aranas_1',
		'fit_aranas_2',
		'fit_aranas_3',
		'fit_aranas_4',
		'sol_m1_1',
		'sol_m1_2',
		'sol_m1_3',
		'sol_m1_4',
		'sol_m2_1',
		'sol_m2_2',
		'sol_m2_3',
		'sol_m2_4',
		'sol_m3_1',
		'sol_m3_2',
		'sol_m3_3',
		'sol_m3_4',
		'sol_m4_1',
		'sol_m4_2',
		'sol_m4_3',
		'sol_m4_4',
		'sol_m5_1',
		'sol_m5_2',
		'sol_m5_3',
		'sol_m5_4',
		'aci_m1_1',
		'aci_m1_2',
		'aci_m1_3',
		'aci_m1_4',
		'aci_m2_1',
		'aci_m2_2',
		'aci_m2_3',
		'aci_m2_4',
		'aci_m3_1',
		'aci_m3_2',
		'aci_m3_3',
		'aci_m3_4',
		'cpu_m1_1',
		'cpu_m1_2',
		'cpu_m1_3',
		'cpu_m1_4',
		'cpu_m2_1',
		'cpu_m2_2',
		'cpu_m2_3',
		'cpu_m2_4',
		'cpu_m3_1',
		'cpu_m3_2',
		'cpu_m3_3',
		'cpu_m3_4',
		'cpu_m4_1',
		'cpu_m4_2',
		'cpu_m4_3',
		'cpu_m4_4',
		'cpu_m5_1',
		'cpu_m5_2',
		'cpu_m5_3',
		'cpu_m5_4',
		'fir_m1_1',
		'fir_m1_2',
		'fir_m1_3',
		'fir_m1_4',
		'fir_m2_1',
		'fir_m2_2',
		'fir_m2_3',
		'fir_m2_4',
		'fir_m3_1',
		'fir_m3_2',
		'fir_m3_3',
		'fir_m3_4',
		'fir_m4_1',
		'fir_m4_2',
		'fir_m4_3',
		'fir_m4_4',
		'fir_m5_1',
		'fir_m5_2',
		'fir_m5_3',
		'fir_m5_4',
		'fir_m6_1',
		'fir_m6_2',
		'fir_m6_3',
		'fir_m6_4',
		'fir_m7_1',
		'fir_m7_2',
		'fir_m7_3',
		'fir_m7_4',
		'fir_m8_1',
		'fir_m8_2',
		'fir_m8_3',
		'fir_m8_4',
		'fir_m9_1',
		'fir_m9_2',
		'fir_m9_3',
		'fir_m9_4',
		'fir_m10_1',
		'fir_m10_2',
		'fir_m10_3',
		'fir_m10_4',
		'fir_m11_1',
		'fir_m11_2',
		'fir_m11_3',
		'fir_m11_4',
		'fir_m12_1',
		'fir_m12_2',
		'fir_m12_3',
		'fir_m12_4',
		'fir_m13_1',
		'fir_m13_2',
		'fir_m13_3',
		'fir_m13_4',
		'fir_m14_1',
		'fir_m14_2',
		'fir_m14_3',
		'fir_m14_4',
		'fir_m15_1',
		'fir_m15_2',
		'fir_m15_3',
		'fir_m15_4',
		'tol_blandos_1',
		'tol_cic_2',
		'tol_def_2',
		'tol_desgarro_2',
		'tol_deshidratado_2',
		'tol_frutosr4_1',
		'tol_polvo1_1',
		'tol_restosf_2',
		'tol_restosp_2',
		'tol_blandos_3',
		'tol_cic_3',
		'tol_def_3',
		'tol_desgarro2_2',
		'tol_deshidratado2_2',
		'tol_frutosr4_2',
		'tol_polvo1_2',
		'tol_restosf2_2',
		'tol_restosp2_2',
		'tol_blandos3_3',
		'tol_cic2_3',
		'tol_def2_3',
		'tol_desgarro2_3',
		'tol_deshidratado2_3',
		'tol_frutosr4_3',
		'tol_polvo1_3',
		'tol_restosf3_2',
		'tol_restosp3_2',
		'tol_blandos4_3',
		'tol_cic2_4',
		'tol_def2_4',
		'tol_desgarro2_4',
		'tol_deshidratado2_4',
		'tol_frutosr4_4',
		'tol_polvo1_4',
		'tol_restosf4_2',
		'tol_restosp4_2',
		'anexo_prioridad',
		'observacion'
	

		]

		labels={
			
		"idacopio":"N° PALET",
		"fecha":"FECHA",
		"anexo_tipo_envase":"TIPO DE ENVASE",
		"tpulpa":"TEMPERATURA PULPA",
		"dl_tamano1":"DATOS DE LLEGADA||Tamaño de muestra (g):1",
		"dl_tamano2":"DATOS DE LLEGADA||Tamaño de muestra (g):2",
		"dl_tamano3":"DATOS DE LLEGADA||Tamaño de muestra (g):3",
		"dl_tamano4":"DATOS DE LLEGADA||Tamaño de muestra (g):4",
		"dc_mediano":"DISTRIBUCIÓN DE CALIBRES (%)||Mediano(12-14mm.):1",
		"dc_grande":"DISTRIBUCIÓN DE CALIBRES (%)||Grande(14-17mm):1",
		"dc_extra":"DISTRIBUCIÓN DE CALIBRES (%)||Extra(17-20mm):1",
		"dc_jumbo":"DISTRIBUCIÓN DE CALIBRES (%)||Jumbo(20++mm.):1",
		"nb_n1_1":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):1.",
		"nb_n1_2":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):2",
		"nb_n1_3":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):3",
		"nb_n1_4":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):4",
		"nb_n2_1":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):1",
		"nb_n2_2":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):2",
		"nb_n2_3":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):3",
		"nb_n2_4":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):4",
		"nb_n3_1":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):1",
		"nb_n3_2":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):2",
		"nb_n3_3":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):3",
		"nb_n3_4":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):4",
		"nb_n4_1":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):1",
		"nb_n4_2":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):2",
		"nb_n4_3":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):3",
		"nb_n4_4":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):4",
		"cd_pudricion_1":"CONDICIÓN||Pudrición:1",
		"cd_pudricion_2":"CONDICIÓN||Pudrición:2",
		"cd_pudricion_3":"CONDICIÓN||Pudrición:3",
		"cd_pudricion_4":"CONDICIÓN||Pudrición:4",
		"cd_blando_1":"CONDICIÓN||Blando:1",
		"cd_blando_2":"CONDICIÓN||Blando:2",
		"cd_blando_3":"CONDICIÓN||Blando:3",
		"cd_blando_4":"CONDICIÓN||Blando:4",
		"cd_micelio_1":"CONDICIÓN||Micelio:1",
		"cd_micelio_2":"CONDICIÓN||Micelio:2",
		"cd_micelio_3":"CONDICIÓN||Micelio:3",
		"cd_micelio_4":"CONDICIÓN||Micelio:4",
		"cd_herida_1":"CONDICIÓN||Heridas:1",
		"cd_herida_2":"CONDICIÓN||Heridas:2",
		"cd_herida_3":"CONDICIÓN||Heridas:3",
		"cd_herida_4":"CONDICIÓN||Heridas:4",
		"cd_deshidratacion_1":"CONDICIÓN||Deshidratación:1",
		"cd_deshidratacion_2":"CONDICIÓN||Deshidratación:2",
		"cd_deshidratacion_3":"CONDICIÓN||Deshidratación:3",
		"cd_deshidratacion_4":"CONDICIÓN||Deshidratación:4",
		"cd_desgarro_1":"CONDICIÓN||Desgarro Pedicelar:1",
		"cd_desgarro_2":"CONDICIÓN||Desgarro Pedicelar:2",
		"cd_desgarro_3":"CONDICIÓN||Desgarro Pedicelar:3",
		"cd_desgarro_4":"CONDICIÓN||Desgarro Pedicelar:4",
		"cd_exudacion_1":"CONDICIÓN||Exudación jugo:1",
		"cd_exudacion_2":"CONDICIÓN||Exudación jugo:2",
		"cd_exudacion_3":"CONDICIÓN||Exudación jugo:3",
		"cd_exudacion_4":"CONDICIÓN||Exudación jugo:4",
		"cd_machucon_1":"CONDICIÓN||Machucón:1",
		"cd_machucon_2":"CONDICIÓN||Machucón:2",
		"cd_machucon_3":"CONDICIÓN||Machucón:3",
		"cd_machucon_4":"CONDICIÓN||Machucón:4",
		"cd_partidura_1":"CONDICIÓN||Partidura:1",
		"cd_partidura_2":"CONDICIÓN||Partidura:2",
		"cd_partidura_3":"CONDICIÓN||Partidura:3",
		"cd_partidura_4":"CONDICIÓN||Partidura:4",
		"cd_fruta_hinchada_1":"CONDICIÓN||Fruta Hinchada:1",
		"cd_fruta_hinchada_2":"CONDICIÓN||Fruta Hinchada:2",
		"cd_fruta_hinchada_3":"CONDICIÓN||Fruta Hinchada:3",
		"cd_fruta_hinchada_4":"CONDICIÓN||Fruta Hinchada:4",
		"cd_globito_1":"CONDICIÓN||Globito:1",
		"cd_globito_2":"CONDICIÓN||Globito:2",
		"cd_globito_3":"CONDICIÓN||Globito:3",
		"cd_globito_4":"CONDICIÓN||Globito:4",
		"cal_polvo_1":"CALIDAD||Tierra:1",
		"cal_polvo_2":"CALIDAD||Tierra:2",
		"cal_polvo_3":"CALIDAD||Tierra:3",
		"cal_polvo_4":"CALIDAD||Tierra:4",
		"cal_deformes_1":"CALIDAD||Deformes:1",
		"cal_deformes_2":"CALIDAD||Deformes:2",
		"cal_deformes_3":"CALIDAD||Deformes:3",
		"cal_deformes_4":"CALIDAD||Deformes:4",
		"cal_picadura_ave_1":"CALIDAD||Picadura de Ave:1",
		"cal_picadura_ave_2":"CALIDAD||Picadura de Ave:2",
		"cal_picadura_ave_3":"CALIDAD||Picadura de Ave:3",
		"cal_picadura_ave_4":"CALIDAD||Picadura de Ave:4",
		"cal_russet_1":"CALIDAD||Russet:1",
		"cal_russet_2":"CALIDAD||Russet:2",
		"cal_russet_3":"CALIDAD||Russet:3",
		"cal_russet_4":"CALIDAD||Russet:4",
		"cal_cicatriz_1":"CALIDAD||Cicatriz:1",
		"cal_cicatriz_2":"CALIDAD||Cicatriz:2",
		"cal_cicatriz_3":"CALIDAD||Cicatriz:3",
		"cal_cicatriz_4":"CALIDAD||Cicatriz:4",
		"cal_presenciap_1":"CALIDAD||Presencia de Pedicelo:1",
		"cal_presenciap_2":"CALIDAD||Presencia de Pedicelo:2",
		"cal_presenciap_3":"CALIDAD||Presencia de Pedicelo:3",
		"cal_presenciap_4":"CALIDAD||Presencia de Pedicelo:4",
		"cal_restos_1":"CALIDAD||Restos Florales:1",
		"cal_restos_2":"CALIDAD||Restos Florales:2",
		"cal_restos_3":"CALIDAD||Restos Florales:3",
		"cal_restos_4":"CALIDAD||Restos Florales:4",
		"cal_frutaiv_1":"CALIDAD||Fruta inmadura (verde):1",
		"cal_frutaiv_2":"CALIDAD||Fruta inmadura (verde):2",
		"cal_frutaiv_3":"CALIDAD||Fruta inmadura (verde):3",
		"cal_frutaiv_4":"CALIDAD||Fruta inmadura (verde):4",
		"cal_frutair_1":"CALIDAD||Fruta inmadura (Rojizo):1",
		"cal_frutair_2":"CALIDAD||Fruta inmadura (Rojizo):2",
		"cal_frutair_3":"CALIDAD||Fruta inmadura (Rojizo):3",
		"cal_frutair_4":"CALIDAD||Fruta inmadura (Rojizo):4",
		"cal_bajoc_1":"CALIDAD||Bajo calibre:1",
		"cal_bajoc_2":"CALIDAD||Bajo calibre:2",
		"cal_bajoc_3":"CALIDAD||Bajo calibre:3",
		"cal_bajoc_4":"CALIDAD||Bajo calibre:4",
		"cal_materiale_1":"CALIDAD||Material extraño:1",
		"cal_materiale_2":"CALIDAD||Material extraño:2",
		"cal_materiale_3":"CALIDAD||Material extraño:3",
		"cal_materiale_4":"CALIDAD||Material extraño:4",
		"cal_decoloracion_1":"CALIDAD||Decoloración:1",
		"cal_decoloracion_2":"CALIDAD||Decoloración:2",
		"cal_decoloracion_3":"CALIDAD||Decoloración:3",
		"cal_decoloracion_4":"CALIDAD||Decoloración:4",
		"fit_cochinilla_1":"FITOSANITARIO||Cochinilla:1",
		"fit_cochinilla_2":"FITOSANITARIO||Cochinilla:2",
		"fit_cochinilla_3":"FITOSANITARIO||Cochinilla:3",
		"fit_cochinilla_4":"FITOSANITARIO||Cochinilla:4",
		"fit_pulgon_1":"FITOSANITARIO||Pulgon:1",
		"fit_pulgon_2":"FITOSANITARIO||Pulgon:2",
		"fit_pulgon_3":"FITOSANITARIO||Pulgon:3",
		"fit_pulgon_4":"FITOSANITARIO||Pulgon:4",
		
		"fit_moscaf_1":"FITOSANITARIO||Mosca de la fruta:1",
		"fit_moscaf_2":"FITOSANITARIO||Mosca de la fruta:2",
		"fit_moscaf_3":"FITOSANITARIO||Mosca de la fruta:3",
		"fit_moscaf_4":"FITOSANITARIO||Mosca de la fruta:4",
		"fit_aranas_1":"FITOSANITARIO||Arañas (insectos):1",
		"fit_aranas_2":"FITOSANITARIO||Arañas (insectos):2",
		"fit_aranas_3":"FITOSANITARIO||Arañas (insectos):3",
		"fit_aranas_4":"FITOSANITARIO||Arañas (insectos):4",
		"sol_m1_1":"SÓLIDOS SOLUBLES||Muestra 1:1",
		"sol_m1_2":"SÓLIDOS SOLUBLES||Muestra 1:2",
		"sol_m1_3":"SÓLIDOS SOLUBLES||Muestra 1:3",
		"sol_m1_4":"SÓLIDOS SOLUBLES||Muestra 1:4",
		"sol_m2_1":"SÓLIDOS SOLUBLES||Muestra 2:1",
		"sol_m2_2":"SÓLIDOS SOLUBLES||Muestra 2:2",
		"sol_m2_3":"SÓLIDOS SOLUBLES||Muestra 2:3",
		"sol_m2_4":"SÓLIDOS SOLUBLES||Muestra 2:4",
		"sol_m3_1":"SÓLIDOS SOLUBLES||Muestra 3:1",
		"sol_m3_2":"SÓLIDOS SOLUBLES||Muestra 3:2",
		"sol_m3_3":"SÓLIDOS SOLUBLES||Muestra 3:3",
		"sol_m3_4":"SÓLIDOS SOLUBLES||Muestra 3:4",
		"sol_m4_1":"SÓLIDOS SOLUBLES||Muestra 4:1",
		"sol_m4_2":"SÓLIDOS SOLUBLES||Muestra 4:2",
		"sol_m4_3":"SÓLIDOS SOLUBLES||Muestra 4:3",
		"sol_m4_4":"SÓLIDOS SOLUBLES||Muestra 4:4",
		"sol_m5_1":"SÓLIDOS SOLUBLES||Muestra 5:1",
		"sol_m5_2":"SÓLIDOS SOLUBLES||Muestra 5:2",
		"sol_m5_3":"SÓLIDOS SOLUBLES||Muestra 5:3",
		"sol_m5_4":"SÓLIDOS SOLUBLES||Muestra 5:4",
		"aci_m1_1":"ACIDEZ||Muestra 1:1",
		"aci_m1_2":"ACIDEZ||Muestra 1:2",
		"aci_m1_3":"ACIDEZ||Muestra 1:3",
		"aci_m1_4":"ACIDEZ||Muestra 1:4",
		"aci_m2_1":"ACIDEZ||Muestra 2:1",
		"aci_m2_2":"ACIDEZ||Muestra 2:2",
		"aci_m2_3":"ACIDEZ||Muestra 2:3",
		"aci_m2_4":"ACIDEZ||Muestra 2:4",
		"aci_m3_1":"ACIDEZ||Muestra 3:1",
		"aci_m3_2":"ACIDEZ||Muestra 3:2",
		"aci_m3_3":"ACIDEZ||Muestra 3:3",
		"aci_m3_4":"ACIDEZ||Muestra 3:4",
		"cpu_m1_1":"COLOR DE PULPA||Nivel 1:1",
		"cpu_m1_2":"COLOR DE PULPA||Nivel 1:2",
		"cpu_m1_3":"COLOR DE PULPA||Nivel 1:3",
		"cpu_m1_4":"COLOR DE PULPA||Nivel 1:4",
		"cpu_m2_1":"COLOR DE PULPA||Nivel 2:1",
		"cpu_m2_2":"COLOR DE PULPA||Nivel 2:2",
		"cpu_m2_3":"COLOR DE PULPA||Nivel 2:3",
		"cpu_m2_4":"COLOR DE PULPA||Nivel 2:4",
		"cpu_m3_1":"COLOR DE PULPA||Nivel 3:1",
		"cpu_m3_2":"COLOR DE PULPA||Nivel 3:2",
		"cpu_m3_3":"COLOR DE PULPA||Nivel 3:3",
		"cpu_m3_4":"COLOR DE PULPA||Nivel 3:4",
		"cpu_m4_1":"COLOR DE PULPA||Nivel 4:1",
		"cpu_m4_2":"COLOR DE PULPA||Nivel 4:2",
		"cpu_m4_3":"COLOR DE PULPA||Nivel 4:3",
		"cpu_m4_4":"COLOR DE PULPA||Nivel 4:4",
		"cpu_m5_1":"COLOR DE PULPA||Nivel 5:1",
		"cpu_m5_2":"COLOR DE PULPA||Nivel 5:2",
		"cpu_m5_3":"COLOR DE PULPA||Nivel 5:3",
		"cpu_m5_4":"COLOR DE PULPA||Nivel 5:4",
		"fir_m1_1":"FIRMEZA (°)||Muestra 1:1",
		"fir_m1_2":"FIRMEZA (°)||Muestra 1:2",
		"fir_m1_3":"FIRMEZA (°)||Muestra 1:3",
		"fir_m1_4":"FIRMEZA (°)||Muestra 1:4",
		"fir_m2_1":"FIRMEZA (°)||Muestra 2:1",
		"fir_m2_2":"FIRMEZA (°)||Muestra 2:2",
		"fir_m2_3":"FIRMEZA (°)||Muestra 2:3",
		"fir_m2_4":"FIRMEZA (°)||Muestra 2:4",
		"fir_m3_1":"FIRMEZA (°)||Muestra 3:1",
		"fir_m3_2":"FIRMEZA (°)||Muestra 3:2",
		"fir_m3_3":"FIRMEZA (°)||Muestra 3:3",
		"fir_m3_4":"FIRMEZA (°)||Muestra 3:4",
		"fir_m4_1":"FIRMEZA (°)||Muestra 4:1",
		"fir_m4_2":"FIRMEZA (°)||Muestra 4:2",
		"fir_m4_3":"FIRMEZA (°)||Muestra 4:3",
		"fir_m4_4":"FIRMEZA (°)||Muestra 4:4",
		"fir_m5_1":"FIRMEZA (°)||Muestra 5:1",
		"fir_m5_2":"FIRMEZA (°)||Muestra 5:2",
		"fir_m5_3":"FIRMEZA (°)||Muestra 5:3",
		"fir_m5_4":"FIRMEZA (°)||Muestra 5:4",
		"fir_m6_1":"FIRMEZA (°)||Muestra 6:1",
		"fir_m6_2":"FIRMEZA (°)||Muestra 6:2",
		"fir_m6_3":"FIRMEZA (°)||Muestra 6:3",
		"fir_m6_4":"FIRMEZA (°)||Muestra 6:4",
		"fir_m7_1":"FIRMEZA (°)||Muestra 7:1",
		"fir_m7_2":"FIRMEZA (°)||Muestra 7:2",
		"fir_m7_3":"FIRMEZA (°)||Muestra 7:3",
		"fir_m7_4":"FIRMEZA (°)||Muestra 7:4",
		"fir_m8_1":"FIRMEZA (°)||Muestra 8:1",
		"fir_m8_2":"FIRMEZA (°)||Muestra 8:2",
		"fir_m8_3":"FIRMEZA (°)||Muestra 8:3",
		"fir_m8_4":"FIRMEZA (°)||Muestra 8:4",
		"fir_m9_1":"FIRMEZA (°)||Muestra 9:1",
		"fir_m9_2":"FIRMEZA (°)||Muestra 9:2",
		"fir_m9_3":"FIRMEZA (°)||Muestra 9:3",
		"fir_m9_4":"FIRMEZA (°)||Muestra 9:4",
		"fir_m10_1":"FIRMEZA (°)||Muestra 10:1",
		"fir_m10_2":"FIRMEZA (°)||Muestra 10:2",
		"fir_m10_3":"FIRMEZA (°)||Muestra 10:3",
		"fir_m10_4":"FIRMEZA (°)||Muestra 10:4",
		"fir_m11_1":"FIRMEZA (°)||Muestra 11:1",
		"fir_m11_2":"FIRMEZA (°)||Muestra 11:2",
		"fir_m11_3":"FIRMEZA (°)||Muestra 11:3",
		"fir_m11_4":"FIRMEZA (°)||Muestra 11:4",
		"fir_m12_1":"FIRMEZA (°)||Muestra 12:1",
		"fir_m12_2":"FIRMEZA (°)||Muestra 12:2",
		"fir_m12_3":"FIRMEZA (°)||Muestra 12:3",
		"fir_m12_4":"FIRMEZA (°)||Muestra 12:4",
		"fir_m13_1":"FIRMEZA (°)||Muestra 13:1",
		"fir_m13_2":"FIRMEZA (°)||Muestra 13:2",
		"fir_m13_3":"FIRMEZA (°)||Muestra 13:3",
		"fir_m13_4":"FIRMEZA (°)||Muestra 13:4",
		"fir_m14_1":"FIRMEZA (°)||Muestra 14:1",
		"fir_m14_2":"FIRMEZA (°)||Muestra 14:2",
		"fir_m14_3":"FIRMEZA (°)||Muestra 14:3",
		"fir_m14_4":"FIRMEZA (°)||Muestra 14:4",
		"fir_m15_1":"FIRMEZA (°)||Muestra 15:1",
		"fir_m15_2":"FIRMEZA (°)||Muestra 15:2",
		"fir_m15_3":"FIRMEZA (°)||Muestra 15:3",
		"fir_m15_4":"FIRMEZA (°)||Muestra 15:4",
		"tol_blandos_1":"TOLERANCIAS||BLANDOS:1",
		"tol_def_2":"TOLERANCIAS||DEFORMES N2:1",
		"tol_cic_2":"TOLERANCIAS||CICATRIZ N2:1",
		"tol_desgarro_2":"TOLERANCIAS||DESGARRO PEDICELAR N2:1",
		"tol_deshidratado_2":"TOLERANCIAS||DESHIDRATADO N2:1",
		"tol_frutosr4_1":"TOLERANCIAS||FRUTOS ROJIZOS N4:1",
		"tol_polvo1_1":"TOLERANCIAS||POLVO N1:1",
		"tol_restosf_2":"TOLERANCIAS||RESTOS FLORALES:1",
		"tol_restosp_2":"TOLERANCIAS||RESTOS PEDICELO:1",
		"tol_blandos_3":"TOLERANCIAS||BLANDOS:2",
		"tol_cic_3":"TOLERANCIAS||CICATRIZ N2:2",
		"tol_def_3":"TOLERANCIAS||DEFORMES N2:2",
		"tol_desgarro2_2":"TOLERANCIAS||DESGARRO PEDICELAR N2:2",
		"tol_deshidratado2_2":"TOLERANCIAS||DESHIDRATADO N2:2",
		"tol_frutosr4_2":"TOLERANCIAS||FRUTOS ROJIZOS N4:2",
		"tol_polvo1_2":"TOLERANCIAS||POLVO N1:2",
		"tol_restosf2_2":"TOLERANCIAS||RESTOS FLORALES:2",
		"tol_restosp2_2":"TOLERANCIAS||RESTOS PEDICELO:2",
		"tol_blandos3_3":"TOLERANCIAS||BLANDOS:3",
		"tol_cic2_3":"TOLERANCIAS||CICATRIZ N2:3",
		"tol_def2_3":"TOLERANCIAS||DEFORMES N2:3",
		"tol_desgarro2_3":"TOLERANCIAS||DESGARRO PEDICELAR N2:3",
		"tol_deshidratado2_3":"TOLERANCIAS||DESHIDRATADO N2:3",
		"tol_frutosr4_3":"TOLERANCIAS||FRUTOS ROJIZOS N4:3",
		"tol_polvo1_3":"TOLERANCIAS||POLVO N1:3",
		"tol_restosf3_2":"TOLERANCIAS||RESTOS FLORALES:3",
		"tol_restosp3_2":"TOLERANCIAS||RESTOS PEDICELO:3",
		"tol_blandos4_3":"TOLERANCIAS||BLANDOS:4",
		"tol_cic2_4":"TOLERANCIAS||CICATRIZ N2:4",
		"tol_def2_4":"TOLERANCIAS||DEFORMES N2:4",
		"tol_desgarro2_4":"TOLERANCIAS||DESGARRO PEDICELAR N2:4",
		"tol_deshidratado2_4":"TOLERANCIAS||DESHIDRATADO N2:4",
		"tol_frutosr4_4":"TOLERANCIAS||FRUTOS ROJIZOS N4:4",
		"tol_polvo1_4":"TOLERANCIAS||POLVO N1:4",
		"tol_restosf4_2":"TOLERANCIAS||RESTOS FLORALES:4",
		"tol_restosp4_2":"TOLERANCIAS||RESTOS PEDICELO:4",
		"anexo_prioridad":"Priority",
		"observacion":"Observacion"
		

	
		}

#form ICA EVCALACOPIOPLANTA

class evcalacopioplantaarica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalacopioplantaarica2021form, self).__init__(*args, **kwargs)
		
		self.fields['idacopio'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control"})
		self.fields['tpulpa'].widget.attrs.update({"placeholder":"Tamaño Pulpa","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dl_tamano4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_mediano'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_grande'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_extra'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dc_jumbo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nb_n4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_pudricion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_blando_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_micelio_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_herida_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_deshidratacion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_desgarro_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_exudacion_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cd_machucon_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_polvo_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_deformes_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_russet_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_presenciap_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_restos_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutaiv_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_frutair_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_bajoc_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cal_materiale_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_cochinilla_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_moscaf_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fit_aranas_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sol_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['aci_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['cpu_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m3_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m5_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m6_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m7_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m8_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m9_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m10_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m11_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m12_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m13_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m14_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fir_m15_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp2_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos3_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp3_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_blandos4_3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_cic2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_def2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_desgarro2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_deshidratado2_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_frutosr4_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_polvo1_4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosf4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['tol_restosp4_2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_prioridad'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		
		
	class Meta:
		model = EvCalAcopioPlantaArIca202202
		fields = [
			
		'idacopio',
		'fecha',
		'tpulpa',
		'dl_tamano1',
		'dl_tamano2',
		'dl_tamano3',
		'dl_tamano4',
		'dc_mediano',
		'dc_grande',
		'dc_extra',
		'dc_jumbo',
		'nb_n1_1',
		'nb_n1_2',
		'nb_n1_3',
		'nb_n1_4',
		'nb_n2_1',
		'nb_n2_2',
		'nb_n2_3',
		'nb_n2_4',
		'nb_n3_1',
		'nb_n3_2',
		'nb_n3_3',
		'nb_n3_4',
		'nb_n4_1',
		'nb_n4_2',
		'nb_n4_3',
		'nb_n4_4',
		'cd_pudricion_1',
		'cd_pudricion_2',
		'cd_pudricion_3',
		'cd_pudricion_4',
		'cd_blando_1',
		'cd_blando_2',
		'cd_blando_3',
		'cd_blando_4',
		'cd_micelio_1',
		'cd_micelio_2',
		'cd_micelio_3',
		'cd_micelio_4',
		'cd_herida_1',
		'cd_herida_2',
		'cd_herida_3',
		'cd_herida_4',
		'cd_deshidratacion_1',
		'cd_deshidratacion_2',
		'cd_deshidratacion_3',
		'cd_deshidratacion_4',
		'cd_desgarro_1',
		'cd_desgarro_2',
		'cd_desgarro_3',
		'cd_desgarro_4',
		'cd_exudacion_1',
		'cd_exudacion_2',
		'cd_exudacion_3',
		'cd_exudacion_4',
		'cd_machucon_1',
		'cd_machucon_2',
		'cd_machucon_3',
		'cd_machucon_4',
		'cal_polvo_1',
		'cal_polvo_2',
		'cal_polvo_3',
		'cal_polvo_4',
		'cal_deformes_1',
		'cal_deformes_2',
		'cal_deformes_3',
		'cal_deformes_4',
		'cal_russet_1',
		'cal_russet_2',
		'cal_russet_3',
		'cal_russet_4',
		'cal_presenciap_1',
		'cal_presenciap_2',
		'cal_presenciap_3',
		'cal_presenciap_4',
		'cal_restos_1',
		'cal_restos_2',
		'cal_restos_3',
		'cal_restos_4',
		'cal_frutaiv_1',
		'cal_frutaiv_2',
		'cal_frutaiv_3',
		'cal_frutaiv_4',
		'cal_frutair_1',
		'cal_frutair_2',
		'cal_frutair_3',
		'cal_frutair_4',
		'cal_bajoc_1',
		'cal_bajoc_2',
		'cal_bajoc_3',
		'cal_bajoc_4',
		'cal_materiale_1',
		'cal_materiale_2',
		'cal_materiale_3',
		'cal_materiale_4',
		'fit_cochinilla_1',
		'fit_cochinilla_2',
		'fit_cochinilla_3',
		'fit_cochinilla_4',
		'fit_moscaf_1',
		'fit_moscaf_2',
		'fit_moscaf_3',
		'fit_moscaf_4',
		'fit_aranas_1',
		'fit_aranas_2',
		'fit_aranas_3',
		'fit_aranas_4',
		'sol_m1_1',
		'sol_m1_2',
		'sol_m1_3',
		'sol_m1_4',
		'sol_m2_1',
		'sol_m2_2',
		'sol_m2_3',
		'sol_m2_4',
		'sol_m3_1',
		'sol_m3_2',
		'sol_m3_3',
		'sol_m3_4',
		'sol_m4_1',
		'sol_m4_2',
		'sol_m4_3',
		'sol_m4_4',
		'sol_m5_1',
		'sol_m5_2',
		'sol_m5_3',
		'sol_m5_4',
		'aci_m1_1',
		'aci_m1_2',
		'aci_m1_3',
		'aci_m1_4',
		'aci_m2_1',
		'aci_m2_2',
		'aci_m2_3',
		'aci_m2_4',
		'aci_m3_1',
		'aci_m3_2',
		'aci_m3_3',
		'aci_m3_4',
		'cpu_m1_1',
		'cpu_m1_2',
		'cpu_m1_3',
		'cpu_m1_4',
		'cpu_m2_1',
		'cpu_m2_2',
		'cpu_m2_3',
		'cpu_m2_4',
		'cpu_m3_1',
		'cpu_m3_2',
		'cpu_m3_3',
		'cpu_m3_4',
		'cpu_m4_1',
		'cpu_m4_2',
		'cpu_m4_3',
		'cpu_m4_4',
		'cpu_m5_1',
		'cpu_m5_2',
		'cpu_m5_3',
		'cpu_m5_4',
		'fir_m1_1',
		'fir_m1_2',
		'fir_m1_3',
		'fir_m1_4',
		'fir_m2_1',
		'fir_m2_2',
		'fir_m2_3',
		'fir_m2_4',
		'fir_m3_1',
		'fir_m3_2',
		'fir_m3_3',
		'fir_m3_4',
		'fir_m4_1',
		'fir_m4_2',
		'fir_m4_3',
		'fir_m4_4',
		'fir_m5_1',
		'fir_m5_2',
		'fir_m5_3',
		'fir_m5_4',
		'fir_m6_1',
		'fir_m6_2',
		'fir_m6_3',
		'fir_m6_4',
		'fir_m7_1',
		'fir_m7_2',
		'fir_m7_3',
		'fir_m7_4',
		'fir_m8_1',
		'fir_m8_2',
		'fir_m8_3',
		'fir_m8_4',
		'fir_m9_1',
		'fir_m9_2',
		'fir_m9_3',
		'fir_m9_4',
		'fir_m10_1',
		'fir_m10_2',
		'fir_m10_3',
		'fir_m10_4',
		'fir_m11_1',
		'fir_m11_2',
		'fir_m11_3',
		'fir_m11_4',
		'fir_m12_1',
		'fir_m12_2',
		'fir_m12_3',
		'fir_m12_4',
		'fir_m13_1',
		'fir_m13_2',
		'fir_m13_3',
		'fir_m13_4',
		'fir_m14_1',
		'fir_m14_2',
		'fir_m14_3',
		'fir_m14_4',
		'fir_m15_1',
		'fir_m15_2',
		'fir_m15_3',
		'fir_m15_4',
		'tol_blandos_1',
		'tol_cic_2',
		'tol_def_2',
		'tol_desgarro_2',
		'tol_deshidratado_2',
		'tol_frutosr4_1',
		'tol_polvo1_1',
		'tol_restosf_2',
		'tol_restosp_2',
		'tol_blandos_3',
		'tol_cic_3',
		'tol_def_3',
		'tol_desgarro2_2',
		'tol_deshidratado2_2',
		'tol_frutosr4_2',
		'tol_polvo1_2',
		'tol_restosf2_2',
		'tol_restosp2_2',
		'tol_blandos3_3',
		'tol_cic2_3',
		'tol_def2_3',
		'tol_desgarro2_3',
		'tol_deshidratado2_3',
		'tol_frutosr4_3',
		'tol_polvo1_3',
		'tol_restosf3_2',
		'tol_restosp3_2',
		'tol_blandos4_3',
		'tol_cic2_4',
		'tol_def2_4',
		'tol_desgarro2_4',
		'tol_deshidratado2_4',
		'tol_frutosr4_4',
		'tol_polvo1_4',
		'tol_restosf4_2',
		'tol_restosp4_2',
		'anexo_prioridad',
		'observacion'
	

		]

		labels={
			
		"idacopio":"N° PALET",
		"fecha":"FECHA",
		"tpulpa":"TEMPERATURA PULPA",
		"dl_tamano1":"DATOS DE LLEGADA||Tamaño de muestra (g):1",
		"dl_tamano2":"DATOS DE LLEGADA||Tamaño de muestra (g):2",
		"dl_tamano3":"DATOS DE LLEGADA||Tamaño de muestra (g):3",
		"dl_tamano4":"DATOS DE LLEGADA||Tamaño de muestra (g):4",
		"dc_mediano":"DISTRIBUCIÓN DE CALIBRES (%)||Mediano(12-14mm.):1",
		"dc_grande":"DISTRIBUCIÓN DE CALIBRES (%)||Grande(14-17mm):1",
		"dc_extra":"DISTRIBUCIÓN DE CALIBRES (%)||Extra(17-20mm):1",
		"dc_jumbo":"DISTRIBUCIÓN DE CALIBRES (%)||Jumbo(20++mm.):1",
		"nb_n1_1":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):1.",
		"nb_n1_2":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):2",
		"nb_n1_3":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):3",
		"nb_n1_4":"NIVEL DE BLOOM (%)||N1 (75 - 100 %):4",
		"nb_n2_1":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):1",
		"nb_n2_2":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):2",
		"nb_n2_3":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):3",
		"nb_n2_4":"NIVEL DE BLOOM (%)||N2 (50 - 74 %):4",
		"nb_n3_1":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):1",
		"nb_n3_2":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):2",
		"nb_n3_3":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):3",
		"nb_n3_4":"NIVEL DE BLOOM (%)||N3 (25 - 49 %):4",
		"nb_n4_1":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):1",
		"nb_n4_2":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):2",
		"nb_n4_3":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):3",
		"nb_n4_4":"NIVEL DE BLOOM (%)||N4 (0 - 24 %):4",
		"cd_pudricion_1":"CONDICIÓN||Pudrición:1",
		"cd_pudricion_2":"CONDICIÓN||Pudrición:2",
		"cd_pudricion_3":"CONDICIÓN||Pudrición:3",
		"cd_pudricion_4":"CONDICIÓN||Pudrición:4",
		"cd_blando_1":"CONDICIÓN||Blando:1",
		"cd_blando_2":"CONDICIÓN||Blando:2",
		"cd_blando_3":"CONDICIÓN||Blando:3",
		"cd_blando_4":"CONDICIÓN||Blando:4",
		"cd_micelio_1":"CONDICIÓN||Micelio:1",
		"cd_micelio_2":"CONDICIÓN||Micelio:2",
		"cd_micelio_3":"CONDICIÓN||Micelio:3",
		"cd_micelio_4":"CONDICIÓN||Micelio:4",
		"cd_herida_1":"CONDICIÓN||Heridas:1",
		"cd_herida_2":"CONDICIÓN||Heridas:2",
		"cd_herida_3":"CONDICIÓN||Heridas:3",
		"cd_herida_4":"CONDICIÓN||Heridas:4",
		"cd_deshidratacion_1":"CONDICIÓN||Deshidratación:1",
		"cd_deshidratacion_2":"CONDICIÓN||Deshidratación:2",
		"cd_deshidratacion_3":"CONDICIÓN||Deshidratación:3",
		"cd_deshidratacion_4":"CONDICIÓN||Deshidratación:4",
		"cd_desgarro_1":"CONDICIÓN||Desgarro Pedicelar:1",
		"cd_desgarro_2":"CONDICIÓN||Desgarro Pedicelar:2",
		"cd_desgarro_3":"CONDICIÓN||Desgarro Pedicelar:3",
		"cd_desgarro_4":"CONDICIÓN||Desgarro Pedicelar:4",
		"cd_exudacion_1":"CONDICIÓN||Exudación jugo:1",
		"cd_exudacion_2":"CONDICIÓN||Exudación jugo:2",
		"cd_exudacion_3":"CONDICIÓN||Exudación jugo:3",
		"cd_exudacion_4":"CONDICIÓN||Exudación jugo:4",
		"cd_machucon_1":"CONDICIÓN||Machucón:1",
		"cd_machucon_2":"CONDICIÓN||Machucón:2",
		"cd_machucon_3":"CONDICIÓN||Machucón:3",
		"cd_machucon_4":"CONDICIÓN||Machucón:4",
		"cal_polvo_1":"CALIDAD||Polvo / Tierra:1",
		"cal_polvo_2":"CALIDAD||Polvo / Tierra:2",
		"cal_polvo_3":"CALIDAD||Polvo / Tierra:3",
		"cal_polvo_4":"CALIDAD||Polvo / Tierra:4",
		"cal_deformes_1":"CALIDAD||Deformes:1",
		"cal_deformes_2":"CALIDAD||Deformes:2",
		"cal_deformes_3":"CALIDAD||Deformes:3",
		"cal_deformes_4":"CALIDAD||Deformes:4",
		"cal_russet_1":"CALIDAD||Russet / Cicatriz:1",
		"cal_russet_2":"CALIDAD||Russet / Cicatriz:2",
		"cal_russet_3":"CALIDAD||Russet / Cicatriz:3",
		"cal_russet_4":"CALIDAD||Russet / Cicatriz:4",
		"cal_presenciap_1":"CALIDAD||Presencia de Pedicelo:1",
		"cal_presenciap_2":"CALIDAD||Presencia de Pedicelo:2",
		"cal_presenciap_3":"CALIDAD||Presencia de Pedicelo:3",
		"cal_presenciap_4":"CALIDAD||Presencia de Pedicelo:4",
		"cal_restos_1":"CALIDAD||Restos Florales:1",
		"cal_restos_2":"CALIDAD||Restos Florales:2",
		"cal_restos_3":"CALIDAD||Restos Florales:3",
		"cal_restos_4":"CALIDAD||Restos Florales:4",
		"cal_frutaiv_1":"CALIDAD||Fruta inmadura (verde):1",
		"cal_frutaiv_2":"CALIDAD||Fruta inmadura (verde):2",
		"cal_frutaiv_3":"CALIDAD||Fruta inmadura (verde):3",
		"cal_frutaiv_4":"CALIDAD||Fruta inmadura (verde):4",
		"cal_frutair_1":"CALIDAD||Fruta inmadura (Rojizo):1",
		"cal_frutair_2":"CALIDAD||Fruta inmadura (Rojizo):2",
		"cal_frutair_3":"CALIDAD||Fruta inmadura (Rojizo):3",
		"cal_frutair_4":"CALIDAD||Fruta inmadura (Rojizo):4",
		"cal_bajoc_1":"CALIDAD||Bajo calibre:1",
		"cal_bajoc_2":"CALIDAD||Bajo calibre:2",
		"cal_bajoc_3":"CALIDAD||Bajo calibre:3",
		"cal_bajoc_4":"CALIDAD||Bajo calibre:4",
		"cal_materiale_1":"CALIDAD||Material extraño:1",
		"cal_materiale_2":"CALIDAD||Material extraño:2",
		"cal_materiale_3":"CALIDAD||Material extraño:3",
		"cal_materiale_4":"CALIDAD||Material extraño:4",
		"fit_cochinilla_1":"FITOSANITARIO||Cochinilla:1",
		"fit_cochinilla_2":"FITOSANITARIO||Cochinilla:2",
		"fit_cochinilla_3":"FITOSANITARIO||Cochinilla:3",
		"fit_cochinilla_4":"FITOSANITARIO||Cochinilla:4",
		"fit_moscaf_1":"FITOSANITARIO||Mosca de la fruta:1",
		"fit_moscaf_2":"FITOSANITARIO||Mosca de la fruta:2",
		"fit_moscaf_3":"FITOSANITARIO||Mosca de la fruta:3",
		"fit_moscaf_4":"FITOSANITARIO||Mosca de la fruta:4",
		"fit_aranas_1":"FITOSANITARIO||Arañas (insectos):1",
		"fit_aranas_2":"FITOSANITARIO||Arañas (insectos):2",
		"fit_aranas_3":"FITOSANITARIO||Arañas (insectos):3",
		"fit_aranas_4":"FITOSANITARIO||Arañas (insectos):4",
		"sol_m1_1":"SÓLIDOS SOLUBLES||Muestra 1:1",
		"sol_m1_2":"SÓLIDOS SOLUBLES||Muestra 1:2",
		"sol_m1_3":"SÓLIDOS SOLUBLES||Muestra 1:3",
		"sol_m1_4":"SÓLIDOS SOLUBLES||Muestra 1:4",
		"sol_m2_1":"SÓLIDOS SOLUBLES||Muestra 2:1",
		"sol_m2_2":"SÓLIDOS SOLUBLES||Muestra 2:2",
		"sol_m2_3":"SÓLIDOS SOLUBLES||Muestra 2:3",
		"sol_m2_4":"SÓLIDOS SOLUBLES||Muestra 2:4",
		"sol_m3_1":"SÓLIDOS SOLUBLES||Muestra 3:1",
		"sol_m3_2":"SÓLIDOS SOLUBLES||Muestra 3:2",
		"sol_m3_3":"SÓLIDOS SOLUBLES||Muestra 3:3",
		"sol_m3_4":"SÓLIDOS SOLUBLES||Muestra 3:4",
		"sol_m4_1":"SÓLIDOS SOLUBLES||Muestra 4:1",
		"sol_m4_2":"SÓLIDOS SOLUBLES||Muestra 4:2",
		"sol_m4_3":"SÓLIDOS SOLUBLES||Muestra 4:3",
		"sol_m4_4":"SÓLIDOS SOLUBLES||Muestra 4:4",
		"sol_m5_1":"SÓLIDOS SOLUBLES||Muestra 5:1",
		"sol_m5_2":"SÓLIDOS SOLUBLES||Muestra 5:2",
		"sol_m5_3":"SÓLIDOS SOLUBLES||Muestra 5:3",
		"sol_m5_4":"SÓLIDOS SOLUBLES||Muestra 5:4",
		"aci_m1_1":"ACIDEZ||Muestra 1:1",
		"aci_m1_2":"ACIDEZ||Muestra 1:2",
		"aci_m1_3":"ACIDEZ||Muestra 1:3",
		"aci_m1_4":"ACIDEZ||Muestra 1:4",
		"aci_m2_1":"ACIDEZ||Muestra 2:1",
		"aci_m2_2":"ACIDEZ||Muestra 2:2",
		"aci_m2_3":"ACIDEZ||Muestra 2:3",
		"aci_m2_4":"ACIDEZ||Muestra 2:4",
		"aci_m3_1":"ACIDEZ||Muestra 3:1",
		"aci_m3_2":"ACIDEZ||Muestra 3:2",
		"aci_m3_3":"ACIDEZ||Muestra 3:3",
		"aci_m3_4":"ACIDEZ||Muestra 3:4",
		"cpu_m1_1":"COLOR DE PULPA||Nivel 1:1",
		"cpu_m1_2":"COLOR DE PULPA||Nivel 1:2",
		"cpu_m1_3":"COLOR DE PULPA||Nivel 1:3",
		"cpu_m1_4":"COLOR DE PULPA||Nivel 1:4",
		"cpu_m2_1":"COLOR DE PULPA||Nivel 2:1",
		"cpu_m2_2":"COLOR DE PULPA||Nivel 2:2",
		"cpu_m2_3":"COLOR DE PULPA||Nivel 2:3",
		"cpu_m2_4":"COLOR DE PULPA||Nivel 2:4",
		"cpu_m3_1":"COLOR DE PULPA||Nivel 3:1",
		"cpu_m3_2":"COLOR DE PULPA||Nivel 3:2",
		"cpu_m3_3":"COLOR DE PULPA||Nivel 3:3",
		"cpu_m3_4":"COLOR DE PULPA||Nivel 3:4",
		"cpu_m4_1":"COLOR DE PULPA||Nivel 4:1",
		"cpu_m4_2":"COLOR DE PULPA||Nivel 4:2",
		"cpu_m4_3":"COLOR DE PULPA||Nivel 4:3",
		"cpu_m4_4":"COLOR DE PULPA||Nivel 4:4",
		"cpu_m5_1":"COLOR DE PULPA||Nivel 5:1",
		"cpu_m5_2":"COLOR DE PULPA||Nivel 5:2",
		"cpu_m5_3":"COLOR DE PULPA||Nivel 5:3",
		"cpu_m5_4":"COLOR DE PULPA||Nivel 5:4",
		"fir_m1_1":"FIRMEZA (°)||Muestra 1:1",
		"fir_m1_2":"FIRMEZA (°)||Muestra 1:2",
		"fir_m1_3":"FIRMEZA (°)||Muestra 1:3",
		"fir_m1_4":"FIRMEZA (°)||Muestra 1:4",
		"fir_m2_1":"FIRMEZA (°)||Muestra 2:1",
		"fir_m2_2":"FIRMEZA (°)||Muestra 2:2",
		"fir_m2_3":"FIRMEZA (°)||Muestra 2:3",
		"fir_m2_4":"FIRMEZA (°)||Muestra 2:4",
		"fir_m3_1":"FIRMEZA (°)||Muestra 3:1",
		"fir_m3_2":"FIRMEZA (°)||Muestra 3:2",
		"fir_m3_3":"FIRMEZA (°)||Muestra 3:3",
		"fir_m3_4":"FIRMEZA (°)||Muestra 3:4",
		"fir_m4_1":"FIRMEZA (°)||Muestra 4:1",
		"fir_m4_2":"FIRMEZA (°)||Muestra 4:2",
		"fir_m4_3":"FIRMEZA (°)||Muestra 4:3",
		"fir_m4_4":"FIRMEZA (°)||Muestra 4:4",
		"fir_m5_1":"FIRMEZA (°)||Muestra 5:1",
		"fir_m5_2":"FIRMEZA (°)||Muestra 5:2",
		"fir_m5_3":"FIRMEZA (°)||Muestra 5:3",
		"fir_m5_4":"FIRMEZA (°)||Muestra 5:4",
		"fir_m6_1":"FIRMEZA (°)||Muestra 6:1",
		"fir_m6_2":"FIRMEZA (°)||Muestra 6:2",
		"fir_m6_3":"FIRMEZA (°)||Muestra 6:3",
		"fir_m6_4":"FIRMEZA (°)||Muestra 6:4",
		"fir_m7_1":"FIRMEZA (°)||Muestra 7:1",
		"fir_m7_2":"FIRMEZA (°)||Muestra 7:2",
		"fir_m7_3":"FIRMEZA (°)||Muestra 7:3",
		"fir_m7_4":"FIRMEZA (°)||Muestra 7:4",
		"fir_m8_1":"FIRMEZA (°)||Muestra 8:1",
		"fir_m8_2":"FIRMEZA (°)||Muestra 8:2",
		"fir_m8_3":"FIRMEZA (°)||Muestra 8:3",
		"fir_m8_4":"FIRMEZA (°)||Muestra 8:4",
		"fir_m9_1":"FIRMEZA (°)||Muestra 9:1",
		"fir_m9_2":"FIRMEZA (°)||Muestra 9:2",
		"fir_m9_3":"FIRMEZA (°)||Muestra 9:3",
		"fir_m9_4":"FIRMEZA (°)||Muestra 9:4",
		"fir_m10_1":"FIRMEZA (°)||Muestra 10:1",
		"fir_m10_2":"FIRMEZA (°)||Muestra 10:2",
		"fir_m10_3":"FIRMEZA (°)||Muestra 10:3",
		"fir_m10_4":"FIRMEZA (°)||Muestra 10:4",
		"fir_m11_1":"FIRMEZA (°)||Muestra 11:1",
		"fir_m11_2":"FIRMEZA (°)||Muestra 11:2",
		"fir_m11_3":"FIRMEZA (°)||Muestra 11:3",
		"fir_m11_4":"FIRMEZA (°)||Muestra 11:4",
		"fir_m12_1":"FIRMEZA (°)||Muestra 12:1",
		"fir_m12_2":"FIRMEZA (°)||Muestra 12:2",
		"fir_m12_3":"FIRMEZA (°)||Muestra 12:3",
		"fir_m12_4":"FIRMEZA (°)||Muestra 12:4",
		"fir_m13_1":"FIRMEZA (°)||Muestra 13:1",
		"fir_m13_2":"FIRMEZA (°)||Muestra 13:2",
		"fir_m13_3":"FIRMEZA (°)||Muestra 13:3",
		"fir_m13_4":"FIRMEZA (°)||Muestra 13:4",
		"fir_m14_1":"FIRMEZA (°)||Muestra 14:1",
		"fir_m14_2":"FIRMEZA (°)||Muestra 14:2",
		"fir_m14_3":"FIRMEZA (°)||Muestra 14:3",
		"fir_m14_4":"FIRMEZA (°)||Muestra 14:4",
		"fir_m15_1":"FIRMEZA (°)||Muestra 15:1",
		"fir_m15_2":"FIRMEZA (°)||Muestra 15:2",
		"fir_m15_3":"FIRMEZA (°)||Muestra 15:3",
		"fir_m15_4":"FIRMEZA (°)||Muestra 15:4",
		"tol_blandos_1":"TOLERANCIAS||BLANDOS:1",
		"tol_def_2":"TOLERANCIAS||DEFORMES N2:1",
		"tol_cic_2":"TOLERANCIAS||CICATRIZ N2:1",
		"tol_desgarro_2":"TOLERANCIAS||DESGARRO PEDICELAR N2:1",
		"tol_deshidratado_2":"TOLERANCIAS||DESHIDRATADO N2:1",
		"tol_frutosr4_1":"TOLERANCIAS||FRUTOS ROJIZOS N4:1",
		"tol_polvo1_1":"TOLERANCIAS||POLVO N1:1",
		"tol_restosf_2":"TOLERANCIAS||RESTOS FLORALES:1",
		"tol_restosp_2":"TOLERANCIAS||RESTOS PEDICELO:1",
		"tol_blandos_3":"TOLERANCIAS||BLANDOS:2",
		"tol_cic_3":"TOLERANCIAS||CICATRIZ N2:2",
		"tol_def_3":"TOLERANCIAS||DEFORMES N2:2",
		"tol_desgarro2_2":"TOLERANCIAS||DESGARRO PEDICELAR N2:2",
		"tol_deshidratado2_2":"TOLERANCIAS||DESHIDRATADO N2:2",
		"tol_frutosr4_2":"TOLERANCIAS||FRUTOS ROJIZOS N4:2",
		"tol_polvo1_2":"TOLERANCIAS||POLVO N1:2",
		"tol_restosf2_2":"TOLERANCIAS||RESTOS FLORALES:2",
		"tol_restosp2_2":"TOLERANCIAS||RESTOS PEDICELO:2",
		"tol_blandos3_3":"TOLERANCIAS||BLANDOS:3",
		"tol_cic2_3":"TOLERANCIAS||CICATRIZ N2:3",
		"tol_def2_3":"TOLERANCIAS||DEFORMES N2:3",
		"tol_desgarro2_3":"TOLERANCIAS||DESGARRO PEDICELAR N2:3",
		"tol_deshidratado2_3":"TOLERANCIAS||DESHIDRATADO N2:3",
		"tol_frutosr4_3":"TOLERANCIAS||FRUTOS ROJIZOS N4:3",
		"tol_polvo1_3":"TOLERANCIAS||POLVO N1:3",
		"tol_restosf3_2":"TOLERANCIAS||RESTOS FLORALES:3",
		"tol_restosp3_2":"TOLERANCIAS||RESTOS PEDICELO:3",
		"tol_blandos4_3":"TOLERANCIAS||BLANDOS:4",
		"tol_cic2_4":"TOLERANCIAS||CICATRIZ N2:4",
		"tol_def2_4":"TOLERANCIAS||DEFORMES N2:4",
		"tol_desgarro2_4":"TOLERANCIAS||DESGARRO PEDICELAR N2:4",
		"tol_deshidratado2_4":"TOLERANCIAS||DESHIDRATADO N2:4",
		"tol_frutosr4_4":"TOLERANCIAS||FRUTOS ROJIZOS N4:4",
		"tol_polvo1_4":"TOLERANCIAS||POLVO N1:4",
		"tol_restosf4_2":"TOLERANCIAS||RESTOS FLORALES:4",
		"tol_restosp4_2":"TOLERANCIAS||RESTOS PEDICELO:4",
		"anexo_prioridad":"Priority",
		"observacion":"Observacion"
		}




class evcartilladrenadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcartilladrenadoform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
	class Meta:
		model = EvCartillaDrenado
		fields = [
			
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
		
		]

		labels={
			
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"PEP",
			
		}


class detalleevcartilladrenadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevcartilladrenadoform, self).__init__(*args, **kwargs)
		
		self.fields['valvula'].widget.attrs.update({"placeholder":"","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['volumen_drenado'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_1m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_1m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_1f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_1f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})


		self.fields['volumen_drenado_2i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_2i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_2m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_2m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_2f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_2f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})


		self.fields['volumen_drenado_3i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_3i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_3m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_3m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})

		self.fields['volumen_drenado_3f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['volumen_maceta_3f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})



		self.fields['pulso'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['ce'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_1m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_1f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_2i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_2m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_2f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_3i'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_3m'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ce_3f'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['observacion'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['longitud'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['latitud'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		
	class Meta:
		model = DetalleEvCartillaDrenado
		fields = [
			
			'valvula',
		
			
			'volumen_drenado',
			'volumen_maceta',
			'ce',
			
			'volumen_drenado_1m',
			'volumen_maceta_1m',
			'ce_1m',

			'volumen_drenado_1f',
			'volumen_maceta_1f',
			'ce_1f',

			'volumen_drenado_2i',
			'volumen_maceta_2i',
			'ce_2i',
			
			'volumen_drenado_2m',
			'volumen_maceta_2m',
			'ce_2m',

			'volumen_drenado_2f',
			'volumen_maceta_2f',
			'ce_2f',

			'volumen_drenado_3i',
			'volumen_maceta_3i',
			'ce_3i',

			'volumen_drenado_3m',
			'volumen_maceta_3m',
			'ce_3m',

			'volumen_drenado_3f',
			'volumen_maceta_3f',
			'ce_3f',

			'pulso',
						
		
			
			
			'observacion',
			'longitud',
			'latitud',
		]

		labels={
			
			"valvula":"Valvula",
			
			
			"volumen_drenado":"1I-Volumen Drenado(Ml)",
			"volumen_maceta":"1I-Volumen por Maceta(Ml)",
			"ce":"1I-CE Del Drenaje",

			"volumen_drenado_1m":"1M-Volumen Drenado(Ml)",
			"volumen_maceta_1m":"1M-Volumen por Maceta(Ml)",
			"ce_1m":"1M-CE Del Drenaje",

			"volumen_drenado_1f":"1F-Volumen Drenado(Ml)",
			"volumen_maceta_1f":"1F-Volumen por Maceta(Ml)",
			"ce_1f":"1F-CE Del Drenaje",

			"volumen_drenado_2i":"2I-Volumen Drenado(Ml)",
			"volumen_maceta_2i":"2I-Volumen por Maceta(Ml)",
			"ce_2i":"2I-CE Del Drenaje",

			"volumen_drenado_2m":"2M-Volumen Drenado(Ml)",
			"volumen_maceta_2m":"2M-Volumen por Maceta(Ml)",
			"ce_2m":"2M-CE Del Drenaje",

			"volumen_drenado_2f":"2F-Volumen Drenado(Ml)",
			"volumen_maceta_2f":"2F-Volumen por Maceta(Ml)",
			"ce_2f":"2F-CE Del Drenaje",

			"volumen_drenado_3i":"3I-Volumen Drenado(Ml)",
			"volumen_maceta_3i":"3I-Volumen por Maceta(Ml)",
			"ce_3i":"3I-CE Del Drenaje",

			"volumen_drenado_3m":"3M-Volumen Drenado(Ml)",
			"volumen_maceta_3m":"3M-Volumen por Maceta(Ml)",
			"ce_3m":"3M-CE Del Drenaje",

			"volumen_drenado_3f":"3F-Volumen Drenado(Ml)",
			"volumen_maceta_3f":"3F-Volumen por Maceta(Ml)",
			"ce_3f":"3F-CE Del Drenaje",

			"pulso":"Pulso",
			
		
			
			
			"observacion":"Observacion",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}


class seltrabajadorevcalpodaarform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(seltrabajadorevcalpodaarform, self).__init__(*args, **kwargs)
		
		self.fields['desc'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		
	class Meta:
		model = SelTrabajadorEvCalPodaAr
		fields = [
			
			'desc',
			'anexo_tipo',
		
		]

		labels={
			
			"desc":"Trabajador",
			"anexo_tipo":"Tipo Trabajador",
			
			
		}


class evcalpodaarform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalpodaarform, self).__init__(*args, **kwargs)
		self.fields['fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_trabajador']=forms.ModelChoiceField(label="Inspector", queryset=SelTrabajadorEvCalPodaAr.objects.filter(anexo_tipo=1))
		self.fields['anexo_trabajador'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})		
		
	class Meta:
		model = EvCalPodaAr
		fields = [
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'anexo_cultivo',
			'anexo_pep',
			'anexo_trabajador',
		]

		labels={
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_cultivo":"Cultivo",
			"anexo_pep":"PEP",
			"anexo_trabajador":"Trabajador",
		}


class detalleevcalpodaarform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablefundo=kwargs.pop("variable_fundo")
		super(detalleevcalpodaarform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_responsable']=forms.ModelChoiceField(label="Auxiliar", queryset=SelTrabajadorEvCalPodaAr.objects.filter(anexo_tipo=2))
		self.fields['anexo_responsable'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['valvula'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_valvula'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['anexo_tcalidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		#self.fields['anexo_produccion']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.get_by_fundo(variablefundo))
		self.fields['anexo_produccion'].widget.attrs.update({"placeholder":"..","data-required":"false","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul_id=2))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['anexo_distribucion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['num_ramas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['num_ramas_debajo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['num_ramas_encima'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['ramas_cruzados'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['ramas_daniocorte'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['ramas_delgados5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['ramas_flujo3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['num_ramas_5mm'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['num_ramas_16mm'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['corte_recto'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['altura_rama'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
		self.fields['anexo_preg1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_preg2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_preg3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_preg4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_preg5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['num_tirasavias'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
			
	class Meta:
		model = DetalleEvCalPodaAr
		fields = [
			'anexo_responsable',
			'dni',
			'valvula',
			'anexo_valvula',
			'anexo_tcalidad',
			'anexo_produccion',
			'anexo_variedad',
			'anexo_distribucion',
			'num_ramas',
			'num_ramas_5mm',
			'num_ramas_16mm',
			'num_ramas_debajo',
			'num_ramas_encima',
			'num_tirasavias',
			'ramas_cruzados',
			'ramas_daniocorte',
			'ramas_delgados5',
			'ramas_flujo3',
			'corte_recto',
			'altura_rama',
			'observacion',
			'anexo_preg1',
			'anexo_preg2',
			'anexo_preg3',
			'anexo_preg4',
			'anexo_preg5',
		]

		labels={
			"anexo_responsable":"Responsable",
			"dni":"DNI",
			"valvula":"Valvula",
			"anexo_valvula":"Selector Valvula",
			"anexo_tcalidad":"T Calidad",
			"anexo_produccion":"PEP",
			"anexo_variedad":"Variedad",
			"anexo_distribucion":"Categoria",
			"num_ramas":"Numero Ramas",
			"num_ramas_5mm":"Numero Ramas <5 mm",
			"num_ramas_16mm":"Numero Ramas >16 mm",
			"num_ramas_debajo":"Numero ramas debajo de altura indicada ",
			"num_ramas_encima":"Numero ramas encima de altura indicada",
			"num_tirasavias":"N° Tirasavias",
			"ramas_cruzados":"Ramas Cruzados",
			"ramas_daniocorte":"N° Ramas con Daño de Corte",
			"ramas_delgados5":"Nª Ramas Delgadas <5mm",
			"ramas_flujo3":"Nª Ramas con 3 Flujos",
			"corte_recto":"N° Ramas con Corte Recto",
			"altura_rama":"Altura Rama",
			"observacion":"Observacion",
			"anexo_preg1":"Macetas/4 Goteros",
			"anexo_preg2":"Estado de Herramientas",
			"anexo_preg3":"Desinfectado?",
			"anexo_preg4":"Estado de Guantes",
			"anexo_preg5":"Hojas en Maceta",
		}



class evcalmuestreocosechahg2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalmuestreocosechahg2021form, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"placeholder":"N° Planta","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Ancho","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		

		
	class Meta:
		model = EvCalMuestreoCosechaHg2021
		fields = [
			
			'fecha',
			
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			
	
			
		]

		labels={
#			
			"fecha":"Fecha",
			
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Pep",
			
		}




class detalleevcalmuestreocosechahg2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		variablefundo=kwargs.pop("variable_fundo")
		variableturno=kwargs.pop("variable_turno")
		super(detalleevcalmuestreocosechahg2021form, self).__init__(*args, **kwargs)
		
		self.fields['valvula'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=5))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['densidad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['reingreso'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_caseta'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['nfrutas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['inmaduro'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['sobremaduro'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['mal_corte'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['danio_mecanico'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['latex'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['excremento_ave'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['estadio_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['optimo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['fruta_suelo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_auxiliares']=forms.ModelChoiceField(label="Auxiliares Campo", queryset=AuxiliaresCampoAthos.objects.filter(anexo_fundo=variablefundo))
		self.fields['anexo_auxiliares'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		self.fields['exportable'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
		self.fields['longitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		
	class Meta:
		model = DetalleEvCalMuestreoCosechaHg2021
		fields = [
			'valvula',
			'anexo_variedad',
			'dni',
			'densidad',
			'reingreso',
			'anexo_caseta',
			'anexo_tipo',
			'nfrutas',
			'inmaduro',
			'sobremaduro',
			'mal_corte',
			'danio_mecanico',
			'latex',
			'excremento_ave',
			'estadio_2',
			'optimo',
			'fruta_suelo',
			'anexo_auxiliares',
			'longitud',
			'latitud',
			'exportable',
		]

		labels={
			"valvula":"Sector",
			"anexo_variedad":"Variedad",
			"dni":"Dni",
			"densidad":"Densidad",
			"reingreso":"Reingreso",
			"anexo_caseta":"Caseta",
			"anexo_tipo":"Tipo",
			"nfrutas":"N° Frutas",
			"inmaduro":"Inmaduro",
			"sobremaduro":"Sobremaduro",
			"mal_corte":"Mal Corte",
			"danio_mecanico":"Daño Mecanico",
			"latex":"Latex",
			"excremento_ave":"Excremento de Ave",
			"estadio_2":"Estadio 3",
			"optimo":"Optimo",
			"fruta_suelo":"Fruta en el Suelo",
			"anexo_auxiliares":"Auxiliares",
			"longitud":"Longitud",
			"latitud":"Latitud",
			
			"exportable":"Exportable",
		}


class evcalmuestreoplantahgica2021form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(evcalmuestreoplantahgica2021form, self).__init__(*args, **kwargs)
        
        self.fields['fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_zona'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['ubicacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['nro_guia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=5))
        self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['fecha_cosecha'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['njabas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['peso_planta'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['peso_promedio'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['hora_ingreso'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['hora_inicio'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['temperatura_pulpa'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['peso_muestra'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        
    class Meta:
        model = EvCalMuestreoPlantaHgIca2021
        fields = [
            
            'fecha',
            'anexo_zona',
            'anexo_fundo',
            'ubicacion',
            'nro_guia',
            'anexo_variedad',
            'fecha_cosecha',
            'njabas',
            'peso_planta',
            'peso_promedio',
            'hora_ingreso',
            'hora_inicio',
            'temperatura_pulpa',
            'peso_muestra',
            
        ]

        labels={
#            
            "fecha":"Fecha",
            "anexo_zona":"Zona",
            "anexo_fundo":"Fundo",
            "ubicacion":"Pep",
            
            "nro_guia":"Nro Guia",
            "anexo_variedad":"Variedad",
            "fecha_cosecha":"Fecha Cosecha",
            "njabas":"Nro Jabas",


            "peso_planta":"Peso Planta",
            "peso_promedio":"Peso Promedio",
            "hora_ingreso":"Hora Ingreso",
            "hora_inicio":"Hora Inicio",


            "temperatura_pulpa":"Temperatura Pulpa",
            "peso_muestra":"Peso Muestra",
        
        }
class evcalmuestreoplantahgnep2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evcalmuestreoplantahgnep2022form, self).__init__(*args, **kwargs)
        
		self.fields['fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['nro_ticket'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['temperatura_pulpa'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['peso_muestra'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['exportable11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pudricion11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['micelio11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pasmado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['sobremaduro11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_latex11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['ostiolo_abierto11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_mecanico11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pedunculo_malcortado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['agrietado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['deshidratado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['bajo_calibre11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['deformes11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['cicatriz11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['manchas11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['inmadurez_verde11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['excremento_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['picado_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_trips11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_queresa11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_aranita11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_mosca11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['sst_estadio2_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio2_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio2_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['sst_estadio3_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio3_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio3_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['sst_estadio4_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio4_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['sst_estadio4_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['firmeza_estadio2_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_8'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_9'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio2_10'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['firmeza_estadio3_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_8'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_9'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio3_10'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['firmeza_estadio4_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_8'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_9'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['firmeza_estadio4_10'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['longitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        
	class Meta:
		model = EvCalMuestreoPlantaHgNep202202
		fields = [
			'fecha',
			'anexo_planta',
			'nro_ticket',
			'temperatura_pulpa',
			'peso_muestra',

			'exportable11',
			'exportable13',
			'exportable15',
			'exportable18',
			'exportable20',
			'exportable24',
			'exportable27',
			'exportable30',
            
			'pudricion11',
			'pudricion13',
			'pudricion15',
			'pudricion18',
			'pudricion20',
			'pudricion24',
			'pudricion27',
			'pudricion30',

			'micelio11',
			'micelio13',
			'micelio15',
			'micelio18',
			'micelio20',
			'micelio24',
			'micelio27',
			'micelio30',

			'pasmado11',
			'pasmado13',
			'pasmado15',
			'pasmado18',
			'pasmado20',
			'pasmado24',
			'pasmado27',
			'pasmado30',

			'sobremaduro11',
			'sobremaduro13',
			'sobremaduro15',
			'sobremaduro18',
			'sobremaduro20',
			'sobremaduro24',
			'sobremaduro27',
			'sobremaduro30',

			'danio_latex11',
			'danio_latex13',
			'danio_latex15',
			'danio_latex18',
			'danio_latex20',
			'danio_latex24',
			'danio_latex27',
			'danio_latex30',

			'ostiolo_abierto11',
			'ostiolo_abierto13',
			'ostiolo_abierto15',
			'ostiolo_abierto18',
			'ostiolo_abierto20',
			'ostiolo_abierto24',
			'ostiolo_abierto27',
			'ostiolo_abierto30',

			'danio_mecanico11',
			'danio_mecanico13',
			'danio_mecanico15',
			'danio_mecanico18',
			'danio_mecanico20',
			'danio_mecanico24',
			'danio_mecanico27',
			'danio_mecanico30',

			'pedunculo_malcortado11',
			'pedunculo_malcortado13',
			'pedunculo_malcortado15',
			'pedunculo_malcortado18',
			'pedunculo_malcortado20',
			'pedunculo_malcortado24',
			'pedunculo_malcortado27',
			'pedunculo_malcortado30',

			'agrietado11',
			'agrietado13',
			'agrietado15',
			'agrietado18',
			'agrietado20',
			'agrietado24',
			'agrietado27',
			'agrietado30',

			'deshidratado11',
			'deshidratado13',
			'deshidratado15',
			'deshidratado18',
			'deshidratado20',
			'deshidratado24',
			'deshidratado27',
			'deshidratado30',

			'bajo_calibre11',
			'bajo_calibre13',
			'bajo_calibre15',
			'bajo_calibre18',
			'bajo_calibre20',
			'bajo_calibre24',
			'bajo_calibre27',
			'bajo_calibre30',

			'deformes11',
			'deformes13',
			'deformes15',
			'deformes18',
			'deformes20',
			'deformes24',
			'deformes27',
			'deformes30',

			'cicatriz11',
			'cicatriz13',
			'cicatriz15',
			'cicatriz18',
			'cicatriz20',
			'cicatriz24',
			'cicatriz27',
			'cicatriz30',

			'manchas11',
			'manchas13',
			'manchas15',
			'manchas18',
			'manchas20',
			'manchas24',
			'manchas27',
			'manchas30',

			'inmadurez_verde11',
			'inmadurez_verde13',
			'inmadurez_verde15',
			'inmadurez_verde18',
			'inmadurez_verde20',
			'inmadurez_verde24',
			'inmadurez_verde27',
			'inmadurez_verde30',

			'excremento_ave11',
			'excremento_ave13',
			'excremento_ave15',
			'excremento_ave18',
			'excremento_ave20',
			'excremento_ave24',
			'excremento_ave27',
			'excremento_ave30',

			'picado_ave11',
			'picado_ave13',
			'picado_ave15',
			'picado_ave18',
			'picado_ave20',
			'picado_ave24',
			'picado_ave27',
			'picado_ave30',

			'danio_trips11',
			'danio_trips13',
			'danio_trips15',
			'danio_trips18',
			'danio_trips20',
			'danio_trips24',
			'danio_trips27',
			'danio_trips30',

			'danio_queresa11',
			'danio_queresa13',
			'danio_queresa15',
			'danio_queresa18',
			'danio_queresa20',
			'danio_queresa24',
			'danio_queresa27',
			'danio_queresa30',

			'danio_aranita11',
			'danio_aranita13',
			'danio_aranita15',
			'danio_aranita18',
			'danio_aranita20',
			'danio_aranita24',
			'danio_aranita27',
			'danio_aranita30',

			'danio_mosca11',
			'danio_mosca13',
			'danio_mosca15',
			'danio_mosca18',
			'danio_mosca20',
			'danio_mosca24',
			'danio_mosca27',
			'danio_mosca30',

			'sst_estadio2_1',
			'sst_estadio2_2',
			'sst_estadio2_3',

			'sst_estadio3_1',
			'sst_estadio3_2',
			'sst_estadio3_3',

			'sst_estadio4_1',
			'sst_estadio4_2',
			'sst_estadio4_3',

			'firmeza_estadio2_1',
			'firmeza_estadio2_2',
			'firmeza_estadio2_3',
			'firmeza_estadio2_4',
			'firmeza_estadio2_5',
			'firmeza_estadio2_6',
			'firmeza_estadio2_7',
			'firmeza_estadio2_8',
			'firmeza_estadio2_9',
			'firmeza_estadio2_10',

			'firmeza_estadio3_1',
			'firmeza_estadio3_2',
			'firmeza_estadio3_3',
			'firmeza_estadio3_4',
			'firmeza_estadio3_5',
			'firmeza_estadio3_6',
			'firmeza_estadio3_7',
			'firmeza_estadio3_8',
			'firmeza_estadio3_9',
			'firmeza_estadio3_10',

			'firmeza_estadio4_1',
			'firmeza_estadio4_2',
			'firmeza_estadio4_3',
			'firmeza_estadio4_4',
			'firmeza_estadio4_5',
			'firmeza_estadio4_6',
			'firmeza_estadio4_7',
			'firmeza_estadio4_8',
			'firmeza_estadio4_9',
			'firmeza_estadio4_10',

			'longitud',
			'latitud',
		]

		labels={
			"fecha":"Fecha",
			"anexo_planta":"Planta",
			"nro_ticket":"Nro Ticket",
			"temperatura_pulpa":"Temperatura Pulpa",
			"peso_muestra":"Peso Muestra",

			"exportable11":"Exportable 11",
			"exportable13":"Exportable 13",
			"exportable15":"Exportable 15",
			"exportable18":"Exportable 18",
			"exportable20":"Exportable 20",
			"exportable24":"Exportable 24",
			"exportable27":"Exportable 27",
			"exportable30":"Exportable 30",
            
			"pudricion11":"Pudricion 11",
			"pudricion13":"Pudricion 13",
			"pudricion15":"Pudricion 15",
			"pudricion18":"Pudricion 18",
			"pudricion20":"Pudricion 20",
			"pudricion24":"Pudricion 24",
			"pudricion27":"Pudricion 27",
			"pudricion30":"Pudricion 30",

			"micelio11":"Micelio 11",
			"micelio13":"Micelio 13",
			"micelio15":"Micelio 15",
			"micelio18":"Micelio 18",
			"micelio20":"Micelio 20",
			"micelio24":"Micelio 24",
			"micelio27":"Micelio 27",
			"micelio30":"Micelio 30",

			"pasmado11":"Pasmado 11",
			"pasmado13":"Pasmado 13",
			"pasmado15":"Pasmado 15",
			"pasmado18":"Pasmado 18",
			"pasmado20":"Pasmado 20",
			"pasmado24":"Pasmado 24",
			"pasmado27":"Pasmado 27",
			"pasmado30":"Pasmado 30",

			"sobremaduro11":"Sobremaduro 11",
			"sobremaduro13":"Sobremaduro 13",
			"sobremaduro15":"Sobremaduro 15",
			"sobremaduro18":"Sobremaduro 18",
			"sobremaduro20":"Sobremaduro 20",
			"sobremaduro24":"Sobremaduro 24",
			"sobremaduro27":"Sobremaduro 27",
			"sobremaduro30":"Sobremaduro 30",

			"danio_latex11":"Daño Latex 11",
			"danio_latex13":"Daño Latex 13",
			"danio_latex15":"Daño Latex 15",
			"danio_latex18":"Daño Latex 18",
			"danio_latex20":"Daño Latex 20",
			"danio_latex24":"Daño Latex 24",
			"danio_latex27":"Daño Latex 27",
			"danio_latex30":"Daño Latex 30",

			"ostiolo_abierto11":"Ostiolo Abierto 11",
			"ostiolo_abierto13":"Ostiolo Abierto 13",
			"ostiolo_abierto15":"Ostiolo Abierto 15",
			"ostiolo_abierto18":"Ostiolo Abierto 18",
			"ostiolo_abierto20":"Ostiolo Abierto 20",
			"ostiolo_abierto24":"Ostiolo Abierto 24",
			"ostiolo_abierto27":"Ostiolo Abierto 27",
			"ostiolo_abierto30":"Ostiolo Abierto 30",

			"danio_mecanico11":"Daño Mecanico 11",
			"danio_mecanico13":"Daño Mecanico 13",
			"danio_mecanico15":"Daño Mecanico 15",
			"danio_mecanico18":"Daño Mecanico 18",
			"danio_mecanico20":"Daño Mecanico 20",
			"danio_mecanico24":"Daño Mecanico 24",
			"danio_mecanico27":"Daño Mecanico 27",
			"danio_mecanico30":"Daño Mecanico 30",

			"pedunculo_malcortado11":"Pedunculo Malcortado 11",
			"pedunculo_malcortado13":"Pedunculo Malcortado 13",
			"pedunculo_malcortado15":"Pedunculo Malcortado 15",
			"pedunculo_malcortado18":"Pedunculo Malcortado 18",
			"pedunculo_malcortado20":"Pedunculo Malcortado 20",
			"pedunculo_malcortado24":"Pedunculo Malcortado 24",
			"pedunculo_malcortado27":"Pedunculo Malcortado 27",
			"pedunculo_malcortado30":"Pedunculo Malcortado 30",

			"agrietado11":"Agrietado 11",
			"agrietado13":"Agrietado 13",
			"agrietado15":"Agrietado 15",
			"agrietado18":"Agrietado 18",
			"agrietado20":"Agrietado 20",
			"agrietado24":"Agrietado 24",
			"agrietado27":"Agrietado 27",
			"agrietado30":"Agrietado 30",

			"deshidratado11":"Deshidratado 11",
			"deshidratado13":"Deshidratado 13",
			"deshidratado15":"Deshidratado 15",
			"deshidratado18":"Deshidratado 18",
			"deshidratado20":"Deshidratado 20",
			"deshidratado24":"Deshidratado 24",
			"deshidratado27":"Deshidratado 27",
			"deshidratado30":"Deshidratado 30",

			"bajo_calibre11":"Bajo Calibre 11",
			"bajo_calibre13":"Bajo Calibre 13",
			"bajo_calibre15":"Bajo Calibre 15",
			"bajo_calibre18":"Bajo Calibre 18",
			"bajo_calibre20":"Bajo Calibre 20",
			"bajo_calibre24":"Bajo Calibre 24",
			"bajo_calibre27":"Bajo Calibre 27",
			"bajo_calibre30":"Bajo Calibre 30",

			"deformes11":"Deformes 11",
			"deformes13":"Deformes 13",
			"deformes15":"Deformes 15",
			"deformes18":"Deformes 18",
			"deformes20":"Deformes 20",
			"deformes24":"Deformes 24",
			"deformes27":"Deformes 27",
			"deformes30":"Deformes 30",

			"cicatriz11":"Cicatriz 11",
			"cicatriz13":"Cicatriz 13",
			"cicatriz15":"Cicatriz 15",
			"cicatriz18":"Cicatriz 18",
			"cicatriz20":"Cicatriz 20",
			"cicatriz24":"Cicatriz 24",
			"cicatriz27":"Cicatriz 27",
			"cicatriz30":"Cicatriz 30",

			"manchas11":"Manchas 11",
			"manchas13":"Manchas 13",
			"manchas15":"Manchas 15",
			"manchas18":"Manchas 18",
			"manchas20":"Manchas 20",
			"manchas24":"Manchas 24",
			"manchas27":"Manchas 27",
			"manchas30":"Manchas 30",

			"inmadurez_verde11":"Inmadurez Verde 11",
			"inmadurez_verde13":"Inmadurez Verde 13",
			"inmadurez_verde15":"Inmadurez Verde 15",
			"inmadurez_verde18":"Inmadurez Verde 18",
			"inmadurez_verde20":"Inmadurez Verde 20",
			"inmadurez_verde24":"Inmadurez Verde 24",
			"inmadurez_verde27":"Inmadurez Verde 27",
			"inmadurez_verde30":"Inmadurez Verde 30",

			"excremento_ave11":"Excremento Ave 11",
			"excremento_ave13":"Excremento Ave 13",
			"excremento_ave15":"Excremento Ave 15",
			"excremento_ave18":"Excremento Ave 18",
			"excremento_ave20":"Excremento Ave 20",
			"excremento_ave24":"Excremento Ave 24",
			"excremento_ave27":"Excremento Ave 27",
			"excremento_ave30":"Excremento Ave 30",

			"picado_ave11":"Picado Ave 11",
			"picado_ave13":"Picado Ave 13",
			"picado_ave15":"Picado Ave 15",
			"picado_ave18":"Picado Ave 18",
			"picado_ave20":"Picado Ave 20",
			"picado_ave24":"Picado Ave 24",
			"picado_ave27":"Picado Ave 27",
			"picado_ave30":"Picado Ave 30",

			"danio_trips11":"Daño por Trips 11",
			"danio_trips13":"Daño por Trips 13",
			"danio_trips15":"Daño por Trips 15",
			"danio_trips18":"Daño por Trips 18",
			"danio_trips20":"Daño por Trips 20",
			"danio_trips24":"Daño por Trips 24",
			"danio_trips27":"Daño por Trips 27",
			"danio_trips30":"Daño por Trips 30",

			"danio_queresa11":"Daño Queresa 11",
			"danio_queresa13":"Daño Queresa 13",
			"danio_queresa15":"Daño Queresa 15",
			"danio_queresa18":"Daño Queresa 18",
			"danio_queresa20":"Daño Queresa 20",
			"danio_queresa24":"Daño Queresa 24",
			"danio_queresa27":"Daño Queresa 27",
			"danio_queresa30":"Daño Queresa 30",

			"danio_aranita11":"Daño Arañita 11",
			"danio_aranita13":"Daño Arañita 13",
			"danio_aranita15":"Daño Arañita 15",
			"danio_aranita18":"Daño Arañita 18",
			"danio_aranita20":"Daño Arañita 20",
			"danio_aranita24":"Daño Arañita 24",
			"danio_aranita27":"Daño Arañita 27",
			"danio_aranita30":"Daño Arañita 30",

			"danio_mosca11":"Daño Mosca 11",
			"danio_mosca13":"Daño Mosca 13",
			"danio_mosca15":"Daño Mosca 15",
			"danio_mosca18":"Daño Mosca 18",
			"danio_mosca20":"Daño Mosca 20",
			"danio_mosca24":"Daño Mosca 24",
			"danio_mosca27":"Daño Mosca 27",
			"danio_mosca30":"Daño Mosca 30",

			"sst_estadio2_1":"SST:ESTADIO 2_M1",
			"sst_estadio2_2":"SST:ESTADIO 2_M2",
			"sst_estadio2_3":"SST:ESTADIO 2_M3",

			"sst_estadio3_1":"SST:ESTADIO 3_M1",
			"sst_estadio3_2":"SST:ESTADIO 3_M2",
			"sst_estadio3_3":"SST:ESTADIO 3_M3",

			"sst_estadio4_1":"SST:ESTADIO 4_M1",
			"sst_estadio4_2":"SST:ESTADIO 4_M2",
			"sst_estadio4_3":"SST:ESTADIO 4_M3",

			"firmeza_estadio2_1":"FIRMEZA:ESTADIO 2_M1",
			"firmeza_estadio2_2":"FIRMEZA:ESTADIO 2_M2",
			"firmeza_estadio2_3":"FIRMEZA:ESTADIO 2_M3",
			"firmeza_estadio2_4":"FIRMEZA:ESTADIO 2_M4",
			"firmeza_estadio2_5":"FIRMEZA:ESTADIO 2_M5",
			"firmeza_estadio2_6":"FIRMEZA:ESTADIO 2_M6",
			"firmeza_estadio2_7":"FIRMEZA:ESTADIO 2_M7",
			"firmeza_estadio2_8":"FIRMEZA:ESTADIO 2_M8",
			"firmeza_estadio2_9":"FIRMEZA:ESTADIO 2_M9",
			"firmeza_estadio2_10":"FIRMEZA:ESTADIO 2_M10",

			"firmeza_estadio3_1":"FIRMEZA:ESTADIO 3_M1",
			"firmeza_estadio3_2":"FIRMEZA:ESTADIO 3_M2",
			"firmeza_estadio3_3":"FIRMEZA:ESTADIO 3_M3",
			"firmeza_estadio3_4":"FIRMEZA:ESTADIO 3_M4",
			"firmeza_estadio3_5":"FIRMEZA:ESTADIO 3_M5",
			"firmeza_estadio3_6":"FIRMEZA:ESTADIO 3_M6",
			"firmeza_estadio3_7":"FIRMEZA:ESTADIO 3_M7",
			"firmeza_estadio3_8":"FIRMEZA:ESTADIO 3_M8",
			"firmeza_estadio3_9":"FIRMEZA:ESTADIO 3_M9",
			"firmeza_estadio3_10":"FIRMEZA:ESTADIO 3_M10",

			"firmeza_estadio4_1":"FIRMEZA:ESTADIO 4_M1",
			"firmeza_estadio4_2":"FIRMEZA:ESTADIO 4_M2",
			"firmeza_estadio4_3":"FIRMEZA:ESTADIO 4_M3",
			"firmeza_estadio4_4":"FIRMEZA:ESTADIO 4_M4",
			"firmeza_estadio4_5":"FIRMEZA:ESTADIO 4_M5",
			"firmeza_estadio4_6":"FIRMEZA:ESTADIO 4_M6",
			"firmeza_estadio4_7":"FIRMEZA:ESTADIO 4_M7",
			"firmeza_estadio4_8":"FIRMEZA:ESTADIO 4_M8",
			"firmeza_estadio4_9":"FIRMEZA:ESTADIO 4_M9",
			"firmeza_estadio4_10":"FIRMEZA:ESTADIO 4_M10",

			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class evcalmuestreoplantahgica2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evcalmuestreoplantahgica2022form, self).__init__(*args, **kwargs)
        
		self.fields['fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['nro_ticket'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['temperatura_pulpa'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['peso_muestra'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['exportable11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['exportable30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pudricion11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pudricion30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['micelio11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['micelio30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pasmado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pasmado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['sobremaduro11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['sobremaduro30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_latex11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_latex30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['ostiolo_abierto11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['ostiolo_abierto30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_mecanico11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mecanico30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['pedunculo_malcortado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['pedunculo_malcortado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['agrietado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['agrietado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['deshidratado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deshidratado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['bajo_calibre11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['bajo_calibre30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['deformes11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['deformes30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['cicatriz11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['cicatriz30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['manchas11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['manchas30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['inmadurez_verde11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['inmadurez_verde30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['excremento_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['excremento_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['picado_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['picado_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_trips11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_trips30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_queresa11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_queresa30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_aranita11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_aranita30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['danio_mosca11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['danio_mosca30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})

		self.fields['anexo_estadio_brix1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['brix1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estadio_brix2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['brix2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estadio_brix3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['brix3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_firmeza1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['valor_firmeza1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_firmeza2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['valor_firmeza2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_firmeza3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['valor_firmeza3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

		self.fields['longitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        
	class Meta:
		model = EvCalMuestreoPlantaHgIca2022
		fields = [
			'fecha',
			'nro_ticket',
			'temperatura_pulpa',
			'peso_muestra',

			'exportable11',
			'exportable13',
			'exportable15',
			'exportable18',
			'exportable20',
			'exportable24',
			'exportable27',
			'exportable30',
            
			'pudricion11',
			'pudricion13',
			'pudricion15',
			'pudricion18',
			'pudricion20',
			'pudricion24',
			'pudricion27',
			'pudricion30',

			'micelio11',
			'micelio13',
			'micelio15',
			'micelio18',
			'micelio20',
			'micelio24',
			'micelio27',
			'micelio30',

			'pasmado11',
			'pasmado13',
			'pasmado15',
			'pasmado18',
			'pasmado20',
			'pasmado24',
			'pasmado27',
			'pasmado30',

			'sobremaduro11',
			'sobremaduro13',
			'sobremaduro15',
			'sobremaduro18',
			'sobremaduro20',
			'sobremaduro24',
			'sobremaduro27',
			'sobremaduro30',

			'danio_latex11',
			'danio_latex13',
			'danio_latex15',
			'danio_latex18',
			'danio_latex20',
			'danio_latex24',
			'danio_latex27',
			'danio_latex30',

			'ostiolo_abierto11',
			'ostiolo_abierto13',
			'ostiolo_abierto15',
			'ostiolo_abierto18',
			'ostiolo_abierto20',
			'ostiolo_abierto24',
			'ostiolo_abierto27',
			'ostiolo_abierto30',

			'danio_mecanico11',
			'danio_mecanico13',
			'danio_mecanico15',
			'danio_mecanico18',
			'danio_mecanico20',
			'danio_mecanico24',
			'danio_mecanico27',
			'danio_mecanico30',

			'pedunculo_malcortado11',
			'pedunculo_malcortado13',
			'pedunculo_malcortado15',
			'pedunculo_malcortado18',
			'pedunculo_malcortado20',
			'pedunculo_malcortado24',
			'pedunculo_malcortado27',
			'pedunculo_malcortado30',

			'agrietado11',
			'agrietado13',
			'agrietado15',
			'agrietado18',
			'agrietado20',
			'agrietado24',
			'agrietado27',
			'agrietado30',

			'deshidratado11',
			'deshidratado13',
			'deshidratado15',
			'deshidratado18',
			'deshidratado20',
			'deshidratado24',
			'deshidratado27',
			'deshidratado30',

			'bajo_calibre11',
			'bajo_calibre13',
			'bajo_calibre15',
			'bajo_calibre18',
			'bajo_calibre20',
			'bajo_calibre24',
			'bajo_calibre27',
			'bajo_calibre30',

			'deformes11',
			'deformes13',
			'deformes15',
			'deformes18',
			'deformes20',
			'deformes24',
			'deformes27',
			'deformes30',

			'cicatriz11',
			'cicatriz13',
			'cicatriz15',
			'cicatriz18',
			'cicatriz20',
			'cicatriz24',
			'cicatriz27',
			'cicatriz30',

			'manchas11',
			'manchas13',
			'manchas15',
			'manchas18',
			'manchas20',
			'manchas24',
			'manchas27',
			'manchas30',

			'inmadurez_verde11',
			'inmadurez_verde13',
			'inmadurez_verde15',
			'inmadurez_verde18',
			'inmadurez_verde20',
			'inmadurez_verde24',
			'inmadurez_verde27',
			'inmadurez_verde30',

			'excremento_ave11',
			'excremento_ave13',
			'excremento_ave15',
			'excremento_ave18',
			'excremento_ave20',
			'excremento_ave24',
			'excremento_ave27',
			'excremento_ave30',

			'picado_ave11',
			'picado_ave13',
			'picado_ave15',
			'picado_ave18',
			'picado_ave20',
			'picado_ave24',
			'picado_ave27',
			'picado_ave30',

			'danio_trips11',
			'danio_trips13',
			'danio_trips15',
			'danio_trips18',
			'danio_trips20',
			'danio_trips24',
			'danio_trips27',
			'danio_trips30',

			'danio_queresa11',
			'danio_queresa13',
			'danio_queresa15',
			'danio_queresa18',
			'danio_queresa20',
			'danio_queresa24',
			'danio_queresa27',
			'danio_queresa30',

			'danio_aranita11',
			'danio_aranita13',
			'danio_aranita15',
			'danio_aranita18',
			'danio_aranita20',
			'danio_aranita24',
			'danio_aranita27',
			'danio_aranita30',

			'danio_mosca11',
			'danio_mosca13',
			'danio_mosca15',
			'danio_mosca18',
			'danio_mosca20',
			'danio_mosca24',
			'danio_mosca27',
			'danio_mosca30',

			'anexo_estadio_brix1',
            'brix1',
            'anexo_estadio_brix2',
            'brix2',
            'anexo_estadio_brix3',
            'brix3',
          
            'anexo_firmeza1',
            'valor_firmeza1',
            'anexo_firmeza2',
            'valor_firmeza2',
            'anexo_firmeza3',
            'valor_firmeza3',

			'longitud',
			'latitud',
		]

		labels={
			"fecha":"Fecha",
			"nro_ticket":"Nro Ticket",
			"temperatura_pulpa":"Temperatura Pulpa",
			"peso_muestra":"Peso Muestra",

			"exportable11":"Exportable 11",
			"exportable13":"Exportable 13",
			"exportable15":"Exportable 15",
			"exportable18":"Exportable 18",
			"exportable20":"Exportable 20",
			"exportable24":"Exportable 24",
			"exportable27":"Exportable 27",
			"exportable30":"Exportable 30",
            
			"pudricion11":"Pudricion 11",
			"pudricion13":"Pudricion 13",
			"pudricion15":"Pudricion 15",
			"pudricion18":"Pudricion 18",
			"pudricion20":"Pudricion 20",
			"pudricion24":"Pudricion 24",
			"pudricion27":"Pudricion 27",
			"pudricion30":"Pudricion 30",

			"micelio11":"Micelio 11",
			"micelio13":"Micelio 13",
			"micelio15":"Micelio 15",
			"micelio18":"Micelio 18",
			"micelio20":"Micelio 20",
			"micelio24":"Micelio 24",
			"micelio27":"Micelio 27",
			"micelio30":"Micelio 30",

			"pasmado11":"Pasmado 11",
			"pasmado13":"Pasmado 13",
			"pasmado15":"Pasmado 15",
			"pasmado18":"Pasmado 18",
			"pasmado20":"Pasmado 20",
			"pasmado24":"Pasmado 24",
			"pasmado27":"Pasmado 27",
			"pasmado30":"Pasmado 30",

			"sobremaduro11":"Sobremaduro 11",
			"sobremaduro13":"Sobremaduro 13",
			"sobremaduro15":"Sobremaduro 15",
			"sobremaduro18":"Sobremaduro 18",
			"sobremaduro20":"Sobremaduro 20",
			"sobremaduro24":"Sobremaduro 24",
			"sobremaduro27":"Sobremaduro 27",
			"sobremaduro30":"Sobremaduro 30",

			"danio_latex11":"Daño Latex 11",
			"danio_latex13":"Daño Latex 13",
			"danio_latex15":"Daño Latex 15",
			"danio_latex18":"Daño Latex 18",
			"danio_latex20":"Daño Latex 20",
			"danio_latex24":"Daño Latex 24",
			"danio_latex27":"Daño Latex 27",
			"danio_latex30":"Daño Latex 30",

			"ostiolo_abierto11":"Ostiolo Abierto 11",
			"ostiolo_abierto13":"Ostiolo Abierto 13",
			"ostiolo_abierto15":"Ostiolo Abierto 15",
			"ostiolo_abierto18":"Ostiolo Abierto 18",
			"ostiolo_abierto20":"Ostiolo Abierto 20",
			"ostiolo_abierto24":"Ostiolo Abierto 24",
			"ostiolo_abierto27":"Ostiolo Abierto 27",
			"ostiolo_abierto30":"Ostiolo Abierto 30",

			"danio_mecanico11":"Daño Mecanico 11",
			"danio_mecanico13":"Daño Mecanico 13",
			"danio_mecanico15":"Daño Mecanico 15",
			"danio_mecanico18":"Daño Mecanico 18",
			"danio_mecanico20":"Daño Mecanico 20",
			"danio_mecanico24":"Daño Mecanico 24",
			"danio_mecanico27":"Daño Mecanico 27",
			"danio_mecanico30":"Daño Mecanico 30",

			"pedunculo_malcortado11":"Pedunculo Malcortado 11",
			"pedunculo_malcortado13":"Pedunculo Malcortado 13",
			"pedunculo_malcortado15":"Pedunculo Malcortado 15",
			"pedunculo_malcortado18":"Pedunculo Malcortado 18",
			"pedunculo_malcortado20":"Pedunculo Malcortado 20",
			"pedunculo_malcortado24":"Pedunculo Malcortado 24",
			"pedunculo_malcortado27":"Pedunculo Malcortado 27",
			"pedunculo_malcortado30":"Pedunculo Malcortado 30",

			"agrietado11":"Agrietado 11",
			"agrietado13":"Agrietado 13",
			"agrietado15":"Agrietado 15",
			"agrietado18":"Agrietado 18",
			"agrietado20":"Agrietado 20",
			"agrietado24":"Agrietado 24",
			"agrietado27":"Agrietado 27",
			"agrietado30":"Agrietado 30",

			"deshidratado11":"Deshidratado 11",
			"deshidratado13":"Deshidratado 13",
			"deshidratado15":"Deshidratado 15",
			"deshidratado18":"Deshidratado 18",
			"deshidratado20":"Deshidratado 20",
			"deshidratado24":"Deshidratado 24",
			"deshidratado27":"Deshidratado 27",
			"deshidratado30":"Deshidratado 30",

			"bajo_calibre11":"Bajo Calibre 11",
			"bajo_calibre13":"Bajo Calibre 13",
			"bajo_calibre15":"Bajo Calibre 15",
			"bajo_calibre18":"Bajo Calibre 18",
			"bajo_calibre20":"Bajo Calibre 20",
			"bajo_calibre24":"Bajo Calibre 24",
			"bajo_calibre27":"Bajo Calibre 27",
			"bajo_calibre30":"Bajo Calibre 30",

			"deformes11":"Deformes 11",
			"deformes13":"Deformes 13",
			"deformes15":"Deformes 15",
			"deformes18":"Deformes 18",
			"deformes20":"Deformes 20",
			"deformes24":"Deformes 24",
			"deformes27":"Deformes 27",
			"deformes30":"Deformes 30",

			"cicatriz11":"Cicatriz 11",
			"cicatriz13":"Cicatriz 13",
			"cicatriz15":"Cicatriz 15",
			"cicatriz18":"Cicatriz 18",
			"cicatriz20":"Cicatriz 20",
			"cicatriz24":"Cicatriz 24",
			"cicatriz27":"Cicatriz 27",
			"cicatriz30":"Cicatriz 30",

			"manchas11":"Manchas 11",
			"manchas13":"Manchas 13",
			"manchas15":"Manchas 15",
			"manchas18":"Manchas 18",
			"manchas20":"Manchas 20",
			"manchas24":"Manchas 24",
			"manchas27":"Manchas 27",
			"manchas30":"Manchas 30",

			"inmadurez_verde11":"Inmadurez Verde 11",
			"inmadurez_verde13":"Inmadurez Verde 13",
			"inmadurez_verde15":"Inmadurez Verde 15",
			"inmadurez_verde18":"Inmadurez Verde 18",
			"inmadurez_verde20":"Inmadurez Verde 20",
			"inmadurez_verde24":"Inmadurez Verde 24",
			"inmadurez_verde27":"Inmadurez Verde 27",
			"inmadurez_verde30":"Inmadurez Verde 30",

			"excremento_ave11":"Excremento Ave 11",
			"excremento_ave13":"Excremento Ave 13",
			"excremento_ave15":"Excremento Ave 15",
			"excremento_ave18":"Excremento Ave 18",
			"excremento_ave20":"Excremento Ave 20",
			"excremento_ave24":"Excremento Ave 24",
			"excremento_ave27":"Excremento Ave 27",
			"excremento_ave30":"Excremento Ave 30",

			"picado_ave11":"Picado Ave 11",
			"picado_ave13":"Picado Ave 13",
			"picado_ave15":"Picado Ave 15",
			"picado_ave18":"Picado Ave 18",
			"picado_ave20":"Picado Ave 20",
			"picado_ave24":"Picado Ave 24",
			"picado_ave27":"Picado Ave 27",
			"picado_ave30":"Picado Ave 30",

			"danio_trips11":"Daño por Trips 11",
			"danio_trips13":"Daño por Trips 13",
			"danio_trips15":"Daño por Trips 15",
			"danio_trips18":"Daño por Trips 18",
			"danio_trips20":"Daño por Trips 20",
			"danio_trips24":"Daño por Trips 24",
			"danio_trips27":"Daño por Trips 27",
			"danio_trips30":"Daño por Trips 30",

			"danio_queresa11":"Daño Queresa 11",
			"danio_queresa13":"Daño Queresa 13",
			"danio_queresa15":"Daño Queresa 15",
			"danio_queresa18":"Daño Queresa 18",
			"danio_queresa20":"Daño Queresa 20",
			"danio_queresa24":"Daño Queresa 24",
			"danio_queresa27":"Daño Queresa 27",
			"danio_queresa30":"Daño Queresa 30",

			"danio_aranita11":"Daño Arañita 11",
			"danio_aranita13":"Daño Arañita 13",
			"danio_aranita15":"Daño Arañita 15",
			"danio_aranita18":"Daño Arañita 18",
			"danio_aranita20":"Daño Arañita 20",
			"danio_aranita24":"Daño Arañita 24",
			"danio_aranita27":"Daño Arañita 27",
			"danio_aranita30":"Daño Arañita 30",

			"danio_mosca11":"Daño Mosca 11",
			"danio_mosca13":"Daño Mosca 13",
			"danio_mosca15":"Daño Mosca 15",
			"danio_mosca18":"Daño Mosca 18",
			"danio_mosca20":"Daño Mosca 20",
			"danio_mosca24":"Daño Mosca 24",
			"danio_mosca27":"Daño Mosca 27",
			"danio_mosca30":"Daño Mosca 30",

			"anexo_estadio_brix1":"Brix M1-Estadio",
        	"brix1":"Brix- M1",
			"anexo_estadio_brix2":"Brix M2-Estadio",
        	"brix2":"Brix- M2",
        	"anexo_estadio_brix3":"Brix M3-Estadio",
        	"brix3":"Brix- M3",
        	
        	"anexo_firmeza1":"Firmeza M1-Estadio",
        	"valor_firmeza1":"Firmeza- M1",
        	"anexo_firmeza2":"Firmeza M2-Estadio",
        	"valor_firmeza2":"Firmeza- M2",
        	"anexo_firmeza3":"Firmeza M3-Estadio",
        	"valor_firmeza3":"Firmeza- M3",

			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class detalleevcalmuestreoplantahgica2021form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detalleevcalmuestreoplantahgica2021form, self).__init__(*args, **kwargs)
        
        self.fields['exportable11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})    
        self.fields['exportable13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})    
        self.fields['exportable15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['exportable18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['exportable20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['exportable24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['exportable27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['exportable30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['pudricion11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['pudricion18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['pudricion30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['micelio11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['micelio13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['micelio15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['micelio18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['micelio20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['micelio24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['micelio27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['micelio30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['pasmado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pasmado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pasmado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['pasmado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pasmado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pasmado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pasmado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['pasmado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['sobremaduro11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduro13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduro15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['sobremaduro18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduro20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduro24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduro27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['sobremaduro30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        

        self.fields['danio_latex11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_latex13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_latex15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_latex18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_latex20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_latex24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_latex27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_latex30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['ostiolo_abierto11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['ostiolo_abierto13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['ostiolo_abierto15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['ostiolo_abierto18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['ostiolo_abierto20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['ostiolo_abierto24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['ostiolo_abierto27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['ostiolo_abierto30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['danio_mecanico11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_mecanico18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_mecanico30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['pedunculo_malcortado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pedunculo_malcortado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['pedunculo_malcortado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    

        self.fields['agrietado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['agrietado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['agrietado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['agrietado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['agrietado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['agrietado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['agrietado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['agrietado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['deshidratado11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deshidratado13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deshidratado15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['deshidratado18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deshidratado20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deshidratado24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deshidratado27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['deshidratado30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        	
        self.fields['bajo_calibre11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_calibre13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_calibre15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['bajo_calibre18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_calibre20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_calibre24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_calibre27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['bajo_calibre30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['deformes11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deformes13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deformes15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['deformes18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deformes20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deformes24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['deformes27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['deformes30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cicatriz11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['cicatriz18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['cicatriz30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['manchas11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['manchas13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['manchas15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['manchas18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['manchas20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['manchas24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['manchas27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['manchas30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['inmadurez_verde11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['inmadurez_verde13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['inmadurez_verde15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['inmadurez_verde18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['inmadurez_verde20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['inmadurez_verde24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['inmadurez_verde27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['inmadurez_verde30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['excremento_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['excremento_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['excremento_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['excremento_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['excremento_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['excremento_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['excremento_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['excremento_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['picado_ave11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['picado_ave13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['picado_ave15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['picado_ave18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['picado_ave20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['picado_ave24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['picado_ave27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['picado_ave30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['danio_trips11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_trips13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_trips15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_trips18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_trips20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_trips24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_trips27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_trips30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['danio_queresa11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_queresa13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_queresa15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_queresa18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_queresa20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_queresa24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_queresa27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_queresa30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['danio_aranita11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_aranita13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_aranita15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_aranita18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_aranita20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_aranita24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_aranita27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_aranita30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['danio_mosca11'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mosca13'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mosca15'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_mosca18'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mosca20'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mosca24'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mosca27'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['danio_mosca30'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        

        self.fields['longitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['latitud'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_brix1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['brix1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_brix2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['brix2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_brix3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['brix3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_firmeza1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_firmeza1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_firmeza2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_firmeza2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_estadio_firmeza3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_firmeza3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
                
        
    class Meta:
        model = DetalleEvCalMuestreoPlantaHgIca2021
        fields = [
            
            'exportable11',
            'exportable13',
            'exportable15',
            'exportable18',
            'exportable20',
            'exportable24',
            'exportable27',
            'exportable30',
            
            'pudricion11',
            'pudricion13',
            'pudricion15',
            'pudricion18',
            'pudricion20',
            'pudricion24',
            'pudricion27',
            'pudricion30',

            'micelio11',
            'micelio13',
            'micelio15',
            'micelio18',
            'micelio20',
            'micelio24',
            'micelio27',
            'micelio30',

            'pasmado11',
            'pasmado13',
            'pasmado15',
            'pasmado18',
            'pasmado20',
            'pasmado24',
            'pasmado27',
            'pasmado30',

            'sobremaduro11',
            'sobremaduro13',
            'sobremaduro15',
            'sobremaduro18',
            'sobremaduro20',
            'sobremaduro24',
            'sobremaduro27',
            'sobremaduro30',

            'danio_latex11',
            'danio_latex13',
            'danio_latex15',
            'danio_latex18',
            'danio_latex20',
            'danio_latex24',
            'danio_latex27',
            'danio_latex30',

            'ostiolo_abierto11',
            'ostiolo_abierto13',
            'ostiolo_abierto15',
            'ostiolo_abierto18',
            'ostiolo_abierto20',
            'ostiolo_abierto24',
            'ostiolo_abierto27',
            'ostiolo_abierto30',

            'danio_mecanico11',
            'danio_mecanico13',
            'danio_mecanico15',
            'danio_mecanico18',
            'danio_mecanico20',
            'danio_mecanico24',
            'danio_mecanico27',
            'danio_mecanico30',

            'pedunculo_malcortado11',
            'pedunculo_malcortado13',
            'pedunculo_malcortado15',
            'pedunculo_malcortado18',
            'pedunculo_malcortado20',
            'pedunculo_malcortado24',
            'pedunculo_malcortado27',
            'pedunculo_malcortado30',

            'agrietado11',
            'agrietado13',
            'agrietado15',
            'agrietado18',
            'agrietado20',
            'agrietado24',
            'agrietado27',
            'agrietado30',

            'deshidratado11',
            'deshidratado13',
            'deshidratado15',
            'deshidratado18',
            'deshidratado20',
            'deshidratado24',
            'deshidratado27',
            'deshidratado30',

            'bajo_calibre11',
            'bajo_calibre13',
            'bajo_calibre15',
            'bajo_calibre18',
            'bajo_calibre20',
            'bajo_calibre24',
            'bajo_calibre27',
            'bajo_calibre30',

            'deformes11',
            'deformes13',
            'deformes15',
            'deformes18',
            'deformes20',
            'deformes24',
            'deformes27',
            'deformes30',

            'cicatriz11',
            'cicatriz13',
            'cicatriz15',
            'cicatriz18',
            'cicatriz20',
            'cicatriz24',
            'cicatriz27',
            'cicatriz30',

            'manchas11',
            'manchas13',
            'manchas15',
            'manchas18',
            'manchas20',
            'manchas24',
            'manchas27',
            'manchas30',

            'inmadurez_verde11',
            'inmadurez_verde13',
            'inmadurez_verde15',
            'inmadurez_verde18',
            'inmadurez_verde20',
            'inmadurez_verde24',
            'inmadurez_verde27',
            'inmadurez_verde30',

            'excremento_ave11',
            'excremento_ave13',
            'excremento_ave15',
            'excremento_ave18',
            'excremento_ave20',
            'excremento_ave24',
            'excremento_ave27',
            'excremento_ave30',

            'picado_ave11',
            'picado_ave13',
            'picado_ave15',
            'picado_ave18',
            'picado_ave20',
            'picado_ave24',
            'picado_ave27',
            'picado_ave30',

            'danio_trips11',
            'danio_trips13',
            'danio_trips15',
            'danio_trips18',
            'danio_trips20',
            'danio_trips24',
            'danio_trips27',
            'danio_trips30',

            'danio_queresa11',
            'danio_queresa13',
            'danio_queresa15',
            'danio_queresa18',
            'danio_queresa20',
            'danio_queresa24',
            'danio_queresa27',
            'danio_queresa30',

            'danio_aranita11',
            'danio_aranita13',
            'danio_aranita15',
            'danio_aranita18',
            'danio_aranita20',
            'danio_aranita24',
            'danio_aranita27',
            'danio_aranita30',

            'danio_mosca11',
            'danio_mosca13',
            'danio_mosca15',
            'danio_mosca18',
            'danio_mosca20',
            'danio_mosca24',
            'danio_mosca27',
            'danio_mosca30',

            'longitud',
            'latitud',
            
            'anexo_estadio_brix1',
            'brix1',
            'anexo_estadio_brix2',
            'brix2',
            'anexo_estadio_brix3',
            'brix3',
          
            'anexo_estadio_firmeza1',
            'anexo_firmeza1',

            
            'anexo_estadio_firmeza2',
            'anexo_firmeza2',



            'anexo_estadio_firmeza3',
            'anexo_firmeza3',



        ]

        labels={
#            
          	"exportable11":"Exportable 11",
            "exportable13":"Exportable 13",
            "exportable15":"Exportable 15",
            "exportable18":"Exportable 18",
            "exportable20":"Exportable 20",
            "exportable24":"Exportable 24",
            "exportable27":"Exportable 27",
            "exportable30":"Exportable 30",
            
            "pudricion11":"Pudricion 11",
            "pudricion13":"Pudricion 13",
            "pudricion15":"Pudricion 15",
            "pudricion18":"Pudricion 18",
            "pudricion20":"Pudricion 20",
            "pudricion24":"Pudricion 24",
            "pudricion27":"Pudricion 27",
            "pudricion30":"Pudricion 30",

            "micelio11":"Micelio 11",
            "micelio13":"Micelio 13",
            "micelio15":"Micelio 15",
            "micelio18":"Micelio 18",
            "micelio20":"Micelio 20",
            "micelio24":"Micelio 24",
            "micelio27":"Micelio 27",
            "micelio30":"Micelio 30",

            "pasmado11":"Pasmado 11",
            "pasmado13":"Pasmado 13",
            "pasmado15":"Pasmado 15",
            "pasmado18":"Pasmado 18",
            "pasmado20":"Pasmado 20",
            "pasmado24":"Pasmado 24",
            "pasmado27":"Pasmado 27",
            "pasmado30":"Pasmado 30",

            "sobremaduro11":"Sobremaduro 11",
            "sobremaduro13":"Sobremaduro 13",
            "sobremaduro15":"Sobremaduro 15",
            "sobremaduro18":"Sobremaduro 18",
            "sobremaduro20":"Sobremaduro 20",
            "sobremaduro24":"Sobremaduro 24",
            "sobremaduro27":"Sobremaduro 27",
            "sobremaduro30":"Sobremaduro 30",

            "danio_latex11":"Daño Latex 11",
            "danio_latex13":"Daño Latex 13",
            "danio_latex15":"Daño Latex 15",
            "danio_latex18":"Daño Latex 18",
            "danio_latex20":"Daño Latex 20",
            "danio_latex24":"Daño Latex 24",
            "danio_latex27":"Daño Latex 27",
            "danio_latex30":"Daño Latex 30",

            "ostiolo_abierto11":"Ostiolo Abierto 11",
            "ostiolo_abierto13":"Ostiolo Abierto 13",
            "ostiolo_abierto15":"Ostiolo Abierto 15",
            "ostiolo_abierto18":"Ostiolo Abierto 18",
            "ostiolo_abierto20":"Ostiolo Abierto 20",
            "ostiolo_abierto24":"Ostiolo Abierto 24",
            "ostiolo_abierto27":"Ostiolo Abierto 27",
            "ostiolo_abierto30":"Ostiolo Abierto 30",

            "danio_mecanico11":"Daño Mecanico 11",
            "danio_mecanico13":"Daño Mecanico 13",
            "danio_mecanico15":"Daño Mecanico 15",
            "danio_mecanico18":"Daño Mecanico 18",
            "danio_mecanico20":"Daño Mecanico 20",
            "danio_mecanico24":"Daño Mecanico 24",
            "danio_mecanico27":"Daño Mecanico 27",
            "danio_mecanico30":"Daño Mecanico 30",

            "pedunculo_malcortado11":"Pedunculo Malcortado 11",
            "pedunculo_malcortado13":"Pedunculo Malcortado 13",
            "pedunculo_malcortado15":"Pedunculo Malcortado 15",
            "pedunculo_malcortado18":"Pedunculo Malcortado 18",
            "pedunculo_malcortado20":"Pedunculo Malcortado 20",
            "pedunculo_malcortado24":"Pedunculo Malcortado 24",
            "pedunculo_malcortado27":"Pedunculo Malcortado 27",
            "pedunculo_malcortado30":"Pedunculo Malcortado 30",

            "agrietado11":"Agrietado 11",
            "agrietado13":"Agrietado 13",
            "agrietado15":"Agrietado 15",
            "agrietado18":"Agrietado 18",
            "agrietado20":"Agrietado 20",
            "agrietado24":"Agrietado 24",
            "agrietado27":"Agrietado 27",
            "agrietado30":"Agrietado 30",

            "deshidratado11":"Deshidratado 11",
            "deshidratado13":"Deshidratado 13",
            "deshidratado15":"Deshidratado 15",
            "deshidratado18":"Deshidratado 18",
            "deshidratado20":"Deshidratado 20",
            "deshidratado24":"Deshidratado 24",
            "deshidratado27":"Deshidratado 27",
            "deshidratado30":"Deshidratado 30",

            "bajo_calibre11":"Bajo Calibre 11",
            "bajo_calibre13":"Bajo Calibre 13",
            "bajo_calibre15":"Bajo Calibre 15",
            "bajo_calibre18":"Bajo Calibre 18",
            "bajo_calibre20":"Bajo Calibre 20",
            "bajo_calibre24":"Bajo Calibre 24",
            "bajo_calibre27":"Bajo Calibre 27",
            "bajo_calibre30":"Bajo Calibre 30",

            "deformes11":"Deformes 11",
            "deformes13":"Deformes 13",
            "deformes15":"Deformes 15",
            "deformes18":"Deformes 18",
            "deformes20":"Deformes 20",
            "deformes24":"Deformes 24",
            "deformes27":"Deformes 27",
            "deformes30":"Deformes 30",

            "cicatriz11":"Cicatriz 11",
            "cicatriz13":"Cicatriz 13",
            "cicatriz15":"Cicatriz 15",
            "cicatriz18":"Cicatriz 18",
            "cicatriz20":"Cicatriz 20",
            "cicatriz24":"Cicatriz 24",
            "cicatriz27":"Cicatriz 27",
            "cicatriz30":"Cicatriz 30",

            "manchas11":"Manchas 11",
            "manchas13":"Manchas 13",
            "manchas15":"Manchas 15",
            "manchas18":"Manchas 18",
            "manchas20":"Manchas 20",
            "manchas24":"Manchas 24",
            "manchas27":"Manchas 27",
            "manchas30":"Manchas 30",

            "inmadurez_verde11":"Inmadurez Verde 11",
            "inmadurez_verde13":"Inmadurez Verde 13",
            "inmadurez_verde15":"Inmadurez Verde 15",
            "inmadurez_verde18":"Inmadurez Verde 18",
            "inmadurez_verde20":"Inmadurez Verde 20",
            "inmadurez_verde24":"Inmadurez Verde 24",
            "inmadurez_verde27":"Inmadurez Verde 27",
            "inmadurez_verde30":"Inmadurez Verde 30",

            "excremento_ave11":"Excremento Ave 11",
            "excremento_ave13":"Excremento Ave 13",
            "excremento_ave15":"Excremento Ave 15",
            "excremento_ave18":"Excremento Ave 18",
            "excremento_ave20":"Excremento Ave 20",
            "excremento_ave24":"Excremento Ave 24",
            "excremento_ave27":"Excremento Ave 27",
            "excremento_ave30":"Excremento Ave 30",

            "picado_ave11":"Picado Ave 11",
            "picado_ave13":"Picado Ave 13",
            "picado_ave15":"Picado Ave 15",
            "picado_ave18":"Picado Ave 18",
            "picado_ave20":"Picado Ave 20",
            "picado_ave24":"Picado Ave 24",
            "picado_ave27":"Picado Ave 27",
            "picado_ave30":"Picado Ave 30",

            "danio_trips11":"Daño por Trips 11",
            "danio_trips13":"Daño por Trips 13",
            "danio_trips15":"Daño por Trips 15",
            "danio_trips18":"Daño por Trips 18",
            "danio_trips20":"Daño por Trips 20",
            "danio_trips24":"Daño por Trips 24",
            "danio_trips27":"Daño por Trips 27",
            "danio_trips30":"Daño por Trips 30",

            "danio_queresa11":"Daño Queresa 11",
            "danio_queresa13":"Daño Queresa 13",
            "danio_queresa15":"Daño Queresa 15",
            "danio_queresa18":"Daño Queresa 18",
            "danio_queresa20":"Daño Queresa 20",
            "danio_queresa24":"Daño Queresa 24",
            "danio_queresa27":"Daño Queresa 27",
            "danio_queresa30":"Daño Queresa 30",

            "danio_aranita11":"Daño Arañita 11",
            "danio_aranita13":"Daño Arañita 13",
            "danio_aranita15":"Daño Arañita 15",
            "danio_aranita18":"Daño Arañita 18",
            "danio_aranita20":"Daño Arañita 20",
            "danio_aranita24":"Daño Arañita 24",
            "danio_aranita27":"Daño Arañita 27",
            "danio_aranita30":"Daño Arañita 30",

            "danio_mosca11":"Daño Mosca 11",
            "danio_mosca13":"Daño Mosca 13",
            "danio_mosca15":"Daño Mosca 15",
            "danio_mosca18":"Daño Mosca 18",
            "danio_mosca20":"Daño Mosca 20",
            "danio_mosca24":"Daño Mosca 24",
            "danio_mosca27":"Daño Mosca 27",
            "danio_mosca30":"Daño Mosca 30",

            "longitud":"Longitud",
            "latitud":"Latitud",
        
        	"anexo_estadio_brix1":"Brix M1-Estadio",
        	"brix1":"Brix- M1",
			
			"anexo_estadio_brix2":"Brix M2-Estadio",
        	"brix2":"Brix- M2",

        	"anexo_estadio_brix3":"Brix M3-Estadio",
        	"brix3":"Brix- M3",
        	
        	"anexo_estadio_firmeza1":"Firmeza M1-Estadio",
        	"anexo_firmeza1":"Firmeza- M1",
        	
        	"anexo_estadio_firmeza2":"Firmeza M2-Estadio",
        	"anexo_firmeza2":"Firmeza- M2",
        	
        	"anexo_estadio_firmeza3":"Firmeza M3-Estadio",
        	"anexo_firmeza3":"Firmeza- M3",
        	
        }




class evcalbrixgrica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalbrixgrica2021form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"N° Planta","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Ancho","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=1))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		

		
	class Meta:
		model = EvCalBrixGrIca2021
		fields = [
			
			'anexo_cultivo',
			
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			'anexo_variedad',
			'fecha',
	
			
		]

		labels={

			"anexo_cultivo":"Cultivo",
#			
			
			
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"Pep",
			"anexo_variedad":"Variedad",
			"fecha":"Fecha",
		}



class detalleevcalbrixgrica2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevcalbrixgrica2021form, self).__init__(*args, **kwargs)
		
		self.fields['peso'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['diametro'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['diametro_polar'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['color_interno'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['color_externo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['brix'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['gasto_naoh'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['acidez'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['indice_madurez'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['sector'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		
		self.fields['peso_arilo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['peso_cascara'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
		self.fields['anexo_llenado'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})	
					

		
	class Meta:
		model = DetalleEvCalBrixGrIca2021
		fields = [
			
			'peso',
			
			'diametro',
			'diametro_polar',
			
			'color_interno',
			'color_externo',
			'brix',
			'gasto_naoh',

			'acidez',
			'indice_madurez',
			'sector',
			'peso_arilo',
			'peso_cascara',
			'anexo_llenado',	
			
		]

		labels={

			"peso":"Peso",
			"diametro":"Diametro Ecuatorial",
			"diametro_polar":"Diametro Polar",
			"color_interno":"Color Interno",
			"color_externo":"Color Externo",
			"brix":"Brix",
			"gasto_naoh":"Gasto NAOH",

			"acidez":"Acidez",
			"indice_madurez":"Indice Madurez",
			"sector":"Sector",
			"peso_arilo":"Peso Arilo",
			"peso_cascara":"Peso Cascara",
			"anexo_llenado":"LLenado Arilo",
		}




class evcalmmppgrica2021form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(evcalmmppgrica2021form, self).__init__(*args, **kwargs)
        
        self.fields['npalet'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_tipocalidad'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_fecha_cosecha'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_nro_guia'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_pep'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['fecha_evaluacion'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['temperatura_pulpa'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['peso_muestra'].widget.attrs.update({"placeholder":"Alto","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        

        
    class Meta:
        model = EvCalMmppGrIca2021
        fields = [
            
            'npalet',
            'anexo_tipocalidad',
            'anexo_fundo',
            'anexo_fecha_cosecha',
            'anexo_nro_guia',
            'anexo_pep',
            'anexo_variedad',
            'fecha_evaluacion',
            'temperatura_pulpa',
            'peso_muestra',
            
        ]

        labels={

            "npalet":"N° Palet",
            "anexo_tipocalidad":"Tipo Calidad",
            "anexo_fundo":"Fundo",
            "anexo_fecha_cosecha":"Fecha Cosecha",
            "anexo_nro_guia":"Nro Guia",
            "anexo_pep":"PEP",
            "anexo_variedad":"Variedad",
            "fecha_evaluacion":"Fecha Evaluacion",        
            "temperatura_pulpa":"Temperatura Pulpa",
            "peso_muestra":"Peso Muestra",
        }

class detalleevcalmmppgrica2021form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detalleevcalmmppgrica2021form, self).__init__(*args, **kwargs)
        
        self.fields['brix1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['brix2'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['brix3'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['brix4'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['acidez1'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['acidez2'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['acidez3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['acidez4'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['acidez5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['indice_madurez1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['indice_madurez2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['indice_madurez3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['indice_madurez4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['alternaria'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['gelechi'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['sobremaduracion'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['arilo_pardo'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cydia'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['conforme'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_interna1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_interna2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_interna3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_interna4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_interna5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_externa1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_externa2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_externa25'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_externa3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_externa35'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_externa4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['color_externa5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext1_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext1_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext1_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext1_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext1_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext2_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext2_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext2_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext2_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext2_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext25_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext25_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext25_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext25_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext25_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext3_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext3_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext3_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext3_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext3_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext35_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext35_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext35_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext35_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext35_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext4_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext4_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext4_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext4_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext4_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['color_ext5_int1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext5_int2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext5_int3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext5_int4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['color_ext5_int5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})

        self.fields['cat1_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_cicatriz_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_cicatriz_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_thrips_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_thrips_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_deformes_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deformes_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_deshidratadol_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_deshidratadol_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_manchas_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_manchas_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_palidas_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_palidas_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_pedunculo_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_pedunculo_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_rajadas_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_rajadas_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_recuperable_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_recuperable_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_russet_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_russet_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_danio_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_danio_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cat2_insolacion_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_insolacion_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['cati_rajada_sa_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cati_rajada_sa_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_pesome_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_deshisev_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['desc_deshisev_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_deshisev_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
                
        self.fields['desc_magullado_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_magullado_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_moscaf_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_moscaf_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_gelechi_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_gelechi_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_hongosi_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_hongosi_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_inmadurez_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_inmadurez_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_insolacion_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_insolacion_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_quereza_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_quereza_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_botritis_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_botritis_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_cochinilla_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_cochinilla_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_pudricion_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_pudricion_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['desc_rajadasae_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_20'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_22'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['desc_rajadasae_24'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        

        

        
    class Meta:
        model = DetalleEvCalMmppGrIca2021
        fields = [
            
            'brix1',
            'brix2',
            'brix3',
            'brix4',
            'acidez1',
            'acidez2',
            'acidez3',
            'acidez4',
            'acidez5',
            'indice_madurez1',
            'indice_madurez2',
            'indice_madurez3',
            'indice_madurez4',
            'alternaria',
            'gelechi',
            'sobremaduracion',
            'arilo_pardo',
            'cydia',
            'conforme',
            'color_interna1',
            'color_interna2',
            'color_interna3',
            'color_interna4',
            'color_interna5',
            'color_externa1',
            'color_externa2',
            'color_externa25',
            'color_externa3',
            'color_externa35',
            'color_externa4',
            'color_externa5',
            'color_ext1_int1',
            'color_ext1_int2',
            'color_ext1_int3',
            'color_ext1_int4',
            'color_ext1_int5',
            'color_ext2_int1',
            'color_ext2_int2',
            'color_ext2_int3',
            'color_ext2_int4',
            'color_ext2_int5',
            'color_ext25_int1',
            'color_ext25_int2',
            'color_ext25_int3',
            'color_ext25_int4',
            'color_ext25_int5',
            'color_ext3_int1',
            'color_ext3_int2',
            'color_ext3_int3',
            'color_ext3_int4',
            'color_ext3_int5',
            'color_ext35_int1',
            'color_ext35_int2',
            'color_ext35_int3',
            'color_ext35_int4',
            'color_ext35_int5',
            'color_ext4_int1',
            'color_ext4_int2',
            'color_ext4_int3',
            'color_ext4_int4',
            'color_ext4_int5',
            'color_ext5_int1',
            'color_ext5_int2',
            'color_ext5_int3',
            'color_ext5_int4',
            'color_ext5_int5',
            'cat1_4',
            'cat1_5',
            'cat1_6',
            'cat1_7',
            'cat1_8',
            'cat1_9',
            'cat1_10',
            'cat1_12',
            'cat1_14',
            'cat1_16',
            'cat1_18',
            'cat1_20',
            'cat1_22',
            'cat1_24',
            
            'cat2_cicatriz_4',
            'cat2_cicatriz_5',
            'cat2_cicatriz_6',
            'cat2_cicatriz_7',
            'cat2_cicatriz_8',
            'cat2_cicatriz_9',
            'cat2_cicatriz_10',
            'cat2_cicatriz_12',
            'cat2_cicatriz_14',
            'cat2_cicatriz_16',
            'cat2_cicatriz_18',
            'cat2_cicatriz_20',
            'cat2_cicatriz_22',
            'cat2_cicatriz_24',
            
            'cat2_thrips_4',
            'cat2_thrips_5',
            'cat2_thrips_6',
            'cat2_thrips_7',
            'cat2_thrips_8',
            'cat2_thrips_9',
            'cat2_thrips_10',
            'cat2_thrips_12',
            'cat2_thrips_14',
            'cat2_thrips_16',
            'cat2_thrips_18',
            'cat2_thrips_20',
            'cat2_thrips_22',
            'cat2_thrips_24',
            
            'cat2_deformes_4',
            'cat2_deformes_5',
            'cat2_deformes_6',
            'cat2_deformes_7',
            'cat2_deformes_8',
            'cat2_deformes_9',
            'cat2_deformes_10',
            'cat2_deformes_12',
            'cat2_deformes_14',
            'cat2_deformes_16',
            'cat2_deformes_18',
            'cat2_deformes_20',
            'cat2_deformes_22',
            'cat2_deformes_24',
            
            'cat2_deshidratadol_4',
            'cat2_deshidratadol_5',
            'cat2_deshidratadol_6',
            'cat2_deshidratadol_7',
            'cat2_deshidratadol_8',
            'cat2_deshidratadol_9',
            'cat2_deshidratadol_10',
            'cat2_deshidratadol_12',
            'cat2_deshidratadol_14',
            'cat2_deshidratadol_16',
            'cat2_deshidratadol_18',
            'cat2_deshidratadol_20',
            'cat2_deshidratadol_22',
            'cat2_deshidratadol_24',
            
            'cat2_manchas_4',
            'cat2_manchas_5',
            'cat2_manchas_6',
            'cat2_manchas_7',
            'cat2_manchas_8',
            'cat2_manchas_9',
            'cat2_manchas_10',
            'cat2_manchas_12',
            'cat2_manchas_14',
            'cat2_manchas_16',
            'cat2_manchas_18',
            'cat2_manchas_20',
            'cat2_manchas_22',
            'cat2_manchas_24',
            
            'cat2_palidas_4',
            'cat2_palidas_5',
            'cat2_palidas_6',
            'cat2_palidas_7',
            'cat2_palidas_8',
            'cat2_palidas_9',
            'cat2_palidas_10',
            'cat2_palidas_12',
            'cat2_palidas_14',
            'cat2_palidas_16',
            'cat2_palidas_18',
            'cat2_palidas_20',
            'cat2_palidas_22',
            'cat2_palidas_24',
            
            'cat2_pedunculo_4',
            'cat2_pedunculo_5',
            'cat2_pedunculo_6',
            'cat2_pedunculo_7',
            'cat2_pedunculo_8',
            'cat2_pedunculo_9',
            'cat2_pedunculo_10',
            'cat2_pedunculo_12',
            'cat2_pedunculo_14',
            'cat2_pedunculo_16',
            'cat2_pedunculo_18',
            'cat2_pedunculo_20',
            'cat2_pedunculo_22',
            'cat2_pedunculo_24',
            
            'cat2_rajadas_4',
            'cat2_rajadas_5',
            'cat2_rajadas_6',
            'cat2_rajadas_7',
            'cat2_rajadas_8',
            'cat2_rajadas_9',
            'cat2_rajadas_10',
            'cat2_rajadas_12',
            'cat2_rajadas_14',
            'cat2_rajadas_16',
            'cat2_rajadas_18',
            'cat2_rajadas_20',
            'cat2_rajadas_22',
            'cat2_rajadas_24',
            
            'cat2_recuperable_4',
            'cat2_recuperable_5',
            'cat2_recuperable_6',
            'cat2_recuperable_7',
            'cat2_recuperable_8',
            'cat2_recuperable_9',
            'cat2_recuperable_10',
            'cat2_recuperable_12',
            'cat2_recuperable_14',
            'cat2_recuperable_16',
            'cat2_recuperable_18',
            'cat2_recuperable_20',
            'cat2_recuperable_22',
            'cat2_recuperable_24',


            'cat2_russet_4',
            'cat2_russet_5',
            'cat2_russet_6',
            'cat2_russet_7',
            'cat2_russet_8',
            'cat2_russet_9',
            'cat2_russet_10',
            'cat2_russet_12',
            'cat2_russet_14',
            'cat2_russet_16',
            'cat2_russet_18',
            'cat2_russet_20',
            'cat2_russet_22',
            'cat2_russet_24',
            
            'cat2_danio_4',
            'cat2_danio_5',
            'cat2_danio_6',
            'cat2_danio_7',
            'cat2_danio_8',
            'cat2_danio_9',
            'cat2_danio_10',
            'cat2_danio_12',
            'cat2_danio_14',
            'cat2_danio_16',
            'cat2_danio_18',
			'cat2_danio_20',
            'cat2_danio_22',
            'cat2_danio_24',

            'cat2_insolacion_4',
            'cat2_insolacion_5',
            'cat2_insolacion_6',
            'cat2_insolacion_7',
            'cat2_insolacion_8',
            'cat2_insolacion_9',
            'cat2_insolacion_10',
            'cat2_insolacion_12',
            'cat2_insolacion_14',
            'cat2_insolacion_16',
            'cat2_insolacion_18',
            'cat2_insolacion_20',
            'cat2_insolacion_22',
            'cat2_insolacion_24',
            
            'cati_rajada_sa_4',
            'cati_rajada_sa_5',
            'cati_rajada_sa_6',
            'cati_rajada_sa_7',
            'cati_rajada_sa_8',
            'cati_rajada_sa_9',
            'cati_rajada_sa_10',
            'cati_rajada_sa_12',
            'cati_rajada_sa_14',
            'cati_rajada_sa_16',
            'cati_rajada_sa_18',
            'cati_rajada_sa_20',
            'cati_rajada_sa_22',
            'cati_rajada_sa_24',
            
            'desc_pesome_4',
            
            'desc_deshisev_4',
            'desc_deshisev_5',
            'desc_deshisev_6',
            'desc_deshisev_7',
            'desc_deshisev_8',
            'desc_deshisev_9',
            'desc_deshisev_10',
            'desc_deshisev_12',
            'desc_deshisev_14',
            'desc_deshisev_16',
            'desc_deshisev_18',
            'desc_deshisev_20',
            'desc_deshisev_22',
            'desc_deshisev_24',
            
            'desc_magullado_4',
            'desc_magullado_5',
            'desc_magullado_6',
            'desc_magullado_7',
            'desc_magullado_8',
            'desc_magullado_9',
            'desc_magullado_10',
            'desc_magullado_12',
            'desc_magullado_14',
            'desc_magullado_16',
            'desc_magullado_18',
            'desc_magullado_20',
            'desc_magullado_22',
            'desc_magullado_24',
            
            'desc_moscaf_4',
            'desc_moscaf_5',
            'desc_moscaf_6',
            'desc_moscaf_7',
            'desc_moscaf_8',
            'desc_moscaf_9',
            'desc_moscaf_10',
            'desc_moscaf_12',
            'desc_moscaf_14',
            'desc_moscaf_16',
            'desc_moscaf_18',
            'desc_moscaf_20',
            'desc_moscaf_22',
            'desc_moscaf_24',
            
            'desc_gelechi_4',
            'desc_gelechi_5',
            'desc_gelechi_6',
            'desc_gelechi_7',
            'desc_gelechi_8',
            'desc_gelechi_9',
            'desc_gelechi_10',
            'desc_gelechi_12',
            'desc_gelechi_14',
            'desc_gelechi_16',
            'desc_gelechi_18',
            'desc_gelechi_20',
            'desc_gelechi_22',
            'desc_gelechi_24',
            
            'desc_hongosi_4',
            'desc_hongosi_5',
            'desc_hongosi_6',
            'desc_hongosi_7',
            'desc_hongosi_8',
            'desc_hongosi_9',
            'desc_hongosi_10',
            'desc_hongosi_12',
            'desc_hongosi_14',
            'desc_hongosi_16',
            'desc_hongosi_18',
            'desc_hongosi_20',
            'desc_hongosi_22',
            'desc_hongosi_24',
            
            'desc_inmadurez_4',
            'desc_inmadurez_5',
            'desc_inmadurez_6',
            'desc_inmadurez_7',
            'desc_inmadurez_8',
            'desc_inmadurez_9',
            'desc_inmadurez_10',
            'desc_inmadurez_12',
            'desc_inmadurez_14',
            'desc_inmadurez_16',
            'desc_inmadurez_18',
            'desc_inmadurez_20',
            'desc_inmadurez_22',
            'desc_inmadurez_24',
            
            'desc_insolacion_4',
            'desc_insolacion_5',
            'desc_insolacion_6',
            'desc_insolacion_7',
            'desc_insolacion_8',
            'desc_insolacion_9',
            'desc_insolacion_10',
            'desc_insolacion_12',
            'desc_insolacion_14',
            'desc_insolacion_16',
            'desc_insolacion_18',
            'desc_insolacion_20',
            'desc_insolacion_22',
            'desc_insolacion_24',
            
            'desc_quereza_4',
            'desc_quereza_5',
            'desc_quereza_6',
            'desc_quereza_7',
            'desc_quereza_8',
            'desc_quereza_9',
            'desc_quereza_10',
            'desc_quereza_12',
            'desc_quereza_14',
            'desc_quereza_16',
            'desc_quereza_18',
            'desc_quereza_14',
            'desc_quereza_16',
            'desc_quereza_18',
            'desc_quereza_20',
            'desc_quereza_22',
            'desc_quereza_24',
            
            'desc_botritis_4',
            'desc_botritis_5',
            'desc_botritis_6',
            'desc_botritis_7',
            'desc_botritis_8',
            'desc_botritis_9',
            'desc_botritis_10',
            'desc_botritis_12',
            'desc_botritis_14',
            'desc_botritis_16',
            'desc_botritis_18',
            'desc_botritis_20',
            'desc_botritis_22',
            'desc_botritis_24',
            
            'desc_cochinilla_4',
            'desc_cochinilla_5',
            'desc_cochinilla_6',
            'desc_cochinilla_7',
            'desc_cochinilla_8',
            'desc_cochinilla_9',
            'desc_cochinilla_10',
            'desc_cochinilla_12',
            'desc_cochinilla_14',
            'desc_cochinilla_16',
            'desc_cochinilla_18',
            'desc_cochinilla_20',
            'desc_cochinilla_22',
            'desc_cochinilla_24',
            
            'desc_pudricion_4',
            'desc_pudricion_5',
            'desc_pudricion_6',
            'desc_pudricion_7',
            'desc_pudricion_8',
            'desc_pudricion_9',
            'desc_pudricion_10',
            'desc_pudricion_12',
            'desc_pudricion_14',
            'desc_pudricion_16',
            'desc_pudricion_18',
            'desc_pudricion_20',
            'desc_pudricion_22',
            'desc_pudricion_24',
            
            'desc_rajadasae_4',
            'desc_rajadasae_5',
            'desc_rajadasae_6',
            'desc_rajadasae_7',
            'desc_rajadasae_8',
            'desc_rajadasae_9',
            'desc_rajadasae_10',
            'desc_rajadasae_12',
            'desc_rajadasae_14',
            'desc_rajadasae_16',
            'desc_rajadasae_18',
            'desc_rajadasae_20',
            'desc_rajadasae_22',
            'desc_rajadasae_24',
            
        ]

        labels={

            "brix1":"Brix 1",
            "brix2":"Brix 2",
            "brix3":"Brix 3",
            "brix4":"Brix 4",
            "acidez1":"Acidez 1",
            "acidez2":"Acidez 2",
            "acidez3":"Acidez 3",
            "acidez4":"Acidez 4",
            "acidez5":"Acidez 5",
            "indice_madurez1":"Indice Madurez 1",
            "indice_madurez2":"Indice Madurez 2",
            "indice_madurez3":"Indice Madurez 3",
            "indice_madurez4":"Indice Madurez 4",
            "alternaria":"Alternaria",
            "gelechi":"Gelechiidae",
            "sobremaduracion":"Sobremaduracion",
            "arilo_pardo":"Arilo Pardo",
            "cydia":"Cydia",
            "conforme":"Conforme",
            "color_interna1":"Color Interno 1",
            "color_interna2":"Color Interno 2",
            "color_interna3":"Color interno 3",
            "color_interna4":"Color interno 4",
            "color_interna5":"Color Interno 5",
            "color_externa1":"Color Externo 1",
            "color_externa2":"Color Externo 2",
            "color_externa25":"Color Externo 2.5",
            "color_externa3":"Color Externo 3",
            "color_externa35":"Color Externo 3.5",
            "color_externa4":"Color Externo 4",
            "color_externa5":"Color Externa 5",
            "color_ext1_int1":"Color Externo1 - Interno 1",
            "color_ext1_int2":"Color Externo1 - Interno 2",
            "color_ext1_int3":"Color Externo1 - Interno 3",
            "color_ext1_int4":"Color Externo1 - Interno 4",
            "color_ext1_int5":"Color Externo1 - Interno 5",
            "color_ext2_int1":"Color Externo2 - Interno 1",
            "color_ext2_int2":"Color Externo2 - Interno 2",
            "color_ext2_int3":"Color Externo2 - Interno 3",
            "color_ext2_int4":"Color Externo2 - Interno 4",
            "color_ext2_int5":"Color Externo2 - Interno 5",
            "color_ext25_int1":"Color Externo2.5 - Interno 1",
            "color_ext25_int2":"Color Externo2.5 - Interno 2",
            "color_ext25_int3":"Color Externo2.5 - Interno 3",
            "color_ext25_int4":"Color Externo2.5 - Interno 4",
            "color_ext25_int5":"Color Externo2.5 - Interno 5",
            "color_ext3_int1":"Color Externo3 - Interno 1",
            "color_ext3_int2":"Color Externo3 - Interno 2",
            "color_ext3_int3":"Color Externo3 - Interno 3",
            "color_ext3_int4":"Color Externo3 - Interno 4",
            "color_ext3_int5":"Color Externo3 - Interno 5",
            "color_ext35_int1":"Color Externo3.5 - Interno 1",
            "color_ext35_int2":"Color Externo3.5 - Interno 2",
            "color_ext35_int3":"Color Externo3.5 - Interno 3",
            "color_ext35_int4":"Color Externo3.5 - Interno 4",
            "color_ext35_int5":"Color Externo3.5 - Interno 5",
            "color_ext4_int1":"Color Externo4 - Interno 1",
            "color_ext4_int2":"Color Externo4 - Interno 2",
            "color_ext4_int3":"Color Externo4 - Interno 3",
            "color_ext4_int4":"Color Externo4 - Interno 4",
            "color_ext4_int5":"Color Externo4 - Interno 5",
            "color_ext5_int1":"Color Externo5 - Interno 1",
            "color_ext5_int2":"Color Externo5 - Interno 2",
            "color_ext5_int3":"Color Externo5 - Interno 3",
            "color_ext5_int4":"Color Externo5 - Interno 4",
            "color_ext5_int5":"Color Externo5 - Interno 5",
            "cat1_4":"Cat1-Calibre 4",
            "cat1_5":"Cat1-Calibre 5",
            "cat1_6":"Cat1-Calibre 6",
            "cat1_7":"Cat1-Calibre 7",
            "cat1_8":"Cat1-Calibre 8",
            "cat1_9":"Cat1-Calibre 9",
            "cat1_10":"Cat1-Calibre 10",
            "cat1_12":"Cat1-Calibre 12",
            "cat1_14":"Cat1-Calibre 14",
            "cat1_16":"Cat1-Calibre 16",
            "cat1_18":"Cat1-Calibre 18",
            "cat1_20":"Cat1-Calibre 20",
            "cat1_22":"Cat1-Calibre 22",
            "cat1_24":"Cat1-Calibre 24",

            "cat2_cicatriz_4":"Cat2-Cicatriz-Calibre 4",
            "cat2_cicatriz_5":"Cat2-Cicatriz-Calibre 5",
            "cat2_cicatriz_6":"Cat2-Cicatriz-Calibre 6",
            "cat2_cicatriz_7":"Cat2-Cicatriz-Calibre 7",
            "cat2_cicatriz_8":"Cat2-Cicatriz-Calibre 8",
            "cat2_cicatriz_9":"Cat2-Cicatriz-Calibre 9",
            "cat2_cicatriz_10":"Cat2-Cicatriz-Calibre 10",
            "cat2_cicatriz_12":"Cat2-Cicatriz-Calibre 12",
            "cat2_cicatriz_14":"Cat2-Cicatriz-Calibre 14",
            "cat2_cicatriz_16":"Cat2-Cicatriz-Calibre 16",
            "cat2_cicatriz_18":"Cat2-Cicatriz-Calibre 18",
            "cat2_cicatriz_20":"Cat2-Cicatriz-Calibre 20",
            "cat2_cicatriz_22":"Cat2-Cicatriz-Calibre 22",
            "cat2_cicatriz_24":"Cat2-Cicatriz-Calibre 24",

            "cat2_thrips_4":"Cat2-Thrips-Calibre 4",
            "cat2_thrips_5":"Cat2-Thrips-Calibre 5",
            "cat2_thrips_6":"Cat2-Thrips-Calibre 6",
            "cat2_thrips_7":"Cat2-Thrips-Calibre 7",
            "cat2_thrips_8":"Cat2-Thrips-Calibre 8",
            "cat2_thrips_9":"Cat2-Thrips-Calibre 9",
            "cat2_thrips_10":"Cat2-Thrips-Calibre 10",
            "cat2_thrips_12":"Cat2-Thrips-Calibre 12",
            "cat2_thrips_14":"Cat2-Thrips-Calibre 14",
            "cat2_thrips_16":"Cat2-Thrips-Calibre 16",
            "cat2_thrips_18":"Cat2-Thrips-Calibre 18",
            "cat2_thrips_20":"Cat2-Thrips-Calibre 20",
            "cat2_thrips_22":"Cat2-Thrips-Calibre 22",
            "cat2_thrips_24":"Cat2-Thrips-Calibre 24",
            
            "cat2_deformes_4":"Cat2-Deformes-Calibre 4",
            "cat2_deformes_5":"Cat2-Deformes-Calibre 5",
            "cat2_deformes_6":"Cat2-Deformes-Calibre 6",
            "cat2_deformes_7":"Cat2-Deformes-Calibre 7",
            "cat2_deformes_8":"Cat2-Deformes-Calibre 8",
            "cat2_deformes_9":"Cat2-Deformes-Calibre 9",
            "cat2_deformes_10":"Cat2-Deformes-Calibre 10",
            "cat2_deformes_12":"Cat2-Deformes-Calibre 12",
            "cat2_deformes_14":"Cat2-Deformes-Calibre 14",
            "cat2_deformes_16":"Cat2-Deformes-Calibre 16",
            "cat2_deformes_18":"Cat2-Deformes-Calibre 18",
            "cat2_deformes_20":"Cat2-Deformes-Calibre 20",
            "cat2_deformes_22":"Cat2-Deformes-Calibre 22",
            "cat2_deformes_24":"Cat2-Deformes-Calibre 24",

            "cat2_deshidratadol_4":"Cat2-Deshidratado Leve-Calibre 4",
            "cat2_deshidratadol_5":"Cat2-Deshidratado Leve-Calibre 5",
            "cat2_deshidratadol_6":"Cat2-Deshidratado Leve-Calibre 6",
            "cat2_deshidratadol_7":"Cat2-Deshidratado Leve-Calibre 7",
            "cat2_deshidratadol_8":"Cat2-Deshidratado Leve-Calibre 8",
            "cat2_deshidratadol_9":"Cat2-Deshidratado Leve-Calibre 9",
            "cat2_deshidratadol_10":"Cat2-Deshidratado Leve-Calibre 10",
            "cat2_deshidratadol_12":"Cat2-Deshidratado Leve-Calibre 12",
            "cat2_deshidratadol_14":"Cat2-Deshidratado Leve-Calibre 14",
            "cat2_deshidratadol_16":"Cat2-Deshidratado Leve-Calibre 16",
            "cat2_deshidratadol_18":"Cat2-Deshidratado Leve-Calibre 18",
            "cat2_deshidratadol_20":"Cat2-Deshidratado Leve-Calibre 20",
            "cat2_deshidratadol_22":"Cat2-Deshidratado Leve-Calibre 22",
            "cat2_deshidratadol_24":"Cat2-Deshidratado Leve-Calibre 24",

            "cat2_manchas_4":"Cat2-Manchas-Calibre 4",
            "cat2_manchas_5":"Cat2-Manchas-Calibre 5",
            "cat2_manchas_6":"Cat2-Manchas-Calibre 6",
            "cat2_manchas_7":"Cat2-Manchas-Calibre 7",
            "cat2_manchas_8":"Cat2-Manchas-Calibre 8",
            "cat2_manchas_9":"Cat2-Manchas-Calibre 9",
            "cat2_manchas_10":"Cat2-Manchas-Calibre 10",
            "cat2_manchas_12":"Cat2-Manchas-Calibre 12",
            "cat2_manchas_14":"Cat2-Manchas-Calibre 14",
            "cat2_manchas_16":"Cat2-Manchas-Calibre 16",
            "cat2_manchas_18":"Cat2-Manchas-Calibre 18",

            "cat2_palidas_4":"Cat2-Palidas-Calibre 4",
            "cat2_palidas_5":"Cat2-Palidas-Calibre 5",
            "cat2_palidas_6":"Cat2-Palidas-Calibre 6",
            "cat2_palidas_7":"Cat2-Palidas-Calibre 7",
            "cat2_palidas_8":"Cat2-Palidas-Calibre 8",
            "cat2_palidas_9":"Cat2-Palidas-Calibre 9",
            "cat2_palidas_10":"Cat2-Palidas-Calibre 10",
            "cat2_palidas_12":"Cat2-Palidas-Calibre 12",
            "cat2_palidas_14":"Cat2-Palidas-Calibre 14",
            "cat2_palidas_16":"Cat2-Palidas-Calibre 16",
            "cat2_palidas_18":"Cat2-Palidas-Calibre 18",
            "cat2_palidas_20":"Cat2-Palidas-Calibre 20",
            "cat2_palidas_22":"Cat2-Palidas-Calibre 22",
            "cat2_palidas_24":"Cat2-Palidas-Calibre 24",
            
            "cat2_pedunculo_4":"Cat2-Pedunculo mal cortado-Calibre 4",
            "cat2_pedunculo_5":"Cat2-Pedunculo mal cortado-Calibre 5",
            "cat2_pedunculo_6":"Cat2-Pedunculo mal cortado-Calibre 6",
            "cat2_pedunculo_7":"Cat2-Pedunculo mal cortado-Calibre 7",
            "cat2_pedunculo_8":"Cat2-Pedunculo mal cortado-Calibre 8",
            "cat2_pedunculo_9":"Cat2-Pedunculo mal cortado-Calibre 9",
            "cat2_pedunculo_10":"Cat2-Pedunculo mal cortado-Calibre 10",
            "cat2_pedunculo_12":"Cat2-Pedunculo mal cortado-Calibre 12",
            "cat2_pedunculo_14":"Cat2-Pedunculo mal cortado-Calibre 14",
            "cat2_pedunculo_16":"Cat2-Pedunculo mal cortado-Calibre 16",
            "cat2_pedunculo_18":"Cat2-Pedunculo mal cortado-Calibre 18",
            "cat2_pedunculo_20":"Cat2-Pedunculo mal cortado-Calibre 20",
            "cat2_pedunculo_22":"Cat2-Pedunculo mal cortado-Calibre 22",
            "cat2_pedunculo_24":"Cat2-Pedunculo mal cortado-Calibre 24",

            "cat2_rajadas_4":"Cat2-Rajadas-Calibre 4",
            "cat2_rajadas_5":"Cat2-Rajadas-Calibre 5",
            "cat2_rajadas_6":"Cat2-Rajadas-Calibre 6",
            "cat2_rajadas_7":"Cat2-Rajadas-Calibre 7",
            "cat2_rajadas_8":"Cat2-Rajadas-Calibre 8",
            "cat2_rajadas_9":"Cat2-Rajadas-Calibre 9",
            "cat2_rajadas_10":"Cat2-Rajadas-Calibre 10",
            "cat2_rajadas_12":"Cat2-Rajadas-Calibre 12",
            "cat2_rajadas_14":"Cat2-Rajadas-Calibre 14",
            "cat2_rajadas_16":"Cat2-Rajadas-Calibre 16",
            "cat2_rajadas_18":"Cat2-Rajadas-Calibre 18",
            "cat2_rajadas_20":"Cat2-Rajadas-Calibre 20",
            "cat2_rajadas_22":"Cat2-Rajadas-Calibre 22",
            "cat2_rajadas_24":"Cat2-Rajadas-Calibre 24",

            "cat2_recuperable_4":"Cat2-Recuperable-Calibre 4",
            "cat2_recuperable_5":"Cat2-Recuperable-Calibre 5",
            "cat2_recuperable_6":"Cat2-Recuperable-Calibre 6",
            "cat2_recuperable_7":"Cat2-Recuperable-Calibre 7",
            "cat2_recuperable_8":"Cat2-Recuperable-Calibre 8",
            "cat2_recuperable_9":"Cat2-Recuperable-Calibre 9",
            "cat2_recuperable_10":"Cat2-Recuperable-Calibre 10",
            "cat2_recuperable_12":"Cat2-Recuperable-Calibre 12",
            "cat2_recuperable_14":"Cat2-Recuperable-Calibre 14",
            "cat2_recuperable_16":"Cat2-Recuperable-Calibre 16",
            "cat2_recuperable_18":"Cat2-Recuperable-Calibre 18",
            "cat2_recuperable_20":"Cat2-Recuperable-Calibre 20",
            "cat2_recuperable_22":"Cat2-Recuperable-Calibre 22",
            "cat2_recuperable_24":"Cat2-Recuperable-Calibre 24",

            "cat2_russet_4":"Cat2-Russet-Calibre 4",
            "cat2_russet_5":"Cat2-Russet-Calibre 5",
            "cat2_russet_6":"Cat2-Russet-Calibre 6",
            "cat2_russet_7":"Cat2-Russet-Calibre 7",
            "cat2_russet_8":"Cat2-Russet-Calibre 8",
            "cat2_russet_9":"Cat2-Russet-Calibre 9",
            "cat2_russet_10":"Cat2-Russet-Calibre 10",
            "cat2_russet_12":"Cat2-Russet-Calibre 12",
            "cat2_russet_14":"Cat2-Russet-Calibre 14",
            "cat2_russet_16":"Cat2-Russet-Calibre 16",
            "cat2_russet_18":"Cat2-Russet-Calibre 18",
            "cat2_russet_20":"Cat2-Russet-Calibre 20",
            "cat2_russet_22":"Cat2-Russet-Calibre 22",
            "cat2_russet_24":"Cat2-Russet-Calibre 24",

            "cat2_danio_4":"Cat2-Daño Mecanico-Calibre 4",
            "cat2_danio_5":"Cat2-Daño Mecanico-Calibre 5",
            "cat2_danio_6":"Cat2-Daño Mecanico-Calibre 6",
            "cat2_danio_7":"Cat2-Daño Mecanico-Calibre 7",
            "cat2_danio_8":"Cat2-Daño Mecanico-Calibre 8",
            "cat2_danio_9":"Cat2-Daño Mecanico-Calibre 9",
            "cat2_danio_10":"Cat2-Daño Mecanico-Calibre 10",
            "cat2_danio_12":"Cat2-Daño Mecanico-Calibre 12",
            "cat2_danio_14":"Cat2-Daño Mecanico-Calibre 14",
            "cat2_danio_16":"Cat2-Daño Mecanico-Calibre 16",
            "cat2_danio_18":"Cat2-Daño Mecanico-Calibre 18",
            "cat2_danio_20":"Cat2-Daño Mecanico-Calibre 20",
            "cat2_danio_22":"Cat2-Daño Mecanico-Calibre 22",
            "cat2_danio_24":"Cat2-Daño Mecanico-Calibre 24",

            "cat2_insolacion_4":"Cat2-Insolacion-Calibre 4",
            "cat2_insolacion_5":"Cat2-Insolacion-Calibre 5",
            "cat2_insolacion_6":"Cat2-Insolacion-Calibre 6",
            "cat2_insolacion_7":"Cat2-Insolacion-Calibre 7",
            "cat2_insolacion_8":"Cat2-Insolacion-Calibre 8",
            "cat2_insolacion_9":"Cat2-Insolacion-Calibre 9",
            "cat2_insolacion_10":"Cat2-Insolacion-Calibre 10",
            "cat2_insolacion_12":"Cat2-Insolacion-Calibre 12",
            "cat2_insolacion_14":"Cat2-Insolacion-Calibre 14",
            "cat2_insolacion_16":"Cat2-Insolacion-Calibre 16",
            "cat2_insolacion_18":"Cat2-Insolacion-Calibre 18",
            "cat2_insolacion_20":"Cat2-Insolacion-Calibre 20",
            "cat2_insolacion_22":"Cat2-Insolacion-Calibre 22",
            "cat2_insolacion_24":"Cat2-Insolacion-Calibre 24",

            "cati_rajada_sa_4":"Cat.Ind. Rajada sin arilo-Calibre 4",
            "cati_rajada_sa_5":"Cat.Ind. Rajada sin arilo-Calibre 5",
            "cati_rajada_sa_6":"Cat.Ind. Rajada sin arilo-Calibre 6",
            "cati_rajada_sa_7":"Cat.Ind. Rajada sin arilo-Calibre 7",
            "cati_rajada_sa_8":"Cat.Ind. Rajada sin arilo-Calibre 8",
            "cati_rajada_sa_9":"Cat.Ind. Rajada sin arilo-Calibre 9",
            "cati_rajada_sa_10":"Cat.Ind. Rajada sin arilo-Calibre 10",
            "cati_rajada_sa_12":"Cat.Ind. Rajada sin arilo-Calibre 12",
            "cati_rajada_sa_14":"Cat.Ind. Rajada sin arilo-Calibre 14",
            "cati_rajada_sa_16":"Cat.Ind. Rajada sin arilo-Calibre 16",
            "cati_rajada_sa_18":"Cat.Ind. Rajada sin arilo-Calibre 18",
            "cati_rajada_sa_20":"Cat.Ind. Rajada sin arilo-Calibre 20",
            "cati_rajada_sa_22":"Cat.Ind. Rajada sin arilo-Calibre 22",
            "cati_rajada_sa_24":"Cat.Ind. Rajada sin arilo-Calibre 24",

            "desc_pesome_4":"Desc. Peso menor a 160 gr",
            
			"desc_deshisev_4":"Desc. Deshidratado severo-Calibre 4",
            "desc_deshisev_5":"Desc. Deshidratado severo-Calibre 5",
            "desc_deshisev_6":"Desc. Deshidratado severo-Calibre 6",
            "desc_deshisev_7":"Desc. Deshidratado severo-Calibre 7",
            "desc_deshisev_8":"Desc. Deshidratado severo-Calibre 8",
            "desc_deshisev_9":"Desc. Deshidratado severo-Calibre 9",
            "desc_deshisev_10":"Desc. Deshidratado severo-Calibre 10",
            "desc_deshisev_12":"Desc. Deshidratado severo-Calibre 12",
            "desc_deshisev_14":"Desc. Deshidratado severo-Calibre 14",
            "desc_deshisev_16":"Desc. Deshidratado severo-Calibre 16",
            "desc_deshisev_18":"Desc. Deshidratado severo-Calibre 18",
            "desc_deshisev_20":"Desc. Deshidratado severo-Calibre 20",
            "desc_deshisev_22":"Desc. Deshidratado severo-Calibre 22",
            "desc_deshisev_24":"Desc. Deshidratado severo-Calibre 24",

            "desc_magullado_4":"Desc. Magullado -Calibre 4",
            "desc_magullado_5":"Desc. Magullado -Calibre 5",
            "desc_magullado_6":"Desc. Magullado -Calibre 6",
            "desc_magullado_7":"Desc. Magullado -Calibre 7",
            "desc_magullado_8":"Desc. Magullado -Calibre 8",
            "desc_magullado_9":"Desc. Magullado -Calibre 9",
            "desc_magullado_10":"Desc. Magullado -Calibre 10",
            "desc_magullado_12":"Desc. Magullado -Calibre 12",
            "desc_magullado_14":"Desc. Magullado -Calibre 14",
            "desc_magullado_16":"Desc. Magullado -Calibre 16",
            "desc_magullado_18":"Desc. Magullado -Calibre 18",
            "desc_magullado_20":"Desc. Magullado -Calibre 20",
            "desc_magullado_22":"Desc. Magullado -Calibre 22",
            "desc_magullado_24":"Desc.  Magullado-Calibre 24",

			"desc_moscaf_4":"Desc. Daño Mosca Fruta-Calibre 4",
            "desc_moscaf_5":"Desc. Daño Mosca Fruta-Calibre 5",
            "desc_moscaf_6":"Desc. Daño Mosca Fruta-Calibre 6",
            "desc_moscaf_7":"Desc. Daño Mosca Fruta-Calibre 7",
            "desc_moscaf_8":"Desc. Daño Mosca Fruta-Calibre 8",
            "desc_moscaf_9":"Desc. Daño Mosca Fruta-Calibre 9",
            "desc_moscaf_10":"Desc. Daño Mosca Fruta-Calibre 10",
            "desc_moscaf_12":"Desc. Daño Mosca Fruta-Calibre 12",
            "desc_moscaf_14":"Desc. Daño Mosca Fruta-Calibre 14",
            "desc_moscaf_16":"Desc. Daño Mosca Fruta-Calibre 16",
            "desc_moscaf_18":"Desc. Daño Mosca Fruta-Calibre 18",
            "desc_moscaf_20":"Desc. Daño Mosca Fruta-Calibre 20",
            "desc_moscaf_22":"Desc. Daño Mosca Fruta-Calibre 22",
            "desc_moscaf_24":"Desc. Daño Mosca Fruta-Calibre 24",
            
            "desc_gelechi_4":"Desc. Gelechiadae-Calibre 4",
            "desc_gelechi_5":"Desc. Gelechiadae-Calibre 5",
            "desc_gelechi_6":"Desc. Gelechiadae-Calibre 6",
            "desc_gelechi_7":"Desc. Gelechiadae-Calibre 7",
            "desc_gelechi_8":"Desc. Gelechiadae-Calibre 8",
            "desc_gelechi_9":"Desc. Gelechiadae-Calibre 9",
            "desc_gelechi_10":"Desc. Gelechiadae-Calibre 10",
            "desc_gelechi_12":"Desc. Gelechiadae-Calibre 12",
            "desc_gelechi_14":"Desc. Gelechiadae-Calibre 14",
            "desc_gelechi_16":"Desc. Gelechiadae-Calibre 16",
            "desc_gelechi_18":"Desc. Gelechiadae-Calibre 18",
            "desc_gelechi_20":"Desc. Gelechiadae-Calibre 20",
            "desc_gelechi_22":"Desc. Gelechiadae-Calibre 22",
            "desc_gelechi_24":"Desc. Gelechiadae-Calibre 24",


            "desc_hongosi_4":"Desc. Hongos Interno-Alternaria-Calibre 4",
            "desc_hongosi_5":"Desc. Hongos Interno-Alternaria-Calibre 5",
            "desc_hongosi_6":"Desc. Hongos Interno-Alternaria-Calibre 6",
            "desc_hongosi_7":"Desc. Hongos Interno-Alternaria-Calibre 7",
            "desc_hongosi_8":"Desc. Hongos Interno-Alternaria-Calibre 8",
            "desc_hongosi_9":"Desc. Hongos Interno-Alternaria-Calibre 9",
            "desc_hongosi_10":"Desc. Hongos Interno-Alternaria-Calibre 10",
            "desc_hongosi_12":"Desc. Hongos Interno-Alternaria-Calibre 12",
            "desc_hongosi_14":"Desc. Hongos Interno-Alternaria-Calibre 14",
            "desc_hongosi_16":"Desc. Hongos Interno-Alternaria-Calibre 16",
            "desc_hongosi_18":"Desc. Hongos Interno-Alternaria-Calibre 18",
            "desc_hongosi_20":"Desc. Hongos Interno-Alternaria-Calibre 20",
            "desc_hongosi_22":"Desc. Hongos Interno-Alternaria-Calibre 22",
            "desc_hongosi_24":"Desc. Hongos Interno-Alternaria-Calibre 24",

            "desc_inmadurez_4":"Desc. Inmadurez-Calibre 4",
            "desc_inmadurez_5":"Desc. Inmadurez-Calibre 5",
            "desc_inmadurez_6":"Desc. Inmadurez-Calibre 6",
            "desc_inmadurez_7":"Desc. Inmadurez-Calibre 7",
            "desc_inmadurez_8":"Desc. Inmadurez-Calibre 8",
            "desc_inmadurez_9":"Desc. Inmadurez-Calibre 9",
            "desc_inmadurez_10":"Desc. Inmadurez-Calibre 10",
            "desc_inmadurez_12":"Desc. Inmadurez-Calibre 12",
            "desc_inmadurez_14":"Desc. Inmadurez-Calibre 14",
            "desc_inmadurez_16":"Desc. Inmadurez-Calibre 16",
            "desc_inmadurez_18":"Desc. Inmadurez-Calibre 18",
            "desc_inmadurez_20":"Desc. Inmadurez-Calibre 20",
            "desc_inmadurez_22":"Desc. Inmadurez-Calibre 22",
            "desc_inmadurez_24":"Desc. Inmadurez-Calibre 24",

            "desc_insolacion_4":"Desc. Insolacion-Calibre 4",
            "desc_insolacion_5":"Desc. Insolacion-Calibre 5",
            "desc_insolacion_6":"Desc. Insolacion-Calibre 6",
            "desc_insolacion_7":"Desc. Insolacion-Calibre 7",
            "desc_insolacion_8":"Desc. Insolacion-Calibre 8",
            "desc_insolacion_9":"Desc. Insolacion-Calibre 9",
            "desc_insolacion_10":"Desc. Insolacion-Calibre 10",
            "desc_insolacion_12":"Desc. Insolacion-Calibre 12",
            "desc_insolacion_14":"Desc. Insolacion-Calibre 14",
            "desc_insolacion_16":"Desc. Insolacion-Calibre 16",
            "desc_insolacion_18":"Desc. Insolacion-Calibre 18",
            "desc_insolacion_20":"Desc. Insolacion-Calibre 20",
            "desc_insolacion_22":"Desc. Insolacion-Calibre 22",
            "desc_insolacion_24":"Desc. Insolacion-Calibre 24",

            "desc_quereza_4":"Desc. Quereza-Calibre 4",
            "desc_quereza_5":"Desc. Quereza-Calibre 5",
            "desc_quereza_6":"Desc. Quereza-Calibre 6",
            "desc_quereza_7":"Desc. Quereza-Calibre 7",
            "desc_quereza_8":"Desc. Quereza-Calibre 8",
            "desc_quereza_9":"Desc. Quereza-Calibre 9",
            "desc_quereza_10":"Desc. Quereza-Calibre 10",
            "desc_quereza_12":"Desc. Quereza-Calibre 12",
            "desc_quereza_14":"Desc. Quereza-Calibre 14",
            "desc_quereza_16":"Desc. Quereza-Calibre 16",
            "desc_quereza_18":"Desc. Quereza-Calibre 18",
            "desc_quereza_20":"Desc. Quereza-Calibre 20",
            "desc_quereza_22":"Desc. Quereza-Calibre 22",
            "desc_quereza_24":"Desc. Quereza-Calibre 24",

            "desc_botritis_4":"Desc. Botrytis-Calibre 4",
            "desc_botritis_5":"Desc. Botrytis-Calibre 5",
            "desc_botritis_6":"Desc. Botrytis-Calibre 6",
            "desc_botritis_7":"Desc. Botrytis-Calibre 7",
            "desc_botritis_8":"Desc. Botrytis-Calibre 8",
            "desc_botritis_9":"Desc. Botrytis-Calibre 9",
            "desc_botritis_10":"Desc. Botrytis-Calibre 10",
            "desc_botritis_12":"Desc. Botrytis-Calibre 12",
            "desc_botritis_14":"Desc. Botrytis-Calibre 14",
            "desc_botritis_16":"Desc. Botrytis-Calibre 16",
            "desc_botritis_18":"Desc. Botrytis-Calibre 18",
            "desc_botritis_20":"Desc. Botrytis-Calibre 20",
            "desc_botritis_22":"Desc. Botrytis-Calibre 22",
            "desc_botritis_24":"Desc. Botrytis-Calibre 24",

            "desc_cochinilla_4":"Desc. Cochinilla-Calibre 4",
            "desc_cochinilla_5":"Desc. Cochinilla-Calibre 5",
            "desc_cochinilla_6":"Desc. Cochinilla-Calibre 6",
            "desc_cochinilla_7":"Desc. Cochinilla-Calibre 7",
            "desc_cochinilla_8":"Desc. Cochinilla-Calibre 8",
            "desc_cochinilla_9":"Desc. Cochinilla-Calibre 9",
            "desc_cochinilla_10":"Desc. Cochinilla-Calibre 10",
            "desc_cochinilla_12":"Desc. Cochinilla-Calibre 12",
            "desc_cochinilla_14":"Desc. Cochinilla-Calibre 14",
            "desc_cochinilla_16":"Desc. Cochinilla-Calibre 16",
            "desc_cochinilla_18":"Desc. Cochinilla-Calibre 18",
            "desc_cochinilla_20":"Desc. Cochinilla-Calibre 14",
            "desc_cochinilla_22":"Desc. Cochinilla-Calibre 16",
            "desc_cochinilla_24":"Desc. Cochinilla-Calibre 18",

            "desc_pudricion_4":"Desc. Pudricion-Calibre 4",
            "desc_pudricion_5":"Desc. Pudricion-Calibre 5",
            "desc_pudricion_6":"Desc. Pudricion-Calibre 6",
            "desc_pudricion_7":"Desc. Pudricion-Calibre 7",
            "desc_pudricion_8":"Desc. Pudricion-Calibre 8",
            "desc_pudricion_9":"Desc. Pudricion-Calibre 9",
            "desc_pudricion_10":"Desc. Pudricion-Calibre 10",
            "desc_pudricion_12":"Desc. Pudricion-Calibre 12",
            "desc_pudricion_14":"Desc. Pudricion-Calibre 14",
            "desc_pudricion_16":"Desc. Pudricion-Calibre 16",
            "desc_pudricion_18":"Desc. Pudricion-Calibre 18",
            "desc_pudricion_20":"Desc. Pudricion-Calibre 20",
            "desc_pudricion_22":"Desc. Pudricion-Calibre 22",
            "desc_pudricion_24":"Desc. Pudricion-Calibre 24",

            "desc_rajadasae_4":"Desc. Rajadas Arilo Expuesto-Calibre 4",
            "desc_rajadasae_5":"Desc. Rajadas Arilo Expuesto-Calibre 5",
            "desc_rajadasae_6":"Desc. Rajadas Arilo Expuesto-Calibre 6",
            "desc_rajadasae_7":"Desc. Rajadas Arilo Expuesto-Calibre 7",
            "desc_rajadasae_8":"Desc. Rajadas Arilo Expuesto-Calibre 8",
            "desc_rajadasae_9":"Desc. Rajadas Arilo Expuesto-Calibre 9",
            "desc_rajadasae_10":"Desc. Rajadas Arilo Expuesto-Calibre 10",
            "desc_rajadasae_12":"Desc. Rajadas Arilo Expuesto-Calibre 12",
            "desc_rajadasae_14":"Desc. Rajadas Arilo Expuesto-Calibre 14",
            "desc_rajadasae_16":"Desc. Rajadas Arilo Expuesto-Calibre 16",
            "desc_rajadasae_18":"Desc. Rajadas Arilo Expuesto-Calibre 18",
            "desc_rajadasae_20":"Desc. Rajadas Arilo Expuesto-Calibre 20",
            "desc_rajadasae_22":"Desc. Rajadas Arilo Expuesto-Calibre 22",
            "desc_rajadasae_24":"Desc. Rajadas Arilo Expuesto-Calibre 24",


          
        }


class evcalcontroldescartegrica2022form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(evcalcontroldescartegrica2022form, self).__init__(*args, **kwargs)
        
        self.fields['fecha_proceso'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_linea'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['controlador_prod'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        
    class Meta:
        model = EvCalControlDescarteGrIca2022
        fields = [
            
            'fecha_proceso',
            'anexo_linea',
            'controlador_prod',
            
        ]

        labels={

            "fecha_proceso":"Fecha Proceso",
            "anexo_linea":"Linea",
            "controlador_prod":"Controlador Produccion",
            
        }


class detalleevcalcontroldescartegrica2022form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detalleevcalcontroldescartegrica2022form, self).__init__(*args, **kwargs)
        
        self.fields['hora_inspeccion'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['fecha_cosecha'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['anexo_proveedor']=forms.ModelChoiceField(label="Proveedor", queryset=fundo.objects.filter(zona=1))
        
        self.fields['anexo_proveedor'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=1))
        
        self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat1_exportable'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cat2_exportable'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['catind_exportable'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['rajadas_ae'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['rajadas_golpe'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['insolacion_fuerte'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['bajo_peso'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['danio_roedor'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['alternaria'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cochinilla'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['inmadures_verde'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['gelechi'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['hongo_corona'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['quereza'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['golpe_fuerte'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['botrytis'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['cicatriz'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['corona_deshidratada'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['rajada_severo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_mecanico_pl'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['danio_ave'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['deforme'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['golpe_fuerte_pl'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['insolacion_leve'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['manchas'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pudricion_corona'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['rajadas_hongos'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['rajadas_golpe_pl'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['russet'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        self.fields['arilo_pardo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['desh_severo_cuerpo'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        self.fields['pres_mosca_fruta'].widget.attrs.update({"placeholder":"","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})    
        
        
        
    class Meta:
        model = DetalleEvCalControlDescarteGrIca2022
        fields = [
            
            'hora_inspeccion',
            'fecha_cosecha',
            'anexo_proveedor',
            
            'anexo_variedad',
            'cat1_exportable',
            'cat2_exportable',
            'catind_exportable',
            'rajadas_ae',
            'rajadas_golpe',
            'insolacion_fuerte',
            'danio_mecanico',
            'bajo_peso',
            'danio_roedor',
            'alternaria',
            'cochinilla',
            'inmadures_verde',
            'gelechi',
            'pudricion',
            'hongo_corona',
            'quereza',
            'golpe_fuerte',

            'botrytis',
            'cicatriz',
            'corona_deshidratada',
            'rajada_severo',
            'danio_mecanico_pl',
            'danio_ave',
            'deforme',
            'golpe_fuerte_pl',
            'insolacion_leve',
            'manchas',
            'pudricion_corona',
            'rajadas_hongos',
            'rajadas_golpe_pl',
            'russet',

            'arilo_pardo',
            'desh_severo_cuerpo',
            'pres_mosca_fruta',
            

          
        ]

        labels={

            "hora_inspeccion":"Hora Inspeccion",
            "fecha_cosecha":"Fecha Cosecha",
            "anexo_proveedor":"Proveedor",
            "anexo_variedad":"Variedad",
            "cat1_exportable":"Cat 1- Exportable",
            "cat2_exportable":"Cat 2- Exportable",
            "catind_exportable":"Cat Ind. Exportable",
            "rajadas_ae":"Rajados con arilo expuesto",
            "rajadas_golpe":"Rajados por golpe",
            "insolacion_fuerte":"Insolacion Fuerte",
            "danio_mecanico":"Daño mecanico",
            "bajo_peso":"Bajo peso",
            "danio_roedor":"Daño por roedor",
            "alternaria":"Presencia de Alternaria",
            "cochinilla":"Presencia de Cochinilla",
            "inmadures_verde":"Inmadurez verde",
            "gelechi":"Gelechiidae",
            "pudricion":"Pudricion",
            "hongo_corona":"Hongo Corona",
            "quereza":"Quereza",
            "golpe_fuerte":"Golpe Fuerte",
            
            "botrytis":"Botrytis",
            "cicatriz":"Cicatriz",
            "corona_deshidratada":"Corona Deshidratado",
            "rajada_severo":"Rajada Severo",
            "danio_mecanico_pl":"Daño Mecanico PLanta",
            "danio_ave":"Daño por Ave",
            "deforme":"Deforme",
            "golpe_fuerte_pl":"GOlpe fuerte Planta",
            "insolacion_leve":"INsolacion Leve",
            "manchas":"Manchas",
            "pudricion":"Pudricion",
            "rajadas_hongos":"Rajadas con hongos",
            "rajadas_golpe_pl":"Rajadas Golpe Planta",
            "russet":"Russet",

            "arilo_pardo":"Arilo Pardo",
            "desh_severo_cuerpo":"Deshidratado Severo Cuerpo",
            "pres_mosca_fruta":"Presencia Mosca Fruta",
            
        }


class evcalcontroldescartearica2022form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(evcalcontroldescartearica2022form, self).__init__(*args, **kwargs)
        
        self.fields['fecha_proceso'].widget.attrs.update({"placeholder":"Fecha Proceso","required":"true","data-error-message":"Fecha Requerida","class":"form-control"})
        self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"Turno requerido","class":"form-control"})
        self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo","required":"true","data-error-message":"Tipo requerido","class":"form-control"})
        self.fields['anexo_fundo']=forms.ModelChoiceField(label="Fundo", queryset=MaestraFundoCultivo.objects.filter(anexo_cultivo=2))
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Fundo requerido","class":"form-control"})
        self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=2))
        self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad","required":"true","data-error-message":"Variedad requerida","class":"form-control"})
        self.fields['ticket'].widget.attrs.update({"placeholder":"Ticket","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
        self.fields['cantidad_muestra'].widget.attrs.update({"placeholder":"Cantidad de Muestra","required":"true","data-error-message":"Cantidad requerida","class":"form-control"})
        
    class Meta:
        model = EvCalControlDescarteAr2022
        fields = [
            'fecha_proceso',
            'anexo_turno',
            'anexo_tipo',
            'anexo_fundo',
            'anexo_variedad',
            'ticket',
            'fecha_cosecha',
            'cantidad_muestra',
        ]
        labels={
            "fecha_proceso":"Fecha Proceso",
            "anexo_turno":"Turno",
            "anexo_tipo":"Tipo",
            "anexo_fundo":"Fundo",
            "anexo_variedad":"Variedad",
            "ticket":"Ticket",
            "fecha_cosecha":"Fecha Cosecha",
            "cantidad_muestra":"Cantidad de Muestra (gr)",
        }


class detalleevcalcontroldescartearica2022form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detalleevcalcontroldescartearica2022form, self).__init__(*args, **kwargs)

        self.fields['exportable1'].widget.attrs.update({"placeholder":"< 12 mm","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['exportable2'].widget.attrs.update({"placeholder":"12-14 mm","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['exportable2_5'].widget.attrs.update({"placeholder":"14-17 mm","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['exportable3'].widget.attrs.update({"placeholder":"17-20 mm","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['exportable4'].widget.attrs.update({"placeholder":"> 20 mm","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

        self.fields['condicion1'].widget.attrs.update({"placeholder":"Pudrición","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion2'].widget.attrs.update({"placeholder":"Blando","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion3'].widget.attrs.update({"placeholder":"Micelio Fruto","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion4'].widget.attrs.update({"placeholder":"Heridas","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion5'].widget.attrs.update({"placeholder":"Deshidratado","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion6'].widget.attrs.update({"placeholder":"Desgarro","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion7'].widget.attrs.update({"placeholder":"Desgarro Protuberancia","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion8'].widget.attrs.update({"placeholder":"Exudación","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion9'].widget.attrs.update({"placeholder":"Micelio Flores","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion10'].widget.attrs.update({"placeholder":"Daño Mecanico","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion11'].widget.attrs.update({"placeholder":"Daño por Ave","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion12'].widget.attrs.update({"placeholder":"Machucon","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion13'].widget.attrs.update({"placeholder":"Machucon","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['condicion14'].widget.attrs.update({"placeholder":"Machucon","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

        self.fields['calidad1'].widget.attrs.update({"placeholder":"Polvo / Tierra","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad2'].widget.attrs.update({"placeholder":"Excretas / Aves","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad3'].widget.attrs.update({"placeholder":"Polen / Excreta de Abeja","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad4'].widget.attrs.update({"placeholder":"Deformes","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad5'].widget.attrs.update({"placeholder":"Russet / Cicatriz","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad6'].widget.attrs.update({"placeholder":"Presencia de Pedicelo","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad7'].widget.attrs.update({"placeholder":"Resto Floral","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad8'].widget.attrs.update({"placeholder":"Fruta Plana / Quemadura","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad9'].widget.attrs.update({"placeholder":"Fruta Inamadura Verde","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad10'].widget.attrs.update({"placeholder":"Fruta Inmadura Rojizo","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad11'].widget.attrs.update({"placeholder":"Bajo Calibre","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad12'].widget.attrs.update({"placeholder":"Material Extraño","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['calidad13'].widget.attrs.update({"placeholder":"Material Extraño","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

        self.fields['fitosanitario1'].widget.attrs.update({"placeholder":"Cochinilla","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['fitosanitario2'].widget.attrs.update({"placeholder":"Picadura_Insecto","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['fitosanitario3'].widget.attrs.update({"placeholder":"Picadura_Larva","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['fitosanitario4'].widget.attrs.update({"placeholder":"Mosca de la Fruta","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        self.fields['fitosanitario5'].widget.attrs.update({"placeholder":"Arañas","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        
    class Meta:
        model = DetalleEvCalControlDescarteAr2022
        fields = [
            'exportable1',
            'exportable2',
            'exportable2_5',
            'exportable3',
            'exportable4',
            'condicion1',
            'condicion2',
            'condicion3',
            'condicion4',
            'condicion5',
            'condicion6',
            'condicion7',
            'condicion8',
            'condicion9',
            'condicion10',
            'condicion11',
            'condicion12',
            'condicion13',
            'condicion14',
            'calidad1',
            'calidad2',
            'calidad3',
            'calidad4',
            'calidad5',
            'calidad6',
            'calidad7',
            'calidad8',
            'calidad9',
            'calidad10',
            'calidad11',
            'calidad12',
            'calidad13',
            'fitosanitario1',
            'fitosanitario2',
            'fitosanitario3',
            'fitosanitario4',
            'fitosanitario5',
        ]

        labels={
            "exportable1":"Export < 12 mm",
            "exportable2":"Export 12-14 mm",
            "exportable2_5":"Export 14-17 mm",
            "exportable3":"Export 17-20 mm",
            "exportable4":"Export > 20 mm",
            "condicion1":"Cond. Pudrición",
            "condicion2":"Cond. Blando",
            "condicion3":"Cond. Micelio Fruto",
            "condicion4":"Cond. Heridas",
            "condicion5":"Cond. Deshidratado",
            "condicion6":"Cond. Desgarro",
            "condicion7":"Cond. Desgarro Protuberancia",
            "condicion8":"Cond. Exudación",
            "condicion9":"Cond. Micelio Flores",
            "condicion10":"Cond. Daño Mecanico",
            "condicion11":"Cond. Daño por Ave",
            "condicion12":"Cond. Machucon",
            "condicion13":"Cond. Partidura",
            "condicion14":"Cond. Globito",
            "calidad1":"Cal. Polvo / Tierra",
            "calidad2":"Cal. Excretas / Aves",
            "calidad3":"Cal. Polen / Excreta de Abeja",
            "calidad4":"Cal. Deformes",
            "calidad5":"Cal. Russet / Cicatriz",
            "calidad6":"Cal. Presencia de Pedicelo",
            "calidad7":"Cal. Resto Floral",
            "calidad8":"Cal. Fruta Plana / Quemadura",
            "calidad9":"Cal. Fruta Inmadura Verde",
            "calidad10":"Cal. Fruta Inmadura Rojizo",
            "calidad11":"Cal. Bajo Calibre",
            "calidad12":"Cal. Material Extraño",
            "calidad13":"Cal. Decoloración",
            "fitosanitario1":"Fito Cochinilla",
            "fitosanitario2":"Fito Picadura Insecto",
            "fitosanitario3":"Fito Picadura Larva",
            "fitosanitario4":"Fito Mosca de la Fruta",
            "fitosanitario5":"Fito Arañas",
        }

class evcontroldescartear2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evcontroldescartear2022form, self).__init__(*args, **kwargs)
        
		self.fields['fecha_proceso'].widget.attrs.update({"placeholder":"Fecha Proceso","required":"true","data-error-message":"Fecha Requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Fundo requerido","class":"form-control"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=2))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad","required":"true","data-error-message":"Variedad requerida","class":"form-control"})
        
	class Meta:
		model = EvControlDescarteAr202202
		fields = [
			'fecha_proceso',
			'anexo_fundo',
			'anexo_variedad',
		]
		labels={
			"fecha_proceso":"Fecha Proceso",
			"anexo_fundo":"Fundo",
			"anexo_variedad":"Variedad",
		}

class detalleevcontroldescartear2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(detalleevcontroldescartear2022form, self).__init__(*args, **kwargs)

		self.fields['fecha_cosecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Cosecha","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_fundo']=forms.ModelChoiceField(label="Fundo", queryset=MaestraFundoCultivo.objects.filter(anexo_cultivo=2))
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Fundo requerido","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"Turno requerido","class":"form-control"})

		self.fields['acopio1'].widget.attrs.update({"placeholder":"Muestreo","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['acopio2'].widget.attrs.update({"placeholder":"Muestreo","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

		self.fields['seleccion1'].widget.attrs.update({"placeholder":"Defectos","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['seleccion2'].widget.attrs.update({"placeholder":"Piso","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

		self.fields['calibrado1'].widget.attrs.update({"placeholder":"Calibre Menor","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['calibrado2'].widget.attrs.update({"placeholder":"Machucones","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['calibrado3'].widget.attrs.update({"placeholder":"Recuperable/Defectos","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['calibrado4'].widget.attrs.update({"placeholder":"Piso","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

		self.fields['empaque1'].widget.attrs.update({"placeholder":"Recuperable","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque2'].widget.attrs.update({"placeholder":"Defectos","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque3'].widget.attrs.update({"placeholder":"Machucones","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque4'].widget.attrs.update({"placeholder":"Piso","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque5'].widget.attrs.update({"placeholder":"Otros","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque6'].widget.attrs.update({"placeholder":"Otros","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['empaque7'].widget.attrs.update({"placeholder":"Otros","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})

		self.fields['calidad1'].widget.attrs.update({"placeholder":"Muestreo Línea","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
        
	class Meta:
		model = DetalleEvControlDescarteAr202202
		fields = [
			'fecha_cosecha',
			'anexo_fundo',
			'anexo_turno',
			'acopio1',
			'acopio2',
			'seleccion1',
			'seleccion2',
			'calibrado1',
			'calibrado2',
			'calibrado3',
			'calibrado4',
			'empaque1',
			'empaque2',
			'empaque3',
			'empaque4',
			'empaque5',
			'empaque6',
			'empaque7',
			'calidad1',
		]

		labels={
			"fecha_cosecha":"Fecha Cosecha",
			"anexo_fundo":"Fundo",
			"anexo_turno":"Turno",
			"acopio1":"ACOPIO: Muestreo",
			"acopio2":"ACOPIO: Otros",
			"seleccion1":"SELECCION: Defectos",
			"seleccion2":"SELECCION: Piso",
			"calibrado1":"CALIBRADO: Calibre Menor",
			"calibrado2":"CALIBRADO: Machucones",
			"calibrado3":"CALIBRADO: Recuperable/Defectos",
			"calibrado4":"CALIBRADO: Piso",
			"empaque1":"EMPAQUE: Recuperable",
			"empaque2":"EMPAQUE: Defectos",
			"empaque3":"EMPAQUE: Machucones",
			"empaque4":"EMPAQUE: Piso",
			"empaque5":"EMPAQUE: Otros",
			"empaque6":"EMPAQUE: Otros 1",
			"empaque7":"EMPAQUE: Otros 2",
			"calidad1":"CALIDAD: Muestreo Línea",
		}

class materialescalidadform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(materialescalidadform, self).__init__(*args, **kwargs)
		
		self.fields['marca'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['desc'].widget.attrs.update({"placeholder":"Ancho","data-required":"true","data-error-message":"Ancho requerida","class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Largo","data-required":"true","data-error-message":"Largo requerida","class":"form-control"})
		self.fields['anexo_alveolo'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['anexo_bolsa'].widget.attrs.update({"placeholder":"Cant. Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
				
		
	class Meta:
		model = MaterialesCalidad
		fields = [
			
			'marca',
			'desc',
			'peso',
			'anexo_alveolo',
			'anexo_bolsa',
			
			
		]

		labels={
			
			"marca":"Marca",
			"desc":"Descripcion Material",
			"peso":"Peso",
			"anexo_alveolo":"Tipo Alveolo",
			"anexo_bolsa":"TIpo de Bolsa",
			
		}

class evcalcontrolpesosgrica2022form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcalcontrolpesosgrica2022form, self).__init__(*args, **kwargs)
		
		self.fields['fecha_evaluacion'].widget.attrs.update({"autocomplete":"off","required":"true","class":"form-control"})
		self.fields['anexo_linea'].widget.attrs.update({"required":"true","data-error-message":"Ancho requerida","class":"form-control"})
		self.fields['supervisor'].widget.attrs.update({"placeholder":"Supervisor..","data-required":"true","data-error-message":"Largo requerida","class":"form-control"})
		self.fields['inspector'].widget.attrs.update({"placeholder":"Inspector..","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Sector..","required":"true","data-error-message":"Turno requerido","class":"form-control"})
				
		
	class Meta:
		model = EvCalControlPesosGrIca2022
		fields = [
			
			'fecha_evaluacion',
			'anexo_linea',
			'supervisor',
			'inspector',
			'anexo_turno',
			
		]

		labels={
			
			"fecha_evaluacion":"Fecha Evaluacion",
			"anexo_linea":"Linea Empaque",
			"supervisor":"Supervisor",
			"inspector":"Inspector",
			"anexo_turno":"Turno",
		}


class detalleevcalcontrolpesosgrica2022form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(detalleevcalcontrolpesosgrica2022form, self).__init__(*args, **kwargs)
		
		self.fields['anexo_presentacion'].widget.attrs.update({"required":"true","class":"form-control"})
		self.fields['marca'].widget.attrs.update({"placeholder":"Marca..","required":"true","data-error-message":"Marca requerida","class":"form-control"})
		
		self.fields['anexo_cliente']=forms.ModelChoiceField(label="Cliente", queryset=ClientesAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_cliente'].widget.attrs.update({"required":"true","data-error-message":"Cliente requerido","class":"form-control"})
		self.fields['hora_evaluacion'].widget.attrs.update({"required":"true","data-error-message":"Hora requerida","class":"form-control"})

		self.fields['anexo_calibre1']=forms.ModelChoiceField(label="Calibre-M1", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre1'].widget.attrs.update({"placeholder":"Primer Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		
		self.fields['peso_neto1'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre2']=forms.ModelChoiceField(label="Calibre-M2", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre2'].widget.attrs.update({"placeholder":"Segundo Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto2'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre3']=forms.ModelChoiceField(label="Calibre-M3", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre3'].widget.attrs.update({"placeholder":"Tercer Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto3'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre4']=forms.ModelChoiceField(label="Calibre-M4", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre4'].widget.attrs.update({"placeholder":"Cuarto Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto4'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre5']=forms.ModelChoiceField(label="Calibre-M5", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre5'].widget.attrs.update({"placeholder":"Quinto Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto5'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre6']=forms.ModelChoiceField(label="Calibre-M6", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre6'].widget.attrs.update({"placeholder":"Sexto Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto6'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre7']=forms.ModelChoiceField(label="Calibre-M7", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre7'].widget.attrs.update({"placeholder":"Septimo Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto7'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre8']=forms.ModelChoiceField(label="Calibre-M8", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre8'].widget.attrs.update({"placeholder":"Octavo Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto8'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre9']=forms.ModelChoiceField(label="Calibre-M9", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre9'].widget.attrs.update({"placeholder":"Noveno Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto9'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
		
		self.fields['anexo_calibre10']=forms.ModelChoiceField(label="Calibre-M10", queryset=CalibresAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_calibre10'].widget.attrs.update({"placeholder":"Decimo Anexo..","required":"true","data-error-message":"Anexo requerido","class":"form-control"})
		self.fields['peso_neto10'].widget.attrs.update({"placeholder":"Peso Neto..","required":"true","data-error-message":"Peso Neto requerido","class":"form-control"})
				
		
	class Meta:
		model = DetalleEvCalControlPesosGrIca2022
		fields = [
			
	
			'anexo_presentacion',
			'anexo_cliente',
			'marca',
			'hora_evaluacion',
			'anexo_calibre1',
			'peso_neto1',
			'anexo_calibre2',
			'peso_neto2',
			'anexo_calibre3',
			'peso_neto3',
			'anexo_calibre4',
			'peso_neto4',
			'anexo_calibre5',
			'peso_neto5',
			'anexo_calibre6',
			'peso_neto6',
			'anexo_calibre7',
			'peso_neto7',
			'anexo_calibre8',
			'peso_neto8',
			'anexo_calibre9',
			'peso_neto9',
			'anexo_calibre10',
			'peso_neto10',
			
			
		]

		labels={
			
	
			"anexo_presentacion":"Presentacion",
			"anexo_cliente":"Cliente",
			"marca":"Marca",
			"hora_evaluacion":"Hora",
			"supervisor":"Supervisor",
			"inspector":"Inspector",
			"anexo_calibre1":"Primer Anexo",
			"pesoneto1" : "Peso Neto",
			"anexo_calibre2":"Segundo Anexo",
			"pesoneto2" : "Peso Neto",
			"anexo_calibre3":"Tercer Anexo",
			"pesoneto3" : "Peso Neto",
			"anexo_calibre4":"Cuarto Anexo",
			"pesoneto4" : "Peso Neto",
			"anexo_calibre5":"Quinto Anexo",
			"pesoneto5" : "Peso Neto",
			"anexo_calibre6":"Sexto Anexo",
			"pesoneto6" : "Peso Neto",
			"anexo_calibre7":"Septimo Anexo",
			"pesoneto7" : "Peso Neto",
			"anexo_calibre8":"Octavo Anexo",
			"pesoneto8" : "Peso Neto",
			"anexo_calibre9":"Noveno Anexo",
			"pesoneto9" : "Peso Neto",
			"anexo_calibre10":"Decimo Anexo",
			"pesoneto10" : "Peso Neto",
			
			
		}

class evplantonesplnaz2022form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(evplantonesplnaz2022form, self).__init__(*args, **kwargs)
        
        self.fields['anexo_fundo'].widget.attrs.update({"autocomplete":"off","data-error-message":"Fundo Requerido","required":"true","class":"form-control"})
        self.fields['fecha_evaluacion'].widget.attrs.update({"required":"true","data-error-message":"Fecha de evaluación requerida","class":"form-control"})
        self.fields['anexo_produccion'].widget.attrs.update({"placeholder":"Lote..","required":"true","data-error-message":"Lote requerido","class":"form-control"})
        self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Sector..","required":"true","data-error-message":"Sector requerido","class":"form-control"})
        self.fields['hora_evaluacion'].widget.attrs.update({"required":"true","data-error-message":"Hora de evaluación requerida","class":"form-control"})
        self.fields['supervisor'].widget.attrs.update({"placeholder":"Supervisor..","required":"true","data-error-message":"Supervidor requerido","class":"form-control"})
        self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad..","required":"true","data-error-message":"Variedad requerida","class":"form-control"})
        self.fields['n_personas'].widget.attrs.update({"placeholder":"N° Personas..","required":"true","data-error-message":"N° personas requeridas","class":"form-control"})
        
    class Meta:
        model = EvPlantonesPlNaz2022
        fields = [
            
            'anexo_fundo',
            'fecha_evaluacion',
            'anexo_produccion',
            'anexo_turno',
            'hora_evaluacion',
            'supervisor',
            'anexo_variedad',
            'n_personas',
            
        ]

        labels={
            
            "anexo_fundo":"Fundo",
            "fecha_evaluacion":"Fecha Evaluación",
            "anexo_produccion":"Lote",
            "anexo_turno":"Sector",
            "hora_evaluacion":"Hora Evaluación",
            "supervisor":"Supervisor",
            "anexo_variedad":"Variedad",
            "n_personas":"N° Personas Sembrando",
            
        }


class detalleevplantonesplnaz2022form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detalleevplantonesplnaz2022form, self).__init__(*args, **kwargs)
        
        self.fields['nombres'].widget.attrs.update({"placeholder":"Nombres..","required":"true","class":"form-control"})
        self.fields['primera_ausencia'].widget.attrs.update({"placeholder":"Primera ausencia..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['segunda_ausencia'].widget.attrs.update({"placeholder":"Segunda ausencia..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['tercera_ausencia'].widget.attrs.update({"placeholder":"Tercera ausencia..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['presencia_planta'].widget.attrs.update({"placeholder":"Presencia de la planta..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['presencia_suelo'].widget.attrs.update({"placeholder":"Presencia del suelo..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['siembra_profunda'].widget.attrs.update({"placeholder":"Siembra profunda..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['tutor_posicionado'].widget.attrs.update({"placeholder":"Tutor posicionado..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['buen_siembra'].widget.attrs.update({"placeholder":"Buen siembra..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['promedio_planta'].widget.attrs.update({"placeholder":"Promedio de planta..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        self.fields['observacion'].widget.attrs.update({"placeholder":"Observaciones..","required":"true","data-error-message":"Captación requerida","class":"form-control"})
        
        
    class Meta:
        model = DetalleEvPlantonesPlNaz2022
        fields = [
            
            'nombres',
            'primera_ausencia',
            'segunda_ausencia',
            'tercera_ausencia',
            'presencia_planta',
            'presencia_suelo',
            'siembra_profunda',
            'tutor_posicionado',
            'buen_siembra',
            'promedio_planta',
            'observacion',
            
        ]

        labels={
            
    
            "nombres":"Nombres",
            "primera_ausencia":"Ausencia de primera compactación",
            "segunda_ausencia":"Ausencia de segunda compactación",
            "tercera_ausencia":"Ausencia de tercera comptación",
            "presencia_planta":"Presencia de planta inclinada",
            "presencia_suelo":"Presencia de suelo mal compactado",
            "siembra_profunda":"Siembra profunda",
            "tutor_posicionado" : "Tutor bien posicionado",
            "buen_siembra":"Buen siembra",
            "promedio_planta" : "Promedio planta",
            "observacion":"Observación",
            
        }


#CARTILLA EV MUESTRA CAJAS EMPACADAS GR2022
class evcalmuestracajasempacadasgr2022form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(evcalmuestracajasempacadasgr2022form, self).__init__(*args, **kwargs)

        self.fields['fecha_evaluacion'].widget.attrs.update({"placeholder":"...","autocomplete":"off","required":"true","data-error-message":"Fecha de evaluación requerida","class":"form-control"})
        self.fields['responsable'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Responsable requerido","class":"form-control"})
        self.fields['npalet'].widget.attrs.update({"placeholder":"...","autocomplete":"off","required":"true","data-error-message":"Npalet requerido","class":"form-control"})
        self.fields['hora_inspeccion'].widget.attrs.update({"placeholder":"...","autocomplete":"off","required":"true","data-error-message":"Hora de Inspección requerido","class":"form-control"})
        self.fields['anexo_categoria'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Categoria requerida","class":"form-control"})
        self.fields['marca_caja'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Marca de Caja requerida","class":"form-control"})
        self.fields['variedad'].widget.attrs.update({"readonly":"true","placeholder":"...","autocomplete":"off","data-error-message":"Variedad Requerida","required":"true","class":"form-control"})
        self.fields['anexo_calibre'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Calibre requerido","class":"form-control"})
        self.fields['marca'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Marca requerida","class":"form-control"})
        self.fields['marca_sticker'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Marca de Sticker requerida","class":"form-control"})
        self.fields['proveedor'].widget.attrs.update({"readonly":"true","placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Proveedor requerido","class":"form-control"})
        self.fields['fecha_cosecha'].widget.attrs.update({"readonly":"true","placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Fecha de Cosecha requerida","class":"form-control"})
        self.fields['anexo_corte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Corte requerida","class":"form-control"})
        self.fields['peso_neto'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Peso neto requerido","class":"form-control"})
        self.fields['anexo_sobrepeso'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Sobrepeso requerido","class":"form-control"})
        
    class Meta:
        model = EvMuestrasCajasEmpacadasGR2022
        fields = [
            
            'fecha_evaluacion',
            'responsable',
            'npalet',
            'hora_inspeccion',
            'anexo_categoria',
            'marca_caja',
            'variedad',
            'anexo_calibre',
            'marca',
            'marca_sticker',
            'proveedor',
            'fecha_cosecha',
            'anexo_corte',
            'peso_neto',
            'anexo_sobrepeso',
            
        ]

        labels={
            
            "fecha_evaluacion":"Fecha de Evaluación",
            "responsable":"Responsable / Supervisor",
            "npalet":"N° de Palet",
            "hora_inspeccion":"Hora de Inspección",
            "anexo_categoria":"Categoria",
            "marca_caja":"Marca de Caja",
            "variedad":"Variedad",
            "anexo_calibre":"Calibre",
            "marca":"Marca / Tipo de Bolsa AM",
            "marca_sticker":"Marca de Sticker",
            "proveedor":"Proveedor",
            "fecha_cosecha":"Fecha de Cosecha",
            "anexo_corte":"Corte en Corona",
            "peso_neto":"Peso Neto de Caja",
            "anexo_sobrepeso":"Sobrepeso",
            
        }


class detalleevcalmuestracajasempacadasgr2022form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        variableCategoria=kwargs.pop("variable_categoria")
        super(detalleevcalmuestracajasempacadasgr2022form, self).__init__(*args, **kwargs)
        
        self.fields['cicatriz_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['danio_roce_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['deformes_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['insolacion_leve_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['libre_defectos_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['manchas_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['rajaduras_cat1'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['suma_cat1'].widget.attrs.update({"placeholder":"....","readonly":"true","autocomplete":"off","required":"true","data-error-message":"Error de Suma","class":"form-control"})

        self.fields['insolacion_moderada_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['cicatriz_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['corona_deshidratada_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['danio_mecanico_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['danio_roce_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['golpe_leve_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['manchas_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['rajaduras_cat2'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['suma_cat2'].widget.attrs.update({"placeholder":"....","readonly":"true","autocomplete":"off","required":"true","data-error-message":"Error de Suma","class":"form-control"})

        self.fields['cicatriz_industrial'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['danio_roce_industrial'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['manchas_industrial'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['rajaduras_industrial'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['suma_industrial'].widget.attrs.update({"placeholder":"....","readonly":"true","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})

        self.fields['arilo_expuesto_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['corona_deshidratada_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['danio_plagas_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['golpe_fuerte_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['insolado_fuerte_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['pudricion_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['rajados_severos_descarte'].widget.attrs.update({"placeholder":"....","autocomplete":"off","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        self.fields['suma_descarte'].widget.attrs.update({"placeholder":"....","readonly":"true","autocomplete":"off","required":"true","data-error-message":"Error de Suma","class":"form-control"})

        self.fields['unidades_totales_muestreadas'].widget.attrs.update({"placeholder":"....","autocomplete":"off","readonly":"true","required":"true","data-error-message":"Dato requerido","class":"form-control"})
        
    class Meta:
        model = DetalleEvMuestrasCajasEmpacadasGR2022
        fields = [
            
            'cicatriz_cat1',
            'danio_roce_cat1',
            'deformes_cat1',
            'insolacion_leve_cat1',
            'libre_defectos_cat1',
            'manchas_cat1',
            'rajaduras_cat1',
            'suma_cat1',
            'insolacion_moderada_cat2',
            'cicatriz_cat2',
            'corona_deshidratada_cat2',
            'danio_mecanico_cat2',
            'danio_roce_cat2',
            'golpe_leve_cat2',
            'manchas_cat2',
            'rajaduras_cat2',
            'suma_cat2',
            'cicatriz_industrial',
            'danio_roce_industrial',
            'manchas_industrial',
            'rajaduras_industrial',
            'suma_industrial',
            'arilo_expuesto_descarte',
            'corona_deshidratada_descarte',
            'danio_plagas_descarte',
            'golpe_fuerte_descarte',
            'insolado_fuerte_descarte',
            'pudricion_descarte',
            'rajados_severos_descarte',
            'suma_descarte',
            'unidades_totales_muestreadas',
            
        ]

        labels={
            
    
            "cicatriz_cat1":"Cicatrices < 25%",
            "danio_roce_cat1":"Daño por Roce < 10%",
            "deformes_cat1":"Deformes",
            "insolacion_leve_cat1":"Insolación Leve",
            "libre_defectos_cat1":"Libre de Defectos",
            "manchas_cat1":"Manchas < 25%",
            "rajaduras_cat1":"Rajaduras < 1%",
            "suma_cat1" : "Suma CAT1",
            "insolacion_moderada_cat2":"Insolación Moderada",
            "cicatriz_cat2" : "Cicatrices > 25%",
            "corona_deshidratada_cat2":"Corona Deshidradata Leve",
            "danio_mecanico_cat2":"Daño Mecanico",
            "danio_roce_cat2":"Daño por Roce > 10%",
            "golpe_leve_cat2":"Golpe Leve",
            "manchas_cat2":"Manchas > 25%",
            "rajaduras_cat2":"Rajaduras < 3%",
            "suma_cat2":"Suma CAT2",
            "insolacion_moderada_cat2_porc":"Insolación Moderada",
            "cicatriz_industrial":"Cicactrices > 50%",
            "danio_roce_industrial" : "Daño por Roce > 30%",
            "manchas_industrial":"Manchas > 50%",
            "rajaduras_industrial" : "Rajaduras > 3%",
            "suma_industrial":"Suma CAT INDUSTRIAL",
            "arilo_expuesto_descarte":"Arilo Expuesto",
            "corona_deshidratada_descarte":"Corona Deshidratada",
            "danio_plagas_descarte":"Daño por Plagas",
            "golpe_fuerte_descarte":"Golpe Fuerte",
            "insolado_fuerte_descarte":"Insolado Fuerte",
            "pudricion_descarte":"Pudrición",
            "rajados_severos_descarte":"Rajados Severos",
            "suma_descarte" : "Suma DESCARTE",
            "unidades_totales_muestreadas":"UNID. TOT. MUESTREADAS",
            
        }

class evcontroldescartegr2022form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evcontroldescartegr2022form, self).__init__(*args, **kwargs)
		
		self.fields['fecha_proceso'].widget.attrs.update({"autocomplete":"off","required":"true","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"required":"true","data-error-message":"Dato requerido","class":"form-control"})
		#self.fields['material']=forms.ModelChoiceField(label="Material", queryset=MaterialMMPP.objects.filter(anexo_cultivo=1))
		self.fields['material'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['santiaguillo'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['santiago_apostol'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['los_pobres'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['macacara'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['santa_filomena'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['parcelas'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['sojo'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['las_dunas'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['lindero'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['caylan'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['total_descarte'].widget.attrs.update({"placeholder":"..","readonly":"true","required":"true","data-error-message":"Dato requerido","class":"form-control"})		
		
	class Meta:
		model = EvControlDescarteGR2022
		fields = [
			
			'fecha_proceso',
			'anexo_turno',
			'material',
			'santiaguillo',
			'santiago_apostol',
			'los_pobres',
			'macacara',
			'santa_filomena',
			'parcelas',
			'sojo',
			'las_dunas',
			'lindero',
			'caylan',
			'total_descarte',
		]

		labels={
			
			"fecha_proceso":"Fecha Proceso",
			"anexo_turno":"Turno",
			"material":"Material",
			"santiaguillo":"Santiaguillo",
			"santiago_apostol":"Santiago Apostol",
			"los_pobres":"Los Pobres",
			"macacara":"Macacara",
			"santa_filomena":"Santa Filomena",
			"parcelas":"Parcelas",
			"sojo":"Sojo",
			"las_dunas":"Las Dunas",
			"lindero":"Lindero",
			"caylan":"Caylan",
			"total_descarte":"Total Descarte",
		}

#EV RAMAS ARANDANOS
class evfenramasarandanosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenramasarandanosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"autocomplete":"off","placeholder":"Zona","required":"true","data-error-message":"Zona requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"autocomplete":"off","placeholder":"Fundo","required":"true","data-error-message":"Fundo requerido","class":"form-control"})
		self.fields['ubicacion'].widget.attrs.update({"autocomplete":"off","placeholder":"PEP","required":"true","data-error-message":"PEP requerido","class":"form-control"})
		self.fields['valvula'].widget.attrs.update({"autocomplete":"off","placeholder":"Valvula","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"autocomplete":"off","placeholder":"Tipo evaluacion","data-required":"true","data-error-message":"Tipo evaluacion requerida","class":"form-control"})
		
	class Meta:
		model = EvFenRamasArandanos
		fields = [
			'fecha',
			'anexo_zona',
			'anexo_fundo',
			'ubicacion',
			'valvula',
			'anexo_tipo',
		]

		labels={
			"fecha":"Fecha",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"ubicacion":"PEP",
			"valvula":"Valvula",
			"anexo_tipo":"Tipo Evaluacion",
		}

class evfenramasdetalleplantaform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(evfenramasdetalleplantaform, self).__init__(*args, **kwargs)
		
		self.fields['n_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Planta","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['cant_ramas'].widget.attrs.update({"autocomplete":"off","placeholder":"Cantidad de Ramas","data-required":"true","data-error-message":"Cantidad Ramas requerida","class":"form-control"})
		self.fields['ramas_produccion'].widget.attrs.update({"autocomplete":"off","placeholder":"Ramas en Produccion","data-required":"true","data-error-message":"Ramas en produccion requerida","class":"form-control"})
		self.fields['tira_savia'].widget.attrs.update({"autocomplete":"off","placeholder":"Tira Savia","data-required":"true","data-error-message":"Tira savia requerida","class":"form-control"})
		
	class Meta:
		model = DetallePlantaEvFenRamasArandanos
		fields = [
			'n_planta',
			'cant_ramas',
			'ramas_produccion',
			'tira_savia',
		]

		labels={
			"n_planta":"N° Planta",
			"cant_ramas":"Cantidad de Ramas",
			"ramas_produccion":"Ramas en Produccion",
			"tira_savia":"Tira Savia",
		}

class ramaplantaevfenform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ramaplantaevfenform, self).__init__(*args, **kwargs)
		self.fields['anexo_diametro'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Cuadrante","required":"true","data-error-message":"Diametro requerida","class":"form-control"})
		self.fields['diametro'].widget.attrs.update({"autocomplete":"off","placeholder":"Diametro","data-required":"true","data-error-message":"Diametro requerida","class":"form-control"})
		self.fields['altura'].widget.attrs.update({"autocomplete":"off","placeholder":"Altura","data-required":"true","data-error-message":"Altura requerida","class":"form-control"})
		self.fields['num_ramas'].widget.attrs.update({"autocomplete":"off","placeholder":"Numero ramas","data-required":"true","data-error-message":"Numero ramas requerida","class":"form-control"})
		self.fields['primera_poda'].widget.attrs.update({"autocomplete":"off","placeholder":"Primera poda","data-required":"true","data-error-message":"Primera poda requerida","class":"form-control"})
		self.fields['segunda_poda'].widget.attrs.update({"autocomplete":"off","placeholder":"Segunda poda","data-required":"true","data-error-message":"Segunda poda requerida","class":"form-control"})
		self.fields['tercera_poda'].widget.attrs.update({"autocomplete":"off","placeholder":"Tercera poda","data-required":"true","data-error-message":"Tercera poda requerida","class":"form-control"})
		self.fields['cuarta_poda'].widget.attrs.update({"autocomplete":"off","placeholder":"Cuarta poda","data-required":"true","data-error-message":"Cuarta poda requerida","class":"form-control"})
		self.fields['quinta_poda'].widget.attrs.update({"autocomplete":"off","placeholder":"Quinta poda","data-required":"true","data-error-message":"Quinta poda requerida","class":"form-control"})
		self.fields['longitud'].widget.attrs.update({"autocomplete":"off","placeholder":"Longitud","readonly":"true","required":"false","data-error-message":"Ingresa Longitud","class":"form-control"})
		self.fields['latitud'].widget.attrs.update({"autocomplete":"off","placeholder":"Latitud","readonly":"true","required":"false","data-error-message":"Ingresa Latitud","class":"form-control"})

	class Meta:
		model = RamaPlantaEvFenRamasArandanos
		fields = [
			'anexo_diametro',
			'diametro',
			'altura',
			'num_ramas',
			'primera_poda',
			'segunda_poda',
			'tercera_poda',
			'cuarta_poda',
			'quinta_poda',
			'longitud',
			'latitud',
		]

		labels={
			"anexo_diametro": "N° Cuadrante",
			"diametro":"Diametro de Rama",
			"altura":"Altura",
			"num_ramas":"Número de Ramas",
			"primera_poda":"<4mm",
			"segunda_poda":"4-5mm",
			"tercera_poda":"<5mm",
			"cuarta_poda":"5-8mm",
			"quinta_poda":">8mm",
			"longitud":"Longitud",
			"latitud":"Latitud",
		}

class evcamarashumedasform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evcamarashumedasform, self).__init__(*args, **kwargs)
				
		self.fields['anexo_tipo_evaluacion'].widget.attrs.update({"placeholder":"Tipo Evaluacion","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_zona'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_pep'].widget.attrs.update({"placeholder":"PEP","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['sub_lote'].widget.attrs.update({"placeholder":"Sub lote","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['fecha_instalacion'].widget.attrs.update({"placeholder":"Fecha de Instalacion","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['muestra'].widget.attrs.update({"placeholder":"Muestra","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(Q(cul=2)|Q(cul=6)))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_condicion'].widget.attrs.update({"placeholder":"Condicion","class":"form-control"})
		self.fields['anexo_organo'].widget.attrs.update({"placeholder":"Organo","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['anexo_ubicacion'].widget.attrs.update({"placeholder":"Ubicacion","class":"form-control"})
		self.fields['anexo_producto'].widget.attrs.update({"placeholder":"Producto","class":"form-control"})
		self.fields['anexo_producto2'].widget.attrs.update({"placeholder":"Producto","class":"form-control"})
		self.fields['dias_aplicacion'].widget.attrs.update({"placeholder":"Muestra","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
	class Meta:
		model = EvCamarasHumedas
		fields = [
			'anexo_tipo_evaluacion',
			'anexo_zona',
			'anexo_fundo',
			'anexo_pep',
			'sub_lote',
			'fecha_instalacion',
			'muestra',
			'anexo_variedad',
			'anexo_condicion',
			'anexo_organo',
			'anexo_ubicacion',
			'anexo_producto',
			'anexo_producto2',
			'dias_aplicacion',
		]
		labels={
			"anexo_tipo_evaluacion":"Tipo Evaluación",
			"anexo_zona":"Zona",
			"anexo_fundo":"Fundo",
			"anexo_pep":"PEP",
			"sub_lote":"Sub Lote",
			"fecha_instalacion":"Fecha de Instalación",
			"muestra":"Muestra",
			"anexo_variedad":"Variedad",
			"anexo_condicion":"Condicion",
			"anexo_organo":"Organo",
			"anexo_ubicacion":"Ubicación",
			"anexo_producto":"Producto",
			"anexo_producto2":"Producto",
			"dias_aplicacion":"Días despues de Aplicación",
		}

class detalleevcamarashumedasform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(detalleevcamarashumedasform, self).__init__(*args, **kwargs)
				
		self.fields['fecha_evaluacion'].widget.attrs.update({"placeholder":"Fecha de Evaluacion","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['frutos_infestados'].widget.attrs.update({"placeholder":"Frutos Infestados","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['botrytis_cinerea'].widget.attrs.update({"placeholder":"Botrytis Cinerea","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['alternaria'].widget.attrs.update({"placeholder":"Alternaria","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['cladosporium_sp'].widget.attrs.update({"placeholder":"Cladosporium SP","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['apergillus_niger'].widget.attrs.update({"placeholder":"Apergillus Niger","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['pestalotiopsis_sp'].widget.attrs.update({"placeholder":"Pestalotiopsis SP","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['rhyzopus_spp'].widget.attrs.update({"placeholder":"Rhyzopus SPP","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['penicillum_sp'].widget.attrs.update({"placeholder":"Penicillum SP","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['sin_esporular'].widget.attrs.update({"placeholder":"Sin Esporular","data-required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		
	class Meta:
		model = DetallePlantaEvCamarasHumedas
		fields = [
			'fecha_evaluacion',
			'frutos_infestados',
			'botrytis_cinerea',
			'alternaria',
			'cladosporium_sp',
			'apergillus_niger',
			'pestalotiopsis_sp',
			'rhyzopus_spp',
			'penicillum_sp',
			'sin_esporular',
		]
		labels={
			"fecha_evaluacion":"Fecha Evaluacion",
			"frutos_infestados":"Frutos Infestados",
			"botrytis_cinerea":"Botrytis Cinerea",
			"alternaria":"Alternaria",
			"cladosporium_sp":"Cladosporium SP",
			"apergillus_niger":"Apergillus Niger",
			"pestalotiopsis_sp":"Pestalotiopsis SP",
			"rhyzopus_spp":"Rhyzopus SPP",
			"penicillum_sp":"Penicillum SP",
			"sin_esporular":"Sin Esporular",
		}

#EV CALIDAD CONTROL HG 2022
class evcalcontroldescartehg2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evcalcontroldescartehg2022form, self).__init__(*args, **kwargs)
        
		self.fields['fecha_proceso'].widget.attrs.update({"placeholder":"Fecha Proceso","required":"true","data-error-message":"Fecha Requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"Turno requerido","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo","required":"true","data-error-message":"Tipo requerido","class":"form-control"})
		self.fields['anexo_fundo']=forms.ModelChoiceField(label="Fundo", queryset=MaestraFundoCultivo.objects.filter(anexo_cultivo=5))
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Fundo","required":"true","data-error-message":"Fundo requerido","class":"form-control"})
		self.fields['anexo_variedad']=forms.ModelChoiceField(label="Variedad", queryset=variedad.objects.filter(cul=5))
		self.fields['anexo_variedad'].widget.attrs.update({"placeholder":"Variedad","required":"true","data-error-message":"Variedad requerida","class":"form-control"})
		self.fields['ticket'].widget.attrs.update({"placeholder":"Ticket","data-required":"true","data-error-message":"Ticket requerido","class":"form-control"})
		self.fields['fecha_cosecha'].widget.attrs.update({"placeholder":"Fecha Cosecha","required":"true","data-error-message":"Fecha requerida","class":"form-control"})
		self.fields['cantidad_muestra'].widget.attrs.update({"placeholder":"Peso de Muestra","required":"true","data-error-message":"Cantidad requerida","class":"form-control"})
        
	class Meta:
		model = EvCalControlDescarteHg2022
		fields = [
			'fecha_proceso',
			'anexo_turno',
			'anexo_tipo',
			'anexo_fundo',
			'anexo_variedad',
			'ticket',
			'fecha_cosecha',
			'cantidad_muestra',
		]
		labels={
			"fecha_proceso":"Fecha Proceso",
			"anexo_turno":"Turno",
			"anexo_tipo":"Tipo",
			"anexo_fundo":"Fundo",
			"anexo_variedad":"Variedad",
			"ticket":"Ticket",
			"fecha_cosecha":"Fecha Cosecha",
			"cantidad_muestra":"Peso De Muestra",
		}

class detalleevcalcontroldescartehg2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(detalleevcalcontroldescartehg2022form, self).__init__(*args, **kwargs)

		self.fields['exportable1'].widget.attrs.update({"placeholder":"Calibre 11","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable2'].widget.attrs.update({"placeholder":"Calibre 13","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable3'].widget.attrs.update({"placeholder":"Calibre 15","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable4'].widget.attrs.update({"placeholder":"Calibre 18","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable5'].widget.attrs.update({"placeholder":"Calibre 20","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable6'].widget.attrs.update({"placeholder":"Calibre 24","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable7'].widget.attrs.update({"placeholder":"Calibre 27","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['exportable8'].widget.attrs.update({"placeholder":"Calibre 30","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})

		self.fields['descarte1'].widget.attrs.update({"placeholder":"Bajo calibre","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte2'].widget.attrs.update({"placeholder":"Sobre maduración","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte3'].widget.attrs.update({"placeholder":"Daño por thrips","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte4'].widget.attrs.update({"placeholder":"Latex","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte5'].widget.attrs.update({"placeholder":"Daño mecánico","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte6'].widget.attrs.update({"placeholder":"Agrietado","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte7'].widget.attrs.update({"placeholder":"Deshidratado","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte8'].widget.attrs.update({"placeholder":"Picado por aves","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte9'].widget.attrs.update({"placeholder":"Pedúnculo mal cortado","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte10'].widget.attrs.update({"placeholder":"Quereza","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte11'].widget.attrs.update({"placeholder":"Deformes","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte12'].widget.attrs.update({"placeholder":"Manchas","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte13'].widget.attrs.update({"placeholder":"Verde (inmadurez)","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte14'].widget.attrs.update({"placeholder":"Cicatriz","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte15'].widget.attrs.update({"placeholder":"Ostilo abierto","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte16'].widget.attrs.update({"placeholder":"Excremento de ave","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['descarte17'].widget.attrs.update({"placeholder":"Pasmado","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})

	class Meta:
		model = DetalleEvCalControlDescarteHg2022
		fields = [
			'exportable1',
			'exportable2',
			'exportable3',
			'exportable4',
			'exportable5',
			'exportable6',
			'exportable7',
			'exportable8',
			'descarte1',
			'descarte2',
			'descarte3',
			'descarte4',
			'descarte5',
			'descarte6',
			'descarte7',
			'descarte8',
			'descarte9',
			'descarte10',
			'descarte11',
			'descarte12',
			'descarte13',
			'descarte14',
			'descarte15',
			'descarte16',
			'descarte17',
		]

		labels={
			"exportable1":"Calibre 11",
			"exportable2":"Calibre 13",
			"exportable3":"Calibre 15",
			"exportable4":"Calibre 18",
			"exportable5":"Calibre 20",
			"exportable6":"Calibre 24",
			"exportable7":"Calibre 27",
			"exportable8":"Calibre 30",
			"descarte1":"Bajo Calibre",
			"descarte2":"Sobre Maduración",
			"descarte3":"Daño Por Thrips",
			"descarte4":"Latex",
			"descarte5":"Daño Mecánico",
			"descarte6":"Agrietado",
			"descarte7":"Deshidratado",
			"descarte8":"Picado por Aves",
			"descarte9":"Pedúnculo Mal Cortado",
			"descarte10":"Quereza",
			"descarte11":"Deformes",
			"descarte12":"Manchas",
			"descarte13":"Verdes (inmadurez)",
			"descarte14":"Cicatriz",
			"descarte15":"Ostilo Abierto",
			"descarte16":"Excremento De Ave",
			"descarte17":"Pasmado",
		}

#EV CAL. PROD. TERMINADOS HG 2022
class controlproductoterminadohgform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(controlproductoterminadohgform, self).__init__(*args, **kwargs)

		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"FECHA","required":"true","data-error-message":"N° Planta requerida","class":"form-control","id":"datepickercreacion1"})
		self.fields['anexo_centro'].widget.attrs.update({"autocomplete":"off","placeholder":"Centro","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_linea'].widget.attrs.update({"autocomplete":"off","placeholder":"Linea","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_pagina'].widget.attrs.update({"autocomplete":"off","placeholder":"Pagina","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"autocomplete":"off","placeholder":"Obs..","required":"false","data-error-message":"Obs requerida","class":"form-control"})
		
	class Meta:
		model = ControlProductoTerminadoHg
		fields = [
			'fecha',
			'anexo_centro',
			'anexo_linea',
			'anexo_turno',
			'anexo_pagina',
			'observacion',
		]

		labels={
			"fecha":"Fecha",
			"anexo_centro":"Centro",
			"anexo_linea":"Linea",
			"anexo_turno":"Turno",
			"anexo_pagina":"Pagina",
			'observacion':"Observacion",
		}

class detallecontrolproductoterminadohgform(forms.ModelForm):
	def __init__(self, *args, **kwargs):

		variablecliente=kwargs.pop("variable_cliente")
		variablevariedad=kwargs.pop("variable_variedad")
	
		super(detallecontrolproductoterminadohgform, self).__init__(*args, **kwargs)

		self.fields['trazabilidad'].widget.attrs.update({"autocomplete":"off","placeholder":"Trazabilidad","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['anexo_cliente']=forms.ModelChoiceField(label="Cliente", queryset=variablecliente.AnexoCentroClientes.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_cliente'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_presentaciong']=forms.ModelChoiceField(label="PresentacionesG", queryset=variablecliente.AnexoCentroPresentacionesG.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_presentaciong'].widget.attrs.update({"autocomplete":"off","placeholder":"","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_presentacion']=forms.ModelChoiceField(label="Presentaciones", queryset=variablecliente.AnexoCentroPresentacionesA.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_presentacion'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['tamano_pulpa'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_calibre']=forms.ModelChoiceField(label="Calibres", queryset=variablecliente.AnexoCentroCalibres.filter(anexo_cultivo=variablevariedad))
		self.fields['anexo_calibre'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['anexo_acomodo'].widget.attrs.update({"autocomplete":"off","placeholder":"p1","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['peso1'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso2'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso3'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso4'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso5'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['peso6'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['condicion1'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion2'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion3'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion4'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion5'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion6'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion7'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion8'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion9'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion10'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['condicion11'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['calidad1'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad2'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad3'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad4'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad5'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad6'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad7'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['calidad8'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['fitosanitario1'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['fitosanitario2'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['fitosanitario3'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['p1'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p2'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p3'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p4'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p5'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p6'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p7'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p8'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p9'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p10'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p11'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		self.fields['p12'].widget.attrs.update({"autocomplete":"off","placeholder":"","data-required":"true","data-error-message":"N° Planta requerida","class":"form-control"})
		
	class Meta:
		model = DetalleControlProductoTerminadoHg
		fields = [
			'trazabilidad',
			'npalet',
			'anexo_cliente',
			'anexo_presentaciong',
			'anexo_presentacion',
			'tamano_pulpa',
			'anexo_calibre',
			'anexo_acomodo',
			'peso1',
			'peso2',
			'peso3',
			'peso4',
			'peso5',
			'peso6',
			'condicion1',
			'condicion2',
			'condicion3',
			'condicion4',
			'condicion5',
			'condicion6',
			'condicion7',
			'condicion8',
			'condicion9',
			'condicion10',
			'condicion11',
			'calidad1',
			'calidad2',
			'calidad3',
			'calidad4',
			'calidad5',
			'calidad6',
			'calidad7',
			'calidad8',
			'fitosanitario1',
			'fitosanitario2',
			'fitosanitario3',
			'p1',
			'p2',
			'p3',
			'p4',
			'p5',
			'p6',
			'p7',
			'p8',
			'p9',
			'p10',
			'p11',
			'p12',
		]

		labels={
			"trazabilidad":"Trazabilidad",
			"npalet":"N° Palet",
			"anexo_cliente":"Cliente",
			"anexo_presentaciong":"PresentacionesG",
			"anexo_presentacion":"Presentacion",
			"tamano_pulpa":"Temperatura Pulpa",
			"anexo_calibre":"Calibre",
			"anexo_acomodo":"Acomodo",
			"peso1":"Peso Bruto (Gr)",
			"peso2":"Peso Neto (Gr)",
			"peso3":"Peso Envases (Gr)",
			"peso4":"Peso Max Unidad (Gr)",
			"peso5":"Peso Min Unidad (Gr)",
			"peso6":"Peso Prom. Unidad (Gr)",
			"condicion1":"Pudricion",
			"condicion2":"Daño Mecanico",
			"condicion3":"Pasmado",
			"condicion4":"Micelio",
			"condicion5":"Sobremaduro",
			"condicion6":"Daño Latex",
			"condicion7":"Ostiolo Agrietado",
			"condicion8":"Pedunculo Mal Cortado",
			"condicion9":"Agrietado",
			"condicion10":"Machucón",
			"condicion11":"Deshidratado",
			"calidad1":"Deformes",
			"calidad2":"Cicatriz",
			"calidad3":"Manchas",
			"calidad4":"Inmadurez Verde",
			"calidad5":"Picado Ave",
			"calidad6":"Sin Color",
			"calidad7":"Bajo Calibre",
			"calidad8":"Sobre Calibre",
			"fitosanitario1":"Daño Thrips",
			"fitosanitario2":"Daño Arañita",
			"fitosanitario3":"Daño Quereza",
			"p1":"P1",
			"p2":"P2",
			"p3":"P3",
			"p4":"P4",
			"p5":"P5",
			"p6":"P6",
			"p7":"P7",
			"p8":"P8",
			"p9":"P9",
			"p10":"P10",
			"p11":"P11",
			"p12":"P12",
		}

#EV EFICIENCIA SELECCION Y CALIBRADO
class eveficienciaseleccioncalibradoform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(eveficienciaseleccioncalibradoform, self).__init__(*args, **kwargs)

		self.fields['npalet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","required":"true","data-error-message":"N° Palet Requerida","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"Planta","required":"true","data-error-message":"Planta Requerida","class":"form-control"})
		self.fields['anexo_calibre'].widget.attrs.update({"autocomplete":"off","placeholder":"Calibre","required":"true","data-error-message":"Calibre Requerido","class":"form-control"})
		self.fields['anexo_linea'].widget.attrs.update({"autocomplete":"off","placeholder":"Linea","required":"true","data-error-message":"Linea Requerido","class":"form-control"})
		self.fields['anexo_envase'].widget.attrs.update({"autocomplete":"off","placeholder":"Envase","required":"true","data-error-message":"Envase Requerido","class":"form-control"})
		self.fields['anexo_cliente']=forms.ModelChoiceField(label="Cliente", queryset=ClientesAthos.objects.filter(anexo_cultivo=2))
		self.fields['anexo_cliente'].widget.attrs.update({"required":"true","data-error-message":"Cliente requerido","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

		self.fields['firmeza_1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['firmeza_2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['firmeza_3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		
		self.fields['bloom_1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['bloom_2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['bloom_3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['bloom_4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['condicion1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['condicion10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['calidad1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad11'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['calidad12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['fitosanitario1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['fitosanitario2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['fitosanitario3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"Data Requerida","class":"form-control"})
		
	class Meta:
		model = EvEficienciaSeleccionCalibrado
		fields = [
			'npalet',
			'anexo_planta',
			'anexo_calibre',
			'anexo_linea',
			'anexo_envase',
			'anexo_cliente',
			'anexo_turno',
			'firmeza_1',
			'firmeza_2',
			'firmeza_3',
			'bloom_1',
			'bloom_2',
			'bloom_3',
			'bloom_4',
			'condicion1',
			'condicion2',
			'condicion3',
			'condicion4',
			'condicion5',
			'condicion6',
			'condicion7',
			'condicion8',
			'condicion9',
			'condicion10',
			'calidad1',
			'calidad2',
			'calidad3',
			'calidad4',
			'calidad5',
			'calidad6',
			'calidad7',
			'calidad8',
			'calidad9',
			'calidad10',
			'calidad11',
			'calidad12',
			'fitosanitario1',
			'fitosanitario2',
			'fitosanitario3',
		]

		labels={
			"npalet":"N° Palet",
			"anexo_planta":"Planta",
			"anexo_calibre":"Calibre",
			"anexo_linea":"Linea",
			"anexo_envase":"Envase",
			"anexo_cliente":"Cliente",
			"anexo_turno":"Turno",
			"firmeza_1":"FIRMEZA || Firme",
			"firmeza_2":"FIRMEZA || Sensitivo",
			"firmeza_3":"FIRMEZA || Blando",
			"bloom_1":"BLOOM || N°1",
			"bloom_2":"BLOOM || N°2",
			"bloom_3":"BLOOM || N°3",
			"bloom_4":"BLOOM || N°4",
			"condicion1":"CONDICION || Pudrición",
			"condicion2":"CONDICION || Blando",
			"condicion3":"CONDICION || Micelio",
			"condicion4":"CONDICION || Heridas",
			"condicion5":"CONDICION || Deshidratación",
			"condicion6":"CONDICION || Desgarro Pedicelar",
			"condicion7":"CONDICION || Exudación Jugo",
			"condicion8":"CONDICION || Machucón",
			"condicion9":"CONDICION || Globito",
			"condicion10":"CONDICION || fruta_hinchada",
			"calidad1":"CALIDAD || Polvo",
			"calidad2":"CALIDAD || Tierra",
			"calidad3":"CALIDAD || Deformes",
			"calidad4":"CALIDAD || Russet",
			"calidad5":"CALIDAD || Cicatriz",
			"calidad6":"CALIDAD || Presencia de Pedicelo",
			"calidad7":"CALIDAD || Restos Florales",
			"calidad8":"CALIDAD || Fruta Inmadura (verde)",
			"calidad9":"CALIDAD || Fruta Inmadura (rojizo)",
			"calidad10":"CALIDAD || Bajo Calibre",
			"calidad11":"CALIDAD || Material Extraño",
			"calidad12":"CALIDAD || Decoloración",
			"fitosanitario1":"FITOSANITARIO || Cochinilla",
			"fitosanitario2":"FITOSANITARIO || Mosca de la Fruta",
			"fitosanitario3":"FITOSANITARIO || Arañas (insectos)",
		}

#EV PRODUCTO TERMINADO DESPACHO 2022
class evproductoterminadodespachoform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(evproductoterminadodespachoform, self).__init__(*args, **kwargs)

		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha","required":"true","data-error-message":"N° Palet Requerida","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"autocomplete":"off","placeholder":"Planta","required":"true","data-error-message":"Planta Requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"autocomplete":"off","placeholder":"SR","required":"true","data-error-message":"N° Planta requerida","class":"form-control"})

	class Meta:
		model = EvProductoTerminadoDespacho
		fields = [
			'fecha',
			'anexo_planta',
			'anexo_turno',
		]

		labels={
			"fecha":"Fecha",
			"anexo_planta":"Planta",
			"anexo_turno":"Turno",
		}

class detalleevproductoterminadodespachoform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(detalleevproductoterminadodespachoform, self).__init__(*args, **kwargs)

		#self.fields['anexo_cliente']=forms.ModelChoiceField(label="Cliente", queryset=ClientesAthos.objects.filter(anexo_cultivo=1))
		self.fields['anexo_cliente'].widget.attrs.update({"required":"true","data-error-message":"Cliente requerido","class":"form-control"})
		self.fields['anexo_envio'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['trazabilidad'].widget.attrs.update({"autocomplete":"off","placeholder":"Trazabilidad","required":"true","data-error-message":"Data requerida","class":"form-control"})
		self.fields['npalet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['firmeza_clo1_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo1_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo2_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo3_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo4_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['firmeza_clo5_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['peso_cj01_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj01_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj02_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj03_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj04_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m06'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m07'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m08'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m09'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m10'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m11'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['peso_cj05_m12'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['anexo_bloom'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_bloom2'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_bloom3'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_bloom4'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_bloom5'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['deshidratados_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['deshidratados_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['deshidratados_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['deshidratados_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['deshidratados_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['blandos_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['blandos_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['blandos_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['blandos_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['blandos_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['pudricion_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pudricion_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pudricion_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pudricion_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pudricion_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['frutos_florales_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['frutos_florales_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['frutos_florales_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['frutos_florales_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['frutos_florales_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['pitting_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pitting_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pitting_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pitting_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['pitting_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['machucon_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['machucon_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['machucon_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['machucon_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['machucon_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['heridas_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['heridas_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['heridas_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['heridas_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['heridas_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['desgarro_pedicelar_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['desgarro_pedicelar_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['desgarro_pedicelar_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['desgarro_pedicelar_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['desgarro_pedicelar_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['decoloracion_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['decoloracion_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['decoloracion_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['decoloracion_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['decoloracion_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['rojizos_inmaduro_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['rojizos_inmaduro_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['rojizos_inmaduro_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['rojizos_inmaduro_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['rojizos_inmaduro_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['Exudado_cj01'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['Exudado_cj02'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['Exudado_cj03'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['Exudado_cj04'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})
		self.fields['Exudado_cj05'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet ","data-required":"true","data-error-message":"N° Palet","class":"form-control"})

		self.fields['anexo_etiquetado'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_etiquetado2'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_etiquetado3'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_etiquetado4'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_etiquetado5'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['anexo_embolsado'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_embolsado2'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_embolsado3'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_embolsado4'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_embolsado5'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['anexo_arte_caja'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_arte_caja2'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_arte_caja3'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_arte_caja4'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
		self.fields['anexo_arte_caja5'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})

		self.fields['anexo_decision'].widget.attrs.update({"autocomplete":"off","placeholder":"Envio","required":"true","data-error-message":"Data Requerida","class":"form-control"})
				
	class Meta:
		model = DetalleEvProductoTerminadoDespacho
		fields = [
			'anexo_cliente',
			'anexo_envio',
			'trazabilidad',
			'npalet',
			'firmeza_clo1_m01',
			'firmeza_clo1_m02',
			'firmeza_clo1_m03',
			'firmeza_clo1_m04',
			'firmeza_clo1_m05',
			'firmeza_clo1_m06',
			'firmeza_clo1_m07',
			'firmeza_clo1_m08',
			'firmeza_clo1_m09',
			'firmeza_clo1_m10',
			'firmeza_clo1_m11',
			'firmeza_clo1_m12',
			'firmeza_clo2_m01',
			'firmeza_clo2_m02',
			'firmeza_clo2_m03',
			'firmeza_clo2_m04',
			'firmeza_clo2_m05',
			'firmeza_clo2_m06',
			'firmeza_clo2_m07',
			'firmeza_clo2_m08',
			'firmeza_clo2_m09',
			'firmeza_clo2_m10',
			'firmeza_clo2_m11',
			'firmeza_clo2_m12',
			'firmeza_clo3_m01',
			'firmeza_clo3_m02',
			'firmeza_clo3_m03',
			'firmeza_clo3_m04',
			'firmeza_clo3_m05',
			'firmeza_clo3_m06',
			'firmeza_clo3_m07',
			'firmeza_clo3_m08',
			'firmeza_clo3_m09',
			'firmeza_clo3_m10',
			'firmeza_clo3_m11',
			'firmeza_clo3_m12',
			'firmeza_clo4_m01',
			'firmeza_clo4_m02',
			'firmeza_clo4_m03',
			'firmeza_clo4_m04',
			'firmeza_clo4_m05',
			'firmeza_clo4_m06',
			'firmeza_clo4_m07',
			'firmeza_clo4_m08',
			'firmeza_clo4_m09',
			'firmeza_clo4_m10',
			'firmeza_clo4_m11',
			'firmeza_clo4_m12',
			'firmeza_clo5_m01',
			'firmeza_clo5_m02',
			'firmeza_clo5_m03',
			'firmeza_clo5_m04',
			'firmeza_clo5_m05',
			'firmeza_clo5_m06',
			'firmeza_clo5_m07',
			'firmeza_clo5_m08',
			'firmeza_clo5_m09',
			'firmeza_clo5_m10',
			'firmeza_clo5_m11',
			'firmeza_clo5_m12',
			'peso_cj01_m01',
			'peso_cj01_m02',
			'peso_cj01_m03',
			'peso_cj01_m04',
			'peso_cj01_m05',
			'peso_cj01_m06',
			'peso_cj01_m07',
			'peso_cj01_m08',
			'peso_cj01_m09',
			'peso_cj01_m10',
			'peso_cj01_m11',
			'peso_cj01_m12',
			'peso_cj02_m01',
			'peso_cj02_m02',
			'peso_cj02_m03',
			'peso_cj02_m04',
			'peso_cj02_m05',
			'peso_cj02_m06',
			'peso_cj02_m07',
			'peso_cj02_m08',
			'peso_cj02_m09',
			'peso_cj02_m10',
			'peso_cj02_m11',
			'peso_cj02_m12',
			'peso_cj03_m01',
			'peso_cj03_m02',
			'peso_cj03_m03',
			'peso_cj03_m04',
			'peso_cj03_m05',
			'peso_cj03_m06',
			'peso_cj03_m07',
			'peso_cj03_m08',
			'peso_cj03_m09',
			'peso_cj03_m10',
			'peso_cj03_m11',
			'peso_cj03_m12',
			'peso_cj04_m01',
			'peso_cj04_m02',
			'peso_cj04_m03',
			'peso_cj04_m04',
			'peso_cj04_m05',
			'peso_cj04_m06',
			'peso_cj04_m07',
			'peso_cj04_m08',
			'peso_cj04_m09',
			'peso_cj04_m10',
			'peso_cj04_m11',
			'peso_cj04_m12',
			'peso_cj05_m01',
			'peso_cj05_m02',
			'peso_cj05_m03',
			'peso_cj05_m04',
			'peso_cj05_m05',
			'peso_cj05_m06',
			'peso_cj05_m07',
			'peso_cj05_m08',
			'peso_cj05_m09',
			'peso_cj05_m10',
			'peso_cj05_m11',
			'peso_cj05_m12',
			'anexo_bloom',
			'anexo_bloom2',
			'anexo_bloom3',
			'anexo_bloom4',
			'anexo_bloom5',
			'deshidratados_cj01',
			'deshidratados_cj02',
			'deshidratados_cj03',
			'deshidratados_cj04',
			'deshidratados_cj05',
			'blandos_cj01',
			'blandos_cj02',
			'blandos_cj03',
			'blandos_cj04',
			'blandos_cj05',
			'pudricion_cj01',
			'pudricion_cj02',
			'pudricion_cj03',
			'pudricion_cj04',
			'pudricion_cj05',
			'frutos_florales_cj01',
			'frutos_florales_cj02',
			'frutos_florales_cj03',
			'frutos_florales_cj04',
			'frutos_florales_cj05',
			'pitting_cj01',
			'pitting_cj02',
			'pitting_cj03',
			'pitting_cj04',
			'pitting_cj05',
			'machucon_cj01',
			'machucon_cj02',
			'machucon_cj03',
			'machucon_cj04',
			'machucon_cj05',
			'heridas_cj01',
			'heridas_cj02',
			'heridas_cj03',
			'heridas_cj04',
			'heridas_cj05',
			'desgarro_pedicelar_cj01',
			'desgarro_pedicelar_cj02',
			'desgarro_pedicelar_cj03',
			'desgarro_pedicelar_cj04',
			'desgarro_pedicelar_cj05',
			'decoloracion_cj01',
			'decoloracion_cj02',
			'decoloracion_cj03',
			'decoloracion_cj04',
			'decoloracion_cj05',
			'rojizos_inmaduro_cj01',
			'rojizos_inmaduro_cj02',
			'rojizos_inmaduro_cj03',
			'rojizos_inmaduro_cj04',
			'rojizos_inmaduro_cj05',
			'Exudado_cj01',
			'Exudado_cj02',
			'Exudado_cj03',
			'Exudado_cj04',
			'Exudado_cj05',
			'anexo_etiquetado',
			'anexo_etiquetado2',
			'anexo_etiquetado3',
			'anexo_etiquetado4',
			'anexo_etiquetado5',
			'anexo_embolsado',
			'anexo_embolsado2',
			'anexo_embolsado3',
			'anexo_embolsado4',
			'anexo_embolsado5',
			'anexo_arte_caja',
			'anexo_arte_caja2',
			'anexo_arte_caja3',
			'anexo_arte_caja4',
			'anexo_arte_caja5',
			'anexo_decision',
		]

		labels={
			"anexo_cliente":"Cliente",
			"anexo_envio":"Tipo de Envio",
			"trazabilidad":"Trazabilidad",
			"npalet":"N° Palet",
			"firmeza_clo1_m01":"Firmeza CL1 MO1",
			"firmeza_clo1_m02":"Firmeza CL1 MO2",
			"firmeza_clo1_m03":"Firmeza CL1 MO3",
			"firmeza_clo1_m04":"Firmeza CL1 MO4",
			"firmeza_clo1_m05":"Firmeza CL1 MO5",
			"firmeza_clo1_m06":"Firmeza CL1 MO6",
			"firmeza_clo1_m07":"Firmeza CL1 MO7",
			"firmeza_clo1_m08":"Firmeza CL1 MO8",
			"firmeza_clo1_m09":"Firmeza CL1 MO9",
			"firmeza_clo1_m10":"Firmeza CL1 MO10",
			"firmeza_clo1_m11":"Firmeza CL1 MO11",
			"firmeza_clo1_m12":"Firmeza CL1 MO12",
			"firmeza_clo2_m01":"Firmeza CL2 MO1",
			"firmeza_clo2_m02":"Firmeza CL2 MO2",
			"firmeza_clo2_m03":"Firmeza CL2 MO3",
			"firmeza_clo2_m04":"Firmeza CL2 MO4",
			"firmeza_clo2_m05":"Firmeza CL2 MO5",
			"firmeza_clo2_m06":"Firmeza CL2 MO6",
			"firmeza_clo2_m07":"Firmeza CL2 MO7",
			"firmeza_clo2_m08":"Firmeza CL2 MO8",
			"firmeza_clo2_m09":"Firmeza CL2 MO9",
			"firmeza_clo2_m10":"Firmeza CL2 MO10",
			"firmeza_clo2_m11":"Firmeza CL2 MO11",
			"firmeza_clo2_m12":"Firmeza CL2 MO12",
			"firmeza_clo3_m01":"Firmeza CL3 MO1",
			"firmeza_clo3_m02":"Firmeza CL3 MO2",
			"firmeza_clo3_m03":"Firmeza CL3 MO3",
			"firmeza_clo3_m04":"Firmeza CL3 MO4",
			"firmeza_clo3_m05":"Firmeza CL3 MO5",
			"firmeza_clo3_m06":"Firmeza CL3 MO6",
			"firmeza_clo3_m07":"Firmeza CL3 MO7",
			"firmeza_clo3_m08":"Firmeza CL3 MO8",
			"firmeza_clo3_m09":"Firmeza CL3 MO9",
			"firmeza_clo3_m10":"Firmeza CL3 MO10",
			"firmeza_clo3_m11":"Firmeza CL3 MO11",
			"firmeza_clo3_m12":"Firmeza CL3 MO12",
			"firmeza_clo4_m01":"Firmeza CL4 MO1",
			"firmeza_clo4_m02":"Firmeza CL4 MO2",
			"firmeza_clo4_m03":"Firmeza CL4 MO3",
			"firmeza_clo4_m04":"Firmeza CL4 MO4",
			"firmeza_clo4_m05":"Firmeza CL4 MO5",
			"firmeza_clo4_m06":"Firmeza CL4 MO6",
			"firmeza_clo4_m07":"Firmeza CL4 MO7",
			"firmeza_clo4_m08":"Firmeza CL4 MO8",
			"firmeza_clo4_m09":"Firmeza CL4 MO9",
			"firmeza_clo4_m10":"Firmeza CL4 MO10",
			"firmeza_clo4_m11":"Firmeza CL4 MO11",
			"firmeza_clo4_m12":"Firmeza CL4 MO12",
			"firmeza_clo5_m01":"Firmeza CL5 MO1",
			"firmeza_clo5_m02":"Firmeza CL5 MO2",
			"firmeza_clo5_m03":"Firmeza CL5 MO3",
			"firmeza_clo5_m04":"Firmeza CL5 MO4",
			"firmeza_clo5_m05":"Firmeza CL5 MO5",
			"firmeza_clo5_m06":"Firmeza CL5 MO6",
			"firmeza_clo5_m07":"Firmeza CL5 MO7",
			"firmeza_clo5_m08":"Firmeza CL5 MO8",
			"firmeza_clo5_m09":"Firmeza CL5 MO9",
			"firmeza_clo5_m10":"Firmeza CL5 MO10",
			"firmeza_clo5_m11":"Firmeza CL5 MO11",
			"firmeza_clo5_m12":"Firmeza CL5 MO12",
			"peso_cj01_m01":"Peso Clamshell CJ1 MO1",
			"peso_cj01_m02":"Peso Clamshell CJ1 MO2",
			"peso_cj01_m03":"Peso Clamshell CJ1 MO3",
			"peso_cj01_m04":"Peso Clamshell CJ1 MO4",
			"peso_cj01_m05":"Peso Clamshell CJ1 MO5",
			"peso_cj01_m06":"Peso Clamshell CJ1 MO6",
			"peso_cj01_m07":"Peso Clamshell CJ1 MO7",
			"peso_cj01_m08":"Peso Clamshell CJ1 MO8",
			"peso_cj01_m09":"Peso Clamshell CJ1 MO9",
			"peso_cj01_m10":"Peso Clamshell CJ1 MO10",
			"peso_cj01_m11":"Peso Clamshell CJ1 MO11",
			"peso_cj01_m12":"Peso Clamshell CJ1 MO12",
			"peso_cj02_m01":"Peso Clamshell CJ2 MO1",
			"peso_cj02_m02":"Peso Clamshell CJ2 MO2",
			"peso_cj02_m03":"Peso Clamshell CJ2 MO3",
			"peso_cj02_m04":"Peso Clamshell CJ2 MO4",
			"peso_cj02_m05":"Peso Clamshell CJ2 MO5",
			"peso_cj02_m06":"Peso Clamshell CJ2 MO6",
			"peso_cj02_m07":"Peso Clamshell CJ2 MO7",
			"peso_cj02_m08":"Peso Clamshell CJ2 MO8",
			"peso_cj02_m09":"Peso Clamshell CJ2 MO9",
			"peso_cj02_m10":"Peso Clamshell CJ2 MO10",
			"peso_cj02_m11":"Peso Clamshell CJ2 MO11",
			"peso_cj02_m12":"Peso Clamshell CJ2 MO12",
			"peso_cj03_m01":"Peso Clamshell CJ3 MO1",
			"peso_cj03_m02":"Peso Clamshell CJ3 MO2",
			"peso_cj03_m03":"Peso Clamshell CJ3 MO3",
			"peso_cj03_m04":"Peso Clamshell CJ3 MO4",
			"peso_cj03_m05":"Peso Clamshell CJ3 MO5",
			"peso_cj03_m06":"Peso Clamshell CJ3 MO6",
			"peso_cj03_m07":"Peso Clamshell CJ3 MO7",
			"peso_cj03_m08":"Peso Clamshell CJ3 MO8",
			"peso_cj03_m09":"Peso Clamshell CJ3 MO9",
			"peso_cj03_m10":"Peso Clamshell CJ3 MO10",
			"peso_cj03_m11":"Peso Clamshell CJ3 MO11",
			"peso_cj03_m12":"Peso Clamshell CJ3 MO12",
			"peso_cj04_m01":"Peso Clamshell CJ4 MO1",
			"peso_cj04_m02":"Peso Clamshell CJ4 MO2",
			"peso_cj04_m03":"Peso Clamshell CJ4 MO3",
			"peso_cj04_m04":"Peso Clamshell CJ4 MO4",
			"peso_cj04_m05":"Peso Clamshell CJ4 MO5",
			"peso_cj04_m06":"Peso Clamshell CJ4 MO6",
			"peso_cj04_m07":"Peso Clamshell CJ4 MO7",
			"peso_cj04_m08":"Peso Clamshell CJ4 MO8",
			"peso_cj04_m09":"Peso Clamshell CJ4 MO9",
			"peso_cj04_m10":"Peso Clamshell CJ4 MO10",
			"peso_cj04_m11":"Peso Clamshell CJ4 MO11",
			"peso_cj04_m12":"Peso Clamshell CJ4 MO12",
			"peso_cj05_m01":"Peso Clamshell CJ5 MO1",
			"peso_cj05_m02":"Peso Clamshell CJ5 MO2",
			"peso_cj05_m03":"Peso Clamshell CJ5 MO3",
			"peso_cj05_m04":"Peso Clamshell CJ5 MO4",
			"peso_cj05_m05":"Peso Clamshell CJ5 MO5",
			"peso_cj05_m06":"Peso Clamshell CJ5 MO6",
			"peso_cj05_m07":"Peso Clamshell CJ5 MO7",
			"peso_cj05_m08":"Peso Clamshell CJ5 MO8",
			"peso_cj05_m09":"Peso Clamshell CJ5 MO9",
			"peso_cj05_m10":"Peso Clamshell CJ5 MO10",
			"peso_cj05_m11":"Peso Clamshell CJ5 MO11",
			"peso_cj05_m12":"Peso Clamshell CJ5 MO12",
			"anexo_bloom":"BLOOM CJ01",
			"anexo_bloom2":"BLOOM CJ02",
			"anexo_bloom3":"BLOOM CJ03",
			"anexo_bloom4":"BLOOM CJ04",
			"anexo_bloom5":"BLOOM CJ05",
			"deshidratados_cj01":"DESHIDRATADOS CJ1",
			"deshidratados_cj02":"DESHIDRATADOS CJ2",
			"deshidratados_cj03":"DESHIDRATADOS CJ3",
			"deshidratados_cj04":"DESHIDRATADOS CJ4",
			"deshidratados_cj05":"DESHIDRATADOS CJ5",
			"blandos_cj01":"BLANDOS CJ1",
			"blandos_cj02":"BLANDOS CJ2",
			"blandos_cj03":"BLANDOS CJ3",
			"blandos_cj04":"BLANDOS CJ4",
			"blandos_cj05":"BLANDOS CJ5",
			"pudricion_cj01":"PUDRICION CJ1",
			"pudricion_cj02":"PUDRICION CJ2",
			"pudricion_cj03":"PUDRICION CJ3",
			"pudricion_cj04":"PUDRICION CJ4",
			"pudricion_cj05":"PUDRICION CJ5",
			"frutos_florales_cj01":"FRUTOS C/. R. FLORALES CJ1",
			"frutos_florales_cj02":"FRUTOS C/. R. FLORALES CJ2",
			"frutos_florales_cj03":"FRUTOS C/. R. FLORALES CJ3",
			"frutos_florales_cj04":"FRUTOS C/. R. FLORALES CJ4",
			"frutos_florales_cj05":"FRUTOS C/. R. FLORALES CJ5",
			"pitting_cj01":"PITTING CJ1",
			"pitting_cj02":"PITTING CJ2",
			"pitting_cj03":"PITTING CJ3",
			"pitting_cj04":"PITTING CJ4",
			"pitting_cj05":"PITTING CJ5",
			"machucon_cj01":"MACHUCON CJ1",
			"machucon_cj02":"MACHUCON CJ2",
			"machucon_cj03":"MACHUCON CJ3",
			"machucon_cj04":"MACHUCON CJ4",
			"machucon_cj05":"MACHUCON CJ5",
			"heridas_cj01":"HERIDAS CJ1",
			"heridas_cj02":"HERIDAS CJ2",
			"heridas_cj03":"HERIDAS CJ3",
			"heridas_cj04":"HERIDAS CJ4",
			"heridas_cj05":"HERIDAS CJ5",
			"desgarro_pedicelar_cj01":"DESGARRO PEDICELAR CJ1",
			"desgarro_pedicelar_cj02":"DESGARRO PEDICELAR CJ2",
			"desgarro_pedicelar_cj03":"DESGARRO PEDICELAR CJ3",
			"desgarro_pedicelar_cj04":"DESGARRO PEDICELAR CJ4",
			"desgarro_pedicelar_cj05":"DESGARRO PEDICELAR CJ5",
			"decoloracion_cj01":"DECOLORACION CJ1",
			"decoloracion_cj02":"DECOLORACION CJ2",
			"decoloracion_cj03":"DECOLORACION CJ3",
			"decoloracion_cj04":"DECOLORACION CJ4",
			"decoloracion_cj05":"DECOLORACION CJ5",
			"rojizos_inmaduro_cj01":"ROJIZOS - INMADUROS CJ1",
			"rojizos_inmaduro_cj02":"ROJIZOS - INMADUROS CJ2",
			"rojizos_inmaduro_cj03":"ROJIZOS - INMADUROS CJ3",
			"rojizos_inmaduro_cj04":"ROJIZOS - INMADUROS CJ4",
			"rojizos_inmaduro_cj05":"ROJIZOS - INMADUROS CJ5",
			"Exudado_cj01":"EXUDADO CJ1",
			"Exudado_cj02":"EXUDADO CJ2",
			"Exudado_cj03":"EXUDADO CJ3",
			"Exudado_cj04":"EXUDADO CJ4",
			"Exudado_cj05":"EXUDADO CJ5",
			"anexo_etiquetado":"ETIQUETADO CJ01",
			"anexo_etiquetado2":"ETIQUETADO CJ02",
			"anexo_etiquetado3":"ETIQUETADO CJ03",
			"anexo_etiquetado4":"ETIQUETADO CJ04",
			"anexo_etiquetado5":"ETIQUETADO CJ05",
			"anexo_embolsado":"EMBOLSADO CJ01",
			"anexo_embolsado2":"EMBOLSADO CJ02",
			"anexo_embolsado3":"EMBOLSADO CJ03",
			"anexo_embolsado4":"EMBOLSADO CJ04",
			"anexo_embolsado5":"EMBOLSADO CJ05",
			"anexo_arte_caja":"ARTE DE CAJA CJ01",
			"anexo_arte_caja2":"ARTE DE CAJA CJ02",
			"anexo_arte_caja3":"ARTE DE CAJA CJ03",
			"anexo_arte_caja4":"ARTE DE CAJA CJ04",
			"anexo_arte_caja5":"ARTE DE CAJA CJ05",
			"anexo_decision":"DECISIÓN",
		}
