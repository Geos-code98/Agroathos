from django.contrib import admin

from .models import GuiaAthosDtIca2022
from .models import GuiaDetallesAthosDtIca2022
from .models import InfoPaletDtIca2022

# Register your models here.
admin.site.register(GuiaAthosDtIca2022)
admin.site.register(GuiaDetallesAthosDtIca2022)
admin.site.register(InfoPaletDtIca2022)