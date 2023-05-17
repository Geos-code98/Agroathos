from django.contrib import admin
from .models import ProductosRiego
from .models import MetodoRiego
from .models import PozosRiego
from .models import LeyNutricionRiego
from .models import ProyeccionSemanalRiego
from .models import DetalleProyeccionSemanalRiego
from .models import RegistroRiegoFertilizacion
from .models  import DetalleRegistroRiegoFertilizacion
from .models import TanqueRiegoFertilizacion
from .models import DetRequerimientoRiegoFert
from .models import ConsumoRequerimientoRiegoFert

from .models import ExplotacionPozos
from .models import DetalleExplotacionPozos
from .models import DetalleRequerimientoRiegot
# Register your models here.

admin.site.register(ProductosRiego)
admin.site.register(MetodoRiego)
admin.site.register(PozosRiego)
admin.site.register(LeyNutricionRiego)
admin.site.register(ProyeccionSemanalRiego)
admin.site.register(DetalleProyeccionSemanalRiego)
admin.site.register(RegistroRiegoFertilizacion)
admin.site.register(DetalleRegistroRiegoFertilizacion)
admin.site.register(TanqueRiegoFertilizacion)

admin.site.register(DetRequerimientoRiegoFert)
admin.site.register(ConsumoRequerimientoRiegoFert)
admin.site.register(ExplotacionPozos)
admin.site.register(DetalleExplotacionPozos)
admin.site.register(DetalleRequerimientoRiegot)