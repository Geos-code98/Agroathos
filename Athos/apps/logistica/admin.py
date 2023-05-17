from django.contrib import admin

from .models import ProveedoresAthos
from .models import TipoOperacion
from .models import Monedas
from .models import EstadoLogistica
from .models import CartillaProveedoresAthos


# Register your models here.
admin.site.register(ProveedoresAthos)
admin.site.register(TipoOperacion)
admin.site.register(Monedas)
admin.site.register(EstadoLogistica)
admin.site.register(CartillaProveedoresAthos)