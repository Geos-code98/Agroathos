from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



from django.conf.urls import include
from apps.menu.views import usuarios
from apps.menu.views import nuevousuario
from apps.menu.views import editarusuario
from apps.menu.views import items_subitems
from apps.menu.views import registrarsubitem
from apps.menu.views import editarsubitem

from apps.menu.views import menu
from apps.menu.views import editarmenu
from apps.menu.views import crearmenu

from apps.menu.views import items
from apps.menu.views import editaritems
from apps.menu.views import crearitems

from apps.menu.views import campo
from apps.menu.views import crearcampo
from apps.menu.views import editarcampo

from apps.menu.views import cultivo
from apps.menu.views import crearcultivo
from apps.menu.views import editarcultivo

from apps.menu.views import crearfeno
from apps.menu.views import editarfeno

from apps.menu.views import crearcampana
from apps.menu.views import editarcampana

from apps.menu.views import crearvariedad
from apps.menu.views import editarvariedad
from apps.menu.views import crearmodulo
from apps.menu.views import editarmodulo

from apps.menu.views import crearlote
from apps.menu.views import editarlote

from apps.menu.views import crearproduccion
from apps.menu.views import editarproduccion

from apps.menu.views import produccionfenologias
from apps.menu.views import crearproduccionfeno
from apps.menu.views import editarproduccionfeno

from apps.menu.views import crearflujo
from apps.menu.views import editarflujo

from apps.menu.views import crearaccion
from apps.menu.views import editaraccion

from apps.menu.views import crearproceso
from apps.menu.views import editarproceso

from apps.menu.views import crearsolicitud
from apps.menu.views import editarsolicitud

from apps.menu.views import pep
from apps.menu.views import crearpep
from apps.menu.views import editarpep

from apps.menu.views import logout


from apps.menu.views import ProgramaProduccionListView
from apps.menu.views import ProgramaProduccionCreateView
from apps.menu.views import ProgramaProduccionUpdateView
from apps.menu.views import (load_modulitos, load_lotecitos)

urlpatterns = [
 	path('logout', logout, name="logout"),
	path('', include("django.contrib.auth.urls")),
	path('admin/', admin.site.urls),
	path('athos/', login_required(usuarios), name="usuarios"),
	path('athos/usuarios/registrar', login_required(nuevousuario), name="nuevousuario"),
	path('athos/usuarios/<int:id>', login_required(editarusuario), name="editarusuario"),




	path('athos/items', login_required(items), name="items"),
	path('athos/items/<int:id>', login_required(editaritems), name="editaritems"),
	path('athos/items/crear', login_required(crearitems), name="crearitems"),

	path('athos/menu', login_required(menu), name="menu"),
	path('athos/menu/<int:id>', login_required(editarmenu), name="editarmenu"),
	path('athos/menu/crear', login_required(crearmenu), name="crearmenu"),


	


	path('athos/items/subitems/<int:id>', login_required(items_subitems), name="items_subitems"),
	path('athos/items/subitems/<int:id>/nuevo', login_required(registrarsubitem), name="registrarsubitem"),
	path('athos/items/subitems/<int:id>/editar/<int:idsub>', login_required(editarsubitem), name="editarsubitem"),
	
	

	path('athos/campo/<int:id>', login_required(campo), name="campo"),
	path('athos/campo/<int:id>', login_required(crearmenu), name="crearmenu"),
	path('athos/campo/<int:id>', login_required(cultivo), name="cultivo"),

	

	path('athos/nuevocampo', login_required(crearcampo), name="crearcampo"),
	path('athos/editarcampo/<int:id>/editar/<int:subid>', login_required(editarcampo), name="editarcampo"),

	path('athos/nuevocultivo', login_required(crearcultivo), name="crearcultivo"),
	path('athos/editarcultivo/<int:id>/editar/<int:subid>', login_required(editarcultivo), name="editarcultivo"),
	
	path('athos/nuevovariedad', login_required(crearvariedad), name="crearvariedad"),
	path('athos/editarvariedad/<int:id>/editar/<int:subid>', login_required(editarvariedad), name="editarvariedad"),
	path('athos/nuevomodulo', login_required(crearmodulo), name="crearmodulo"),
	path('athos/editarmodulo/<int:id>/editar/<int:subid>', login_required(editarmodulo), name="editarmodulo"),

	path('athos/nuevolote', login_required(crearlote), name="crearlote"),
	path('athos/editarlote/<int:id>/editar/<int:subid>', login_required(editarlote), name="editarlote"),

	path('athos/nuevofeno', login_required(crearfeno), name="crearfeno"),
	path('athos/editarfeno/<int:id>/editar/<int:subid>', login_required(editarfeno), name="editarfeno"),

	path('athos/nuevocampana', login_required(crearcampana), name="crearcampana"),
	path('athos/editarcampana/<int:id>/editar/<int:subid>', login_required(editarcampana), name="editarcampana"),

	path('athos/nuevoproduccion', login_required(crearproduccion), name="crearproduccion"),
	path('athos/editarproduccion/<int:id>/editar/<int:subid>', login_required(editarproduccion), name="editarproduccion"),

	path('athos/verfeno/<int:id>/ver/<int:subid>', login_required(produccionfenologias), name="produccionfenologias"),


	path('athos/nuevoproduccionfeno/<int:id>/registro/<int:subid>', login_required(crearproduccionfeno), name="crearproduccionfeno"),
	path('athos/editarprodufeno/<int:id>/produccionfeno/<int:subid>/editar/<int:fenid>', login_required(editarproduccionfeno), name="editarproduccionfeno"),

	path('athos/nuevoflujo', login_required(crearflujo), name="crearflujo"),
	path('athos/editarflujo/<int:id>/editar/<int:subid>', login_required(editarflujo), name="editarflujo"),

	path('athos/nuevoaccion', login_required(crearaccion), name="crearaccion"),
	path('athos/editaraccion/<int:id>/editar/<int:subid>', login_required(editaraccion), name="editaraccion"),

	path('athos/nuevoproceso', login_required(crearproceso), name="crearproceso"),
	path('athos/editarproceso/<int:id>/editar/<int:subid>', login_required(editarproceso), name="editarproceso"),

	path('athos/nuevosolicitud', login_required(crearsolicitud), name="crearsolicitud"),
	path('athos/editarsolicitud/<int:id>/editar/<int:subid>', login_required(editarsolicitud), name="editarsolicitud"),

	path('athos/pep/<int:id>/ver/<int:subid>', login_required(pep), name="pep"),
	path('athos/nuevoelementopep/<int:id>/registro/<int:subid>', login_required(crearpep), name="crearpep"),
	path('athos/editarpep/<int:id>/pep/<int:subid>/editar/<int:pepid>', login_required(editarpep), name="editarpep"),



	path('', ProgramaProduccionListView.as_view(), name='programa_changelist'),
    path('add/', ProgramaProduccionCreateView.as_view(), name='programa_add'),
    path('<int:id>/', ProgramaProduccionUpdateView.as_view(), name='programa_change'),

    path('ajax/load-modulitos/<int:id>/', load_modulitos, name='ajax_load_modulitos'),  # <-- this one here
    path('ajax/load-lotecitos/<int:id>/', load_lotecitos, name='ajax_load_lotecitos'),
]	
