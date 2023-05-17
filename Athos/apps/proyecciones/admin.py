from django.contrib import admin
from .models import ProyeccionArandano
from .models import DetalleProyeccionArandano
from .models import ProyeccionSemanalArandano
from .models import ProyeccionDiariaArandano
from .models import DetProyeccionDiariaArandano
from .models import ProyeccionAnualArandano
from .models import DetalleProyeccionAnualArandano


# Register your models here.
admin.site.register(ProyeccionArandano)
admin.site.register(DetalleProyeccionArandano)
admin.site.register(ProyeccionSemanalArandano)
admin.site.register(ProyeccionDiariaArandano)
admin.site.register(DetProyeccionDiariaArandano)
admin.site.register(ProyeccionAnualArandano)
admin.site.register(DetalleProyeccionAnualArandano)