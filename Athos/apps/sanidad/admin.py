from django.contrib import admin
from .models import ProductosSanidad 
from .models import IngredientesSanidad 
from .models import ToxicologiaSanidad 
from .models import PlagasEnfermedadesSanidad 
from .models import TipoMetodoSanidad 
from .models import EquiposSanidad 
from .models import TipoDosisSanidad 
from .models import LugaresAplicacionSanidad 
from .models import TractoresAthos 
from .models import BoquillasSanidadAthos 
from .models import OperadoresSanidadAthos 
from .models import UbicacionProductosAutorizados
from .models import PermitidoSanidad
from .models import ProductosAutorizados


from .models import MaestraLMR
from .models import DetalleProductosAutorizados
from .models import DetalleLmrPa


from .models import UbicacionRegistroAplicacion
from .models import RegistroAplicacion
from .models import DetalleRegistroAplicacion
from .models import ConfirmativaRegistroAplicacion



# Register your models here.

admin.site.register(ProductosSanidad)
admin.site.register(IngredientesSanidad)
admin.site.register(ToxicologiaSanidad)
admin.site.register(PlagasEnfermedadesSanidad)
admin.site.register(TipoMetodoSanidad)
admin.site.register(EquiposSanidad)
admin.site.register(TipoDosisSanidad)
admin.site.register(LugaresAplicacionSanidad)
admin.site.register(TractoresAthos)
admin.site.register(BoquillasSanidadAthos)
admin.site.register(OperadoresSanidadAthos)

admin.site.register(UbicacionProductosAutorizados)
admin.site.register(PermitidoSanidad)
admin.site.register(ProductosAutorizados)

admin.site.register(MaestraLMR)
admin.site.register(DetalleProductosAutorizados)
admin.site.register(DetalleLmrPa)

admin.site.register(UbicacionRegistroAplicacion)
admin.site.register(RegistroAplicacion)
admin.site.register(DetalleRegistroAplicacion)

admin.site.register(ConfirmativaRegistroAplicacion)