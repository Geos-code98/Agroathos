from django.urls import path
#TAREO
from .views import MobileNivelUnoView
from .views import MobileNivelDosView
from .views import MobileNivelTresView

#TAREO V2
from .views import MobileTareoNivelUnoView
from .views import MobileTareoNivelDosView
from .views import MobileTareoNivelTresView

#GARITA
from .views import MobileGaritaBusView
from .views import MobileGaritaBusIntermedioView
from .views import MobileGaritaPersonalView
from .views import MobileGaritaUnidadView

#PRODUCTIVIDAD
from .views import MobileProductividadDestajoView

#TAREO PLANTA
from .views import MobileTareoPlantaNivelUnoView
from .views import MobileTareoPlantaNivelDosView
from .views import MobileTareoPlantaNivelTresView

#SEGURIDAD
from .views import MobileDataUsuariosSeguridad
from .views import MobileSeguridadNivelUnoView

#PRODUCTIVIDAD PLANTA
from .views import MobileProductividadPlanta
from .views import MobileProductividadPlantaView

#LOGIN
from .views import MobileDataUsuarios

urlpatterns = [
	
	#TAREO
	path('nivel_uno', MobileNivelUnoView.as_view(), name='data_mobile'),
	path('nivel_dos', MobileNivelDosView.as_view(), name='data_mobile_ndos'),
	path('nivel_tres', MobileNivelTresView.as_view(), name='data_mobile_ntres'),

	#TAREO V2
	path('tareo_nivel_uno', MobileTareoNivelUnoView.as_view(), name='data_mobile_tareo_n1'),
	path('tareo_nivel_dos', MobileTareoNivelDosView.as_view(), name='data_mobile_tareo_n2'),
	path('tareo_nivel_tres', MobileTareoNivelTresView.as_view(), name='data_mobile_tareo_n3'),

	#TAREO V2 LISTADO ESPECIFICO
	path('nivel_uno/<int:id>', MobileTareoNivelUnoView.as_view(), name='data_mobile_especific'),

	#GARITA
	path('garita_bus_uno', MobileGaritaBusView.as_view(), name='data_mobile_garita_uno'),
	path('garita_bus_dos', MobileGaritaBusIntermedioView.as_view(), name='data_mobile_garita_dos'),
	path('garita_personal', MobileGaritaPersonalView.as_view(), name='data_mobile_garita_personal'),
	path('garita_unidad', MobileGaritaUnidadView.as_view(), name='data_mobile_garita_unidad'),

	#PRODUCTIVIDAD
	path('productividad', MobileProductividadDestajoView.as_view(), name='data_mobile_productividad'),
	path('productividad/<int:jarra>', MobileProductividadDestajoView.as_view(), name='data_mobile_product_especific'),

	#TAREO PLANTA
	path('tareo_planta_nivel_uno', MobileTareoPlantaNivelUnoView.as_view(), name='data_mobile_tareo_planta_n1'),
	path('tareo_planta_nivel_dos', MobileTareoPlantaNivelDosView.as_view(), name='data_mobile_tareo_planta_n2'),
	path('tareo_planta_nivel_tres', MobileTareoPlantaNivelTresView.as_view(), name='data_mobile_tareo_planta_n3'),

	#SEGURIDAD
	path('seguridad_nivel_uno', MobileSeguridadNivelUnoView.as_view(), name='data_mobile_seguridad_n1'),

	#PRODUCTIVIDAD PLANTA
	path('productividad_qr', MobileProductividadPlantaView.as_view(), name='data_mobile_productividad_planta'),

	#LOGIN LISTA USUARIOS
	path('login', MobileDataUsuarios.as_view(), name='data_users'),
	path('login/<int:dni>', MobileDataUsuarios.as_view(), name='data_users_especific'),
	path('login-seguridad', MobileDataUsuariosSeguridad.as_view(), name='data_users_seguridad'),
	path('login-seguridad/<int:dni>', MobileDataUsuariosSeguridad.as_view(), name='data_seguridad_users_especific'),
]