from django.contrib import admin

from .models import GuiaAthosHgPisco2021
from .models import GuiaDetallesAthosHgPisco2021
from .models import InfoPaletHgPisco2021

from .models import GuiaAthosHgNepena2022
from .models import GuiaDetallesAthosHgNepena2022
from .models import InfoPaletHgNepena2022

# Register your models here.
admin.site.register(GuiaAthosHgPisco2021)
admin.site.register(GuiaDetallesAthosHgPisco2021)
admin.site.register(InfoPaletHgPisco2021)

admin.site.register(GuiaAthosHgNepena2022)
admin.site.register(GuiaDetallesAthosHgNepena2022)
admin.site.register(InfoPaletHgNepena2022)