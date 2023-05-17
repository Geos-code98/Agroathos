from django.contrib import admin

from .models import GuiaAthosArCaraz202202
from .models import GuiaDetallesAthosArCaraz202202
from .models import InfoPaletArCaraz202202

from .models import GuiaAthosArIca202202
from .models import GuiaDetallesAthosArIca202202
from .models import InfoPaletArIca202202

# Register your models here.
admin.site.register(GuiaAthosArCaraz202202)
admin.site.register(GuiaDetallesAthosArCaraz202202)
admin.site.register(InfoPaletArCaraz202202)


admin.site.register(GuiaAthosArIca202202)
admin.site.register(GuiaDetallesAthosArIca202202)
admin.site.register(InfoPaletArIca202202)