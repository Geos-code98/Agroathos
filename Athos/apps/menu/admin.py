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
from .models import TurnoProgramaProduccion
from .models import elementoPEP
from .models import VersionAgronomica
from .models import SubVariableAgronomica
from .models import Flujo
from .models import Acciones
from .models import TipoRespuesta
from .models import Procesos
from .models import solicitud
from .models import EstadoCampana
from .models import elementoPEP

from .models import LPaletas
from .models import LPaletasReal
from .models import Turno
from .models import ConfigurarDia
from .models import AreaPlanta
from .models import ConfAsistenciaPlanta

from .models import AreaCapacitacion
from .models import CompetenciaCapacitacion
from .models import TemaCapacitacion
from .models import AlcanceCapacitacion
from .models import DatosEmpresa
from .models import ParticipantesCapacitacion
from .models import TipoCapacitacion
from .models import CapacitacionCapacitacion
from .models import AsistenciaCapacitacion

from .models import siembra
from .models import GuiaAthos

from .models import TipoTransporte
from .models import TipoUnidad

from .models import RutasAthos
from .models import GuiaDetallesAthos
from .models import LugarAthos
from .models import MaterialMMPP
from .models import Nave 
from .models import PproduccionVariable
from .models import HitosFenologicos
from .models import MaterialTransporte
from .models import LaborPlanta

admin.site.register(Nave)
admin.site.register(MaterialTransporte)
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
admin.site.register(TurnoProgramaProduccion)
admin.site.register(Flujo)
admin.site.register(Acciones)
admin.site.register(TipoRespuesta)
admin.site.register(Procesos)
admin.site.register(solicitud)
admin.site.register(EstadoCampana)
admin.site.register(elementoPEP)
admin.site.register(VersionAgronomica)
admin.site.register(LPaletas)
admin.site.register(LPaletasReal)
admin.site.register(Turno)
admin.site.register(ConfigurarDia)
admin.site.register(AreaPlanta)
admin.site.register(ConfAsistenciaPlanta)
admin.site.register(AreaCapacitacion)
admin.site.register(CompetenciaCapacitacion)
admin.site.register(TemaCapacitacion)
admin.site.register(AlcanceCapacitacion)
admin.site.register(DatosEmpresa)
admin.site.register(ParticipantesCapacitacion)
admin.site.register(TipoCapacitacion)
admin.site.register(CapacitacionCapacitacion)
admin.site.register(AsistenciaCapacitacion)
admin.site.register(siembra)
admin.site.register(GuiaAthos)

admin.site.register(TipoTransporte)
admin.site.register(TipoUnidad)
admin.site.register(RutasAthos)
admin.site.register(GuiaDetallesAthos)
admin.site.register(LugarAthos)
admin.site.register(MaterialMMPP)
admin.site.register(SubVariableAgronomica)
admin.site.register(PproduccionVariable)

admin.site.register(HitosFenologicos)
admin.site.register(LaborPlanta)