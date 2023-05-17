from django.contrib import admin


from .models import GaritaAthos
from .models import TrasladoGaritaAthos
from .models import DetalleGaritaBusAthos


# Register your models here.
admin.site.register(GaritaAthos)
admin.site.register(TrasladoGaritaAthos)
admin.site.register(DetalleGaritaBusAthos)
