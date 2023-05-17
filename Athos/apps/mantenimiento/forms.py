from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#TERCEROS
from apps.maestras.models import LaboresPlantaAthos
from apps.menu.models import ProgramaProduccion
from apps.maestras.models import ActividadesAthos

from apps.mantenimiento.models import MantenimientoEquipoPlantaAthos
from apps.mantenimiento.models import DetalleMantenimientoEquipoPlantaAthos

#MANTENIMIENTO EQUIPOS
class mantenimientoequipoplantaathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(mantenimientoequipoplantaathosform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_proveedor'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        
    class Meta:
        model = MantenimientoEquipoPlantaAthos
        fields = [            
            'anexo_fundo',
            'anexo_cultivo',
            'anexo_proveedor',
            ]

        labels={
            "anexo_fundo":"Fundo",
            "anexo_cultivo":"Cultivo",
            "anexo_proveedor":"Proveedor",
        }

class detallemantenimientoequipoplantaathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        anexocultivo=kwargs.pop("variablecultivo")
        anexofundo=kwargs.pop("variablefundo")
        super(detallemantenimientoequipoplantaathosform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.filter(anexo_fundo=anexofundo,anexo_variedad__cul=anexocultivo,estado_id=1))
        self.fields['anexo_pep'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_proceso'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_labor']=forms.ModelChoiceField(label="LABOR", queryset=LaboresPlantaAthos.objects.filter(anexo_cultivo=anexocultivo))
        self.fields['anexo_labor'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_implemento'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})

        self.fields['fecha_mantenimiento'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['hora_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['hora_final'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['total_horas'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Data requerida","class":"form-control"})
        
    class Meta:
        model = DetalleMantenimientoEquipoPlantaAthos
        fields = [
            'anexo_pep',
            'anexo_proceso',
            'anexo_labor',
            'anexo_implemento',
            'fecha_mantenimiento',
            'hora_inicio',
            'hora_final',
            'total_horas',
            ]

        labels={
            "anexo_pep":"PEP",
            "anexo_proceso":"PROCESO",
            "anexo_labor":"LABOR",
            "anexo_implemento":"IMPLEMENTO",
            "fecha_mantenimiento":"Fecha de Mantenimiento",
            "hora_inicio":"Hora de Inicio",
            "hora_final":"Hora de Fin",
            "total_horas":"Total de Horas",
        }