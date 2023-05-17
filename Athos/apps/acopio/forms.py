from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.acopio.models import ModEnfriadoArCaraz2021
from apps.acopio.models import ModEnfriadoArCaraz202102
from apps.acopio.models import DistribucionEnfriadoArCaraz2021
from apps.acopio.models import DistribucionEnfriadoArCaraz202102
from apps.acopio.models import TemperaturaEnfriadoArCaraz2021
from apps.acopio.models import TemperaturaEnfriadoArCaraz202102
from apps.acopio.models import DescarteAthos
from apps.acopio.models import SalidaDescarte

from apps.acopio.models import ModEnfriado
from apps.acopio.models import ModEnfriado2022
from apps.acopio.models import ConfirmacionModEnfriado2022
from apps.acopio.models import ConfirmacionTicketModEnfriado2022
from apps.acopio.models import RegistroTemperaturaModEnfriado2022
from apps.acopio.models import TomaDatosModEnfriado2022
from apps.acopio.models import DistribucionEnfriado
from apps.acopio.models import TemperaturaEnfriado

#DESCARTE PL HG 2022
from apps.menu.models import MaterialMMPP
from apps.acopio.models import DescartePlantaHgAthos

class modenfriadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(modenfriadoform, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control", "id":"datepicker"})
		self.fields['cod_termometro'].widget.attrs.update({"placeholder":"Codigo Termometro","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['cod_vac1'].widget.attrs.update({"placeholder":"Codigo Vacuometro 1","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['cod_vac2'].widget.attrs.update({"placeholder":"Codigo Vacuometro 2","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['cod_vac3'].widget.attrs.update({"placeholder":"Codigo Vacuometro 3","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		
	class Meta:
		model = ModEnfriado
		fields = [
			'fecha',
			'cod_termometro',
			'cod_vac1',
			'cod_vac2',
			'cod_vac3',
			
		]

		labels={
			"fecha":"Fecha",
			"cod_termometro":"Codigo de Termometro",
			"cod_vac1":"Codigo Vacuometro 1",
			"cod_vac2":"Codigo Vacuometro 2",
			"cod_vac3":"Codigo Vacuometro 3",
			

		}

class modenfriado2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(modenfriado2022form, self).__init__(*args, **kwargs)
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control", "id":"datepicker"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Planta","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['n_tunel'].widget.attrs.update({"placeholder":"Tunel","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		self.fields['n_batch'].widget.attrs.update({"placeholder":"Batch","data-required":"true","data-error-message":"Dato requerido","class":"form-control"})
		
	class Meta:
		model = ModEnfriado2022
		fields = [
			'fecha',
			'anexo_planta',
			'anexo_tipo',
			'n_tunel',
			'n_batch',
		]

		labels={
			"fecha":"Fecha",
			"anexo_planta":"Planta",
			"anexo_tipo":"Tipo",
			"n_tunel":"Tunel",
			"n_batch":"Batch",
		}

class confirmacionmodenfriado2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(confirmacionmodenfriado2022form, self).__init__(*args, **kwargs)
		self.fields['n_palet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet","data-required":"true","data-error-message":"N° ticket requerido","class":"form-control"})
		
	class Meta:
		model = ConfirmacionModEnfriado2022
		fields = [
			'n_palet',
		]

		labels={
			"n_palet":"N° Palet",
		}

class confirmacionticketmodenfriado2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(confirmacionticketmodenfriado2022form, self).__init__(*args, **kwargs)
		self.fields['n_ticket'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Ticket","data-required":"true","data-error-message":"N° ticket requerido","class":"form-control"})
		
	class Meta:
		model = ConfirmacionTicketModEnfriado2022
		fields = [
			'n_ticket',
		]

		labels={
			"n_ticket":"N° Ticket",
		}

class registrotemperaturamodenfriado2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(registrotemperaturamodenfriado2022form, self).__init__(*args, **kwargs)
		self.fields['m_tempambiente'].widget.attrs.update({"placeholder":"Temperatura Ambiente","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		
	class Meta:
		model = RegistroTemperaturaModEnfriado2022
		fields = [
			'm_tempambiente',
		]

		labels={
			"m_tempambiente":"Temperatura Ambiente",
		}

class tomadatosmodenfriado2022form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(tomadatosmodenfriado2022form, self).__init__(*args, **kwargs)
		self.fields['n_palet'].widget.attrs.update({"autocomplete":"off","placeholder":"N° Palet","data-required":"true","data-error-message":"N° ticket requerido","class":"form-control"})
		self.fields['anexo_lado'].widget.attrs.update({"placeholder":"Lado","data-required":"true","data-error-message":"Lado requerida","class":"form-control"})
		self.fields['m_tempinterna'].widget.attrs.update({"placeholder":"Temperatura Interna","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['m_tempexterna'].widget.attrs.update({"placeholder":"Temperatura Externa","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		
	class Meta:
		model = TomaDatosModEnfriado2022
		fields = [
			'n_palet',
			'anexo_lado',
			'm_tempinterna',
			'm_tempexterna',
		]

		labels={
			"n_palet":"N° Palet",
			"anexo_lado":"N° Lado",
			"m_tempinterna":"Temperatura Interna",
			"m_tempexterna":"Temperatura Externa",
		}

class distribucionenfriadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(distribucionenfriadoform, self).__init__(*args, **kwargs)
		
		self.fields['tunel'].widget.attrs.update({"placeholder":"N° de Tunel..la","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['n_tunel'].widget.attrs.update({"placeholder":"N° de Compartimento","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['anexo_lado'].widget.attrs.update({"placeholder":"Lado","data-required":"true","data-error-message":"Lado requerida","class":"form-control"})
		self.fields['lectura_qr'].widget.attrs.update({"placeholder":"Lectura QR","data-required":"true","data-error-message":"QR requerida","class":"form-control"})
		self.fields['n_palet'].widget.attrs.update({"placeholder":"N° Palet","data-required":"true","data-error-message":"N° palet requerida","class":"form-control"})
		
	class Meta:
		model = DistribucionEnfriado
		fields = [
			'tunel',
			'n_tunel',
			'anexo_lado',
			'lectura_qr',
			'n_palet',
			
		]

		labels={
			"tunel":"N° Tunel(Escribir 1 o 2 segun corresponda)",
			"n_tunel":"N° Compartimento",
			"anexo_lado":"Lado",
			"lectura_qr":"Lectura QR",
			"n_palet":"N° Palet",
			

		}

class temperaturaenfriadoform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(temperaturaenfriadoform, self).__init__(*args, **kwargs)
		
		self.fields['m_tempambiente'].widget.attrs.update({"placeholder":"Temperatura Ambiente","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['m_tempinterna'].widget.attrs.update({"placeholder":"Temperatura Interna","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['m_tempexterna'].widget.attrs.update({"placeholder":"Temperatura Externa","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = TemperaturaEnfriado
		fields = [
			
			'm_tempambiente',
			'm_tempinterna',
			'm_tempexterna',
			
		]

		labels={
			
			"m_tempambiente":"Temperatura Ambiente",
			"m_tempinterna":"Temperatura Interna",
			"m_tempexterna":"Temperatura Externa",
			
		}


#campaña2021CarazAr
class modenfriadoarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(modenfriadoarcaraz2021form, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control", "id":"datepicker"})
		self.fields['cod_termometro'].widget.attrs.update({"placeholder":"Codigo Termometro","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['cod_vac1'].widget.attrs.update({"placeholder":"Codigo Vacuometro 1","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['cod_vac2'].widget.attrs.update({"placeholder":"Codigo Vacuometro 2","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['cod_vac3'].widget.attrs.update({"placeholder":"Codigo Vacuometro 3","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		
	class Meta:
		model = ModEnfriadoArCaraz2021
		fields = [
			'fecha',
			'cod_termometro',
			'cod_vac1',
			'cod_vac2',
			'cod_vac3',
			
		]

		labels={
			"fecha":"Fecha",
			"cod_termometro":"Codigo de Termometro",
			"cod_vac1":"Codigo Vacuometro 1",
			"cod_vac2":"Codigo Vacuometro 2",
			"cod_vac3":"Codigo Vacuometro 3",
			

		}

class distribucionenfriadoarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(distribucionenfriadoarcaraz2021form, self).__init__(*args, **kwargs)
		
		self.fields['tunel'].widget.attrs.update({"placeholder":"N° de Tunel","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['n_tunel'].widget.attrs.update({"placeholder":"N° de Compartimento","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['anexo_lado'].widget.attrs.update({"placeholder":"Lado","data-required":"true","data-error-message":"Lado requerida","class":"form-control"})
		self.fields['lectura_qr'].widget.attrs.update({"placeholder":"Lectura QR","data-required":"true","data-error-message":"QR requerida","class":"form-control"})
		self.fields['n_palet'].widget.attrs.update({"placeholder":"N° Palet","data-required":"true","data-error-message":"N° palet requerida","class":"form-control"})
		
	class Meta:
		model = DistribucionEnfriadoArCaraz2021
		fields = [
			'tunel',
			'n_tunel',
			'anexo_lado',
			'lectura_qr',
			'n_palet',
			
		]

		labels={
			"tunel":"N° Tunel(Escribir 1 o 2 segun corresponda)",
			"n_tunel":"N° Compartimento",
			"anexo_lado":"Lado",
			"lectura_qr":"Lectura QR",
			"n_palet":"N° Palet",
			

		}

class temperaturaenfriadoarcaraz2021form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(temperaturaenfriadoarcaraz2021form, self).__init__(*args, **kwargs)
		
		self.fields['m_tempambiente'].widget.attrs.update({"placeholder":"Temperatura Ambiente","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['m_tempinterna'].widget.attrs.update({"placeholder":"Temperatura Interna","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['m_tempexterna'].widget.attrs.update({"placeholder":"Temperatura Externa","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = TemperaturaEnfriadoArCaraz2021
		fields = [
			
			'm_tempambiente',
			'm_tempinterna',
			'm_tempexterna',
			
		]

		labels={
			
			"m_tempambiente":"Temperatura Ambiente",
			"m_tempinterna":"Temperatura Interna",
			"m_tempexterna":"Temperatura Externa",
			
		}

#CAMPAÑA CARAZ 2021 02 AR
class modenfriadoarcaraz202102form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(modenfriadoarcaraz202102form, self).__init__(*args, **kwargs)
		
		self.fields['fecha'].widget.attrs.update({"autocomplete":"off","placeholder":"fecha","data-required":"true","data-error-message":"fecha requerida","class":"form-control", "id":"datepicker"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cod_termometro'].widget.attrs.update({"placeholder":"Codigo Termometro","data-required":"true","data-error-message":"Cod. Termometro requerido!!","class":"form-control"})
		self.fields['cod_vac1'].widget.attrs.update({"placeholder":"Codigo Vacuometro 1","data-required":"true","data-error-message":"Vacuometro1 requerido","class":"form-control"})
		self.fields['cod_vac2'].widget.attrs.update({"placeholder":"Codigo Vacuometro 2","data-required":"true","data-error-message":"Vacuometro2 requerido","class":"form-control"})
		self.fields['cod_vac3'].widget.attrs.update({"placeholder":"Codigo Vacuometro 3","data-required":"true","data-error-message":"Vacuometro3 requerido","class":"form-control"})
		
	class Meta:
		model = ModEnfriadoArCaraz202102
		fields = [
			'fecha',
			'anexo_planta',
			'cod_termometro',
			'cod_vac1',
			'cod_vac2',
			'cod_vac3',
		]

		labels={
			"fecha":"Fecha",
			"anexo_planta":"Planta",
			"cod_termometro":"Codigo de Termometro",
			"cod_vac1":"Codigo Vacuometro 1",
			"cod_vac2":"Codigo Vacuometro 2",
			"cod_vac3":"Codigo Vacuometro 3",
		}

class distribucionenfriadoarcaraz202102form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(distribucionenfriadoarcaraz202102form, self).__init__(*args, **kwargs)
		
		self.fields['tunel'].widget.attrs.update({"placeholder":"N° de Tunel","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['n_tunel'].widget.attrs.update({"placeholder":"N° de Compartimento","data-required":"true","data-error-message":"Tunel requerida","class":"form-control"})
		self.fields['anexo_lado'].widget.attrs.update({"placeholder":"Lado","data-required":"true","data-error-message":"Lado requerida","class":"form-control"})
		self.fields['lectura_qr'].widget.attrs.update({"placeholder":"Lectura QR","data-required":"true","data-error-message":"QR requerida","class":"form-control"})
		self.fields['n_palet'].widget.attrs.update({"placeholder":"N° Palet","data-required":"true","data-error-message":"N° palet requerida","class":"form-control"})
		
	class Meta:
		model = DistribucionEnfriadoArCaraz202102
		fields = [
			'tunel',
			'n_tunel',
			'anexo_lado',
			'lectura_qr',
			'n_palet',
		]

		labels={
			"tunel":"N° Tunel(Escribir 1 o 2 segun corresponda)",
			"n_tunel":"N° Compartimento",
			"anexo_lado":"Lado",
			"lectura_qr":"Lectura QR",
			"n_palet":"N° Palet",
		}

class temperaturaenfriadoarcaraz202102form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(temperaturaenfriadoarcaraz202102form, self).__init__(*args, **kwargs)
		
		self.fields['m_tempambiente'].widget.attrs.update({"placeholder":"Temperatura Ambiente","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['m_tempinterna'].widget.attrs.update({"placeholder":"Temperatura Interna","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['m_tempexterna'].widget.attrs.update({"placeholder":"Temperatura Externa","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = TemperaturaEnfriadoArCaraz202102
		fields = [
			'm_tempambiente',
			'm_tempinterna',
			'm_tempexterna',
		]

		labels={
			"m_tempambiente":"Temperatura Ambiente",
			"m_tempinterna":"Temperatura Interna",
			"m_tempexterna":"Temperatura Externa",
		}


class descarteathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(descarteathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_nave'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"VACIO requerida","class":"form-control"})

		self.fields['cant_jabas'].widget.attrs.update({"placeholder":"Cant. Jabas","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"VACIO requerida","class":"form-control"})

		self.fields['fecha_lanzado'].widget.attrs.update({"placeholder":"Fecha","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['peso_bruto'].widget.attrs.update({"placeholder":"Peso Bruto","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['peso_descarte'].widget.attrs.update({"placeholder":"Descarte Planta","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['merma_maquina'].widget.attrs.update({"placeholder":"Merma Maquina","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['merma_proceso'].widget.attrs.update({"placeholder":"Merma Proceso","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['merma_recepcion'].widget.attrs.update({"placeholder":"Merma Recepcion","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['descarte_mini'].widget.attrs.update({"placeholder":"Descarte Mini","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['recuperable'].widget.attrs.update({"placeholder":"Recuperable","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['norecuperable'].widget.attrs.update({"placeholder":"No Recuperable","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})




	class Meta:
		model = DescarteAthos
		fields = [
			
			'anexo_eje',
			'anexo_planta',
			'anexo_nave',
			'anexo_material',
			'anexo_turno',
			'fecha_lanzado',
			'peso_bruto',
			'peso_descarte',
			'merma_maquina',
			'merma_proceso',
			'merma_recepcion',
			'descarte_mini',
			'recuperable',
			'norecuperable',
			'cant_jabas',
			'anexo_fundo',
			
		]

		labels={
			
			"anexo_eje":"Zona",
			"anexo_planta":"Planta",
			"anexo_nave":"Nave",
			"anexo_material":"Material",
			"anexo_turno":"Turno",
			"peso_bruto":"Peso Bruto",
			"peso_descarte":"´Descarte Planta",
			"merma_maquina":"Merma Maquina",
			"merma_proceso":"Merma Proceso",
			"merma_recepcion":"Merma Recepcion",
			"descarte_mini":"Descarte Mini",
			"recuperable":"Recuperable",
			"norecuperable":"No Recuperable",
			"cant_jabas":"Cantidad Jabas",
			"anexo_fundo":"Fundo",
		}


class salidadescarteform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(salidadescarteform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_eje'].widget.attrs.update({"placeholder":"Zona","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder":"Cantidad","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo Salida","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		self.fields['nroguia'].widget.attrs.update({"placeholder":"Nro Guia","data-required":"true","data-error-message":"TEMP requerida","class":"form-control"})
		

	class Meta:
		model = SalidaDescarte
		fields = [
			
			'anexo_eje',
			'cantidad',
			'anexo_cultivo',
			'anexo_tipo',
			'nroguia',
			
		]

		labels={
			"anexo_eje":"Zona",
			"cantidad":"Cantidad",
			"anexo_cultivo":"Cultivo",
			"anexo_tipo":"Tipo de Salida",
			"nroguia":"	Nro Guia"

		}

class descarteplantahgathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(descarteplantahgathosform, self).__init__(*args, **kwargs)
		
		self.fields['fecha_proceso'].widget.attrs.update({"placeholder":"Fecha","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_turno'].widget.attrs.update({"placeholder":"Turno","required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_planta'].widget.attrs.update({"placeholder":"Ubicacion","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})
		self.fields['anexo_material']=forms.ModelChoiceField(label="Material", queryset=MaterialMMPP.objects.filter(anexo_cultivo=5))
		self.fields['anexo_material'].widget.attrs.update({"placeholder":"Material","data-required":"true","data-error-message":"VACIO requerida","class":"form-control"})

		self.fields['descarte1'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte2'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte3'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte4'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte5'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte6'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte7'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte8'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte9'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte10'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte11'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte12'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte13'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte14'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte15'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte16'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte17'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['descarte18'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})
		self.fields['total_descarte'].widget.attrs.update({"placeholder":"...","data-required":"true","data-error-message":"dato requerido","class":"form-control"})

	class Meta:
		model = DescartePlantaHgAthos
		fields = [
			'fecha_proceso',
			'anexo_turno',
			'anexo_planta',
			'anexo_material',
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
			'descarte18',
			'total_descarte',
		]
		labels={
			"fecha_proceso":"Fecha Proceso",
			"anexo_turno":"Turno",
			"anexo_planta":"Planta",
			"anexo_material":"Material",
			"descarte1":"Bajo calibre",
			"descarte2":"Sobremaduración",
			"descarte3":"Daño por thrips",
			"descarte4":"Latex",
			"descarte5":"Daño mecánico",
			"descarte6":"Agrietado",
			"descarte7":"Deshidradatado",
			"descarte8":"Picado por aves",
			"descarte9":"Pedúnculo mal cortado",
			"descarte10":"Quereza",
			"descarte11":"Deformes",
			"descarte12":"Manchas",
			"descarte13":"Verde (inmadurez)",
			"descarte14":"Cicatriz",
			"descarte15":"Ostilo abierto",
			"descarte16":"Excremento de ave",
			"descarte17":"Pasmado",
			"descarte18":"Otros",
			"total_descarte":"Total descartes",
		}
