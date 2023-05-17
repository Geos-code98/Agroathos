from django.contrib import admin
from .models import PresentacionesAthos
from .models import ClientesAthos
from .models import MaestraPresentacionesAthos
from .models import CalibresAthos
from .models import AcomodoAthos
from .models import AuxiliaresCampoAthos
from .models import ActividadesAthos
from .models import LaboresPlantaAthos
from .models import LaboresAthos
from .models import MaestraFundoCultivo
from .models import TipoAuxiliarCampoAthos

# Register your models here.
admin.site.register(PresentacionesAthos)
admin.site.register(ClientesAthos)
admin.site.register(MaestraPresentacionesAthos)
admin.site.register(CalibresAthos)
admin.site.register(AcomodoAthos)
admin.site.register(AuxiliaresCampoAthos)
admin.site.register(ActividadesAthos)
admin.site.register(LaboresPlantaAthos)
admin.site.register(LaboresAthos)
admin.site.register(MaestraFundoCultivo)
admin.site.register(TipoAuxiliarCampoAthos)
