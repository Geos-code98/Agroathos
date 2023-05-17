from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.conf import settings 
from django.conf.urls.static import static

from django.conf.urls import include
#importar view menu
from apps.menu.views import *

#importar view proyecciones
from apps.proyecciones.views import *

#importar view acopio_athos.granada
from apps.acopio_athos.granada.views import *

#importar view acopio
from apps.acopio.views import *

#importar view evaluaciones
from apps.evaluaciones.views import *

# importar view productoterminado
from apps.prterminado.views import *

#cgfenologias 
from apps.cgfenologias.views import *

#maestras
from apps.maestras.views import *

#logistica
from apps.logistica.views import *

#sanidad
from apps.sanidad.views import *

#riego
from apps.riego.views import *

#acopio-athos-GRANADA
from apps.acopio_athos.granada.views import *

#acopio-athos-DATIL
from apps.acopio_athos.datil.views import *

#acopio-athos-ARANDANO
from apps.acopio_athos.arandano.views import *

#acopio-athos-04-ACOPIO HIGO
from apps.acopio_athos.higo.views import *

#acopio-athos-05-ACOPIO AGUAYMANTO
from apps.acopio_athos.aguaymanto.views import *

#garita
from apps.garita.views import *

#plantagranada
from apps.planta.granada_planta.views import *

#plantahigo
from apps.planta.higo_planta.views import *

#programaproduccion
from apps.programaproduccion.views import *

#calidadagricola
from apps.calidadagricola.views import *

#topico
from apps.topico.views import *

#planificacion
from apps.planificacion.views import *

#capacitaciones
from apps.capacitaciones.views import *

#rrhh
from apps.rrhh.views import *

#MANTENIMIENTO
from apps.mantenimiento.views import *

