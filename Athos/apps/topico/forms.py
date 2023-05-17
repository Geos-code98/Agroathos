from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.topico.models import JustificacionTopico
from apps.topico.models import FichaEpidemiologica
from apps.topico.models import FichaSintomatologiaCovid





class justificaciontopicoform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(justificaciontopicoform, self).__init__(*args, **kwargs)
        
        self.fields['dni'].widget.attrs.update({"autocomplete":"off","placeholder":"DNI","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['fecha_justificacion'].widget.attrs.update({"autocomplete":"off","placeholder":"Fecha Justificacion","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['fecha_inicio'].widget.attrs.update({"autocomplete":"off","placeholder":"Inicio Fecha  a Justificar","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['fecha_fin'].widget.attrs.update({"autocomplete":"off","placeholder":"Fin Fecha  a Justificar","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        
        self.fields['anexo_zona'].widget.attrs.update({"autocomplete":"off","placeholder":"RUC","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"Proveedor..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_motivo'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_detallemotivo'].widget.attrs.update({"placeholder":"Estado","required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['imagen_justificacion1'].widget.attrs.update({"placeholder":"Proveedor..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['imagen_justificacion2'].widget.attrs.update({"placeholder":"Estado","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
    
        self.fields['justificacion'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['adjunta'].widget.attrs.update({"autocomplete":"off","placeholder":"..","data-required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        
        
    class Meta:
        model = JustificacionTopico
        fields = [
            
            'dni',
            'fecha_justificacion',
            'fecha_inicio',
            'fecha_fin',
            'anexo_zona',
            'anexo_motivo',
            'anexo_detallemotivo',            
            'anexo_lugar',    

            'imagen_justificacion1',            
            'imagen_justificacion2',
            'justificacion',
            'adjunta',            
        ]

        labels={
            
            "dni":"DNI",
            "fecha_justificacion":"Fecha Justificacion",
            "fecha_inicio":"Inicio F. Justificacion",
            "fecha_fin":"FIn F. Justificacion",
            "anexo_zona":"Zona",
            "anexo_lugar":"Lugar",        
            "anexo_motivo":"Motivo",
            "anexo_detallemotivo":"Detalle Motivo",
            "imagen_justificacion1":"Imagen Justificacion 1",        
            "imagen_justificacion2":"Imagen Justificacion 2",
            "justificacion":"Justificacion Detallada",
            "adjunta":"Documentos a adjuntar?",
        }


class fichaepidemiologicaform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(fichaepidemiologicaform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_zona'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['anexo_lugar'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['dni'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['fecha_evaluacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['nombre_completo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['edad'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['genero'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2_7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        

        self.fields['fecha_sintomas'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg4_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['lugar_visita'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['anexo_preg5_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['trimestre_embarazo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['anexo_preg6_2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_7'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_8'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_9'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6_10'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        

    
        
    class Meta:
        model = FichaEpidemiologica
        fields = [
            
            
            'anexo_zona',
            'anexo_lugar',
            'dni',            
            'fecha_evaluacion',    
                
            'nombre_completo',        
            'edad',

            'genero',
            'anexo_preg1',
            'anexo_preg2_1',            
            'anexo_preg2_2',    
            'anexo_preg2_3',            
            'anexo_preg2_4',        
            'anexo_preg2_5',
            'anexo_preg2_6',        
            'anexo_preg2_7',

            'fecha_sintomas',
            'anexo_preg4_1',
            'lugar_visita',            
            'anexo_preg5_1',    
            'anexo_preg6_1',
            'trimestre_embarazo',            
            'anexo_preg6_2',        
            'anexo_preg6_3',    

            'anexo_preg6_4',
            'anexo_preg6_5',
            'anexo_preg6_6',            
            'anexo_preg6_7',    
            'anexo_preg6_8',            
            'anexo_preg6_9',        
            'anexo_preg6_10',
        ]

        labels={
            
            "anexo_zona":"Zona",
            "anexo_lugar":"Lugar",
            "dni":"DNI",        
            "fecha_evaluacion":"Fecha Evaluacion",    
            "nombre_completo":"Nombre del Personal",
            "edad":"Edad",

            "genero":"Genero",
            "anexo_preg1":"Estoy en riesgo de haber contraido COVID?",
            "anexo_preg2_1":"Tos?",        
            "anexo_preg2_2":"Fiebre(Temperatura >=38)/Escalofrios",    
            "anexo_preg2_3":"Dolor de Garganta?",
            "anexo_preg2_4":"Congestion Nasal?",

            "anexo_preg2_5":"Malestar General?",
            "anexo_preg2_6":"Dolor?",
            "anexo_preg2_7":"Ningun Sintoma",        
            "fecha_sintomas":"Fecha de Sintomas",    
            "anexo_preg4_1":"Has estado fuera de ica en los últimos 14 dias?",
            "lugar_visita":"Lugares visitados",

            "anexo_preg5_1":"Has estado en contacto con un caso sospechoso o confirmado COVID-19",
            "anexo_preg6_1":"Embarazo?",
            "trimestre_embarazo":"Trimestre Embarazo",
            "anexo_preg6_2":"Enfermedad Cardiovascular/Hipertensión?",        
            "anexo_preg6_3":"Diabetes?",    
            "anexo_preg6_4":"Enfermedad hepatica?",
            "anexo_preg6_5":"Enfermedad cronica neurologica?",

            "anexo_preg6_6":"Post Parto <6 semanas?",    
            "anexo_preg6_7":"Enfermedad Renal?",
            "anexo_preg6_8":"Daño Hepático?",
            "anexo_preg6_9":"Enfermedad pulmonar crónica?",
            "anexo_preg6_10":"Cáncer?",
        }

class fichasintomatologiacovidform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(fichasintomatologiacovidform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_empresa'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['dni'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['nombre_completo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['area_trabajo'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['direccion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['celular'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg1'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg2'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg3'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg4'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg5'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_preg6'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['fecha'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
    class Meta:
        model = FichaSintomatologiaCovid
        fields = [
            
            
            'anexo_empresa',
            'dni',            
            'nombre_completo',    
            'area_trabajo',        
            'direccion',

            'celular',
            'anexo_preg1',
            'anexo_preg2',            
            'anexo_preg3',    
            'anexo_preg4',            
            'anexo_preg5',        
            'anexo_preg6',
            'fecha',
        ]

        labels={
            
            "anexo_empresa":"Empresa",
            "dni":"DNI",
            "nombre_completo":"Nombre Completo",        
            "area_trabajo":"Area",    
            "direccion":"Direccion",
            "celular":"Celular",

            "anexo_preg1":"Sensacion Termica de alza o Fiebre",
            "anexo_preg2":"Tos, estornudos o dificultad para respirar",
            "anexo_preg3":"Expectoracion o flema amarilla o verdosa",        
            "anexo_preg4":"Pérdida del Gusto y/o olfato",    
            "anexo_preg5":"Contacto con personas confirmadas COVID-19",
            "anexo_preg6":"Esta tomando alguna medicacion",
            "fecha":"Fecha",
        }
