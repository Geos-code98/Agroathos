from django.contrib import admin

from .models import ProyeccionSemanalPersonal
from .models import DetalleProyeccionSemanalPersonal

from .models import LineaProductividadPlanta
from .models import MesaProductividadPlanta

from .models import ProductividadPlanta
from .models import DetalleProductividadPlanta

from .models import ProductividadPlantaAsistencia
from .models import DetalleProductividadPlantaAsistencia

# Register your models here.
admin.site.register(ProyeccionSemanalPersonal)
admin.site.register(DetalleProyeccionSemanalPersonal)

admin.site.register(LineaProductividadPlanta)
admin.site.register(MesaProductividadPlanta)

admin.site.register(ProductividadPlanta)
admin.site.register(DetalleProductividadPlanta)

admin.site.register(ProductividadPlantaAsistencia)
admin.site.register(DetalleProductividadPlantaAsistencia)