urlpatterns = [
 	path('logout', logout, name="logout"),
	path('', include("django.contrib.auth.urls")),
	path('admin/', admin.site.urls),
	path('evaluaciones/', include('apps.evaluaciones.urls')),
	path('athos/evaluaciones/<int:id>', login_required(evaluaciones), name="evaluaciones"), #view evaluaciones
	

	path('athos/', login_required(usuarios), name="usuarios"),
	path('athos/usuarios/registrar', login_required(nuevousuario), name="nuevousuario"),
	path('athos/usuarios/<int:id>', login_required(editarusuario), name="editarusuario"),

	path('athos/items', login_required(items), name="items"),
	path('athos/items/<int:id>', login_required(editaritems), name="editaritems"),
	path('athos/items/crear', login_required(crearitems), name="crearitems"),

	path('athos/menu', login_required(menu), name="menu"),
	path('athos/menu/<int:id>', login_required(editarmenu), name="editarmenu"),
	path('athos/menu/crear', login_required(crearmenu), name="crearmenu"),

	path('home/', login_required(home), name="home"),
	
	path('athos/items/subitems/<int:id>', login_required(items_subitems), name="items_subitems"),
	path('athos/items/subitems/<int:id>/nuevo', login_required(registrarsubitem), name="registrarsubitem"),
	path('athos/items/subitems/<int:id>/editar/<int:idsub>', login_required(editarsubitem), name="editarsubitem"),
	
	path('athos/campo/<int:id>', login_required(campo), name="campo"),
	path('athos/campo/<int:id>', login_required(crearmenu), name="crearmenu"),
	path('athos/campo/<int:id>', login_required(cultivo), name="cultivo"),

	#views-id- acopio - evaluaciones-prdterminado-proyecciones-cgfenologias-maestras-logistica-sanidad-
	path('athos/acopio/campos/<int:id>', login_required(campos), name="campos"), #view acopio
	path('athos/terminado/prterminado/<int:id>', login_required(prterminado), name="prterminado"), #view prterminado
	path('athos/proyecciones/athos/<int:id>', login_required(proyecciones), name="proyecciones"), #view proyecciones
	path('athos/cgfenologias/athos/<int:id>', login_required(cgfeno), name="cgfeno"), #view cgfenologias
	path('athos/maestras/athos/<int:id>', login_required(maestras), name="maestras"), #view maestras
	path('athos/logistica/athos/<int:id>', login_required(logistica), name="logistica"), #view logistica
	path('athos/sanidad/athos/<int:id>', login_required(sanidad), name="sanidad"), #view sanidad
	path('athos/riego/athos/<int:id>', login_required(riego), name="riego"), #view riego
	path('athos/acopio-athos/athos/<int:id>', login_required(acopio_athos), name="acopio_athos"), #view acopio athos
	path('athos/acopio-athos_02/athos/<int:id>', login_required(acopio_athos_02), name="acopio_athos_02"), #view acopio athos
	path('athos/acopio-athos_03/athos/<int:id>', login_required(acopio_athos_03), name="acopio_athos_03"), #view acopio athos
	path('athos/acopio-athos_04/athos/<int:id>', login_required(acopio_athos_04), name="acopio_athos_04"), #view acopio athos
	path('athos/acopio-athos_05/athos/<int:id>', login_required(acopio_athos_05), name="acopio_athos_05"), #view acopio athos
	path('athos/garita-athos/athos/<int:id>', login_required(garita), name="garita"), #view acopio athos
	path('athos/planta-granada2020/athos/<int:id>', login_required(plantagranada), name="plantagranada"), #view planta granada
	path('athos/planta-higo2021/athos/<int:id>', login_required(plantahigo), name="plantahigo"), #view planta higo
	
	path('athos/calidad-agricola/<int:id>', login_required(calidadagricola), name="calidadagricola"),
	path('athos/topico/<int:id>', login_required(topico), name="topico"),
	path('athos/planificacion/<int:id>', login_required(planificacion), name="planificacion"),
	path('athos/capacitaciones/<int:id>', login_required(capacitaciones), name="capacitaciones"),
	path('athos/rrhh/<int:id>', login_required(rrhh), name="rrhh"),
	path('athos/mantenimiento/<int:id>', login_required(mantenimiento), name="mantenimiento"),



	path('athos/nuevocampo/<int:id>', login_required(crearcampo), name="crearcampo"),
	path('athos/editarcampo/<int:id>/editar/<int:subid>', login_required(editarcampo), name="editarcampo"),

	path('athos/nuevocultivo/<int:id>', login_required(crearcultivo), name="crearcultivo"),
	path('athos/editarcultivo/<int:id>/editar/<int:subid>', login_required(editarcultivo), name="editarcultivo"),
	
	path('athos/nuevovariedad/<int:id>', login_required(crearvariedad), name="crearvariedad"),
	path('athos/editarvariedad/<int:id>/editar/<int:subid>', login_required(editarvariedad), name="editarvariedad"),
	path('athos/nuevomodulo/<int:id>', login_required(crearmodulo), name="crearmodulo"),
	path('athos/editarmodulo/<int:id>/editar/<int:subid>', login_required(editarmodulo), name="editarmodulo"),

	path('athos/nuevolote/<int:id>', login_required(crearlote), name="crearlote"),
	path('athos/editarlote/<int:id>/editar/<int:subid>', login_required(editarlote), name="editarlote"),

	path('athos/nuevofeno/<int:id>', login_required(crearfeno), name="crearfeno"),
	path('athos/editarfeno/<int:id>/editar/<int:subid>', login_required(editarfeno), name="editarfeno"),

	path('athos/nuevocampana', login_required(crearcampana), name="crearcampana"),
	path('athos/editarcampana/<int:id>/editar/<int:subid>', login_required(editarcampana), name="editarcampana"),

	path('athos/nuevoproduccion', login_required(crearproduccion), name="crearproduccion"),
	path('athos/editarproduccion/<int:id>/editar/<int:subid>', login_required(editarproduccion), name="editarproduccion"),

	path('athos/verfeno/<int:id>/ver/<int:subid>', login_required(produccionfenologias), name="produccionfenologias"),
	path('athos/nuevoproduccionfeno/<int:id>/registro/<int:subid>', login_required(crearproduccionfeno), name="crearproduccionfeno"),
	path('athos/editarprodufeno/<int:id>/produccionfeno/<int:subid>/editar/<int:fenid>', login_required(editarproduccionfeno), name="editarproduccionfeno"),

	path('athos/VAL-programaproduccion/<int:id>/ver/<int:subid>', login_required(turnoprogramaproduccion), name="turnoprogramaproduccion"),
	path('athos/VAL-programaproduccion/<int:id>/registro/<int:subid>', login_required(crearturnoprogramaproduccion), name="crearturnoprogramaproduccion"),
	path('athos/VAL-programaproduccion/<int:id>/turno/<int:subid>/editar/<int:fenid>', login_required(editarturnoprogramaproduccion), name="editarturnoprogramaproduccion"),

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
	
	path('athos/nuevovariable/<int:id>', login_required(crearvariableagro), name="crearvariableagro"),
	path('athos/editarvariable/<int:id>/editar/<int:subid>', login_required(editarvariableagro), name="editarvariableagro"),

	path('athos/subvariable/<int:id>/sub/<int:subid>', login_required(subvariableagronomica), name="subvariableagronomica"),
	path('athos/nuevosub/<int:id>/registro/<int:subid>', login_required(crearsubvariableagronomica), name="crearsubvariableagronomica"),
	path('athos/editarsub/<int:id>/variable/<int:subid>/editar/<int:varid>', login_required(editarsubvariableagronomica), name="editarsubvariableagronomica"),

	path('athos/nuevoversion/<int:id>', login_required(crearversionagro), name="crearversionagro"),
	path('athos/editarversion/<int:id>/editar/<int:subid>', login_required(editarversionagro), name="editarversionagro"),

	path('athos/ppvar/<int:id>/ver/<int:subid>', login_required(produccionvariable), name="produccionvariable"),
	path('athos/nuevoppvar/<int:id>/registro/<int:subid>', login_required(crearproduccionvariables), name="crearproduccionvariables"),
	path('athos/editarppvar/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarproduccionvariables), name="editarproduccionvariables"),


	path('athos/nuevoplanta', login_required(crearplanta), name="crearplanta"),
	path('athos/editarplanta/<int:id>/editar/<int:subid>', login_required(editarplanta), name="editarplanta"),

	path('athos/nuevonave', login_required(crearnave), name="crearnave"),
	path('athos/editarnave/<int:id>/editar/<int:subid>', login_required(editarnave), name="editarnave"),

	path('athos/nuevolinea', login_required(crearlinea), name="crearlinea"),
	path('athos/editarlinea/<int:id>/editar/<int:subid>', login_required(editarlinea), name="editarlinea"),

	path('', ProgramaProduccionListView.as_view(), name='programa_changelist'),
    path('add/', ProgramaProduccionCreateView.as_view(), name='programa_add'),
    path('<int:id>/', ProgramaProduccionUpdateView.as_view(), name='programa_change'),

    path('ajax/load-modulitos/<int:id>/', load_modulitos, name='ajax_load_modulitos'),  # <-- this one here
    path('ajax/load-lotecitos/<int:id>/', load_lotecitos, name='ajax_load_lotecitos'),
    #path('ajax/load-planta/<int:id>/', load_planta, name='ajax_load_planta'),
     path('ajax/load-fundos/<int:id>/', load_fundos, name='ajax_load_fundos'),
     path('ajax/load-rutas/<int:id>/', load_rutas, name='ajax_load_rutas'),
     path('ajax/load-pep/<int:id>/', load_pep, name='ajax_load_pep'),
     path('ajax/load-procesos/<int:id>/', load_procesos, name='ajax_load_procesos'),
   	 path('ajax/load-objetivos/<int:id>/', load_objetivos, name='ajax_load_objetivos'),
   	 path('ajax/load-planta/<int:id>/', load_planta, name='ajax_load_planta'),
   	 path('ajax/load-nave/<int:id>/', load_nave, name='ajax_load_nave'),
   	 path('ajax/load-data-pep/<int:id>/', load_data_pep, name='ajax_load_data_pep'),
   	 path('ajax/load-producto/<int:id>/', load_producto, name='ajax_load_producto'),
   	 path('ajax/load-lineas/<int:id>/', load_lineasempaque, name='ajax_load_lineasempaque'),
   	 path('ajax/load-proveedor/<int:id>/', load_proveedor, name='ajax_load_proveedores'),
   	 path('ajax/load-tema/<int:id>/', load_tema, name='ajax_load_tema'),
   	 path('ajax/load-equipos/<int:id>/', load_equipos, name='ajax_load_equipos'),
   	 path('ajax/load-almacenes/<int:id>/', load_almacenes, name='ajax_load_almacenes'),
   	 path('ajax/load-vehiculos/<int:id>/', load_vehiculos, name='ajax_load_vehiculos'),
    path('ajax/load-chofer/<int:id>/', load_chofer, name='ajax_load_chofer'),
    path('ajax/load-ubicacion/<int:id>/', load_ubicacion, name='ajax_load_ubicacion'),
    path('ajax/load-variables/<int:id>/', load_variables, name='ajax_load_variables'),
    path('ajax/load-equipossanidad/<int:id>/', load_equipossanidad, name='ajax_load_equipos'),
    path('ajax/load-operariossanidad/<int:id>/', load_operariossanidad, name='ajax_load_operarios'),
    path('ajax/load-objetivoplagas/<int:id>/', load_objetivoplagas, name='ajax_load_objetivo'),
     path('ajax/load-pozos/<int:id>/', load_pozos, name='ajax_load_pozos'),
    path('ajax/load-turnopp/<int:id>/', load_turnopp, name='ajax_load_turnoṕp'),
  
    path('ajax/load-factor-premezcla/<int:ubicacion_id>/<int:objetivo_id>/<int:tipo_id>', load_factor_premezcla, name='ajax_load_factor_premezcla'),
   
     path('ajax/load-area-pp/<int:pep_id>/', load_area_pproduccion, name='ajax_load_area_pproduccion'),
     path('ajax/load-rutas-placas/<slug:id>', load_rutas_placas, name='ajax_load_rutas_placas'),
    

    #programaproduccion
    path('ajax/load-subgrupo/<int:id>/', load_subgrupo, name='ajax_load_subgrupo'),
    path('ajax/load-hito/<int:id>/', load_hito, name='ajax_load_hito'),
    path('ajax/load-subhito/<int:id>/', load_subhito, name='ajax_load_subhito'),

	path('athos/nuevopersonalplanta', login_required(crearpersonalplanta), name="crearpersonalplanta"),
	path('athos/editarpersonalplanta/<int:id>/editar/<int:subid>', login_required(editarpersonalplanta), name="editarpersonalplanta"),

	path('athos/nuevolanzadopaletas', login_required(crearlanzadopaletas), name="crearlanzadopaletas"),
	path('athos/editarlanzadopaletas/<int:id>/editar/<int:subid>', login_required(editarlanzadopaletas), name="editarlanzadopaletas"),



	path('athos/llr/<int:id>/ver/<int:subid>', login_required(lanzadopaletasreal), name="lanzadopaletasreal"),
	path('athos/nuevollr/<int:id>/registro/<int:subid>', login_required(crearlanzadopaletasreal), name="crearlanzadopaletasreal"),
	path('athos/editarpreal/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarlanzadopaletasreal), name="editarlanzadopaletasreal"),

	path('athos/nuevomaterial', login_required(crearmateriales), name="crearmateriales"),
	path('athos/editarmaterial/<int:id>/editar/<int:subid>', login_required(editarmateriales), name="editarmateriales"),

	path('athos/nuevoordenpedido', login_required(crearordenpedido), name="crearordenpedido"),
	path('athos/editarordenpedido/<int:id>/editar/<int:subid>', login_required(editarordenpedido), name="editarordenpedido"),

	path('athos/nuevozonapaletizado', login_required(crearzonapaletizado), name="crearzonapaletizado"),
	path('athos/editarzonapaletizado/<int:id>/editar/<int:subid>', login_required(editarzonapaletizado), name="editarzonapaletizado"),


	path('athos/ordenpedidoreal/<int:id>/ver/<int:subid>', login_required(ordenpedidoreal), name="ordenpedidoreal"),
	path('athos/nuevoordenpedidoreal/<int:id>/registro/<int:subid>', login_required(crearordenpedidoreal), name="crearordenpedidoreal"),
	path('athos/editarordenpedidoreal/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarordenpedidoreal), name="editarordenpedidoreal"),



	path('athos/paletizado/<int:id>/ver/<int:subid>', login_required(paletizado), name="paletizado"),
	path('athos/nuevopaletizado/<int:id>/registro/<int:subid>', login_required(crearpaletizado), name="crearpaletizado"),
	path('athos/editarpaletizado/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarpaletizado), name="editarpaletizado"),

	

	path('athos/verificarpalet/<int:id>/ver/<int:subid>', login_required(verificarpalet), name="verificarpalet"),
	path('athos/nuevoverificar/<int:id>/registro/<int:subid>', login_required(crearverificarpalet), name="crearverificarpalet"),
	path('athos/Editarrecepcion/<int:id>/registro/<int:subid>/editar/<int:varid>', login_required(editarverificarpalet), name="editarverificarpalet"),

	path('athos/editarpaletizado/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarpaletizado), name="editarpaletizado"),
	path('athos/configasistenciapl/<int:id>', login_required(crearconfigasistenciapl), name="crearconfigasistenciapl"),

	path('athos/ingresopl/<int:id>/ing/<int:subid>', login_required(asistenciaoingresoplanta), name="asistenciaoingresoplanta"),
	path('athos/crearingresopl/<int:id>/registro/<int:subid>', login_required(crearasistenciaingresopl), name="crearasistenciaingresopl"),
	
	path('athos/configasistenciapl/<int:id>', login_required(crearconfigasistenciapl), name="crearconfigasistenciapl"),

	path('athos/ingresopl/<int:id>/ing/<int:subid>', login_required(asistenciaoingresoplanta), name="asistenciaoingresoplanta"),
	path('athos/crearingresopl/<int:id>/registro/<int:subid>', login_required(crearasistenciaingresopl), name="crearasistenciaingresopl"),

	path('athos/salidapl/<int:id>/ing/<int:subid>', login_required(asistenciaosalidaplanta), name="asistenciaosalidaplanta"),
	path('athos/crearsalidapl/<int:id>/registro/<int:subid>', login_required(crearasistenciasalidapl), name="crearasistenciasalidapl"),

	path('athos/nuevoarea', login_required(creararea), name="creararea"),
	path('athos/editararea/<int:id>/editar/<int:subid>', login_required(editararea), name="editararea"),

	path('athos/nuevocompe', login_required(crearcompetencias), name="crearcompetencias"),
	path('athos/editarcompe/<int:id>/editar/<int:subid>', login_required(editarcompetencias), name="editarcompetencias"),

	path('athos/nuevotema', login_required(creartema), name="creartema"),
	path('athos/editartema/<int:id>/editar/<int:subid>', login_required(editartema), name="editartema"),


	path('athos/alcance-capacitacion/<int:id>', login_required(crearalcancecapacitacion), name="crearalcancecapacitacion"),
	path('athos/alcance-capacitacion/<int:id>/editar/<int:subid>', login_required(editaralcancecapacitacion), name="editaralcancecapacitacion"),



	path('athos/nuevocapacitacion/<int:id>', login_required(crearcapacitacion), name="crearcapacitacion"),
	path('athos/editarcapacitacion/<int:id>/editar/<int:subid>', login_required(editarcapacitacion), name="editarcapacitacion"),
	path('athos/confirmar-capacitacion/<int:id>/confirmar/<int:subid>', login_required(confirmativacapacitacion), name="confirmativacapacitacion"),
	
	path('athos/detalle-capacitacion/<int:id>/ver/<int:subid>', login_required(asistenciacapacitacion), name="asistenciacapacitacion"),
	path('athos/detalle-capacitacion/<int:id>/registro/<int:subid>', login_required(crearasistenciacapacitacion), name="crearasistenciacapacitacion"),
	path('athos/detalle-capacitacion/<int:id>/reg/<int:subid>/editar/<int:varid>', login_required(editarasistenciacapacitacion), name="editarasistenciacapacitacion"),
	
	path('athos/nuevolabor', login_required(crearlabor), name="crearlabor"),
	path('athos/editarlabor/<int:id>/editar/<int:subid>', login_required(editarlabor), name="editarlabor"),

	path('athos/nuevoturno', login_required(crearturno), name="crearturno"),
	path('athos/editarturno/<int:id>/editar/<int:subid>', login_required(editarturno), name="editarturno"),

	path('athos/nuevoarealabor', login_required(creararealabor), name="creararealabor"),
	path('athos/editararealabor/<int:id>/editar/<int:subid>', login_required(editararealabor), name="editararealabor"),

	path('athos/nuevofecha', login_required(crearfecha), name="crearfecha"),



	path('athos/nuevomaterialaco', login_required(crearmaterialacopio), name="crearmaterialacopio"),
	path('athos/editarmaterialaco/<int:id>/editar/<int:subid>', login_required(editarmaterialacopio), name="editarmaterialacopio"),

	path('athos/nuevomaterialtransporte', login_required(crearmaterialtransporte), name="crearmaterialtransporte"),
	path('athos/editarmaterialtransporte/<int:id>/editar/<int:subid>', login_required(editarmaterialtransporte), name="editarmaterialtransporte"),

	path('athos/nuevomaterialmmpp', login_required(crearmaterialmmpp), name="crearmaterialmmpp"),
	path('athos/editarmaterialmmpp/<int:id>/editar/<int:subid>', login_required(editarmaterialmmpp), name="editarmaterialmmpp"),



	path('athos/nuevoplacasvehiculares', login_required(crearplacasvehiculares), name="crearplacasvehiculares"),
	path('athos/editarplacas/<int:id>/editar/<int:subid>', login_required(editarplacasvehiculares), name="editarplacasvehiculares"),

	path('athos/detalle-placas-vehiculares/<int:id>/ver/<int:subid>', login_required(detalleplacasvehiculares), name="detalleplacasvehiculares"),
	path('athos/detalle-placas-vehiculares/<int:id>/registro/<int:subid>', login_required(creardetalleplacasvehiculares), name="creardetalleplacasvehiculares"),
	path('athos/detalle-placas-vehiculares/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleplacasvehiculares), name="editardetalleplacasvehiculares"),

	path('athos/nuevochoferesathos', login_required(crearchoferesathos), name="crearchoferesathos"),
	path('athos/editarchoferesathos/<int:id>/editar/<int:subid>', login_required(editarchoferesathos), name="editarchoferesathos"),

	path('athos/nuevounidadvehicular', login_required(crearunidadvehicular), name="crearunidadvehicular"),
	path('athos/editarnuevounidadvehicular/<int:id>/editar/<int:subid>', login_required(editarunidadvehicular), name="editarunidadvehicular"),

	path('athos/nuevoubicacionfundo', login_required(crearubicacionfundo), name="crearubicacionfundo"),
	path('athos/editarubicacionfundo/<int:id>/editar/<int:subid>', login_required(editarubicacionfundo), name="editarubicacionfundo"),

	path('athos/nuevolugarathos', login_required(crearlugarathos), name="crearlugarathos"),
	path('athos/editarlugarathos/<int:id>/editar/<int:subid>', login_required(editarlugarathos), name="editarlugarathos"),

	path('athos/nuevocentrosathos', login_required(crearcentrosathos), name="crearcentrosathos"),
	path('athos/editarcentrosathos/<int:id>/editar/<int:subid>', login_required(editarcentrosathos), name="editarcentrosathos"),

	path('athos/nuevoalmacenesathos', login_required(crearalmacenesathos), name="crearalmacenesathos"),
	path('athos/editaralmacenesathos/<int:id>/editar/<int:subid>', login_required(editaralmacenesathos), name="editaralmacenesathos"),

	path('athos/nuevoguiaathos', login_required(crearguiaathos), name="crearguiaathos"),
	path('athos/editarguiaathos/<int:id>/editar/<int:subid>', login_required(editarguiaathos), name="editarguiaathos"),

	path('athos/guiad/<int:id>/desc/<int:subid>', login_required(guiadetallesathos), name="guiadetallesathos"),
	path('athos/crearguiad/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathos), name="crearguiadetallesathos"),
	path('athos/editarguiad/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathos), name="editarguiadetallesathos"),



	path('athos/infopalet/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopalet), name="infopalet"),
	path('athos/nuevoinfopalet/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopalet), name="crearinfopalet"),
	path('athos/editarinfop/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopalet), name="editarinfopalet"),

	path('athos/print/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpalet), name="printpalet"),
	path('athos/nuevoparihuela', login_required(crearparihuela), name="crearparihuela"),
	path('athos/editarparihuela/<int:id>/editar/<int:subid>', login_required(editarparihuela), name="editarparihuela"),

	path('athos/nuevoacopiogarita', login_required(creargaritaacopio), name="creargaritaacopio"),
	path('athos/editaracopiogarita/<int:id>/editar/<int:subid>', login_required(editargaritaacopio), name="editargaritaacopio"),

	
	path('athos/nuevaruta/<int:id>', login_required(crearrutasathos), name="crearrutasathos"),
	path('athos/editarruta/<int:id>/editar/<int:subid>', login_required(editarrutasathos), name="editarrutasathos"),
	
	path('athos/hitos/<int:id>/athos/<int:subid>', login_required(hitos), name="hitos"),
	path('athos/crearhitos/<int:id>/registro/<int:subid>', login_required(crearhitos), name="crearhitos"),
	path('athos/editarhitos/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarhitos), name="editarhitos"),


	path('athos/subhitos/<int:id>/athos/<int:subid>/ver/<int:varid>', login_required(subhitos), name="subhitos"),
	path('athos/nuevo/subhitos/<int:id>/athos/<int:subid>/registro/<int:varid>/crear', login_required(crearsubhitos), name="crearsubhitos"),
	path('athos/edita/subhitos/<int:id>/var/<int:subid>/subhitos/<int:varid>/editar/<int:catid>', login_required(editarsubhitos), name="editarsubhitos"),

	path('athos/hitos-fenologicos/<int:id>/ver/<int:subid>/sprd/<int:varid>', login_required(hitosfenologicos), name="hitosfenologicos"),
	path('athos/hitos-fenologicos/<int:id>/registro/<int:subid>/sprd/<int:varid>/crear/', login_required(crearhitosfenologicos), name="crearhitosfenologicos"),
	path('athos/hitos-fenologicos/<int:id>/editar/<int:subid>/prdl/<int:varid>/editar/<int:catid>', login_required(editarhitosfenologicos), name="editarhitosfenologicos"),




#acopio
	path('athos/acopio/campos/nuevoenfriadoathos/<int:id>', login_required(crearenfriado), name="crearenfriado"),
	path('athos/acopio/campos/editarenfriadoathos/<int:id>/editar/<int:subid>', login_required(editarenfriado), name="editarenfriado"),


	path('athos/acopio/<int:id>/enfriado/<int:subid>', login_required(distribucionenfriado), name="distribucionenfriado"),
	path('athos/nuevodistribucion/<int:id>/registro/<int:subid>', login_required(creardistribucionenfriado), name="creardistribucionenfriado"),
	path('athos/editardistribucion/<int:id>/enfriado/<int:subid>/editar/<int:varid>', login_required(editardistribucionenfriado), name="editardistribucionenfriado"),

	path('athos/acopio/<int:id>/confirmacion-enfriado/<int:subid>', login_required(confirmacionenfriado), name="confirmacionenfriado"),
	path('athos/nuevoconfirmacion/<int:id>/registro/<int:subid>', login_required(crearconfirmacionenfriado), name="crearconfirmacionenfriado"),
	path('athos/editarconfirmacion/<int:id>/enfriado/<int:subid>/editar/<int:varid>', login_required(editarconfirmacionenfriado), name="editarconfirmacionenfriado"),

	path('athos/acopio/<int:id>/confirmacion-ticket-enfriado/<int:subid>/registro/<int:varid>', login_required(confirmacionticketenfriado), name="confirmacionticketenfriado"),
	path('athos/nuevoconfirmacion/<int:id>/ticket/<int:subid>/registro/<int:varid>/crear', login_required(crearconfirmacionticketenfriado), name="crearconfirmacionticketenfriado"),
	path('athos/editarconfirmacion/<int:id>/ticket/<int:subid>/enfriado/<int:varid>/editar/<int:catid>', login_required(editarconfirmacionticketenfriado), name="editarconfirmacionticketenfriado"),

	path('athos/acopio/<int:id>/temperatura-enfriado/<int:subid>', login_required(registrotemperatura), name="registrotemperatura"),
	path('athos/nueva-temperatura/<int:id>/registro/<int:subid>', login_required(crearregistrotemperaturaenfriado), name="crearregistrotemperaturaenfriado"),
	path('athos/editar-temperatura/<int:id>/enfriado/<int:subid>/editar/<int:varid>', login_required(editarregistrotemperaturaenfriado), name="editarregistrotemperaturaenfriado"),

	path('athos/acopio/<int:id>/toma-de-datos-enfriado/<int:subid>/registro/<int:varid>', login_required(tomadatosenfriado), name="tomadatosenfriado"),
	path('athos/nuevo-toma-datos/<int:id>/enfriado/<int:subid>/registro/<int:varid>/crear', login_required(creartomadatosenfriado), name="creartomadatosenfriado"),
	path('athos/editar-toma-datos/<int:id>/palet/<int:subid>/enfriado/<int:varid>/editar/<int:catid>', login_required(editartomadatosenfriado), name="editartomadatosenfriado"),

	path('athos/temperatura/<int:id>/enfriado/<int:subid>/ver/<int:varid>', login_required(temperaturaenfriado), name="temperaturaenfriado"),
	path('athos/nuevotemperaturat/<int:id>/enfriado/<int:subid>/registro/<int:varid>/crear', login_required(creartemperaturaenfriado), name="creartemperaturaenfriado"),
	path('athos/editartemperatura/<int:id>/var/<int:subid>/enfriado/<int:varid>/editar/<int:catid>', login_required(editartemperaturaenfriado), name="editartemperaturaenfriado"),
	path('athos/nuevodescarte/<int:id>', login_required(creardescarteathos), name="creardescarteathos"),
	path('athos/editardescarte/<int:id>/editar/<int:subid>', login_required(editardescarteathos), name="editardescarteathos"),
	path('athos/nuevodescarte_planta_hg/<int:id>', login_required(creardescarteplantahgathos), name="creardescarteplantahgathos"),
	path('athos/editardescarte_planta_hg/<int:id>/editar/<int:subid>', login_required(editardescarteplantahgathos), name="editardescarteplantahgathos"),

	path('athos/acopio/nuevosalidadescarteathos/<int:id>', login_required(crearsalidadescarte), name="crearsalidadescarte"),
	path('athos/acopio/editarsalidadescarteathos/<int:id>/editar/<int:subid>', login_required(editarsalidadescarte), name="editarsalidadescarte"),

#evaluaciones
	path('athos/ev/fen/nuevoevbrarandano/<int:id>', login_required(crearevfenarandanobrote), name="crearevfenarandanobrote"),
	path('athos/ev/fen/editarevbrarandano/<int:id>/editar/<int:subid>', login_required(editarevfenarandanobrote), name="editarevfenarandanobrote"),

	path('athos/ev/<int:id>/detalle/<int:subid>', login_required(detalleplantaevfenbrotesarandanos), name="detalleplantaevfenbrotesarandanos"),
	path('athos/crear/<int:id>/registro/<int:subid>', login_required(creardetalleplantaevfenbrotesarandanos), name="creardetalleplantaevfenbrotesarandanos"),
	path('athos/editarev/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleplantaevfenbrotesarandanos), name="editardetalleplantaevfenbrotesarandanos"),

	path('athos/brote/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(broteevfenar), name="broteevfenar"),
	path('athos/nuevobrote/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearbroteevfenar), name="crearbroteevfenar"),
	path('athos/editarbrote/<int:id>/var/<int:subid>/editar/<int:varid>/evfen/<int:catid>', login_required(editarbroteevfenar), name="editarbroteevfenar"),
	
	#RAMAS
	path('athos/ev/fen/nuevoevramasarandano/<int:id>', login_required(crearevfenarandanoramas), name="crearevfenarandanoramas"),
	path('athos/ev/fen/editarevramasarandano/<int:id>/editar/<int:subid>', login_required(editarevfenarandanoramas), name="editarevfenarandanoramas"),
	path('athos/ev/<int:id>/detalleramas/<int:subid>', login_required(detalleplantaevfenramasarandanos), name="detalleplantaevfenramasarandanos"),
	path('athos/crear/<int:id>/registroramas/<int:subid>', login_required(creardetalleplantaevfenramasarandanos), name="creardetalleplantaevfenramasarandanos"),
	path('athos/editarev/<int:id>/var/<int:subid>/editarramas/<int:varid>', login_required(editardetalleplantaevfenramasarandanos), name="editardetalleplantaevfenramasarandanos"),
	path('athos/ramas/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(ramasevfenar), name="ramasevfenar"),
	path('athos/nuevoramas/<int:id>/registroramas/<int:subid>/acopio/<int:varid>/crear', login_required(crearramasevfenar), name="crearramasevfenar"),
	path('athos/editarramas/<int:id>/var/<int:subid>/editarramas/<int:varid>/evfen/<int:catid>', login_required(editarramasevfenar), name="editarramasevfenar"),

	path('athos/ev/fen/crearraices/<int:id>', login_required(crearevfenraicesarandanos), name="crearevfenraicesarandanos"),
	path('athos/ev/fen/editarraices/<int:id>/editar/<int:subid>', login_required(editarevfenraicesarandanos), name="editarevfenraicesarandanos"),

	path('athos/evraices/<int:id>/detalle/<int:subid>', login_required(detalleevfenraicesarandanos), name="detalleevfenraicesarandanos"),
	path('athos/crearevraices/<int:id>/registro/<int:subid>', login_required(creardetalleevfenraicesarandanos), name="creardetalleevfenraicesarandanos"),
	path('athos/editarevraicesv/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevfenraicesarandanos), name="editardetalleevfenraicesarandanos"),

	path('athos/raices/<int:id>/ver/<int:subid>/evfen/<int:varid>', login_required(raicesevfenraicesarandanos), name="raicesevfenraicesarandanos"),
	path('athos/nuevoraices/<int:id>/registro/<int:subid>/evfen/<int:varid>/crear', login_required(crearraicesevfenraicesarandanos), name="crearraicesevfenraicesarandanos"),
	path('athos/editarraices/<int:id>/var/<int:subid>/editar/<int:varid>/evfen/<int:catid>', login_required(editarraicesevfenraicesarandanos), name="editarraicesevfenraicesarandanos"),

	path('athos/Control/<int:id>/PT/<int:subid>', login_required(controlproductoterminado), name="controlproductoterminado"),
	path('athos/crear/<int:id>/registroCPT/<int:subid>', login_required(crearcontrolproductoterminado), name="crearcontrolproductoterminado"),
	path('athos/editarev/<int:id>/var/<int:subid>/editarCPT/<int:varid>', login_required(editarcontrolproductoterminado), name="editarcontrolproductoterminado"),

	path('athos/DetControl/<int:id>/ver/<int:subid>/ev/<int:varid>', login_required(detallecontrolproductoterminado), name="detallecontrolproductoterminado"),
	path('athos/nuevoDetControl/<int:id>/registro/<int:subid>/ev/<int:varid>/crear', login_required(creardetallecontrolproductoterminado), name="creardetallecontrolproductoterminado"),
	path('athos/editarDetControl/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:catid>', login_required(editardetallecontrolproductoterminado), name="editardetallecontrolproductoterminado"),

	path('athos/control/<int:id>/PT-Hg/<int:subid>', login_required(controlproductoterminadohg), name="controlproductoterminadohg"),
	path('athos/crear/<int:id>/registro-CPT-Hg/<int:subid>', login_required(crearcontrolproductoterminadohg), name="crearcontrolproductoterminadohg"),
	path('athos/editarev/<int:id>/var/<int:subid>/editar-CPT-Hg/<int:varid>', login_required(editarcontrolproductoterminadohg), name="editarcontrolproductoterminadohg"),

	path('athos/DetControl-Hg/<int:id>/ver/<int:subid>/ev/<int:varid>', login_required(detallecontrolproductoterminadohg), name="detallecontrolproductoterminadohg"),
	path('athos/nuevoDetControl-Hg/<int:id>/registro/<int:subid>/ev/<int:varid>/crear', login_required(creardetallecontrolproductoterminadohg), name="creardetallecontrolproductoterminadohg"),
	path('athos/editarDetControl-Hg/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:catid>', login_required(editardetallecontrolproductoterminadohg), name="editardetallecontrolproductoterminadohg"),

	path('athos/ev/fen/nuevoevbrarandanose/<int:id>', login_required(crearevfenarandanobrotesem), name="crearevfenarandanobrotesem"),
	path('athos/ev/fen/editarevbrarandanose/<int:id>/editar/<int:subid>', login_required(editarevfenarandanobrotesem), name="editarevfenarandanobrotesem"),

	path('athos/ev/<int:id>/detallese/<int:subid>', login_required(detalleplantaevfenbrotesarandanossem), name="detalleplantaevfenbrotesarandanossem"),
	path('athos/crear/<int:id>/registrose/<int:subid>', login_required(creardetalleplantaevfenbrotesarandanossem), name="creardetalleplantaevfenbrotesarandanossem"),
	path('athos/editarevse/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleplantaevfenbrotesarandanossem), name="editardetalleplantaevfenbrotesarandanossem"),


	path('athos/brotese/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(broteevfenarsem), name="broteevfenarsem"),
	path('athos/nuevobrotese/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearbroteevfenarsem), name="crearbroteevfenarsem"),
	path('athos/editarbrotese/<int:id>/var/<int:subid>/editar/<int:varid>/evfen/<int:catid>', login_required(editarbroteevfenarsem), name="editarbroteevfenarsem"),

	path('athos/ev/san/crear-plagas/<int:id>', login_required(crearevsanplagasarandanos), name="crearevsanplagasarandanos"),
	path('athos/ev/san/editar-plagas/<int:id>/editar/<int:subid>', login_required(editarevsanplagasarandanos), name="editarevsanplagasarandanos"),

	path('athos/grupos-plagas/<int:id>/detalle/<int:subid>', login_required(gruposplagasarandanos), name="gruposplagasarandanos"),
	path('athos/crear-grupos/<int:id>/registro/<int:subid>', login_required(creargruposplagasarandanos), name="creargruposplagasarandanos"),
	path('athos/editar-grupos/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editargruposplagasarandanos), name="editargruposplagasarandanos"),


	path('athos/subgrupos-plagas/<int:id>/ver/<int:subid>/ev/<int:varid>', login_required(subgruposplagasarandanos), name="subgruposplagasarandanos"),
	path('athos/nuevosubgrupos-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear', login_required(crearsubgruposplagasarandanos), name="crearsubgruposplagasarandanos"),
	path('athos/editarsubgrupos-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:catid>', login_required(editarsubgruposplagasarandanos), name="editarsubgruposplagasarandanos"),

	path('athos/variables-plagas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(variablesplagasarandanos), name="variablesplagasarandanos"),
	path('athos/nuevovariables-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearvariablesplagasarandanos), name="crearvariablesplagasarandanos"),
	path('athos/editarvariables-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarvariablesplagasarandanos), name="editarvariablesplagasarandanos"),

	path('athos/arana-roja/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(aranaroja), name="aranaroja"),
	path('athos/nuevoaranaroja-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(creararanaroja), name="creararanaroja"),
	path('athos/editararanaroja-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editararanaroja), name="editararanaroja"),

	path('athos/argy/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(argy), name="argy"),
	path('athos/nuevoargy-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearargy), name="crearargy"),
	path('athos/editarargy-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarargy), name="editarargy"),

	path('athos/cigarrita/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(cigarrita), name="cigarrita"),
	path('athos/nuevocigarrita-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcigarrita), name="crearcigarrita"),
	path('athos/editarcigarrita-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcigarrita), name="editarcigarrita"),

	path('athos/cochi/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(cochinilla), name="cochinilla"),
	path('athos/nuevocochinilla-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcochinilla), name="crearcochinilla"),
	path('athos/editarcochi-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcochinilla), name="editarcochinilla"),

	path('athos/crypto/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(crypto), name="crypto"),
	path('athos/nuevocrypto-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcrypto), name="crearcrypto"),
	path('athos/editarcrypto-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcrypto), name="editarcrypto"),

	path('athos/diabro/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(diabro), name="diabro"),
	path('athos/nuevodiabro-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(creardiabro), name="creardiabro"),
	path('athos/editardiabro-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editardiabro), name="editardiabro"),

	path('athos/gryllus/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(gryllus), name="gryllus"),
	path('athos/nuevogryllus-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(creargryllus), name="creargryllus"),
	path('athos/editargryllus-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editargryllus), name="editargryllus"),

	path('athos/helio/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(helio), name="helio"),
	path('athos/nuevohelio-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearhelio), name="crearhelio"),
	path('athos/editarhelio-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarhelio), name="editarhelio"),

	path('athos/membracidos/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(membracidos), name="membracidos"),
	path('athos/nuevomembracidos-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearmembracidos), name="crearmembracidos"),
	path('athos/editarmembracidos-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarmembracidos), name="editarmembracidos"),

	path('athos/moscablanca/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(moscablanca), name="moscablanca"),
	path('athos/nuevomoscablanca-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearmoscablanca), name="crearmoscablanca"),
	path('athos/editarmoscablanca-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarmoscablanca), name="editarmoscablanca"),

	path('athos/moscafruta/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(moscafruta), name="moscafruta"),
	path('athos/nuevomoscafruta-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearmoscafruta), name="crearmoscafruta"),
	path('athos/editarmoscafruta-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarmoscafruta), name="editarmoscafruta"),

	path('athos/plecto/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(plecto), name="plecto"),
	path('athos/nuevoplecto-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearplecto), name="crearplecto"),
	path('athos/editarplecto-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarplecto), name="editarplecto"),

	path('athos/procospidos/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(procospidos), name="procospidos"),
	path('athos/nuevoprocospidos-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearprocospidos), name="crearprocospidos"),
	path('athos/editarprocospidos-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarprocospidos), name="editarprocospidos"),

	path('athos/pulgones/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(pulgones), name="pulgones"),
	path('athos/nuevopulgones-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearpulgones), name="crearpulgones"),
	path('athos/editarpulgones-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarpulgones), name="editarpulgones"),

	path('athos/queresas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(queresas), name="queresas"),
	path('athos/nuevoqueresas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearqueresas), name="crearqueresas"),
	path('athos/editarqueresas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarqueresas), name="editarqueresas"),

	path('athos/spodo/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(spodo), name="spodo"),
	path('athos/nuevospodo-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearspodo), name="crearspodo"),
	path('athos/editarspodo-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarspodo), name="editarspodo"),

	path('athos/trips/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(trips), name="trips"),
	path('athos/nuevotrips-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(creartrips), name="creartrips"),
	path('athos/editartrips-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editartrips), name="editartrips"),

	path('athos/aranas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(aranas), name="aranas"),
	path('athos/nuevoaranas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(creararanas), name="creararanas"),
	path('athos/editararanas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editararanas), name="editararanas"),

	path('athos/cocci/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(cocci), name="cocci"),
	path('athos/nuevococci-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcocci), name="crearcocci"),
	path('athos/editarcocci-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcocci), name="editarcocci"),

	path('athos/crisopas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(crisopas), name="crisopas"),
	path('athos/nuevocrisopas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcrisopas), name="crearcrisopas"),
	path('athos/editarcrisopas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcrisopas), name="editarcrisopas"),

	path('athos/cryptola/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(cryptola), name="cryptola"),
	path('athos/nuevocryptola-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearcryptola), name="crearcryptola"),
	path('athos/editarcryptola-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarcryptola), name="editarcryptola"),

	path('athos/otro/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(otro), name="otro"),
	path('athos/nuevootro-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearotro), name="crearotro"),
	path('athos/editarotro-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarotro), name="editarotro"),

	path('athos/alternaria/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(alternaria), name="alternaria"),
	path('athos/nuevoalternaria-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearalternaria), name="crearalternaria"),
	path('athos/editaralternaria-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editaralternaria), name="editaralternaria"),

	path('athos/antra/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(antra), name="antra"),
	path('athos/nuevoantra-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearantra), name="crearantra"),
	path('athos/editarantra-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarantra), name="editarantra"),

	path('athos/botri/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(botri), name="botri"),
	path('athos/nuevobotri-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearbotri), name="crearbotri"),
	path('athos/editarbotri-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarbotri), name="editarbotri"),

	path('athos/lasio/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(lasio), name="lasio"),
	path('athos/nuevolasio-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearlasio), name="crearlasio"),
	path('athos/editarlasio-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarlasio), name="editarlasio"),

	path('athos/pestalo/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(pestalo), name="pestalo"),
	path('athos/nuevopestalo-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearpestalo), name="crearpestalo"),
	path('athos/editarpestalo-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarpestalo), name="editarpestalo"),

	path('athos/phyto/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(phyto), name="phyto"),
	path('athos/nuevophyto-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearphyto), name="crearphyto"),
	path('athos/editarphyto-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarphyto), name="editarphyto"),

	path('athos/plantaquemada/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(plantaquemada), name="plantaquemada"),
	path('athos/nuevoplantaquemada-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearplantaquemada), name="crearplantaquemada"),
	path('athos/editarplantaquemada-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarplantaquemada), name="editarplantaquemada"),

	path('athos/roya/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(roya), name="roya"),
	path('athos/nuevoroya-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearroya), name="crearroya"),
	path('athos/editarroya-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarroya), name="editarroya"),

	path('athos/hojasanchas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(hojasanchas), name="hojasanchas"),
	path('athos/nuevohojasanchas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearhojasanchas), name="crearhojasanchas"),
	path('athos/editarhojasanchas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarhojasanchas), name="editarhojasanchas"),

	path('athos/hojasangostas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(hojasangostas), name="hojasangostas"),
	path('athos/nuevohojasangostas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearhojasangostas), name="crearhojasangostas"),
	path('athos/editarhojasangostas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarhojasangostas), name="editarhojasangostas"),

	path('athos/abejas/<int:id>/ver/<int:subid>/ev/<int:varid>/var/<int:nicoid>', login_required(abejas), name="abejas"),
	path('athos/nuevoabejas-plagas/<int:id>/registro/<int:subid>/ev/<int:varid>/crear/<int:nicoid>', login_required(crearabejas), name="crearabejas"),
	path('athos/editarabejas-plagas/<int:id>/ev/<int:subid>/editar/<int:varid>/cpt/<int:nicoid>/ed/<int:chelitaid>', login_required(editarabejas), name="editarabejas"),


	path('athos/ev/fenfrutos/crear-frutos/<int:id>', login_required(crearevfenfrutoarandanos), name="crearevfenfrutoarandanos"),
	path('athos/ev/fen/editar-frutos/<int:id>/editar/<int:subid>', login_required(editarevfenfrutoarandanos), name="editarevfenfrutoarandanos"),

	path('athos/evfrutosdet/<int:id>/detalle/<int:subid>', login_required(detalleevfenfrutoarandanos), name="detalleevfenfrutoarandanos"),
	path('athos/evfrutosdet/<int:id>/registro/<int:subid>', login_required(creardetalleevfenfrutoarandanos), name="creardetalleevfenfrutoarandanos"),
	path('athos/evfrutosdet/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevfenfrutoarandanos), name="editardetalleevfenfrutoarandanos"),

	path('athos/crear-evfenplanasa/<int:id>', login_required(crearevfenplanasa), name="crearevfenplanasa"),
	path('athos/editar-evfenplanasa/<int:id>/editar/<int:subid>', login_required(editarevfenplanasa), name="editarevfenplanasa"),

	path('athos/det-evfenplanasa/<int:id>/detalle/<int:subid>', login_required(detalleevfenplanasa), name="detalleevfenplanasa"),
	path('athos/det-evfenplanasa/<int:id>/registro/<int:subid>', login_required(creardetalleevfenplanasa), name="creardetalleevfenplanasa"),
	path('athos/det-evfenplanasa/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevfenplanasa), name="editardetalleevfenplanasa"),

	path('athos/crear-evcaldefectoscampos/<int:id>', login_required(crearevcaldefectoscampo), name="crearevcaldefectoscampo"),
	path('athos/editar-evcaldefectoscampos/<int:id>/editar/<int:subid>', login_required(editarevcaldefectoscampo), name="editarevcaldefectoscampo"),

	path('athos/det-evcaldefectos/<int:id>/detalle/<int:subid>', login_required(detalleevcaldefectoscampo), name="detalleevcaldefectoscampo"),
	path('athos/det-evcaldefectos/<int:id>/registro/<int:subid>', login_required(creardetalleevcaldefectoscampo), name="creardetalleevcaldefectoscampo"),
	path('athos/det-evcaldefectos/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcaldefectoscampo), name="editardetalleevcaldefectoscampo"),

	path('athos/evcalacopioplanta/<int:id>/PT/<int:subid>', login_required(evcalacopioplanta), name="evcalacopioplanta"),
	path('athos/crearevcalacopioplanta/<int:id>/registroCPT/<int:subid>', login_required(crearevcalacopioplanta), name="crearevcalacopioplanta"),
	path('athos/editarevcalacopioplanta/<int:id>/var/<int:subid>/editarCPT/<int:varid>', login_required(editarevcalacopioplanta), name="editarevcalacopioplanta"),


	path('athos/ev-calcajasgrica/<int:id>', login_required(crearevcalmuestracajasempacadasgrica2022), name="crearevcalmuestracajasempacadasgrica2022"),
	path('athos/ev-calcajasgrica/<int:id>/editar/<int:subid>', login_required(editarevcalmuestracajasempacadasgrica2022), name="editarevcalmuestracajasempacadasgrica2022"),
	path('athos/detalle-evcal-cajas-empacadas-gr/<int:id>/Ver/<int:subid>', login_required(detalleevcalmuestracajasempacadasgrica2022), name="detalleevcalmuestracajasempacadasgrica2022"),
	path('athos/detalle-evcal-cajas-empacadas-gr/<int:id>/Registro/<int:subid>', login_required(creardetalleevcalmuestracajasempacadasgrica2022), name="creardetalleevcalmuestracajasempacadasgrica2022"),
	path('athos/detalle-evcal-cajas-empacadas-gr/<int:id>/Editar :)/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalmuestracajasempacadasgrica2022), name="editardetalleevcalmuestracajasempacadasgrica2022"),

	path('ajax/load-palets/<int:palet>/', load_palets, name='ajax_load_palets'),

	path('athos/ev-control-descartegr2022/<int:id>', login_required(crearevcontroldescartegrica2022), name="crearevcontroldescartegrica2022"),
	path('athos/ev-control-descartegr2022/<int:id>/editar/<int:subid>', login_required(editarevcontroldescartegrica2022), name="editarevcontroldescartegrica2022"),

	path('athos/ev-calidad-control-descartear2022/<int:id>', login_required(crearevcalcontroldescartearica2022), name="crearevcalcontroldescartearica2022"),
	path('athos/ev-calidad-control-descartear2022/<int:id>/editar/<int:subid>', login_required(editarevcalcontroldescartearica2022), name="editarevcalcontroldescartearica2022"),
	path('athos/det-evcal-control-descarte-ar-ica/<int:id>/ver/<int:subid>', login_required(detalleevcalcontroldescartearica2022), name="detalleevcalcontroldescartearica2022"),
	path('athos/det-evcal-control-descarte-ar-ica/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcontroldescartearica2022), name="creardetalleevcalcontroldescartearica2022"),
	path('athos/det-evcal-control-descarte-ar-ica/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcontroldescartearica2022), name="editardetalleevcalcontroldescartearica2022"),

	path('athos/ev-calidad-control-descartehg2022/<int:id>', login_required(crearevcalcontroldescartehg2022), name="crearevcalcontroldescartehg2022"),
	path('athos/ev-calidad-control-descartehg2022/<int:id>/editar/<int:subid>', login_required(editarevcalcontroldescartehg2022), name="editarevcalcontroldescartehg2022"),
	path('athos/det-evcal-control-descarte-hg/<int:id>/ver/<int:subid>', login_required(detalleevcalcontroldescartehg2022), name="detalleevcalcontroldescartehg2022"),
	path('athos/det-evcal-control-descarte-hg/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcontroldescartehg2022), name="creardetalleevcalcontroldescartehg2022"),
	path('athos/det-evcal-control-descarte-hg/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcontroldescartehg2022), name="editardetalleevcalcontroldescartehg2022"),

	path('athos/ev-control-descarte_ar2022/<int:id>', login_required(crearevcontroldescartear2022), name="crearevcontroldescartear2022"),
	path('athos/ev-control-descarte_ar2022/<int:id>/editar/<int:subid>', login_required(editarevcontroldescartear2022), name="editarevcontroldescartear2022"),
	path('athos/det-ev-control-descarte-ar2022/<int:id>/ver/<int:subid>', login_required(detalleevcontroldescartear2022), name="detalleevcontroldescartear2022"),
	path('athos/det-nueva_ev-control-descarte-ar2022/<int:id>/registro/<int:subid>', login_required(creardetalleevcontroldescartear2022), name="creardetalleevcontroldescartear2022"),
	path('athos/det-editar_ev-control-descarte-ar2022/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcontroldescartear2022), name="editardetalleevcontroldescartear2022"),

	path('ajax/load-productos/<int:id>/', load_productos, name='ajax_load_productos'),
	path('athos/ev-camaras-humedas_2022/<int:id>', login_required(crearevcamarashumedas), name="crearevcamarashumedas"),
	path('athos/ev-camaras-humedas_2022/<int:id>/editar/<int:subid>', login_required(editarevcamarashumedas), name="editarevcamarashumedas"),
	path('athos/det-ev-camaras-humedas-2022/<int:id>/ver/<int:subid>', login_required(detalleplantaevcamarashumedas), name="detalleplantaevcamarashumedas"),
	path('athos/det-nueva_ev-camaras-humedas-2022/<int:id>/registro/<int:subid>', login_required(creardetalleplantaevcamarashumedas), name="creardetalleplantaevcamarashumedas"),
	path('athos/det-editar_ev-camaras-humedas-2022/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleplantaevcamarashumedas), name="editardetalleplantaevcamarashumedas"),

	path('athos/analisis_eficiencia_2022/<int:id>', login_required(crearanalisiseficiencia), name="crearanalisiseficiencia"),
	path('athos/analisis_eficiencia_2022/<int:id>/editar/<int:subid>', login_required(editarevanalisiseficiencia), name="editarevanalisiseficiencia"),

	path('athos/producto_terminado_despacho_2022/<int:id>', login_required(crearevproductoterminadodespacho), name="crearevproductoterminadodespacho"),
	path('athos/producto_terminado_despacho_2022/<int:id>/editar/<int:subid>', login_required(editarevproductoterminadodespacho), name="editarevproductoterminadodespacho"),
	path('athos/det-eval-producto-terminado-2022/<int:id>/ver/<int:subid>', login_required(detalleevproductoterminadodespacho), name="detalleevproductoterminadodespacho"),
	path('athos/det-nueva_eval-producto-terminado-2022/<int:id>/registro/<int:subid>', login_required(creardetalleevproductoterminadodespacho), name="creardetalleevproductoterminadodespacho"),
	path('athos/det-editar_eval-producto-terminado-2022/<int:id>/editar/<int:subid>', login_required(editardetalleevproductoterminadodespacho), name="editardetalleevproductoterminadodespacho"),

#ica ev cal acopio
	path('athos/evcalacopioplanta-ica-ar2021/<int:id>/PT/<int:subid>', login_required(evcalacopioplantaarica2021), name="evcalacopioplantaarica2021"),
	path('athos/crearevcalacopioplanta-ica-ar2021/<int:id>/registroCPT/<int:subid>', login_required(crearevcalacopioplantaarica2021), name="crearevcalacopioplantaarica2021"),
	path('athos/editarevcalacopioplanta-ica-ar2021/<int:id>/var/<int:subid>/editarCPT/<int:varid>', login_required(editarevcalacopioplantaarica2021), name="editarevcalacopioplantaarica2021"),




	path('athos/crear-evcartilladrenado/<int:id>', login_required(crearevcartilladrenado), name="crearevcartilladrenado"),
	path('athos/editar-evcartilladrenado/<int:id>/editar/<int:subid>', login_required(editarevcartilladrenado), name="editarevcartilladrenado"),

	path('athos/det-evcartilladrenado/<int:id>/detalle/<int:subid>', login_required(detalleevcartilladrenado), name="detalleevcartilladrenado"),
	path('athos/det-evcartilladrenado/<int:id>/registro/<int:subid>', login_required(creardetalleevcartilladrenado), name="creardetalleevcartilladrenado"),
	path('athos/det-evcartilladrenado/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcartilladrenado), name="editardetalleevcartilladrenado"),

	path('athos/Selector-trabajadores-calpoda/<int:id>', login_required(crearseltrabajadorevcalpodaar), name="crearseltrabajadorevcalpodaar"),
	path('athos/Selector-trabajadores-calpoda/<int:id>/editar/<int:subid>', login_required(editarseltrabajadorevcalpodaar), name="editarseltrabajadorevcalpodaar"),

	
#ev cal muestreo cosecha higo
	path('athos/ev-cal-muestreo-cosecha-hg/<int:id>', login_required(crearevcalmuestreocosechahg2021), name="crearevcalmuestreocosechahg2021"),
	path('athos/ev-cal-muestreo-cosecha-hg/<int:id>/editar/<int:subid>', login_required(editarevcalmuestreocosechahg2021), name="editarevcalmuestreocosechahg2021"),

	path('athos/det-evcal-muestreo-cosecha-hg/<int:id>/ver/<int:subid>', login_required(detalleevcalmuestreocosechahg2021), name="detalleevcalmuestreocosechahg2021"),
	path('athos/det-evcal-muestreo-cosecha-hg/<int:id>/registro/<int:subid>', login_required(creardetalleevcalmuestreocosechahg2021), name="creardetalleevcalmuestreocosechahg2021"),
	path('athos/det-evcal-muestreo-cosecha-hg/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalmuestreocosechahg2021), name="editardetalleevcalmuestreocosechahg2021"),


	path('athos/ev-cal-muestreo-planta-hg/<int:id>', login_required(crearevcalmuestreoplantahgica2021), name="crearevcalmuestreoplantahgica2021"),
	path('athos/ev-cal-muestreo-planta-hg/<int:id>/editar/<int:subid>', login_required(editarevcalmuestreoplantahgica2021), name="editarevcalmuestreoplantahgica2021"),

	path('athos/ev-cal-muestreo-planta-hg-nep/<int:id>', login_required(crearevcalmuestreoplantahgnep2022), name="crearevcalmuestreoplantahgnep2022"),
	path('athos/ev-cal-muestreo-planta-hg-nep/<int:id>/editar/<int:subid>', login_required(editarevcalmuestreoplantahgnep2022), name="editarevcalmuestreoplantahgnep2022"),

	path('athos/det-evcal-muestreo-planta-hg/<int:id>/ver/<int:subid>', login_required(detalleevcalmuestreoplantahgica2021), name="detalleevcalmuestreoplantahgica2021"),
	path('athos/det-evcal-muestreo-planta-hg/<int:id>/registro/<int:subid>', login_required(creardetalleevcalmuestreoplantahgica2021), name="creardetalleevcalmuestreoplantahgica2021"),
	path('athos/det-evcal-muestreo-planta-hg/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalmuestreoplantahgica2021), name="editardetalleevcalmuestreoplantahgica2021"),


	path('athos/ev-cal-brix-planta-gr-ica/<int:id>', login_required(crearevcalbrixgrica2021), name="crearevcalbrixgrica2021"),
	path('athos/ev-cal-brix-planta-gr-ica/<int:id>/editar/<int:subid>', login_required(editarevcalbrixgrica2021), name="editarevcalbrixgrica2021"),

	path('athos/det-evcal-brix-planta-gr-ica/<int:id>/ver/<int:subid>', login_required(detalleevcalbrixgrica2021), name="detalleevcalbrixgrica2021"),
	path('athos/det-evcal-brix-planta-gr-ica/<int:id>/registro/<int:subid>', login_required(creardetalleevcalbrixgrica2021), name="creardetalleevcalbrixgrica2021"),
	path('athos/det-evcal-brix-planta-gr-ica/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalbrixgrica2021), name="editardetalleevcalbrixgrica2021"),

	path('athos/ev-cal-mmpp-planta-gr-ica/<int:id>', login_required(crearevcalmmppgrica2021), name="crearevcalmmppgrica2021"),
	path('athos/ev-cal-mmpp-planta-gr-ica/<int:id>/editar/<int:subid>', login_required(editarevcalmmppgrica2021), name="editarevcalmmppgrica2021"),

	path('athos/det-evcal-mmpp-planta-gr-ica/<int:id>/ver/<int:subid>', login_required(detalleevcalmmppgrica2021), name="detalleevcalmmppgrica2021"),
	path('athos/det-evcal-mmpp-planta-gr-ica/<int:id>/registro/<int:subid>', login_required(creardetalleevcalmmppgrica2021), name="creardetalleevcalmmppgrica2021"),
	path('athos/det-evcal-mmpp-planta-gr-ica/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalmmppgrica2021), name="editardetalleevcalmmppgrica2021"),

	path('ajax/load-palets/<int:palet>/', load_palets, name='ajax_load_palets'),

	path('athos/ev-cal-control-descarte-planta-gr-ica/<int:id>', login_required(crearevcalcontroldescartegrica2022), name="crearevcalcontroldescartegrica2022"),
	path('athos/ev-cal-control-descarte-planta-gr-ica/<int:id>/editar/<int:subid>', login_required(editarevcalcontroldescartegrica2022), name="editarevcalcontroldescartegrica2022"),

	path('athos/det-evcal-control-descarte-gr-ica/<int:id>/ver/<int:subid>', login_required(detalleevcalcontroldescartegrica2022), name="detalleevcalcontroldescartegrica2022"),
	path('athos/det-evcal-control-descarte-gr-ica/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcontroldescartegrica2022), name="creardetalleevcalcontroldescartegrica2022"),
	path('athos/det-evcal-control-descarte-gr-ica/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcontroldescartegrica2022), name="editardetalleevcalcontroldescartegrica2022"),

	path('athos/ev-cal-control-pesos-planta-gr-ica/<int:id>', login_required(crearevcalcontrolpesosgrica2022), name="crearevcalcontrolpesosgrica2022"),
	path('athos/ev-cal-control-pesos-planta-gr-ica/<int:id>/editar/<int:subid>', login_required(editarevcalcontrolpesosgrica2022), name="editarevcalcontrolpesosgrica2022"),


	path('athos/det-evcal-control-pesos-gr-ica/<int:id>/ver/<int:subid>', login_required(detalleevcalcontrolpesosgrica2022), name="detalleevcalcontrolpesosgrica2022"),
	path('athos/det-evcal-control-pesos-gr-ica/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcontrolpesosgrica2022), name="creardetalleevcalcontrolpesosgrica2022"),
	path('athos/det-evcal-control-pesos-gr-ica/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcontrolpesosgrica2022), name="editardetalleevcalcontrolpesosgrica2022"),


	path('athos/ev-cal-plantones-palta-naz2022/<int:id>', login_required(crearevplantonesplnaz2022), name="crearevplantonesplnaz2022"),
    path('athos/ev-cal-plantones-palta-naz2022/<int:id>/editar/<int:subid>', login_required(editarevplantonesplnaz2022), name="editarevplantonesplnaz2022"),

    path('athos/det-evcal-plantones-palta-naz2022/<int:id>/ver/<int:subid>', login_required(detalleevplantonesplnaz2022), name="detalleevplantonesplnaz2022"),
    path('athos/det-evcal-plantones-palta-naz2022/<int:id>/registro/<int:subid>', login_required(creardetalleevplantonesplnaz2022), name="creardetalleevplantonesplnaz2022"),
    path('athos/det-evcal-plantones-palta-naz2022/<int:id>/salviomelapela/<int:subid>/editar/<int:varid>', login_required(editardetalleevplantonesplnaz2022), name="editardetalleevplantonesplnaz2022"),



#prterminado
	path('athos/prterminado/nuevo/<int:id>', login_required(crearprterminado), name="crearprterminado"),
	path('athos/prterminado/editar/<int:id>/editar/<int:subid>', login_required(editarprterminado), name="editarprterminado"),

	path('athos/prterminado/<int:id>/prterminado/<int:subid>', login_required(tempprterminado), name="tempprterminado"),
	path('athos/nuevotemp/<int:id>/registro/<int:subid>', login_required(creartempprterminado), name="creartempprterminado"),
	path('athos/editartemp/<int:id>/pt/<int:subid>/editar/<int:varid>', login_required(editartempprterminado), name="editartempprterminado"),

	path('athos/prterminado/nuevo/<int:id>', login_required(crearprterminado), name="crearprterminado"),

#proyecciones
	path('athos/proyecciones/nuevo/<int:id>', login_required(crearproyecciones), name="crearproyecciones"),
	path('athos/proyecciones/editar/<int:id>/editar/<int:subid>', login_required(editarproyecciones), name="editarproyecciones"),

	path('athos/proyecciones/<int:id>/athos/<int:subid>', login_required(detalleproyeccionarandano), name="detalleproyeccionarandano"),
	path('athos/nuevoproyecciones/<int:id>/registro/<int:subid>', login_required(creardetalleproyeccionarandano), name="creardetalleproyeccionarandano"),
	path('athos/editarproyecciones/<int:id>/athos/<int:subid>/editar/<int:varid>', login_required(editardetalleproyeccionarandano), name="editardetalleproyeccionarandano"),

	path('athos/proyeccionessemanales/<int:id>/athos/<int:subid>', login_required(proyeccionsemanalarandano), name="proyeccionsemanalarandano"),
	path('athos/nuevoproyeccionessemanales/<int:id>/registro/<int:subid>', login_required(crearproyeccionsemanalarandano), name="crearproyeccionsemanalarandano"),
	path('athos/editarproyeccionessemanales/<int:id>/athos/<int:subid>/editar/<int:varid>', login_required(editarproyeccionsemanalarandano), name="editarproyeccionsemanalarandano"),

	path('athos/proyeccionesdiarias/nuevo/<int:id>', login_required(crearproyeccionesdiarias), name="crearproyeccionesdiarias"),
	path('athos/proyeccionesdiarias/editar/<int:id>/editar/<int:subid>', login_required(editarproyeccionesdiarias), name="editarproyeccionesdiarias"),

	path('athos/proyeccionesdetdiaria/<int:id>/athos/<int:subid>', login_required(detalleproyecciondiariaarandano), name="detalleproyecciondiariaarandano"),
	path('athos/nuevoproyeccionesdetdiaria/<int:id>/registro/<int:subid>', login_required(creardetalleproyecciondiariaarandano), name="creardetalleproyecciondiariaarandano"),
	path('athos/editarproyeccionesdetdiaria/<int:id>/athos/<int:subid>/editar/<int:varid>', login_required(editardetalleproyecciondiariaarandano), name="editardetalleproyecciondiariaarandano"),

	path('athos/proyeccionesan/nuevo/<int:id>', login_required(crearproyeccionesanual), name="crearproyeccionesanual"),
	path('athos/proyeccionesan/editar/<int:id>/editar/<int:subid>', login_required(editarproyeccionesanual), name="editarproyeccionesanual"),

	path('athos/proyeccionesan/<int:id>/athos/<int:subid>', login_required(detalleproyeccionanualarandano), name="detalleproyeccionanualarandano"),
	path('athos/nuevoproyeccionesan/<int:id>/registro/<int:subid>', login_required(creardetalleproyeccionanualarandano), name="creardetalleproyeccionanualarandano"),
	path('athos/Mnuevoproyeccionesan/<int:id>/registro/<int:subid>', login_required(Mcreardetalleproyeccionanualarandano), name="Mcreardetalleproyeccionanualarandano"),
	path('athos/editarproyeccionesan/<int:id>/athos/<int:subid>/editar/<int:varid>', login_required(editardetalleproyeccionanualarandano), name="editardetalleproyeccionanualarandano"),


	#cgfenologias
	path('athos/cgfenologias/macro/<int:id>/athos/<int:subid>', login_required(macroproceso), name="macroproceso"),
	path('athos/cgfenologias/nuevo/<int:id>/athos/<int:subid>', login_required(crearmacroproceso), name="crearmacroproceso"),
	path('athos/cgfenologias/editar/<int:id>/editar/<int:subid>/editar/<int:varid>', login_required(editarmacroproceso), name="editarmacroproceso"),

	path('athos/cgfenologias/<int:id>/athos/<int:subid>/proceso/<int:varid>', login_required(proceso), name="proceso"),
	path('athos/cgfenologias/<int:id>/registro/<int:subid>/proceso/<int:varid>', login_required(crearproceso), name="crearproceso"),
	path('athos/cgfenologias/<int:id>/athos/<int:subid>/editar/<int:varid>/editar/<int:catid>', login_required(editarproceso), name="editarproceso"),

	path('athos/cgfenologias/<int:id>/athos/<int:subid>/fen/<int:varid>/athos/<int:catid>', login_required(objetivoproceso), name="objetivoproceso"),
	path('athos/cgfenologias/<int:id>/registro/<int:subid>/crear/<int:varid>/athos/<int:catid>', login_required(crearobjetivoproceso), name="crearobjetivoproceso"),
	path('athos/cgfenologias/<int:id>/athos/<int:subid>/editar/<int:varid>/editar/<int:catid>//editar/<int:atid>', login_required(editarobjetivoproceso), name="editarobjetivoproceso"),


	#maestras
	path('athos/maestras/crear-tanques/<int:id>', login_required(creartanquesathos), name="creartanquesathos"),
    path('athos/maestras/editar-tanques/<int:id>/editar/<int:subid>', login_required(editartanquesathos), name="editartanquesathos"),

	path('ajax/load-auxiliares-campo/<int:id>/', load_auxiliarescampo, name='ajax_load_auxiliarescampo'),
	path('athos/maestras/nuevo/<int:id>', login_required(crearpresentacionesathos), name="crearpresentacionesathos"),
	path('athos/maestras/editar/<int:id>/editar/<int:subid>', login_required(editarpresentacionesathos), name="editarpresentacionesathos"),
	path('athos/clientes/nuevo/<int:id>', login_required(crearclientesathos), name="crearclientesathos"),
	path('athos/clientes/editar/<int:id>/editar/<int:subid>', login_required(editarclientesathos), name="editarclientesathos"),

	path('athos/mpresentacion/nuevo/<int:id>', login_required(crearmaestrapresentacionesathos), name="crearmaestrapresentacionesathos"),
	path('athos/mpresentacion/editar/<int:id>/editar/<int:subid>', login_required(editarmaestrapresentacionesathos), name="editarmaestrapresentacionesathos"),
	path('athos/calibres/nuevo/<int:id>', login_required(crearcalibresathos), name="crearcalibresathos"),
	path('athos/calibres/editar/<int:id>/editar/<int:subid>', login_required(editarcalibresathos), name="editarcalibresathos"),
	path('athos/linea-empaque/nuevo/<int:id>', login_required(crearlineaempaqueathos), name="crearlineaempaqueathos"),
	path('athos/linea-empaque/editar/<int:id>/editar/<int:subid>', login_required(editarlineaempaqueathos), name="editarlineaempaqueathos"),
	path('athos/cartillas-athos/nuevo/<int:id>', login_required(crearcartillasathos), name="crearcartillasathos"),
	path('athos/cartillas-athos/editar/<int:id>/editar/<int:subid>', login_required(editarcartillasathos), name="editarcartillasathos"),
	path('athos/labores-athos/nuevo/<int:id>', login_required(crearlaboresathos), name="crearlaboresathos"),
	path('athos/labores-athos/editar/<int:id>/editar/<int:subid>', login_required(editarlaboresathos), name="editarlaboresathos"),
	path('athos/desclabores-athos/nuevo/<int:id>', login_required(creardescripcionlaboresathos), name="creardescripcionlaboresathos"),
	path('athos/desclabores-athos/editar/<int:id>/editar/<int:subid>', login_required(editardescripcionlaboresathos), name="editardescripcionlaboresathos"),

	path('athos/aux-campo-athos/nuevo/<int:id>', login_required(crearauxiliarescampoathos), name="crearauxiliarescampoathos"),
	path('athos/aux-campo-athos/editar/<int:id>/editar/<int:subid>', login_required(editarauxiliarescampoathos), name="editarauxiliarescampoathos"),

	path('athos/maestras/crear-labores-planta-athos/<int:id>', login_required(crearlaboresplantaathos), name="crearlaboresplantaathos"),
	path('athos/maestras/editar-labores-planta-athos/<int:id>/editar/<int:subid>', login_required(editarlaboresplantaathos), name="editarlaboresplantaathos"),

	#logistica 
	path('athos/Prove-logistica/nuevo/<int:id>', login_required(crearproveedorathos), name="crearproveedorathos"),
	path('athos/Prove-logistica/editar/<int:id>/editar/<int:subid>', login_required(editarproveedorathos), name="editarproveedorathos"),
	path('athos/Cartilla-prove-logistica/nuevo/<int:id>', login_required(crearcartillaproveedorathos), name="crearcartillaproveedorathos"),
	path('athos/Cartilla-prove-logistica/editar/<int:id>/editar/<int:subid>', login_required(editarcartillaproveedorathos), name="editarcartillaproveedorathos"),

	#sanidad
	path('athos/productos-sanidad/nuevo/<int:id>', login_required(crearproductossanidad), name="crearproductossanidad"),
	path('athos/productos-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarproductossanidad), name="editarproductossanidad"),
	
	path('athos/ingredientes-sanidad/nuevo/<int:id>', login_required(crearingredientessanidad), name="crearingredientessanidad"),
	path('athos/ingredientes-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editaringredientessanidad), name="editaringredientessanidad"),
	
	path('athos/toxicologia-sanidad/nuevo/<int:id>', login_required(creartoxicologiasanidad), name="creartoxicologiasanidad"),
	path('athos/toxicologia-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editartoxicologiasanidad), name="editartoxicologiasanidad"),
	
	path('athos/plagas-enf-sanidad/nuevo/<int:id>', login_required(crearplagasenfermedadessanidad), name="crearplagasenfermedadessanidad"),
	path('athos/plagas-enf-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarplagasenfermedadessanidad), name="editarplagasenfermedadessanidad"),
	
	path('athos/tipo-metodo-sanidad/nuevo/<int:id>', login_required(creartipometodosanidad), name="creartipometodosanidad"),
	path('athos/tipo-metodo-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editartipometodosanidad), name="editartipometodosanidad"),
	
	path('athos/equipos-sanidad/nuevo/<int:id>', login_required(crearequipossanidad), name="crearequipossanidad"),
	path('athos/equipos-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarequipossanidad), name="editarequipossanidad"),
	
	path('athos/tipo-dosis-sanidad/nuevo/<int:id>', login_required(creartipodosissanidad), name="creartipodosissanidad"),
	path('athos/tipo-dosis-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editartipodosissanidad), name="editartipodosissanidad"),
	
	path('athos/lugares-aplicacion-sanidad/nuevo/<int:id>', login_required(crearlugaresaplicacionsanidad), name="crearlugaresaplicacionsanidad"),
	path('athos/lugares-aplicacion-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarlugaresaplicacionsanidad), name="editarlugaresaplicacionsanidad"),
	
	path('athos/tractores-athos-sanidad/nuevo/<int:id>', login_required(creartractoresathos), name="creartractoresathos"),
	path('athos/tractores-athos-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editartractoresathos), name="editartractoresathos"),
	
	path('athos/boquillas-athos-sanidad/nuevo/<int:id>', login_required(crearboquillassanidadathos), name="crearboquillassanidadathos"),
	path('athos/boquillas-athos-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarboquillassanidadathos), name="editarboquillassanidadathos"),

	path('athos/operadores-sanidad-athos-sanidad/nuevo/<int:id>', login_required(crearoperadoressanidadathos), name="crearoperadoressanidadathos"),
	path('athos/operadores-sanidad-athos-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editaroperadoressanidadathos), name="editaroperadoressanidadathos"),

	path('athos/ubicacion-pr-sanidad-athos/nuevo/<int:id>', login_required(crearubicacionproductosautorizados), name="crearubicacionproductosautorizados"),
	path('athos/ubicacion-pr-sanidad-athos/editar/<int:id>/editar/<int:subid>', login_required(editarubicacionproductosautorizados), name="editarubicacionproductosautorizados"),

	path('athos/productos-autorizado-sanidad/<int:id>/ver/<int:subid>', login_required(productosautorizados), name="productosautorizados"),
	path('athos/productos-autorizado-sanidad/<int:id>/registro/<int:subid>', login_required(crearproductosautorizados), name="crearproductosautorizados"),
	path('athos/productos-autorizado-sanidad/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editarproductosautorizados), name="editarproductosautorizados"),

	path('athos/ubicacion-ra-sanidad-athos/nuevo/<int:id>', login_required(crearubicacionregistroaplicacion), name="crearubicacionregistroaplicacion"),
	path('athos/ubicacion-ra-sanidad-athos/editar/<int:id>/editar/<int:subid>', login_required(editarubicacionregistroaplicacion), name="editarubicacionregistroaplicacion"),

	path('athos/maestra-lmr-sanidad-athos/nuevo/<int:id>', login_required(crearmaestralmr), name="crearmaestralmr"),
	path('athos/maestra-lmr-sanidad-athos/editar/<int:id>/editar/<int:subid>', login_required(editarmaestralmr), name="editarmaestralmr"),

	path('athos/detalle-prdautorizados/<int:id>/ver/<int:subid>/sprd/<int:varid>', login_required(detalleproductosautorizados), name="detalleproductosautorizados"),
	path('athos/detalle-prdautorizados/<int:id>/registro/<int:subid>/sprd/<int:varid>/crear/', login_required(creardetalleproductosautorizados), name="creardetalleproductosautorizados"),
	path('athos/detalle-prdautorizados/<int:id>/editar/<int:subid>/prdl/<int:varid>/editar/<int:catid>', login_required(editardetalleproductosautorizados), name="editardetalleproductosautorizados"),

	path('athos/RegApicacion/<int:id>/ver/<int:subid>/reg', login_required(registroaplicacion), name="registroaplicacion"),
	path('athos/RegApicacion/<int:id>/registro/<int:subid>/crear/', login_required(crearregistroaplicacion), name="crearregistroaplicacion"),
	path('athos/RegApicacion/<int:id>/editar/<int:subid>/prdl/<int:varid>/', login_required(editarregistroaplicacion), name="editarregistroaplicacion"),

	path('athos/detalle-lmr-prdautorizados/<int:id>/ver/<int:subid>/sprd/<int:varid>', login_required(detallelmrpa), name="detallelmrpa"),
	path('athos/detalle-lmr-prdautorizados/<int:id>/registro/<int:subid>/sprd/<int:varid>/crear/', login_required(creardetallelmrpa), name="creardetallelmrpa"),
	path('athos/detalle-lmr-prdautorizados/<int:id>/editar/<int:subid>/prdl/<int:varid>/editar/<int:catid>', login_required(editardetallelmrpa), name="editardetallelmrpa"),


	path('athos/detalle-registro-aplicacion/<int:id>/ver/<int:subid>/sprd/<int:varid>', login_required(detalleregistroaplicacion), name="detalleregistroaplicacion"),
	path('athos/detalle-registro-aplicacion/<int:id>/registro/<int:subid>/sprd/<int:varid>/crear/', login_required(creardetalleregistroaplicacion), name="creardetalleregistroaplicacion"),
	path('athos/detalle-registro-aplicacion/<int:id>/editar/<int:subid>/prdl/<int:varid>/editar/<int:catid>', login_required(editardetalleregistroaplicacion), name="editardetalleregistroaplicacion"),


	path('athos/proyeccionsem-sanidad/nuevo/<int:id>', login_required(crearproyeccionsemanalsanidad), name="crearproyeccionsemanalsanidad"),
	path('athos/proyeccionsem-sanidad/editar/<int:id>/editar/<int:subid>', login_required(editarproyeccionsemanalsanidad), name="editarproyeccionsemanalsanidad"),

	path('athos/detalle-proy-sem-sanidad/<int:id>/ver/<int:subid>', login_required(detalleproyeccionsemanalsanidad), name="detalleproyeccionsemanalsanidad"),
	path('athos/detalle-proy-sem-sanidad/<int:id>/registro/<int:subid>', login_required(creardetalleproyeccionsemanalsanidad), name="creardetalleproyeccionsemanalsanidad"),
	path('athos/detalle-proy-sem-sanidad/<int:id>/sanidad/<int:subid>/editar/<int:varid>', login_required(editardetalleproyeccionsemanalsanidad), name="editardetalleproyeccionsemanalsanidad"),

	
	path('athos/registro-proyeccion-sanidad/<int:id>/ver/<int:subid>/semanal/<int:varid>', login_required(registroproyeccionsemanalsanidad), name="registroproyeccionsemanalsanidad"),
	path('athos/registro-proyeccion-sanidad/<int:id>/registro/<int:subid>/semanal/<int:varid>/crear/', login_required(crearregistroproyeccionsemanalsanidad), name="crearregistroproyeccionsemanalsanidad"),
	path('athos/registro-proyeccion-sanidad/<int:id>/editar/<int:subid>/semanal/<int:varid>/editar/<int:catid>', login_required(editarregistroproyeccionsemanalsanidad), name="editarregistroproyeccionsemanalsanidad"),

	path('athos/Conf-RegApicacion/<int:id>/ver/<int:subid>/reg', login_required(confirmativaregistroaplicacion), name="confirmativaregistroaplicacion"),
	path('athos/Conf-RegApicacion/<int:id>/registro/<int:subid>/crear/', login_required(crearconfirmativaregistroaplicacion), name="crearconfirmativaregistroaplicacion"),
	path('athos/Conf-RegApicacion/<int:id>/editar/<int:subid>/prdl/<int:varid>/', login_required(editarconfirmativaregistroaplicacion), name="editarconfirmativaregistroaplicacion"),





	#riego
	path('ajax/load-tanques/<int:id>', load_tanques, name='ajax_load_tanques'),
	path('athos/soluciones-madres/nuevo/<int:id>', login_required(crearsolucionesmadres), name="crearsolucionesmadres"),
	path('athos/soluciones-madres/editar/<int:id>/editar/<int:subid>', login_required(editarsolucionesmadres), name="editarsolucionesmadres"),
	path('athos/detalle-soluciones-madres/<int:id>/ver/<int:subid>', login_required(detallesolucionesmadres), name="detallesolucionesmadres"),
	path('athos/detalle-soluciones-madres/<int:id>/registro/<int:subid>', login_required(creardetallesolucionesmadres), name="creardetallesolucionesmadres"),
	path('athos/detalle-soluciones-madres/<int:id>/solucionesmadres/<int:subid>/editar/<int:varid>', login_required(editardetallesolucionesmadres), name="editardetallesolucionesmadres"),


	path('athos/productos-riego/nuevo/<int:id>', login_required(crearproductosriego), name="crearproductosriego"),
	path('athos/productos-riego/editar/<int:id>/editar/<int:subid>', login_required(editarproductosriego), name="editarproductosriego"),
	
	path('athos/metodos-riego/nuevo/<int:id>', login_required(crearmetodoriego), name="crearmetodoriego"),
	path('athos/metodos-riego/editar/<int:id>/editar/<int:subid>', login_required(editarmetodoriego), name="editarmetodoriego"),
	
	path('athos/equipos-riego/nuevo/<int:id>', login_required(crearequiposriego), name="crearequiposriego"),
	path('athos/equipos-riego/editar/<int:id>/editar/<int:subid>', login_required(editarequiposriego), name="editarequiposriego"),
	
	path('athos/pozos-riego/nuevo/<int:id>', login_required(crearpozosriego), name="crearpozosriego"),
	path('athos/pozos-riego/editar/<int:id>/editar/<int:subid>', login_required(editarpozosriego), name="editarpozosriego"),
	
	path('athos/operadores-riego-athos/nuevo/<int:id>', login_required(crearoperadoresriegoathos), name="crearoperadoresriegoathos"),
	path('athos/operadores-riego-athos/editar/<int:id>/editar/<int:subid>', login_required(editaroperadoresriegoathos), name="editaroperadoresriegoathos"),


	path('athos/ley-riego/nuevo/<int:id>', login_required(crearleynutricionriego), name="crearleynutricionriego"),
	path('athos/ley-riego/editar/<int:id>/editar/<int:subid>', login_required(editarleynutricionriego), name="editarleynutricionriego"),
	
	path('athos/proyeccionsem-riego/nuevo/<int:id>', login_required(crearproyeccionsemanalriego), name="crearproyeccionsemanalriego"),
	path('athos/proyeccionsem-riego/editar/<int:id>/editar/<int:subid>', login_required(editarproyeccionsemanalriego), name="editarproyeccionsemanalriego"),

	path('athos/detalle-proy-sem-riego/<int:id>/ver/<int:subid>', login_required(detalleproyeccionsemanalriego), name="detalleproyeccionsemanalriego"),
	path('athos/detalle-proy-sem-riego/<int:id>/registro/<int:subid>', login_required(creardetalleproyeccionsemanalriego), name="creardetalleproyeccionsemanalriego"),
	path('athos/detalle-proy-sem-riego/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleproyeccionsemanalriego), name="editardetalleproyeccionsemanalriego"),

	path('athos/registro-riego-fert/nuevo/<int:id>', login_required(crearregistroriegofertilizacion), name="crearregistroriegofertilizacion"),
	path('athos/registro-riego-fert/editar/<int:id>/editar/<int:subid>', login_required(editarregistroriegofertilizacion), name="editarregistroriegofertilizacion"),

	path('athos/registro-proyeccion-sem/<int:id>/ver/<int:subid>/', login_required(registroproyeccionsemanalriego), name="registroproyeccionsemanalriego"),
	path('athos/registro-proyeccion-sem/<int:id>/registro/<int:subid>/crear/', login_required(crearregistroproyeccionsemanalriego), name="crearregistroproyeccionsemanalriego"),
	path('athos/registro-proyeccion-sem/<int:id>/editar/<int:subid>/editar/<int:varid>/', login_required(editarregistroproyeccionsemanalriego), name="editarregistroproyeccionsemanalriego"),

	path('athos/detalle-proy-reg-riego-fer/<int:id>/ver/<int:subid>', login_required(detalleregistroriegofertilizacion), name="detalleregistroriegofertilizacion"),
	path('athos/detalle-proy-reg-riego-fer/<int:id>/registro/<int:subid>', login_required(creardetalleregistroriegofertilizacion), name="creardetalleregistroriegofertilizacion"),
	path('athos/detalle-proy-reg-riego-fer/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleregistroriegofertilizacion), name="editardetalleregistroriegofertilizacion"),

	path('athos/detalle-requerimiento-prd-riego-fer/<int:id>/ver/<int:subid>/', login_required(detrequerimientoriegofert), name="detrequerimientoriegofert"),
	path('athos/detalle-requerimiento-prd-riego-fer/<int:id>/registro/<int:subid>/registro/', login_required(creardetrequerimientoriegofert), name="creardetrequerimientoriegofert"),
	path('athos/detalle-requerimiento-prd-riego-fer/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>/', login_required(editardetrequerimientoriegofert), name="editardetrequerimientoriegofert"),

	path('athos/consumo-fert-riego-fer/<int:id>/ver/<int:subid>/ver/<int:varid>/', login_required(consumorequerimientoriegofert), name="consumorequerimientoriegofert"),
	path('athos/consumo-fert-riego-fer/<int:id>/registro/<int:subid>/registro/<int:varid>', login_required(crearconsumorequerimientoriegofert), name="crearconsumorequerimientoriegofert"),
	path('athos/consumo-fert-riego-fer/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>/editar/<int:catid>/', login_required(editarconsumorequerimientoriegofert), name="editarconsumorequerimientoriegofert"),


	path('athos/detalle-consumo-riego-riego-fer/<int:id>/ver/<int:subid>/ver/<int:varid>/', login_required(detallerequerimientoriegot), name="detallerequerimientoriegot"),
	path('athos/detalle-consumo-riego-riego-fer/<int:id>/registro/<int:subid>/registro/<int:varid>', login_required(creardetallerequerimientoriegot), name="creardetallerequerimientoriegot"),
	path('athos/detalle-consumo-riego-riego-fer/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>/editar/<int:catid>/', login_required(editardetallerequerimientoriegot), name="editardetallerequerimientoriegot"),
	





	
	path('athos/explotacion-pozos/nuevo/<int:id>', login_required(crearexplotacionpozos), name="crearexplotacionpozos"),
	path('athos/explotacion-pozos/editar/<int:id>/editar/<int:subid>', login_required(editarexplotacionpozos), name="editarexplotacionpozos"),


	path('athos/detalle-explotacion-pozos-riego/<int:id>/ver/<int:subid>', login_required(detalleexplotacionpozos), name="detalleexplotacionpozos"),
	path('athos/detalle-explotacion-pozos-riego/<int:id>/registro/<int:subid>', login_required(creardetalleexplotacionpozos), name="creardetalleexplotacionpozos"),
	path('athos/detalle-explotacion-pozos-riego/<int:id>/edit/<int:subid>/editar/<int:varid>', login_required(editardetalleexplotacionpozos), name="editardetalleexplotacionpozos"),



	path('athos/estacion.met-riego-athos/nuevo/<int:id>', login_required(crearestacionmeteorologica), name="crearestacionmeteorologica"),
	path('athos/estacion.met-riego-athos/editar/<int:id>/editar/<int:subid>', login_required(editarestacionmeteorologica), name="editarestacionmeteorologica"),



	
#acopio-athos-GRANADA
	path('athos/nuevoguiaathos-gr2020/<int:id>', login_required(crearguiaathosgr2020), name="crearguiaathosgr2020"),
	path('athos/editarguiaathos-gr2020/<int:id>/editar/<int:subid>', login_required(editarguiaathosgr2020), name="editarguiaathosgr2020"),
	path('athos/guiad-gr2020/<int:id>/desc/<int:subid>', login_required(guiadetallesathosgr2020), name="guiadetallesathosgr2020"),

	path('athos/crearguiad-gr2020/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathosgr2020), name="crearguiadetallesathosgr2020"),
	path('athos/editarguiad-gr2020/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathosgr2020), name="editarguiadetallesathosgr2020"),

	path('athos/infopalet-gr2020/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopaletgr2020), name="infopaletgr2020"),
	path('athos/nuevoinfopalet-gr2020/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopaletgr2020), name="crearinfopaletgr2020"),
	path('athos/editarinfop-gr2020/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopaletgr2020), name="editarinfopaletgr2020"),

	path('athos/print-gr2020/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpaletgr2020), name="printpaletgr2020"),

	path('athos/almacen-acopio/registrar/<int:id>', login_required(crearalmacenacopiogr2020), name="crearalmacenacopiogr2020"),
	path('athos/almacen-acopio/<int:id>/editar/<int:subid>', login_required(editaralmacenacopiogr2020), name="editaralmacenacopiogr2020"),
	
	path('athos/descarte-nuevo-gr-2021/<int:id>', login_required(creardescarteathosgrica2021), name="creardescarteathosgrica2021"),
	path('athos/descarte-editar-gr-2021/<int:id>/editar/<int:subid>', login_required(editardescarteathosgrica2021), name="editardescarteathosgrica2021"),

	path('athos/salida-descarte-nuevo-gr-2021/<int:id>', login_required(crearsalidadescartegrica2021), name="crearsalidadescartegrica2021"),
	path('athos/salida-descarte-editar-gr-2021/<int:id>/editar/<int:subid>', login_required(editarsalidadescartegrica2021), name="editarsalidadescartegrica2021"),
	path('ajax/load-trazabilidad-grica2021/<slug:id>', load_trazabilidadgrica2021, name='ajax_load_trazabilidadgrica2021'),


	path('athos/print-descarte-gr-ica-2021/acopio/<int:palet_id>', login_required(printpaletdescartegr2021), name="printpaletdescartegr2021"),

	path('athos/det-salida-descarte-grica2021/<int:id>/list/<int:subid>', login_required(detallesalidadescartegrica2021), name="detallesalidadescartegrica2021"),
	path('athos/det-salida-descarte-grica2021/<int:id>/registro/<int:subid>', login_required(creardetallesalidadescartegrica2021), name="creardetallesalidadescartegrica2021"),
	path('athos/det-salida-descarte-grica2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetallesalidadescartegrica2021), name="editardetallesalidadescartegrica2021"),

#acopio-athos-DATIL
	path('athos/nuevoguiaathos-dt2021/<int:id>', login_required(crearguiaathosdt2021), name="crearguiaathosdt2021"),
	path('athos/editarguiaathos-dt2021/<int:id>/editar/<int:subid>', login_required(editarguiaathosdt2021), name="editarguiaathosdt2021"),
	path('athos/guiad-dt2021/<int:id>/desc/<int:subid>', login_required(guiadetallesathosdt2021), name="guiadetallesathosdt2021"),

	path('athos/crearguiad-dt2021/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathosdt2021), name="crearguiadetallesathosdt2021"),
	path('athos/editarguiad-dt2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathosdt2021), name="editarguiadetallesathosdt2021"),

	path('athos/infopalet-dt2021/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopaletdt2021), name="infopaletdt2021"),
	path('athos/nuevoinfopalet-dt2021/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopaletdt2021), name="crearinfopaletdt2021"),
	path('athos/editarinfop-dt2021/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopaletdt2021), name="editarinfopaletdt2021"),

	path('athos/print-dt2021/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpaletdt2021), name="printpaletdt2021"),

#acopio-athos-ARANDANO
	#CARAZ
	path('athos/nuevoguiaathos-arcaraz2021/<int:id>', login_required(crearguiaathosarcaraz2021), name="crearguiaathosarcaraz2021"),
	path('athos/editarguiaathos-arcaraz2021/<int:id>/editar/<int:subid>', login_required(editarguiaathosarcaraz2021), name="editarguiaathosarcaraz2021"),
	path('athos/guiad-arcaraz2021/<int:id>/desc/<int:subid>', login_required(guiadetallesathosarcaraz2021), name="guiadetallesathosarcaraz2021"),

	path('athos/crearguiad-arcaraz2021/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathosarcaraz2021), name="crearguiadetallesathosarcaraz2021"),
	path('athos/editarguiad-arcaraz2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathosarcaraz2021), name="editarguiadetallesathosarcaraz2021"),

	path('athos/infopalet-arcaraz2021/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopaletarcaraz2021), name="infopaletarcaraz2021"),
	path('athos/nuevoinfopalet-arcaraz2021/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopaletarcaraz2021), name="crearinfopaletarcaraz2021"),
	path('athos/editarinfop-arcaraz2021/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopaletarcaraz2021), name="editarinfopaletarcaraz2021"),

	path('athos/print-arcaraz2021/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpaletarcaraz2021), name="printpaletarcaraz2021"),

	#AGUAYMANTO - CARAZ
	path('athos/nuevoguiaathos-agcaraz2022/<int:id>', login_required(crearguiaathosagcaraz2022), name="crearguiaathosagcaraz2022"),
	path('athos/editarguiaathos-agcaraz2022/<int:id>/editar/<int:subid>', login_required(editarguiaathosagcaraz2022), name="editarguiaathosagcaraz2022"),

	path('athos/guiad-agcaraz2022/<int:id>/desc/<int:subid>', login_required(guiadetallesathosagcaraz2022), name="guiadetallesathosagcaraz2022"),

	path('athos/crearguiad-agcaraz2022/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathosagcaraz2022), name="crearguiadetallesathosagcaraz2022"),
	path('athos/editarguiad-agcaraz2022/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathosagcaraz2022), name="editarguiadetallesathosagcaraz2022"),

	path('athos/infopalet-agcaraz2022/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopaletagcaraz2022), name="infopaletagcaraz2022"),
	path('athos/nuevoinfopalet-agcaraz2022/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopaletagcaraz2022), name="crearinfopaletagcaraz2022"),
	path('athos/editarinfop-agcaraz2022/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopaletagcaraz2022), name="editarinfopaletagcaraz2022"),

	path('athos/print-agcaraz2022/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpaletagcaraz2022), name="printpaletagcaraz2022"),

	#ICA
	path('athos/nuevoguiaathos-arcica2021/<int:id>', login_required(crearguiaathosarica2021), name="crearguiaathosarica2021"),
	path('athos/editarguiaathos-arica2021/<int:id>/editar/<int:subid>', login_required(editarguiaathosarica2021), name="editarguiaathosarica2021"),
	path('athos/guiad-arica2021/<int:id>/desc/<int:subid>', login_required(guiadetallesathosarica2021), name="guiadetallesathosarica2021"),

	path('athos/infoguia-arica2022/<int:id>/desc/<int:subid>', login_required(infoguiaathosarica2022), name="infoguiaathosarica2022"),
	path('athos/crearinfoguia-arica2022/<int:id>/registro/<int:subid>', login_required(crearinfoguiaathosarica2022), name="crearinfoguiaathosarica2022"),
	path('athos/editarinfoguia-arica2022/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarinfoguiaathosarica2022), name="editarinfoguiaathosarica2022"),

	path('athos/crearguiad-arica2021/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathosarica2021), name="crearguiadetallesathosarica2021"),
	path('athos/editarguiad-arica2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathosarica2021), name="editarguiadetallesathosarica2021"),

	path('athos/infopalet-arica2021/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopaletarica2021), name="infopaletarica2021"),
	path('athos/nuevoinfopalet-arica2021/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopaletarica2021), name="crearinfopaletarica2021"),
	path('athos/editarinfop-arica2021/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopaletarica2021), name="editarinfopaletarica2021"),

	path('athos/print-arica2021/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpaletarica2021), name="printpaletarica2021"),


	path('athos/acopio-enfriado-ica/nuevoenfriadoathos/<int:id>', login_required(crearenfriadoarica2021), name="crearenfriadoarica2021"),
	path('athos/acopio-enfriado-ica/editarenfriadoathos/<int:id>/editar/<int:subid>', login_required(editarenfriadoarica2021), name="editarenfriadoarica2021"),


	path('athos/acopio-ica-distribucion/<int:id>/enfriado/<int:subid>', login_required(distribucionenfriadoarica2021), name="distribucionenfriadoarica2021"),
	path('athos/acopio-ica-distribucion/<int:id>/registro/<int:subid>', login_required(creardistribucionenfriadoarica2021), name="creardistribucionenfriadoarica2021"),
	path('athos/acopio-ica-distribucion/<int:id>/enfriado/<int:subid>/editar/<int:varid>', login_required(editardistribucionenfriadoarica2021), name="editardistribucionenfriadoarica2021"),


	path('athos/temperatura-acopio-ica/<int:id>/enfriado/<int:subid>/ver/<int:varid>', login_required(temperaturaenfriadoarica2021), name="temperaturaenfriadoarica2021"),
	path('athos/temperatura-acopio-icat/<int:id>/enfriado/<int:subid>/registro/<int:varid>/crear', login_required(creartemperaturaenfriadoarica2021), name="creartemperaturaenfriadoarica2021"),
	path('athos/temperatura-acopio-ica/<int:id>/var/<int:subid>/enfriado/<int:varid>/editar/<int:catid>', login_required(editartemperaturaenfriadoarica2021), name="editartemperaturaenfriadoarica2021"),


#ACOPIO ATHOS-HIGO
#PISCO

	path('athos/nuevoguiaathos-hgpisco2021/<int:id>', login_required(crearguiaathoshgpisco2021), name="crearguiaathoshgpisco2021"),
	path('athos/editarguiaathos-hgpisco2021/<int:id>/editar/<int:subid>', login_required(editarguiaathoshgpisco2021), name="editarguiaathoshgpisco2021"),
	path('athos/guiad-hgpisco2021/<int:id>/desc/<int:subid>', login_required(guiadetallesathoshgpisco2021), name="guiadetallesathoshgpisco2021"),

	path('athos/crearguiad-hgpisco2021/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathoshgpisco2021), name="crearguiadetallesathoshgpisco2021"),
	path('athos/editarguiad-hgpisco2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathoshgpisco2021), name="editarguiadetallesathoshgpisco2021"),

	path('athos/infopalet-hgpisco2021/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopalethgpisco2021), name="infopalethgpisco2021"),
	path('athos/nuevoinfopalet-hgpisco2021/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopalethgpisco2021), name="crearinfopalethgpisco2021"),
	path('athos/editarinfop-hgpisco2021/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopalethgpisco2021), name="editarinfopalethgpisco2021"),

	path('athos/print-hgpisco2021/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpalethgpisco2021), name="printpalethgpisco2021"),
#NEPEÑA
	path('athos/nuevoguiaathos-hgnepena2021/<int:id>', login_required(crearguiaathoshgnepena2021), name="crearguiaathoshgnepena2021"),
	path('athos/editarguiaathos-hgnepena2021/<int:id>/editar/<int:subid>', login_required(editarguiaathoshgnepena2021), name="editarguiaathoshgnepena2021"),
	path('athos/guiad-hgnepena2021/<int:id>/desc/<int:subid>', login_required(guiadetallesathoshgnepena2021), name="guiadetallesathoshgnepena2021"),

	path('athos/crearguiad-hgnepena2021/<int:id>/registro/<int:subid>', login_required(crearguiadetallesathoshgnepena2021), name="crearguiadetallesathoshgnepena2021"),
	path('athos/editarguiad-hgnepena2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarguiadetallesathoshgnepena2021), name="editarguiadetallesathoshgnepena2021"),

	path('athos/infopalet-hgnepena2021/<int:id>/ver/<int:subid>/acopio/<int:varid>', login_required(infopalethgnepena2021), name="infopalethgnepena2021"),
	path('athos/nuevoinfopalet-hgnepena2021/<int:id>/registro/<int:subid>/acopio/<int:varid>/crear', login_required(crearinfopalethgnepena2021), name="crearinfopalethgnepena2021"),
	path('athos/editarinfop-hgnepena2021/<int:id>/var/<int:subid>/editar/<int:varid>/palet/<int:catid>', login_required(editarinfopalethgnepena2021), name="editarinfopalethgnepena2021"),

	path('athos/print-hgnepena2021/<int:guia_id>/ver/<int:guia_detalle_id>/acopio/<int:palet_id>', login_required(printpalethgnepena2021), name="printpalethgnepena2021"),




	path('athos/almacen-acopio-hgpisco2021/registrar/<int:id>', login_required(crearalmacenacopiohgpisco2021), name="crearalmacenacopiohgpisco2021"),
	path('athos/almacen-acopio-hgpisco2021/<int:id>/editar/<int:subid>', login_required(editaralmacenacopiohgpisco2021), name="editaralmacenacopiohgpisco2021"),
	
#garita
	path('ajax/load-validar-dni-bus/<int:id>/<int:subid>/<slug:dnivalidar>', load_validardnibus, name='ajax_load_validar_dni_bus'),

	path('ajax/load-buscar-dni-bus/<int:id>/<int:subid>/<slug:dnivalidar>', load_buscarbusdni, name='ajax_load_buscar_bus_dni'),

	path('athos/garita-athos/nuevo/<int:id>', login_required(creargaritaathos), name="creargaritaathos"),
	path('athos/garita-athos/athos/<int:id>/editar/<int:subid>', login_required(editargaritaathos), name="editargaritaathos"),

	path('athos-detgarita/<int:id>/ver/<int:subid>', login_required(detallegaritabusathos), name="detallegaritabusathos"),
	path('athos/crear-detgarita/<int:id>/registro/<int:subid>', login_required(creardetallegaritabusathos), name="creardetallegaritabusathos"),
	path('athos/editar-detgarita/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetallegaritabusathos), name="editardetallegaritabusathos"),

#plantagranada
	path('athos/crear-ubicacionplanta2020/<int:id>/', login_required(crearubicacionplanta), name="crearubicacionplanta"),
	path('athos/editar-ubicacionplanta2020/<int:id>/editar/<int:subid>', login_required(editarubicacionplanta), name="editarubicacionplanta"),

	path('athos-recepciongr2020/<int:id>/ver/<int:subid>', login_required(recepcionpaletasgrica2023), name="recepcionpaletasgrica2023"),
	path('athos/crear-recepciongr2020/<int:id>/registro/<int:subid>', login_required(crearrecepcionpaletasgrica2023), name="crearrecepcionpaletasgrica2023"),
	path('athos/editar-recepciongr2020/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarrecepcionpaletasgrica2023), name="editarrecepcionpaletasgrica2023"),


	path('athos-lanzadogr2020/<int:id>/ver/<int:subid>', login_required(lanzadopaletasgrica2023), name="lanzadopaletasgrica2023"),
	path('athos/crear-lanzadogr2020/<int:id>/registro/<int:subid>', login_required(crearlanzadopaletasgrica2023), name="crearlanzadopaletasgrica2023"),
	path('athos/editar-lanzadogr2020/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarlanzadopaletasgrica2023), name="editarlanzadopaletasgrica2023"),


	path('athos/crear-prepaletizadogrica2020/<int:id>/', login_required(crearprepaletizadogrica2020), name="crearprepaletizadogrica2020"),
	path('athos/editar-prepaletizadogrica2020/<int:id>/editar/<int:subid>', login_required(editarprepaletizadogrica2020), name="editarprepaletizadogrica2020"),
	path('athos/confirmar-prepaletizadogrica2020/<int:id>/editar/<int:subid>', login_required(confirmativaprepaletizadogrica2020), name="confirmativaprepaletizadogrica2020"),


	path('athos-detprepaletizadogrica2020/<int:id>/ver/<int:subid>', login_required(detalleprepaletizadogrica2020), name="detalleprepaletizadogrica2020"),
	path('athos/crear-detprepaletizadogrica2020/<int:id>/registro/<int:subid>', login_required(creardetalleprepaletizadogrica2020), name="creardetalleprepaletizadogrica2020"),
	path('athos/editar-detprepaletizadogrica2020/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleprepaletizadogrica2020), name="editardetalleprepaletizadogrica2020"),

#plantahigo
	
	path('athos-recepcionhgnep2021/<int:id>/ver/<int:subid>', login_required(recepcionpaletashgnep2021), name="recepcionpaletashgnep2021"),
	path('athos/crear-recepcionhgnep2021/<int:id>/registro/<int:subid>', login_required(crearrecepcionpaletashgnep2021), name="crearrecepcionpaletashgnep2021"),
	path('athos/editar-recepcionhgnep2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarrecepcionpaletashgnep2021), name="editarrecepcionpaletashgnep2021"),


	path('athos-lanzadohgnep2021/<int:id>/ver/<int:subid>', login_required(lanzadopaletashgnep2021), name="lanzadopaletashgnep2021"),
	path('athos/crear-lanzadohgnep2021/<int:id>/registro/<int:subid>', login_required(crearlanzadopaletashgnep2021), name="crearlanzadopaletashgnep2021"),
	path('athos/editar-lanzadohgnep2021/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarlanzadopaletashgnep2021), name="editarlanzadopaletashgnep2021"),


#programaproduccion
	path('athos/programaproduccion/<int:id>', login_required(programaproduccion), name="programaproduccion"),
	path('athos/programaproduccion-grupos/nuevo/<int:id>', login_required(creargrupos), name="creargrupos"),
	path('athos/programaproducciongrupos/athos/<int:id>/editar/<int:subid>', login_required(editargrupos), name="editargrupos"),

	path('athos/programaproduccion-subgrupos/nuevo/<int:id>', login_required(crearsubgrupos), name="crearsubgrupos"),
	path('athos/programaproduccion-subgrupos/athos/<int:id>/editar/<int:subid>', login_required(editarsubgrupos), name="editarsubgrupos"),

	path('athos/programaproduccion-hitos/nuevo/<int:id>', login_required(crearhitos), name="crearhitos"),
	path('athos/programaproduccion-hitos/athos/<int:id>/editar/<int:subid>', login_required(editarhitos), name="editarhitos"),
	
	path('athos/programaproduccion-subhitos/nuevo/<int:id>', login_required(crearsubhitos), name="crearsubhitos"),
	path('athos/programaproduccion-subhitos/athos/<int:id>/editar/<int:subid>', login_required(editarsubhitos), name="editarsubhitos"),

#calidad-acopio
	path('athos/calidad-acopio/nuevoevcalcosechagr/<int:id>', login_required(crearevcalcosechagr), name="crearevcalcosechagr"),
	path('athos/calidad-acopio/editarevcalcosechagr/<int:id>/editar/<int:subid>', login_required(editarevcalcosechagr), name="editarevcalcosechagr"),

	path('athos/calidad-acopio-detalle/<int:id>/detalle/<int:subid>', login_required(detalleevcalcosechagrcat1), name="detalleevcalcosechagrcat1"),
	path('athos/calidad-acopio-detalle/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcosechagrcat1), name="creardetalleevcalcosechagrcat1"),
	path('athos/calidad-acopio-detalle/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcosechagrcat1), name="editardetalleevcalcosechagrcat1"),

	path('athos/calidad-acopio-detalle3/<int:id>/detalle/<int:subid>', login_required(detalleevcalcosechagrdescarte), name="detalleevcalcosechagrdescarte"),
	path('athos/calidad-acopio-detalle3/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcosechagrdescarte), name="creardetalleevcalcosechagrdescarte"),
	path('athos/calidad-acopio-detalle3/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcosechagrdescarte), name="editardetalleevcalcosechagrdescarte"),

	path('athos/calidad-acopio-detalle4/<int:id>/detalle/<int:subid>', login_required(detalleevcalcosechagrcampo), name="detalleevcalcosechagrcampo"),
	path('athos/calidad-acopio-detalle4/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcosechagrcampo), name="creardetalleevcalcosechagrcampo"),
	path('athos/calidad-acopio-detalle4/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcosechagrcampo), name="editardetalleevcalcosechagrcampo"),


	path('athos/calidad-acopio-detalle2/<int:id>/detalle/<int:subid>', login_required(detalleevcalcosechagrcat2), name="detalleevcalcosechagrcat2"),
	path('athos/calidad-acopio-detalle2/<int:id>/registro/<int:subid>', login_required(creardetalleevcalcosechagrcat2), name="creardetalleevcalcosechagrcat2"),
	path('athos/calidad-acopio-detalle2/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalcosechagrcat2), name="editardetalleevcalcosechagrcat2"),


	path('athos/calidad-planta/nuevoevcalidadmuestreoplantagr/<int:id>', login_required(crearevcalidadmuestreoplantagr), name="crearevcalidadmuestreoplantagr"),
	path('athos/calidad-planta/editarevcalidadmuestreoplantagr/<int:id>/editar/<int:subid>', login_required(editarevcalidadmuestreoplantagr), name="editarevcalidadmuestreoplantagr"),

#topico
	
	path('athos/topico-justificaciones/nuevo/<int:id>', login_required(crearjustificaciontopico), name="crearjustificaciontopico"),
    path('athos/topico-justificaciones/editar/<int:id>/editar/<int:subid>', login_required(editarjustificaciontopico), name="editarjustificaciontopico"),
    path('athos/print-justificacion/<int:id>/ver/<int:subid>', login_required(printjustificacion), name="printjustificacion"),

    path('athos/topico-fichaepidemiologica/nuevo/<int:id>', login_required(crearfichaepidemiologica), name="crearfichaepidemiologica"),
    path('athos/topico-fichaepidemiologica/editar/<int:id>/editar/<int:subid>', login_required(editarfichaepidemiologica), name="editarfichaepidemiologica"),
    path('athos/print-fichaepidemiologica/<int:id>/ver/<int:subid>', login_required(printfichaepidemiologica), name="printfichaepidemiologica"),
    
    path('athos/topico-fichasintomatologiacovid/nuevo/<int:id>', login_required(crearfichasintomatologiacovid), name="crearfichasintomatologiacovid"),
    path('athos/topico-fichasintomatologiacovid/editar/<int:id>/editar/<int:subid>', login_required(editarfichasintomatologiacovid), name="editarfichasintomatologiacovid"),
    path('athos/print-fichasintomatologiacovid/<int:id>/ver/<int:subid>', login_required(printfichasintomatologiacovid), name="printfichasintomatologiacovid"),
    
    path('athos/print-masivo-fichasintomatologiacovid/', login_required(printmasivofichasintomatologiacovid), name="printmasivofichasintomatologiacovid"),
    path('ajax/load-impresion-ficha-sintomatologica/<slug:id>', load_impresion_ficha_sintomatologica, name='ajax_load_impresion_ficha_sintomatologica'),
    
    path('athos/print-masivo-ficha-epidemiologica/', login_required(printmasivofichaepidemiologica), name="printmasivofichaepidemiologica"),
    path('ajax/load-impresion-ficha-epidemiologica/<slug:id>', load_impresion_ficha_epidemiologica, name='ajax_load_impresion_ficha_epidemiologica'),
    path('ajax/load-impresion-ficha-epidemiologica1/<slug:id>', load_impresion_ficha_epidemiologica1, name='ajax_load_impresion_ficha_epidemiologica1'),




#planificacion
    path('ajax/load-datosmateriales/<int:id>/', load_datosmateriales, name='ajax_load_datosmateriales'),
    path('ajax/load-detalleplan/<int:id>/', load_detalleplan, name='ajax_load_detalleplan'),
    path('ajax/load-detallemateriales/<int:datoid>/', load_detallemateriales, name='ajax_load_detallemateriales'),
    path('ajax/load-ordenproceso/<int:datoid>/', load_ordenproceso, name='ajax_load_ordenproceso'),

    path('athos/regiones-plan/nuevo/<int:id>', login_required(crearmaestraregion), name="crearmaestraregion"),
    path('athos/regiones-plan/editar/<int:id>/editar/<int:subid>', login_required(editarmaestraregion), name="editarmaestraregion"),

    path('athos/clientes-plan/nuevo/<int:id>', login_required(crearmaestraclientes), name="crearmaestraclientes"),
    path('athos/clientes-plan/editar/<int:id>/editar/<int:subid>', login_required(editarmaestraclientes), name="editarmaestraclientes"),

    path('athos/categoria-plan/nuevo/<int:id>', login_required(crearcategoriacultivo), name="crearcategoriacultivo"),
    path('athos/categoria-plan/editar/<int:id>/editar/<int:subid>', login_required(editarcategoriacultivo), name="editarcategoriacultivo"),

    path('athos/marca-pt/nuevo/<int:id>', login_required(crearmarcapt), name="crearmarcapt"),
    path('athos/marca-pt/editar/<int:id>/editar/<int:subid>', login_required(editarmarcapt), name="editarmarcapt"),

    path('athos/material-pt/nuevo/<int:id>', login_required(crearmaterialpt), name="crearmaterialpt"),
    path('athos/material-pt/editar/<int:id>/editar/<int:subid>', login_required(editarmaterialpt), name="editarmaterialpt"),

    path('athos/plan-ventas/nuevo/<int:id>', login_required(crearplanventas), name="crearplanventas"),
    path('athos/plan-ventas/editar/<int:id>/editar/<int:subid>', login_required(editarplanventas), name="editarplanventas"),
    path('athos/importar-plan-ventas/nuevo/<int:id>', login_required(importarplanventas2021), name="importarplanventas2021"),

    
    path('athos/crear-detalle-plan-ventas/nuevo/<int:id>', login_required(creardetalleplanventas), name="creardetalleplanventas"),
    path('athos/editar-detalle-plan-ventas/<int:id>/editar/<int:subid>', login_required(editardetalleplanventas), name="editardetalleplanventas"),

    path('athos/detalle-orden-proceso/<int:id>/detalle/<int:subid>', login_required(ordenproceso), name="ordenproceso"),
    path('athos/detalle-orden-proceso/<int:id>/registro/<int:subid>', login_required(crearordenproceso), name="crearordenproceso"),
    path('athos/detalle-orden-proceso/<int:id>/var/<int:subid>/editar/<int:varid>', login_required(editarordenproceso), name="editarordenproceso"),


    path('athos/programa-produccion-planta/nuevo/<int:id>', login_required(crearprogramaproduccionplanta), name="crearprogramaproduccionplanta"),
    path('athos/programa-produccion-planta/editar/<int:id>/editar/<int:subid>', login_required(editarprogramaproduccionplanta), name="editarprogramaproduccionplanta"),

#capacitaciones
    path('ajax/load-capacitaciones/<int:id>/', load_capacitaciones, name='ajax_load_capacitaciones'),
    path('athos/encuestas-capacitaciones/nuevo/<int:id>', (crearencuestacapacitacion), name="crearencuestacapacitacion"),
    path('athos/encuestas-capacitaciones/editar/<int:id>/editar/<int:subid>', login_required(editarencuestacapacitacion), name="editarencuestacapacitacion"),
    path('athos/gracias-capacitaciones/nuevo/<int:id>', (graciascapacitacion), name="graciascapacitacion"),

#rrhh
    path('ajax/load-lista-negra/<slug:id>', load_lista_negra, name='ajax_load_lista_negra'),
    path('ajax/load-datos-personal/<slug:id>', load_datos_personal, name='ajax_load_datos_personal'),
    path('athos/rrhh-ingresopersonal/nuevo/<int:id>', login_required(crearingresopersonalathos), name="crearingresopersonalathos"),
    path('athos/rrhh-ingresopersonal/editar/<int:id>/editar/<int:subid>', login_required(editaringresopersonalathos), name="editaringresopersonalathos"),
    
    path('athos/rrhh-ficha-personal/nuevo/<int:id>', login_required(crearfichapersonalathos), name="crearfichapersonalathos"),
    path('athos/rrhh-ficha-personal/editar/<int:id>/editar/<int:subid>', login_required(editarfichapersonalathos), name="editarfichapersonalathos"),
    path('athos/print-fichapersonal/<int:id>/ver/<int:subid>', login_required(printfichapersonal), name="printfichapersonal"),

    path('athos/rrhh-requerimiento-personal/nuevo/<int:id>', login_required(crearrequerimientopersonal), name="crearrequerimientopersonal"),
    path('athos/rrhh-requerimiento-personal/editar/<int:id>/editar/<int:subid>', login_required(editarrequerimientopersonal), name="editarrequerimientopersonal"),
    
	path('athos/rrhh-det-req-personal/detalle/<int:id>/det/<int:subid>', login_required(detallerequerimientopersonal), name="detallerequerimientopersonal"),
	path('athos/rrhh-det-req-personal/nuevo/<int:id>/new/<int:subid>', login_required(creardetallerequerimientopersonal), name="creardetallerequerimientopersonal"),
	path('athos/rrhh-det-req-personal/<int:id>/editar/<int:subid>/edit/<int:varid>', login_required(editardetallerequerimientopersonal), name="editardetallerequerimientopersonal"),

	path('athos/rrhh-proyeccion-semanal-personal/nuevo/<int:id>', login_required(crearproyeccionsemanalpersonal), name="crearproyeccionsemanalpersonal"),
	path('athos/rrhh-proyeccion-semanal-personal/editar/<int:id>/editar/<int:subid>', login_required(editarproyeccionsemanalpersonal), name="editarproyeccionsemanalpersonal"),
	path('athos/rrhh-det-proyeccion-semanal-personal/detalle/<int:id>/det/<int:subid>', login_required(detalleproyeccionsemanalpersonal), name="detalleproyeccionsemanalpersonal"),
	path('athos/rrhh-det-proyeccion-semanal-personal/nuevo/<int:id>/new/<int:subid>', login_required(creardetalleproyeccionsemanalpersonal), name="creardetalleproyeccionsemanalpersonal"),
	path('athos/rrhh-det-proyeccion-semanal-personal/<int:id>/editar/<int:subid>/edit/<int:varid>', login_required(editardetalleproyeccionsemanalpersonal), name="editardetalleproyeccionsemanalpersonal"),

	path('athos/rrhh-productividad-planta', login_required(productividadplanta), name="productividadplanta"),
	path('athos/rrhh-productividad-planta/registro', login_required(nuevoregistroproductividad), name="nuevoregistroproductividad"),
	path('athos/rrhh-productividad-planta/editar/<int:id>', login_required(editarproductividadplanta), name="editarproductividadplanta"),
	path('athos/rrhh-det-prod-planta/<int:id>', login_required(detalleproductividadplanta), name="detalleproductividadplanta"),
	path('athos/rrhh-det-prod-planta/<int:id>/registro', login_required(nuevodetalleproductividadplanta), name="nuevodetalleproductividadplanta"),
	path('athos/rrhh-det-prod-planta/editar/<int:id>/registro/<int:subid>', login_required(editardetalleproductividadplanta), name="editardetalleproductividadplanta"),

	path('athos/rrhh-conf-asist-prod-planta/<int:id>', login_required(irConfigurarAsistenciaProductividadPlanta), name="irConfigurarAsistenciaProductividadPlanta"),
	path('athos/rrhh-conf-asist-prod-planta/<int:id>/registro', login_required(nuevoproductividadplantaasistencia), name="nuevoproductividadplantaasistencia"),
	path('athos/rrhh-conf-asist-planta/editar/<int:id>/registro/<int:subid>', login_required(editarproductividadplantaasistencia), name="editarproductividadplantaasistencia"),
	path('athos/rrhh-det-asist-prod-planta/conf/<int:id>/registro/<int:subid>', login_required(detalleAsistenciaProductividadPlanta), name="detalleAsistenciaProductividadPlanta"),
	path('athos/rrhh-reg-det-asist-prod-planta/conf/<int:id>/registro/<int:subid>', login_required(nuevodetalleproductividadplantaasistencia), name="nuevodetalleproductividadplantaasistencia"),
	path('athos/rrhh-edit-det-asist-prod-planta/conf/<int:id>/registro/<int:subid>/editar/<int:varid>', login_required(editardetalleproductividadplantaasistencia), name="editardetalleproductividadplantaasistencia"),

#MANTENIMIENTO
	#path('ajax/load-labores/<int:id>/', load_labores, name='ajax_load_labores'),
	path('ajax/load-labores/<int:id>/<int:subid>/', load_labores, name='ajax_load_labores'),
	path('athos/mantenimiento-equipo/nuevo/<int:id>', login_required(crearmantenimientoequipoplantaathos), name="crearmantenimientoequipoplantaathos"),
	path('athos/mantenimiento-equipo/editar/<int:id>/editar/<int:subid>', login_required(editarmantenimientoequipoplantaathos), name="editarmantenimientoequipoplantaathos"),
	path('athos/mantenimiento-det-equipo/detalle/<int:id>/det/<int:subid>', login_required(detallemantenimientoequipoplantaathos), name="detallemantenimientoequipoplantaathos"),
	path('athos/mantenimiento-det-equipo/nuevo/<int:id>/new/<int:subid>', login_required(creardetallemantenimientoequipoplantaathos), name="creardetallemantenimientoequipoplantaathos"),
	path('athos/mantenimiento-det-equipo/<int:id>/editar/<int:subid>/edit/<int:varid>', login_required(editardetallemantenimientoequipoplantaathos), name="editardetallemantenimientoequipoplantaathos"),

	path('api/', include('apps.api.urls')),
]    

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)