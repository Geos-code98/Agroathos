from django.contrib import admin
from .models import UbicacionPlanta

#from .models import LanzadoPaletasGrIca2021
#from .models import LanzadoPaletasArIca2022
from .models import LineasPlantaHG
from .models import LanzadoPaletasGrIca2023 
# Register your models here.
admin.site.register(UbicacionPlanta)
#admin.site.register(LanzadoPaletasGrIca2021)
#admin.site.register(LanzadoPaletasArIca2022)
admin.site.register(LineasPlantaHG)
admin.site.register(LanzadoPaletasGrIca2023)