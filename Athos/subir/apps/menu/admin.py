from django.contrib import admin
from .models import menu_principal
from .models import item
from .models import sub_item
from .models import perfiles
from .models import rol
from .models import Usuario_Roles
from .models import fundo
from .models import variedad
from .models import cultivo
from .models import fenologia
from .models import campanas
from .models import Estado
from .models import ejezona
from .models import lote
from .models import modulo
from .models import ProgramaProduccion
from .models import ProgramaProduccionFeno

from .models import Flujo
from .models import Acciones
from .models import TipoRespuesta
from .models import Procesos
from .models import solicitud
from .models import EstadoCampana
from .models import elementoPEP



admin.site.register(menu_principal)
admin.site.register(item)
admin.site.register(sub_item)
admin.site.register(perfiles)
admin.site.register(rol)
admin.site.register(Usuario_Roles)
admin.site.register(fundo)
admin.site.register(variedad)
admin.site.register(cultivo)
admin.site.register(fenologia)
admin.site.register(campanas)
admin.site.register(Estado)
admin.site.register(ejezona)
admin.site.register(modulo)
admin.site.register(lote)
admin.site.register(ProgramaProduccion)
admin.site.register(ProgramaProduccionFeno)
admin.site.register(Flujo)
admin.site.register(Acciones)
admin.site.register(TipoRespuesta)
admin.site.register(Procesos)
admin.site.register(solicitud)
admin.site.register(EstadoCampana)
admin.site.register(elementoPEP)