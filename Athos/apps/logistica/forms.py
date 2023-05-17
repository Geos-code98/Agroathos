from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.logistica.models import ProveedoresAthos
from apps.logistica.models import CartillaProveedoresAthos



class proveedoresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(proveedoresathosform, self).__init__(*args, **kwargs)
		
		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"Cultivo","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['ruc'].widget.attrs.update({"autocomplete":"off","pattern":"[0-9]","placeholder":"RUC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['proveedor'].widget.attrs.update({"placeholder":"Proveedor..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		
		
	class Meta:
		model = ProveedoresAthos
		fields = [
			
			'anexo_centro',
			'anexo_cultivo',
			'ruc',
			'proveedor',			
			'anexo_estado',			
		]

		labels={
			
			"anexo_centro":"Centro",
			"anexo_cultivo":"Cultivo",
			"ruc":"RUC",
			"proveedor":"Proveedor",		
			"anexo_estado":"Estado",
			
		}


class cartillaproveedoresathosform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(cartillaproveedoresathosform, self).__init__(*args, **kwargs)

		self.fields['anexo_centro'].widget.attrs.update({"placeholder":"Centro","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_tipo'].widget.attrs.update({"placeholder":"Tipo","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_proveedor']=forms.ModelChoiceField(label="Proveedores", queryset=ProveedoresAthos.objects.filter(anexo_estado_id=1))
		self.fields['anexo_proveedor'].widget.attrs.update({"placeholder":"Proveedor","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['factura'].widget.attrs.update({"autocomplete":"off","placeholder":"Factura","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['orden'].widget.attrs.update({"placeholder":"Orden","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
		self.fields['anticipo'].widget.attrs.update({"placeholder":"Anticipo","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
		self.fields['anexo_moneda'].widget.attrs.update({"placeholder":"Moneda","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['fecha'].widget.attrs.update({"placeholder":"Fecha","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['valor'].widget.attrs.update({"placeholder":"Valor","required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['observacion'].widget.attrs.update({"placeholder":"Observacion","data-required":"true","data-error-message":"Centro requerido","class":"form-control"})
		self.fields['anexo_estado'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Centro requerido","class":"form-control"})


	class Meta:
		model = CartillaProveedoresAthos
		fields = [
			'anexo_centro',
			'anexo_tipo',
			'anexo_proveedor',
			'factura',
			'orden',			
			'anticipo',
			'anexo_moneda',
			'fecha',
			'valor',
			'observacion',
			'anexo_estado'			
		]

		labels={
			"anexo_centro":"Centro",
			"anexo_tipo":"Tipo de Operacion",
			"anexo_proveedor":"Proveedor",
			"factura":"Factura",
			"orden":"Orden",		
			"anticipo":"Anticipo",
			"anexo_moneda":"Moneda",
			"fecha":"Fecha",
			"valor":"Valor",
			"observacion":"Observacion",
			"anexo_estado":"Estado",
			
		}

