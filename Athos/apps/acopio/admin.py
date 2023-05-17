from django.contrib import admin

from .models import DescarteAthos
from .models import TipoModEnfriado
from .models import ModEnfriado2022
from .models import ConfirmacionModEnfriado2022
from .models import ConfirmacionTicketModEnfriado2022
from .models import RegistroTemperaturaModEnfriado2022
from .models import TomaDatosModEnfriado2022

# Register your models here.
admin.site.register(DescarteAthos)
admin.site.register(TipoModEnfriado)

admin.site.register(ModEnfriado2022)
admin.site.register(ConfirmacionModEnfriado2022)
admin.site.register(ConfirmacionTicketModEnfriado2022)
admin.site.register(RegistroTemperaturaModEnfriado2022)
admin.site.register(TomaDatosModEnfriado2022)
