from django.contrib import admin
from .models import SectoresAthos
from .models import NBrotes
from .models import NDiametro


from .models import EvFenBrotesArandanosSem
from .models import DetallePlantaEvFenBrotesArandanosSem
from .models import BrotePlantaEvFenBrotesArandanosSem

from .models import EvFenBrotesArandanos
from .models import DetallePlantaEvFenBrotesArandanos
from .models import BrotePlantaEvFenBrotesArandanos

from .models import ControlProductoTerminado
from .models import DetalleControlProductoTerminado

from .models import EvFenRaicesArandanos
from .models import DetalleEvFenRaicesArandanos
from .models import RaicesEvFenRaicesArandanos

from .models import EvFenFrutoArandanos
from .models import SelectorEvFrutos
from .models import SelectorTipoEnvase
from .models import SelectorTipoEnvasePlanta
from .models import DetalleEvFenFrutoArandanos

from .models import EvFenPlanasa
from .models import SelectorEvPlanasa
from .models import DetalleEvFenPlanasa

from .models import EvCalDefectosCampo
from .models import SelectorTipoCalidad
from .models import DetalleEvCalDefectosCampo

from .models import EvCalAcopioPlanta
from .models import SelectorTipoPrioridad

from .models import EvCartillaDrenado
from .models import DetalleEvCartillaDrenado

from .models import EvCalMuestreoPlantaHgIca2021
from .models import DetalleEvCalMuestreoPlantaHgIca2021

from .models import EvCalMmppGrIca2021
from .models import DetalleEvCalMmppGrIca2021

from .models import TipoAlveoloCalidad
from .models import TipoBolsaCalidad
from .models import MaterialesCalidad

from .models import SelectorCategoriaCalidad
from .models import TipoEvaluacionRm

from .models import TipoEvaluacionAr
from .models import EvCalControlDescarteAr2022
from .models import DetalleEvCalControlDescarteAr2022

from .models import TipoCondicionCamarasHumedas
from .models import TipoOrganoCamarasHumedas
from .models import TipoUbicacionCamarasHumedas
from .models import TipoProductoCamarasHumedas
from .models import EvCamarasHumedas
from .models import DetallePlantaEvCamarasHumedas


from .models import EvCalMuestreoCosechaHg2021
from .models import DetalleEvCalMuestreoCosechaHg2021

from .models import TipoCalibreAnalisisEficiencia
from .models import TipoEnvaseAnalisisEficiencia
from .models import EvEficienciaSeleccionCalibrado

from .models import EvProductoTerminadoDespacho
from .models import DetalleEvProductoTerminadoDespacho
from .models import TipoEnvioPTDespacho
from .models import TipoInspeccionVisualEstado
from .models import TipoInspeccionVisualConformidad
from .models import TipoInspeccionVisualDecision

# Register your models here.
admin.site.register(SectoresAthos)
admin.site.register(NBrotes)
admin.site.register(NDiametro)
admin.site.register(TipoEvaluacionRm)

admin.site.register(EvFenBrotesArandanosSem)
admin.site.register(DetallePlantaEvFenBrotesArandanosSem)
admin.site.register(BrotePlantaEvFenBrotesArandanosSem)

admin.site.register(EvFenBrotesArandanos)
admin.site.register(DetallePlantaEvFenBrotesArandanos)
admin.site.register(BrotePlantaEvFenBrotesArandanos)

admin.site.register(ControlProductoTerminado)
admin.site.register(DetalleControlProductoTerminado)
admin.site.register(EvFenRaicesArandanos)
admin.site.register(DetalleEvFenRaicesArandanos)
admin.site.register(RaicesEvFenRaicesArandanos)

admin.site.register(EvFenFrutoArandanos)
admin.site.register(SelectorEvFrutos)
admin.site.register(SelectorTipoEnvase)
admin.site.register(SelectorTipoEnvasePlanta)
admin.site.register(DetalleEvFenFrutoArandanos)

admin.site.register(EvFenPlanasa)
admin.site.register(SelectorEvPlanasa)
admin.site.register(DetalleEvFenPlanasa)

admin.site.register(EvCalDefectosCampo)
admin.site.register(SelectorTipoCalidad)
admin.site.register(DetalleEvCalDefectosCampo)

admin.site.register(SelectorTipoPrioridad)
admin.site.register(EvCalAcopioPlanta)

admin.site.register(EvCartillaDrenado)
admin.site.register(DetalleEvCartillaDrenado)

admin.site.register(EvCalMuestreoPlantaHgIca2021)
admin.site.register(DetalleEvCalMuestreoPlantaHgIca2021)

admin.site.register(EvCalMmppGrIca2021)
admin.site.register(DetalleEvCalMmppGrIca2021)

admin.site.register(TipoAlveoloCalidad)
admin.site.register(TipoBolsaCalidad)
admin.site.register(MaterialesCalidad)

admin.site.register(SelectorCategoriaCalidad)

admin.site.register(TipoEvaluacionAr)
admin.site.register(EvCalControlDescarteAr2022)
admin.site.register(DetalleEvCalControlDescarteAr2022)

admin.site.register(TipoCondicionCamarasHumedas)
admin.site.register(TipoOrganoCamarasHumedas)
admin.site.register(TipoUbicacionCamarasHumedas)
admin.site.register(TipoProductoCamarasHumedas)
admin.site.register(EvCamarasHumedas)
admin.site.register(DetallePlantaEvCamarasHumedas)

admin.site.register(EvCalMuestreoCosechaHg2021)
admin.site.register(DetalleEvCalMuestreoCosechaHg2021)

admin.site.register(TipoCalibreAnalisisEficiencia)
admin.site.register(TipoEnvaseAnalisisEficiencia)
admin.site.register(EvEficienciaSeleccionCalibrado)

admin.site.register(EvProductoTerminadoDespacho)
admin.site.register(DetalleEvProductoTerminadoDespacho)
admin.site.register(TipoEnvioPTDespacho)
admin.site.register(TipoInspeccionVisualEstado)
admin.site.register(TipoInspeccionVisualConformidad)
admin.site.register(TipoInspeccionVisualDecision)