from django.contrib import admin
from .models import MaestraAccesoAthosMobile
from .models import MobileNivelUno
from .models import TipoUsuarioAccesoAthosMobile
from .models import SedesAthosMobile
from .models import MaestraAccesoSeguridadAthosMobile
from .models import MobileProductividadPlanta
# Register your models here.

#TIPOS DE USUARIOS
admin.site.register(TipoUsuarioAccesoAthosMobile)

#SEDES
admin.site.register(SedesAthosMobile)

#MAESTRAS
admin.site.register(MaestraAccesoAthosMobile)
admin.site.register(MaestraAccesoSeguridadAthosMobile)

#PRODUCTIVIDAD
admin.site.register(MobileProductividadPlanta)

#MODELO NIVEL 1 TAREO AR
#admin.site.register(MobileNivelUno)