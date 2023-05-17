from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.rrhh.models import IngresoPersonalAthos
from apps.rrhh.models import FichaPersonalAthos
from apps.rrhh.models import RequerimientoPersonal
from apps.rrhh.models import DetalleRequerimientoPersonal
from apps.menu.models import ProgramaProduccion
from apps.maestras.models import LaboresPlantaAthos
from apps.rrhh.models import ProyeccionSemanalPersonal
from apps.rrhh.models import DetalleProyeccionSemanalPersonal

#PRODUCTIVIDAD PLANTA
from apps.rrhh.models import ProductividadPlanta
from apps.rrhh.models import DetalleProductividadPlanta

#PRODUCTIVIDAD PLANTA ASISTENCIA
from apps.rrhh.models import ProductividadPlantaAsistencia
from apps.rrhh.models import DetalleProductividadPlantaAsistencia
from apps.menu.models import ConfigurarDia

class ingresopersonalathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ingresopersonalathosform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_documentos'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['nro_documento'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['ApellidoPat'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['ApellidoMat'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['Nombres'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_genero'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        self.fields['FecNac'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['fecha_nacimiento'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['observacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        
    class Meta:
        model = IngresoPersonalAthos
        fields = [
            
            'anexo_documentos',
            'nro_documento',
            'ApellidoPat',
            'ApellidoMat',            
            'Nombres',
            'anexo_genero',    
            'FecNac',            
            'fecha_nacimiento',        
            'observacion'    
        ]

        labels={
            
            "anexo_documentos":"Tipo de Documento",
            "nro_documento":"Nro Documento",
            "ApellidoPat":"Apellido Paterno",
            "ApellidoMat":"Apellido Materno",        
            "Nombres":"Nombres",
            'anexo_genero':"Genero",
            "FecNac":"Fecha Nacimiento(dd.mm.yyyy)",        
            "fecha_nacimiento":"Fecha Nacimiento-Reporte",
            "observacion":"Observacion"
        }


class fichapersonalathosform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(fichapersonalathosform, self).__init__(*args, **kwargs)
        
        self.fields['nro_documento'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['ApellidoPat'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['ApellidoMat'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['Nombres'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['fecha_nacimiento'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_estadocivil'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_grado'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['celular'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['celular_emergencia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_pareja'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['nombre_pareja'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['direccion_pareja'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['celular_pareja'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['cant_hijos'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['empresa_experiencia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        

        self.fields['tiempo_experiencia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['cargo_experiencia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['lugar_nacimiento'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['direccion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['observacion'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_antecedentes'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['antecedente'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_alcohol'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        

        self.fields['anexo_tabaco'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_farmaco'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['anexo_sustancia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        self.fields['otra_sustancia'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        
    class Meta:
        model = FichaPersonalAthos
        fields = [
            
            
            'nro_documento',
            'ApellidoPat',
            'ApellidoMat',            
            'Nombres',    
                
            'fecha_nacimiento',        
            'anexo_estadocivil',

            'anexo_grado',
            'celular',
            'celular_emergencia',            
            'anexo_pareja',    
            'nombre_pareja',            
            'direccion_pareja',        
            'celular_pareja',

            'cant_hijos',
            'empresa_experiencia',
            'tiempo_experiencia',            
            'cargo_experiencia',    
            'lugar_nacimiento',            
            'direccion',        
            'observacion',    

            'anexo_antecedentes',
            'antecedente',
            'anexo_alcohol',            
            'anexo_tabaco',    
            'anexo_farmaco',            
            'anexo_sustancia',        
            'otra_sustancia',
        ]

        labels={
            
        
            "nro_documento":"Nro Documento",
            "ApellidoPat":"Apellido Paterno",
            "ApellidoMat":"Apellido Materno",        
            "Nombres":"Nombres",    
            "fecha_nacimiento":"Fecha Nacimiento",
            "anexo_estadocivil":"Estado Civil",

            "anexo_grado":"Grado de Instruccion",
            "celular":"Celular",
            "celular_emergencia":"En caso de emergencia llamar a :",        
            "anexo_pareja":"Datos del(la) Conyugue-Conviviente",    
            "nombre_pareja":"Nombre Pareja",
            "direccion_pareja":"Dirección Pareja",

            "celular_pareja":"Celular Pareja",
            "cant_hijos":"Cantidad de hijos",
            "empresa_experiencia":"Ultima Experiencia Laboralo",        
            "tiempo_experiencia":"Duración Experiencia Laboral",    
            "cargo_experiencia":"Cargo Experiencia Laboral",
            "lugar_nacimiento":"Lugar Nacimiento",

            "direccion":"Direccion",
            "observacion":"Observacion",
            "anexo_antecedentes":"¿Has tenido antecedentes?",        
            "antecedente":"Antecedente",    
            "anexo_alcohol":"Consumes Alcohol?",
            "anexo_tabaco":"Consumes Tabaco?",

            "anexo_farmaco":"Consumes algun farmaco?",    
            "anexo_sustancia":"Consumes alguna sustancia?",
            "otra_sustancia":"Otra Sustancia",
        }



class requerimientopersonalform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(requerimientopersonalform, self).__init__(*args, **kwargs)
        
        self.fields['anio'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['semana'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_cultivo'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_area'].widget.attrs.update({"placeholder":"..","data-required":"true","data-error-message":"Valvula requerida","class":"form-control"})
        
        
        
    class Meta:
        model = RequerimientoPersonal
        fields = [
            
            'anio',
            'semana',
            'anexo_cultivo',
            'anexo_fundo',            
            'anexo_area',
            ]

        labels={
            
            "anio":"Año",
            "semana":"Semana",
            "anexo_cultivo":"Cultivo",
            "anexo_fundo":"Fundo",        
            "anexo_area":"Area",
            
        }

class detallerequerimientopersonalform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(detallerequerimientopersonalform, self).__init__(*args, **kwargs)
        
        self.fields['labor'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['cantidad'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['cantidad_aprobada'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        
        self.fields['tiempo_contratacion'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['rendimiento_esperado'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        
        
        
    class Meta:
        model = DetalleRequerimientoPersonal
        fields = [
            
            'labor',
            'cantidad',
            'cantidad_aprobada',
            'tiempo_contratacion',
            'rendimiento_esperado',
            
            ]

        labels={
            
            "labor":"Labor",
            "cantidad":"Cantidad",
            "cantidad_aprobada":"Cantidad Aprobada",
            "tiempo_contratacion":"Tiempo Contratación",
            "rendimiento_esperado":"Rendimiento Esperado",
            
            
        }


#PROYECCION SEMANAL PERSONAL
class proyeccionsemanalpersonalform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(proyeccionsemanalpersonalform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_fundo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anexo_cultivo'].widget.attrs.update({"placeholder":"....","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        self.fields['anio'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Centro requerido","class":"form-control"})
        self.fields['semana'].widget.attrs.update({"placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"form-control"})
        
    class Meta:
        model = ProyeccionSemanalPersonal
        fields = [            
            'anexo_fundo',
            'anexo_cultivo',
            'anio',
            'semana',
            ]

        labels={
            "anexo_fundo":"Fundo",
            "anexo_cultivo":"Cultivo",
            "anio":"Año",
            "semana":"Semana",
        }

class detalleproyeccionsemanalpersonalform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        anexocultivo=kwargs.pop("variablecultivo")
        anexofundo=kwargs.pop("variablefundo")
        super(detalleproyeccionsemanalpersonalform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_pep']=forms.ModelChoiceField(label="PEP", queryset=ProgramaProduccion.objects.filter(anexo_fundo=anexofundo,anexo_variedad__cul=anexocultivo,estado_id=1))
        self.fields['anexo_pep'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida"})
        self.fields['anexo_labor']=forms.ModelChoiceField(label="Labor", queryset=LaboresPlantaAthos.objects.filter(anexo_cultivo=anexocultivo))
        self.fields['anexo_labor'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"class_anexo_labor"})
        self.fields['lunes_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_lunes_cantidad"})
        self.fields['lunes_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_lunes_avance"})
        self.fields['martes_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_martes_cantidad"})
        self.fields['martes_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_martes_avance"})
        self.fields['miercoles_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_miercoles_cantidad"})
        self.fields['miercoles_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_miercoles_avance"})
        self.fields['jueves_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_jueves_cantidad"})
        self.fields['jueves_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_jueves_avance"})
        self.fields['viernes_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_viernes_cantidad"})
        self.fields['viernes_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_viernes_avance"})
        self.fields['sabado_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_sabado_cantidad"})
        self.fields['sabado_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_sabado_avance"})
        self.fields['domingo_cantidad'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_domingo_cantidad"})
        self.fields['domingo_avance'].widget.attrs.update({"autocomplete":"off","placeholder":"..","required":"true","data-error-message":"Ubicacion requerida","class":"valores class_domingo_avance"})
        
    class Meta:
        model = DetalleProyeccionSemanalPersonal
        fields = [
            'anexo_pep',
            'anexo_labor',
            'lunes_cantidad',
            'lunes_avance',
            'martes_cantidad',
            'martes_avance',
            'miercoles_cantidad',
            'miercoles_avance',
            'jueves_cantidad',
            'jueves_avance',
            'viernes_cantidad',
            'viernes_avance',
            'sabado_cantidad',
            'sabado_avance',
            'domingo_cantidad',
            'domingo_avance',
            ]

        labels={
            "anexo_pep":"PEP",
            "anexo_labor":"LABOR",
            "lunes_cantidad":"LUNES - CANTIDAD",
            "lunes_avance":"LUNES - AVANCE",
            "martes_cantidad":"MARTES - CANTIDAD",
            "martes_avance":"MARTES - AVANCE",
            "miercoles_cantidad":"MIERCOLES - CANTIDAD",
            "miercoles_avance":"MIERCOLES - AVANCE",
            "jueves_cantidad":"JUEVES - CANTIDAD",
            "jueves_avance":"JUEVES - AVANCE",
            "viernes_cantidad":"VIERNES - CANTIDAD",
            "viernes_avance":"VIERNES - AVANCE",
            "sabado_cantidad":"SABADO - CANTIDAD",
            "sabado_avance":"SABADO - AVANCE",
            "domingo_cantidad":"DOMINGO - CANTIDAD",
            "domingo_avance":"DOMINGO - AVANCE",
        }

#PRODUCTIVIDAD PLANTA
class productividadplantaform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productividadplantaform, self).__init__(*args, **kwargs)
        
        self.fields['zona'].widget.attrs.update({"placeholder":"Ingresa la zona","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['nave'].widget.attrs.update({"placeholder":"Ingresa la nave","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['cultivo'].widget.attrs.update({"placeholder":"Ingresa el cultivo","required":"true","data-error-message":"Data requerida","class":"form-control"})
        
    class Meta:
        model = ProductividadPlanta
        fields = [            
            'zona',
            'nave',
            'cultivo',
        ]

        labels={
            "zona":"Zona",
            "nave":"Nave",
            "cultivo":"Cultivo",
        }

class detalleproductividadplantaform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detalleproductividadplantaform, self).__init__(*args, **kwargs)
        
        self.fields['qr'].widget.attrs.update({"placeholder":"Lectura QR","required":"true","data-error-message":"QR Requerido","class":"form-control"})
        
    class Meta:
        model = DetalleProductividadPlanta
        fields = [
            'qr',
        ]

        labels={
            "qr":"QR",
        }

class productividadplantaasistenciaform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productividadplantaasistenciaform, self).__init__(*args, **kwargs)
        
        self.fields['anexo_fecha']=forms.ModelChoiceField(label="Fecha",queryset=ConfigurarDia.objects.all().order_by("-fecha"))
        self.fields['anexo_fecha'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_linea'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_actividad_labor'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
        self.fields['anexo_mesa'].widget.attrs.update({"placeholder":"...","required":"true","data-error-message":"Data requerida","class":"form-control"})
        
    class Meta:
        model = ProductividadPlantaAsistencia
        fields = [            
            'anexo_fecha',
            'anexo_linea',
            'anexo_actividad_labor',
            'anexo_mesa',
        ]

        labels={
            "anexo_fecha":"Fecha",
            "anexo_linea":"Linea",
            "anexo_actividad_labor":"Labor/Actividad",
            "anexo_mesa":"Mesa",
        }

class detalleproductividadplantaasistenciaform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detalleproductividadplantaasistenciaform, self).__init__(*args, **kwargs)
        
        self.fields['qr'].widget.attrs.update({"placeholder":"Lectura QR","required":"true","data-error-message":"QR Requerido","class":"form-control"})
        
    class Meta:
        model = DetalleProductividadPlantaAsistencia
        fields = [
            'qr',
        ]

        labels={
            "qr":"QR",
        }

