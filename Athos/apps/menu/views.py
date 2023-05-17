from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from apps.menu.forms import UserAthosForm
from apps.menu.forms import UserAthosForm2
from apps.menu.forms import perfilesform
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from apps.menu.models import perfiles
from apps.menu.models import item
from apps.menu.models import sub_item
from apps.menu.models import menu_principal
from apps.menu.forms import subitemform
from apps.menu.forms import menuform
from apps.menu.forms import itemform
from django.contrib import auth
from apps.menu.models import fundo
from apps.menu.forms import Fundoform
from apps.menu.models import cultivo
from apps.menu.forms import Cultivoform
from apps.menu.models import fenologia
from apps.menu.forms import Fenologiaform

from apps.menu.models import campanas
from apps.menu.forms import Campanaform

from apps.menu.models import ejezona

from apps.menu.models import variedad
from apps.menu.forms import Variedadform

from apps.menu.models import Estado

from apps.menu.models import modulo
from apps.menu.forms import Moduloform

from apps.menu.models import lote
from apps.menu.forms import Loteform

from apps.menu.models import ProgramaProduccion
from apps.menu.forms import Produccionform

from apps.menu.models import ProgramaProduccionFeno
from apps.menu.forms import ProduccionFenoform

from apps.menu.models import TurnoProgramaProduccion
from apps.menu.forms import turnoprogramaproduccionform

from apps.menu.models import Flujo
from apps.menu.forms import Flujoform

from apps.menu.models import Acciones
from apps.menu.forms import Accionesform

from apps.menu.models import Procesos
from apps.menu.forms import Procesosform

from apps.menu.models import solicitud
from apps.menu.forms import Solicitudform

from apps.menu.models import elementoPEP
from apps.menu.forms import elementoPEPform

from apps.menu.models import VariableAgronomica
from apps.menu.forms import Variableform

from apps.menu.models import SubVariableAgronomica
from apps.menu.forms import subvariableform

from apps.menu.models import VersionAgronomica
from apps.menu.forms import VersionAgroform

from apps.menu.models import PproduccionVariable
from apps.menu.forms import ProduccionVariableform

from apps.menu.models import Planta
from apps.menu.forms import plantaform

from apps.menu.models import Nave
from apps.menu.forms import  naveform

from apps.menu.models import PersonalPlanta
from apps.menu.forms import personalplantaform

from apps.menu.models import Linea
from apps.menu.forms import lineaform

from apps.menu.models import LPaletas
from apps.menu.forms import lanzadopaletasform

from apps.menu.models import LPaletasReal
from apps.menu.forms import lanzadopaletasrealform

from apps.menu.models import Materiales
from apps.menu.forms import materialesform

from apps.menu.models import OrdenPedido
from apps.menu.forms import ordenpedidoform

from apps.menu.models import OrdenPedidoMaterialf
from apps.menu.forms import ordenpedidomaterialfform

from apps.menu.models import Paletizado
from apps.menu.forms import paletizadoform

from apps.menu.models import ZonaPaletizado
from apps.menu.forms import zonapaletizadoform

from apps.menu.models import ConfAsistenciaPlanta
from apps.menu.forms import configurarasistenciaplantaform

from apps.menu.models import IngresoAsistenciaPlanta
from apps.menu.forms import ingresoplantaform

from apps.menu.models import SalidaAsistenciaPlanta
from apps.menu.forms import salidaplantaform

from apps.menu.models import AreaCapacitacion
from apps.menu.forms import areaform

from apps.menu.models import CompetenciaCapacitacion
from apps.menu.forms import competenciaform

from apps.menu.models import TemaCapacitacion
from apps.menu.forms import temaform

from apps.menu.models import CapacitacionCapacitacion
from apps.menu.forms import capacitacionform

from apps.menu.models import AsistenciaCapacitacion
from apps.menu.forms import asistenciacapacitacionform

from apps.menu.models import Turno
from apps.menu.forms import turnoform

from apps.menu.models import AreaPlanta
from apps.menu.forms import arealaborform

from apps.menu.models import LaborPlanta
from apps.menu.forms import laborform 

from apps.menu.models import ConfigurarDia
from apps.menu.forms import configurarfechaform

from apps.menu.models import MaterialAcopio
from apps.menu.forms import materialacopioform 

from apps.menu.models import PlacasVehiculares
from apps.menu.forms import placasvehicularesform

from apps.menu.models import DetallePlacasVehiculares
from apps.menu.forms import detalleplacasvehicularesform

from apps.menu.models import ChoferesVehiculos
from apps.menu.forms import choferesvehiculosform

from apps.menu.models import UnidadVehicular
from apps.menu.forms import unidadvehicularform

from apps.menu.models import UbicacionFundo
from apps.menu.forms import ubicacionfundoform

from apps.menu.models import LugarAthos
from apps.menu.forms import lugarathosform

from apps.menu.models import CentrosAthos
from apps.menu.forms import centrosathosform

from apps.menu.models import AlmacenesAthos
from apps.menu.forms import almacenesathosform

from apps.menu.models import GuiaAthos
from apps.menu.forms import guiaathosform

from apps.menu.models import GuiaDetallesAthos
from apps.menu.forms import guiadetallesathosform

from apps.menu.models import InfoPalet
from apps.menu.forms import infopaletform

from apps.menu.models import MaterialMMPP
from apps.menu.forms import materialmmppform

from apps.menu.models import MaterialTransporte
from apps.menu.forms import materialtransporteform

from apps.menu.models import TipoParihuela
from apps.menu.forms import tipoparihuelaform

from apps.menu.models import GaritaAthos
from apps.menu.forms import garitaathosform

from apps.menu.models import RutasAthos
from apps.menu.forms import rutasathosform

from apps.menu.models import HitosFenologicos
from apps.menu.forms import hitosfenologicosform

from apps.menu.models import AlcanceCapacitacion
from apps.menu.forms import alcancecapacitacionform


from apps.cgfenologias.models  import Hitos
from apps.cgfenologias.forms import hitosform
from apps.cgfenologias.models  import SubHitos
from apps.cgfenologias.forms import subhitosform
from apps.cgfenologias.models import Macroproceso
from apps.cgfenologias.models import Proceso

from apps.acopio.models import DescarteAthos
from apps.sanidad.models import ProductosAutorizados

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    redirect('../login')

def crearitems(request):
	form = itemform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('items')
	return render(request, 'athos/crearitem.html', context)


def editaritems(request, id):
	mnu = get_object_or_404(item, id=id)
	form = itemform(request.POST or None, instance=mnu)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('items')
	return render(request, 'athos/crearitem.html', context)

def items(request):
	mprincipal = item.objects.all()
	context = {"item":mprincipal}
	return render(request, 'athos/item.html', context)



def crearmenu(request):
	form = menuform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('menu')
	return render(request, 'athos/menu.html', context)

def editarmenu(request, id):
	mnu = get_object_or_404(menu_principal, id=id)
	form = menuform(request.POST or None, instance=mnu)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('menu')
	return render(request, 'athos/menu.html', context)

def menu(request):
	mprincipal = menu_principal.objects.all()
	context = {"mprincipal":mprincipal}
	return render(request, 'athos/menu_principal.html', context)




def editarusuario(request, id):
	usuario = get_object_or_404(User, id=id)
	perfilusuario =get_object_or_404(perfiles, usuario=id)
	form = UserAthosForm2(request.POST or None, instance=usuario)
	form2 = perfilesform(request.POST or None, instance=perfilusuario)
	context = {"form":form,"form2":form2}
	if request.method=='POST':
		if form.is_valid():
			if form2.is_valid():
				result = form.save(commit=False)
				result.set_password(self.cleaned_data["pasword1"])
				result.save()
				form2.save()
				return redirect('usuarios')
			else:
				print("f2")
		else:
			print("f1")
	return render(request, 'athos/editarusuario.html', context)

def nuevousuario(request):
	form = UserAthosForm(request.POST or None)
	form2 = perfilesform(request.POST or None)
	context = {"form":form,"form2":form2}
	if request.method=='POST':
		if form.is_valid():
				if form2.is_valid():
					result = form.save()
					result2 = form2.save(commit=False)
					result2.usuario = result
					result2.save()
					return redirect('usuarios')
	return render(request, 'athos/nuevousuario.html', context)

def registrarsubitem(request, id):
	form = subitemform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			itt = get_object_or_404(item, id = id)
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.id_item = itt
			result.save()
			return redirect('items_subitems', id)
	return render(request, 'athos/registrarsubitem.html', context)

def editarsubitem(request, id, idsub):
	sub = get_object_or_404(sub_item, id=idsub)
	form = subitemform(request.POST or None, instance=sub)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			# mi = get_object_or_404(menu_item, id=id)
			# menu_Item_SubItem.objects.create(id_menu_item=mi, id_SubItem=result, estado="activo", usuario_creacion_id=current_user.id)
			return redirect('items_subitems', id)
	return render(request, 'athos/registrarsubitem.html', context)

def items_subitems(request, id):
	mis = sub_item.objects.filter(id_item=id)
	context = {"mis":mis,"id":id}
	return render(request, 'athos/mis.html', context)

def home(request):
	
	
	return render(request, 'athos/home.html')

def usuarios(request):
	usuario = User.objects.all()
	context = {"usuario":usuario}
	if request.user.is_superuser:
		return render(request, 'athos/escritorio.html', context)
	return redirect('home')


def campo(request, id):

	campopr = fundo.objects.all()[:50]
	context = {"campopr":campopr, "id":id}

	cultivopr=cultivo.objects.all()[:50]
	context2={"cultivopr":cultivopr, "id":id}

	campanapr=campanas.objects.all()[:50]
	context4={"campanapr":campanapr, "id":id}

	variedadpr=variedad.objects.all()[:50]
	context3={"variedadpr":variedadpr, "id":id}

	fenopr=fenologia.objects.all()[:50]
	context5={"fenopr":fenopr, "id":id}

	modulopr=modulo.objects.all()[:50]
	context7={"modulopr":modulopr, "id":id}

	produccionpr=ProgramaProduccion.objects.all().order_by("-fecha_hora_creacion")[:500]
	context6={"produccionpr":produccionpr, "id":id}

	lotepr=lote.objects.all()[:50]
	context8={"lotepr":lotepr, "id":id}

	flujopr=Flujo.objects.all()[:50]
	context9={"flujopr":flujopr, "id":id}

	accionpr=Acciones.objects.all()[:50]
	context10={"accionpr":accionpr, "id":id}

	procesopr=Procesos.objects.all()[:50]
	context11={"procesopr":procesopr, "id":id}

	solicitudpr=solicitud.objects.all()[:50]
	context12={"solicitudpr":solicitudpr, "id":id}

	variablepr=VariableAgronomica.objects.all()[:50]
	context13={"variablepr":variablepr, "id":id}

	versionpr=VersionAgronomica.objects.all()[:50]
	context14={"versionpr":versionpr, "id":id}
	
	plantapr=Planta.objects.all()[:50]
	context15={"plantapr":plantapr, "id":id}

	navepr=Nave.objects.all()[:50]
	context16={"navepr":navepr, "id":id}
	
	personalplantapr=PersonalPlanta.objects.all()[:50]
	context18={"personalplantapr":personalplantapr, "id":id}

	lineapr=Linea.objects.all()[:50]
	context17={"lineapr":lineapr, "id":id}

	lanzadopaletaspr=LPaletas.objects.filter(anexo_estado=1)[:50]
	context20={"lanzadopaletaspr":lanzadopaletaspr, "id":id}

	lanzadopaletaspr=LPaletas.objects.filter(anexo_estado=1)[:50]
	context19={"lanzadopaletaspr":lanzadopaletaspr, "id":id}

	materialespr=Materiales.objects.all()[:50]
	context25={"materialespr":materialespr, "id":id}

	ordenpedidopr=OrdenPedido.objects.all()[:50]
	context26={"ordenpedidopr":ordenpedidopr, "id":id}

	zonapaletizadopr=ZonaPaletizado.objects.all()[:50]
	context27={"zonapaletizadopr":zonapaletizadopr, "id":id}

	paletizadopr=Paletizado.objects.all()[:50]
	context28={"paletizadopr":paletizadopr, "id":id}

	configurarpr=ConfAsistenciaPlanta.objects.all().order_by("-anexo_configuracion")[:30]
	context21={"configurarpr":configurarpr, "id":id}

	configurarpr=ConfAsistenciaPlanta.objects.all()[:50]
	context23={"configurarpr":configurarpr, "id":id}

	areapr=AreaCapacitacion.objects.all()[:50]
	context24={"areapr":areapr, "id":id}

	competenciapr=CompetenciaCapacitacion.objects.all()[:50]
	context25={"competenciapr":competenciapr, "id":id}

	temapr=TemaCapacitacion.objects.all()[:50]
	context26={"temapr":temapr, "id":id}

	capacitacionpr=CapacitacionCapacitacion.objects.all().order_by("-fecha_hora_inicio")[:50]
	context27={"capacitacionpr":capacitacionpr, "id":id}

	turnopr=Turno.objects.all()[:50]
	context28={"turnopr":turnopr, "id":id}

	arealaborpr=AreaPlanta.objects.all()[:50]
	context31={"arealaborpr":arealaborpr, "id":id}	

	laborpr=LaborPlanta.objects.all()[:50]
	context30={"laborpr":laborpr, "id":id}	

	configurarfechapr=ConfigurarDia.objects.all().order_by("-fecha")[:30]
	context29={"configurarfechapr":configurarfechapr, "id":id}

	materialacopiopr=MaterialAcopio.objects.filter(anexo_estado=1)[:50]
	context41={"materialacopiopr":materialacopiopr, "id":id}

	placaspr=PlacasVehiculares.objects.all().order_by("-fecha_hora_creacion")[:50]
	context32={"placaspr":placaspr, "id":id}

	choferespr=ChoferesVehiculos.objects.all()[:50]
	context33={"choferespr":choferespr, "id":id}

	unidadvehicularpr=UnidadVehicular.objects.all()[:50]
	context50={"unidadvehicularpr":unidadvehicularpr, "id":id}

	ubicacionfunpr=UbicacionFundo.objects.all()[:50]
	context36={"ubicacionfunpr":ubicacionfunpr, "id":id}

	ubicaciongenpr=LugarAthos.objects.all()[:50]
	context37={"ubicaciongenpr":ubicaciongenpr, "id":id}

	centrosathospr=CentrosAthos.objects.all()[:50]
	context34={"centrosathospr":centrosathospr, "id":id}

	almacenesathospr=AlmacenesAthos.objects.all()[:50]
	context35={"almacenesathospr":almacenesathospr, "id":id}

	guiaathospr=GuiaAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context42={"guiaathospr":guiaathospr, "id":id}

	materialmmpppr=MaterialMMPP.objects.all()[:50]
	context38={"materialmmpppr":materialmmpppr, "id":id}

	materialtranspr=MaterialTransporte.objects.all()[:50]
	context39={"materialtranspr":materialtranspr, "id":id}

	parihuelapr=TipoParihuela.objects.all()[:50]
	context40={"parihuelapr":parihuelapr, "id":id}

	garitapr=GaritaAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context43={"garitapr":garitapr, "id":id}

	rutaspr=RutasAthos.objects.all()[:50]
	context49={"rutaspr":rutaspr, "id":id}

	alcancepr=AlcanceCapacitacion.objects.all()[:50]
	context108={"alcancepr":alcancepr, "id":id}

	if (id==1):
		return render(request, 'athos/campo.html', context)
	else:
		if(id==2):
			return render(request, 'athos/cultivo.html', context2)
		else:
			if(id==3):
				return render(request, 'athos/variedad.html', context3)
			else:
				if(id==5):
					return render(request, 'athos/fenologias.html', context5)
				else:
					if(id==4):
						return render(request, 'athos/campana.html', context4)
					else:
						if(id==7):
							return render(request, 'athos/modulo.html', context7)
						else:
							if(id==8):
								return render(request, 'athos/lote.html', context8)
							else:
								if(id==6):
									return render(request, 'athos/produccion.html', context6)
								else:
									if(id==9):
										return render(request, 'athos/flujo.html', context9)
									else:
										if(id==10):
											return render(request, 'athos/accion.html', context10)
										else:
											if(id==11):
												return render(request, 'athos/procesos.html', context11)
											else:
												if(id==12):
													return render(request, 'athos/solicitud.html', context12)
												else:
													if(id==13):
														return render(request, 'athos/variableagronomica.html', context13)
													else:
														if(id==14):
															return render(request, 'athos/versionagronomica.html', context14)
														else:
															if(id==15):
																return render(request, 'athos/planta.html', context15)
															else:
																if(id==16):
																	return render(request, 'athos/nave.html', context16)
																else:
																	if(id==18):
																		return render(request, 'athos/personalplanta.html', context18)
																	else:
																		if(id==17):
																			return render(request, 'athos/linea.html', context17)
																		else:
																			if(id==19):
																				return render(request, 'athos/lanzadopaletas.html', context19)
																			else:
																				if(id==20):
																					return render(request, 'athos/verificarlazadopaletas.html', context20)
																				else:
																					if(id==22):
																						return render(request, 'athos/configurarasistenciaplanta.html',context21)
																					else:
																						if(id==23):
																							return render(request, 'athos/configurarasistenciaplantasalida.html',context23)
																						else:
																							if(id==24):
																								return render(request, 'athos/area.html',context24)
																							else:
																								if(id==25):
																									return render(request, 'athos/competencia.html',context25)
																								else:
																									if(id==26):
																										return render(request, 'athos/tema.html',context26)
																									else:
																										if(id==27):
																											return render(request, 'athos/capacitacion.html',context27)
																										else:
																											if(id==28):
																												return render(request, 'athos/turno.html',context28)
																											else:
																												if(id==31):
																													return render(request, 'athos/arealabor.html',context31)
																												else:
																													if(id==30):
																														return render(request, 'athos/laborplanta.html',context30)
																													else:
																														if(id==29):
																															return render(request, 'athos/configurafecha.html',context29)
																														else:
																															if(id==41):
																																return render(request, 'athos/materialacopio.html',context41)
																															else:
																																if(id==32):
																																	return render(request, 'athos/placasvehiculares.html',context32)
																																else:
																																	if(id==33):
																																		return render(request, 'athos/choferesathos.html',context33)
																																	else:
																																		if(id==50):
																																			return render(request, 'athos/unidadvehicular.html',context50)
																																		else:
																																			if(id==36):
																																				return render(request, 'athos/ubicacionfundo.html',context36)
																																			else:
																																				if(id==37):
																																					return render(request, 'athos/lugarathos.html',context37)
																																				else:
																																					if(id==34):
																																						return render(request, 'athos/centrosathos.html',context34)
																																					else:
																																						if(id==35):
																																							return render(request, 'athos/almacenesathos.html',context35)
																																						else:
																																							if(id==42):
																																								return render(request, 'athos/guiaathos.html',context42)
																																							else:
																																								if(id==38):
																																									return render(request, 'athos/materialmmpp.html',context38)
																																								else:
																																									if(id==39):
																																										return render(request, 'athos/materialtransporte.html',context39)
																																									else:
																																										if(id==40):
																																											return render(request, 'athos/parihuela.html',context40)
																																										else:
																																											if(id==43):
																																												return render(request, 'athos/garitaathos.html',context43)
																																											else:
																																												if(id==49):
																																													return render(request, 'athos/rutasathos.html',context49)
																																												else:
																																													if(id==108):
																																														return render(request, 'athos/alcancecapacitacion.html',context108)




#def cultivo(request, id):
#	cultivopr=cultivo.objects.all()
#	context2={"cultivopr":cultivopr, "id":id}
#	return render(request, 'athos/cultivo.html', context2)


def crearcampo(request,id):
	form = Fundoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocampo.html', context)

def editarcampo(request, id, subid):
	sub_campo = get_object_or_404(fundo, id=subid)
	form =Fundoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocampo.html', context)


def crearmodulo(request, id):
	form = Moduloform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomodulo.html', context)

def editarmodulo(request, id, subid):
	sub_campo = get_object_or_404(modulo, id=subid)
	form =Moduloform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomodulo.html', context)



def crearcultivo(request, id):
	form = Cultivoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocultivo.html', context)


def editarcultivo(request, id, subid):
	sub_campo = get_object_or_404(cultivo, id=subid)
	form = Cultivoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cultivo', id)
	return render(request, 'athos/nuevocultivo.html', context)


def crearvariedad(request, id):
	form = Variedadform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevovariedad.html', context)

def editarvariedad(request, id, subid):
	sub_campo = get_object_or_404(variedad, id=subid)
	form = Variedadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevovariedad.html', context)

def crearfeno(request, id):
	form = Fenologiaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevofenologia.html', context)


def editarfeno(request, id, subid):
	sub_campo = get_object_or_404(fenologia, id=subid)
	form = Fenologiaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevofenologia.html', context)


def hitos(request, id, subid):

	hitospr = Hitos.objects.filter(anexo_fenologia_id=subid)
	context = {"hitospr":hitospr, "id":id, "subid":subid}
	return render(request, 'athos/hitos.html', context)



def crearhitos(request, id, subid):
	form = hitosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(fenologia,id=subid)
			result.anexo_fenologia = progra
			result.save()
			return redirect('hitos',id, subid)
	return render(request, 'athos/nuevohitos.html', context)

def editarhitos(request, id, subid,varid):
	sub_campo = get_object_or_404(Hitos, id=varid)
	form =hitosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('hitos', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevohitos.html', context)




def subhitos(request, id, subid,varid):
	subhitospr = SubHitos.objects.filter(anexo_hito_id=varid)
	context = {"subhitospr":subhitospr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/subhitos.html', context)


def crearsubhitos(request, id, subid,varid):
	print("anexo_feno")
	traer_cultivo=Hitos.objects.get(id=varid).anexo_fenologia.id
	legal=fenologia.objects.get(id=traer_cultivo).id_cultivo.id
	print(traer_cultivo)
	form =  subhitosform(request.POST or None,cultivo=legal)
	

	context = {"form":form,"varid":varid,"traer_cultivo":traer_cultivo,"legal":legal}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(Hitos,id=varid)
				result.anexo_hito = progravar
				result.save()

				return redirect('subhitos', id, subid, varid)
	return render(request, 'athos/nuevosubhitos.html', context)

def editarsubhitos(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(SubHitos, id=varid)

	form = subhitosform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('subhitos', id, subid, catid)
	return render(request, 'athos/nuevosubhitos.html', context)
	

def crearcampana(request):
	form = Campanaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevocampana.html', context)

def editarcampana(request, id, subid):
	sub_campo = get_object_or_404(campanas, id=subid)
	form = Campanaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocampana.html', context)

def crearlote(request,id):
	form = Loteform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolote.html', context)

def editarlote(request, id, subid):
	sub_campo = get_object_or_404(lote, id=subid)
	form = Loteform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolote.html', context)


def crearproduccion(request):
	form = Produccionform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			anexo_modulo=modulo.objects.get(id=request.POST.get("anexo_modulo"))
			anexo_lote=lote.objects.get(id=request.POST.get("anexo_lote"))
			result = form.save(commit=False)
			result.anexo_modulo=anexo_modulo
			result.anexo_lote=anexo_lote
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 6)
	return render(request, 'athos/nuevoproduccion.html', context)

def editarproduccion(request, id, subid):
	sub_campo = get_object_or_404(ProgramaProduccion, id=subid)
	
	if request.method=='POST':
		form = Produccionform(request.POST or None, instance=sub_campo)
		if form.is_valid():
			anexo_modulo=modulo.objects.get(id=request.POST.get("anexo_modulo"))
			anexo_lote=lote.objects.get(id=request.POST.get("anexo_lote"))
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			result.anexo_modulo=anexo_modulo
			result.anexo_lote=anexo_lote
			form.save()
			return redirect('campo', id)
	else:
		form = Produccionform(instance=sub_campo)
	context = {"form":form,"sub_campo":sub_campo, 'id':id, 'subid':subid}
	return render(request, 'athos/update_produccion.html', context)



def produccionfenologias(request, id, subid):

	produfenopr = ProgramaProduccionFeno.objects.filter(programa_produccion_id=subid)
	context = {"produfenopr":produfenopr, "id":id, "subid":subid}
	return render(request, 'athos/produccionfenologia.html', context)



def crearproduccionfeno(request, id, subid):
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul

	form = ProduccionFenoform(request.POST or None,anexo_cultivo=VariableCultivo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProgramaProduccion,id=subid)
			result.programa_produccion = progra
			result.save()
			return redirect('produccionfenologias',id, subid)
	return render(request, 'athos/nuevoprodufeno.html', context)

def editarproduccionfeno(request, id, subid,fenid):
	
	sub_campo = get_object_or_404(ProgramaProduccionFeno, id=fenid)
	
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul

	form = ProduccionFenoform(request.POST or None, instance=sub_campo,anexo_cultivo=VariableCultivo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('produccionfenologias', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevoprodufeno.html', context)


def hitosfenologicos (request, id, subid, varid):

	detallepr=HitosFenologicos.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid}
	return render(request, 'athos/programaproduccion/hitosfenologicos.html', context)


def crearhitosfenologicos(request, id, subid, varid):
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul
	form = hitosfenologicosform(request.POST or None,anexo_cultivo=VariableCultivo)

	context = {"form":form,"subid":subid,"varid":varid,"VariableCultivo":VariableCultivo }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProgramaProduccionFeno,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('hitosfenologicos',id,subid,varid)
	print(context)
	return render(request, 'athos/programaproduccion/nuevohitosfenologicos.html', context)


def editarhitosfenologicos(request, id, subid,varid,catid):

	sub_campo = get_object_or_404(HitosFenologicos, id=catid)
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul
	form = hitosfenologicosform(request.POST or None, instance=sub_campo,anexo_cultivo=VariableCultivo)
	context = {"form":form,"VariableCultivo":VariableCultivo}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('hitosfenologicos', id, subid, varid)
	return render(request, 'athos/programaproduccion/nuevohitosfenologicos.html', context)


	

def turnoprogramaproduccion(request, id, subid):

	turnopr = TurnoProgramaProduccion.objects.filter(anexo_programa_id=subid)
	context = {"turnopr":turnopr, "id":id, "subid":subid}
	return render(request, 'athos/programaproduccion/turnopp.html', context)



def crearturnoprogramaproduccion(request, id, subid):
	form = turnoprogramaproduccionform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProgramaProduccion,id=subid)
			result.anexo_programa = progra
			result.save()
			return redirect('turnoprogramaproduccion',id, subid)
	return render(request, 'athos/programaproduccion/nuevoturnopp.html', context)

def editarturnoprogramaproduccion(request, id, subid,fenid):
	sub_campo = get_object_or_404(TurnoProgramaProduccion, id=fenid)
	form = turnoprogramaproduccionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('turnoprogramaproduccion', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/programaproduccion/nuevoturnopp.html', context)
	


def crearflujo(request):
	form = Flujoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoflujo.html', context)


def editarflujo(request, id, subid):
	sub_campo = get_object_or_404(Flujo, id=subid)
	form = Flujoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoflujo.html', context)


def crearaccion(request):
	form = Accionesform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoaccion.html', context)


def editaraccion(request, id, subid):
	sub_campo = get_object_or_404(Acciones, id=subid)
	form = Accionesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoaccion.html', context)


def crearproceso(request):
	form = Procesosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoproceso.html', context)


def editarproceso(request, id, subid):
	sub_campo = get_object_or_404(Acciones, id=subid)
	form = Procesosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoproceso.html', context)

def crearsolicitud(request):
	form = Solicitudform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevosolicitud.html', context)


def editarsolicitud(request, id, subid):
	sub_campo = get_object_or_404(solicitud, id=subid)
	form = Solicitudform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevosolicitud.html', context)

def pep(request, id, subid):

	peppr = elementoPEP.objects.filter(programa_produccion_id=subid, anexo_estado_id =1)
	context = {"peppr":peppr, "id":id, "subid":subid}
	return render(request, 'athos/elementopep.html', context)


def crearpep(request, id, subid):
	

	form = elementoPEPform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			prograpep = get_object_or_404(ProgramaProduccion,id=subid)
			result.programa_produccion = prograpep
			result.save()
			return redirect('pep',id, subid)
	return render(request, 'athos/nuevoelementopep.html', context)

def editarpep(request, id, subid,pepid):
	sub_campo = get_object_or_404(elementoPEP, id=pepid)
	form = elementoPEPform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('pep', id, subid)
	return render(request, 'athos/nuevoelementopep.html', context)




class ProgramaProduccionListView(ListView):
    model = ProgramaProduccion
    context_object_name = 'programa'

class ProgramaProduccionCreateView(CreateView):
    model = ProgramaProduccion
    form_class = Produccionform
    fields = ('anexo_fundo', 'anexo_modulo', 'anexo_lote', 'anexo_campana','ano_campana','anexo_variedad','area','cierre_campana','estado')
    success_url = reverse_lazy('programa_changelist')

class ProgramaProduccionUpdateView(UpdateView):
    model = ProgramaProduccion
    form_class = Produccionform
    fields = ('anexo_fundo', 'anexo_modulo', 'anexo_lote', 'anexo_campana','ano_campana','anexo_variedad','area','cierre_campana','estado')
    success_url = reverse_lazy('programa_changelist')

def load_productos(request, id):
    modu = list(ProductosAutorizados.objects.filter(anexo_detalle_id=id).values('id','nom_comercial'))
    return JsonResponse(modu,safe=False)

def load_modulitos(request, id):
    modu = list(modulo.objects.filter(idfundo=id).values('id','nombremodulo'))
    return JsonResponse(modu,safe=False)

def load_lotecitos(request, id):
    lot = list(lote.objects.filter(mod=id).values('id','nom_lote'))
    return JsonResponse(lot,safe=False)

def load_fundos(request, id):
	fundos = list(ejezona.objects.get(id=id).ejezona.all().values('id','nom_fundo'))
	return JsonResponse(fundos,safe=False)

def load_rutas(request, id):
	rutas = list(fundo.objects.get(id=id).AnexoUbifundo.all().values('id','rutas'))
	return JsonResponse(rutas,safe=False)

def load_pep(request, id):
	pep = list(fundo.objects.get(id=id).fundo3.filter(estado=1).values('id','anexo_fundo__abreviatura','anexo_modulo__nombremodulo','anexo_lote__nom_lote','ano_campana'))
	print(pep)
	return JsonResponse(pep,safe=False)

def load_procesos(request, id):
	procesos = list(Macroproceso.objects.get(id=id).AnexoMacroproceso.all().values('id','descripcion'))
	return JsonResponse(procesos,safe=False)

def load_objetivos(request, id):
	objetivos = list(Proceso.objects.get(id=id).AnexoProceso.all().values('id','descripcion'))
	return JsonResponse(objetivos,safe=False)

def load_planta(request, id):
	planta = list(ejezona.objects.get(id=id).ejezona20.all().values('id','nom_planta'))
	return JsonResponse(planta,safe=False)

def load_nave(request, id):
	nave = list(Planta.objects.get(id=id).Planta.all().values('id','nom_nave'))
	return JsonResponse(nave,safe=False)

def crearvariableagro(request,id):
	form = Variableform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevovariableagronomica.html', context)

def editarvariableagro(request, id, subid):
	sub_campo = get_object_or_404(VariableAgronomica, id=subid)
	form =Variableform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevovariableagronomica.html', context)


def subvariableagronomica(request, id, subid):

	subvariablepr = SubVariableAgronomica.objects.filter(anexo_variable_id=subid)
	context = {"subvariablepr":subvariablepr, "id":id, "subid":subid}
	return render(request, 'athos/subvariableagronomica.html', context)



def crearsubvariableagronomica(request, id, subid):
	form = subvariableform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(VariableAgronomica,id=subid)
			result.anexo_variable = progra
			result.save()
			return redirect('subvariableagronomica',id, subid)
	return render(request, 'athos/nuevosubvariableagronomica.html', context)

def editarsubvariableagronomica(request, id, subid,varid):
	sub_campo = get_object_or_404(SubVariableAgronomica, id=varid)
	form = subvariableform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('subvariableagronomica', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevosubvariableagronomica.html', context)





def crearversionagro(request, id ):
	form = VersionAgroform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoversionagronomica.html', context)

def editarversionagro(request, id, subid):
	sub_campo = get_object_or_404(VersionAgronomica, id=subid)
	form =VersionAgroform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoversionagronomica.html', context)


def produccionvariable(request, id, subid):

	pvarpr = PproduccionVariable.objects.filter(programa_produccion_id=subid)
	context = {"pvarpr":pvarpr, "id":id, "subid":subid}
	return render(request, 'athos/produccionvariable.html', context)


def crearproduccionvariables(request, id, subid):
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul

	form = ProduccionVariableform(request.POST or None,anexo_cultivo=VariableCultivo)

	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProgramaProduccion,id=subid)
			result.programa_produccion = progravar
			result.save()
			return redirect('produccionvariable',id, subid)
	return render(request, 'athos/nuevoproduccionvariable.html', context)

def editarproduccionvariables(request, id, subid,varid):
	sub_campo = get_object_or_404(PproduccionVariable, id=varid)
	
	idcultivo=subid
	VariableCultivo=ProgramaProduccion.objects.get(id=idcultivo).anexo_variedad.cul

	form = ProduccionVariableform(request.POST or None, instance=sub_campo,anexo_cultivo=VariableCultivo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('produccionvariable', id, subid)
	return render(request, 'athos/nuevoproduccionvariable.html', context)

def crearplanta(request):

	form = plantaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 15)
	return render(request, 'athos/nuevoplanta.html', context)

def editarplanta(request, id, subid):
	sub_campo = get_object_or_404(Planta, id=subid)
	form = plantaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoplanta.html', context)

def crearnave(request):

	form = naveform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 16)
	return render(request, 'athos/nuevonave.html', context)

def editarnave(request, id, subid):
	sub_campo = get_object_or_404(Nave, id=subid)
	form = naveform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevonave.html', context)


def crearlinea(request):

	form = lineaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 17)
	return render(request, 'athos/nuevolinea.html', context)

def editarlinea(request, id, subid):
	sub_campo = get_object_or_404(Linea, id=subid)
	form = lineaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolinea.html', context)


def crearpersonalplanta(request):
	form = personalplantaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 18)
	return render(request, 'athos/nuevopersonalplanta.html', context)

def editarpersonalplanta(request, id, subid):
	sub_campo = get_object_or_404(PersonalPlanta, id=subid)
	
	if request.method=='POST':
		form = personalplantaform(request.POST or None, instance=sub_campo)
		if form.is_valid():
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			form.save()
			return redirect('campo', id)
	else:
		form = personalplantaform(instance=sub_campo)
	context = {"form":form,"sub_campo":sub_campo, 'id':id, 'subid':subid}
	return render(request, 'athos/update_personalplanta.html', context)


def crearlanzadopaletas(request):
	form = lanzadopaletasform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 19)
	return render(request, 'athos/nuevolanzadopaletas.html', context)

def editarlanzadopaletas(request, id, subid):
	sub_campo = get_object_or_404(LPaletas, id=subid)
	
	if request.method=='POST':
		form = lanzadopaletasform(request.POST or None, instance=sub_campo)
		if form.is_valid():
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			form.save()
			return redirect('campo', id)
	else:
		form = lanzadopaletasform(instance=sub_campo)
	context = {"form":form,"sub_campo":sub_campo, 'id':id, 'subid':subid}
	return render(request, 'athos/update_lanzadopaletas.html', context)



def lanzadopaletasreal(request, id, subid):

	lpralpr = LPaletasReal.objects.filter(anexo_lanzado_id=subid, estado_id=1).order_by("-fecha_hora_creacion")[:50]
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/lanzadopaletasreal.html', context)


def crearlanzadopaletasreal(request, id, subid):
	form = lanzadopaletasrealform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			return redirect('crearlanzadopaletasreal',id, subid)
	return render(request, 'athos/nuevolanzadopaletasreal.html', context)

def editarlanzadopaletasreal(request, id, subid,varid):
	sub_campo = get_object_or_404(LPaletasReal, id=varid)
	form = lanzadopaletasrealform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			result = form.save(commit=False)
			result.fecha_hora_modificacion=timezone.now()
			result.save()
			return redirect('lanzadopaletasreal', id, subid)
	return render(request, 'athos/nuevolanzadopaletasreal.html', context)

def crearmateriales(request):

	form = materialesform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 25)
	return render(request, 'athos/nuevomateriales.html', context)

def editarmateriales(request, id, subid):
	sub_campo = get_object_or_404(Materiales, id=subid)
	form = materialesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomateriales.html', context)


def crearordenpedido(request):

	form = ordenpedidoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 26)
	return render(request, 'athos/nuevoordenpedido.html', context)

def editarordenpedido(request, id, subid):
	sub_campo = get_object_or_404(OrdenPedido, id=subid)
	form = ordenpedidoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoordenpedido.html', context)


def crearzonapaletizado(request):
	form = zonapaletizadoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 27)
	return render(request, 'athos/nuevozonapaletizado.html', context)

def editarzonapaletizado(request, id, subid):
	sub_campo = get_object_or_404(ZonaPaletizado, id=subid)
	
	if request.method=='POST':
		form = zonapaletizadoform(request.POST or None, instance=sub_campo)
		if form.is_valid():
			anexo_planta=Planta.objects.get(id=request.POST.get("anexo_planta"))
			anexo_nave=Nave.objects.get(id=request.POST.get("anexo_nave"))
			result = form.save(commit=False)
			result.anexo_planta=anexo_planta
			result.anexo_nave=anexo_nave
			form.save()
			return redirect('campo', id)
	else:
		form = zonapaletizadoform(instance=sub_campo)
	context = {"form":form,"sub_campo":sub_campo, 'id':id, 'subid':subid}
	return render(request, 'athos/update_zonapaletizado.html', context)



def paletizado(request, id, subid):

	lpalpr = Paletizado.objects.filter(anexo_lanzado_id=subid)
	context = {"lpalpr":lpalpr, "id":id, "subid":subid}
	return render(request, 'athos/paletizadoreal.html', context)


def crearpaletizado(request, id, subid):
	form = paletizadoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(ZonaPaletizado,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			return redirect('crearpaletizado',id, subid)
	return render(request, 'athos/nuevopaletizadoreal.html', context)

def editarpaletizado(request, id, subid,varid):
	sub_campo = get_object_or_404(Paletizado, id=varid)
	form = paletizadoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('paletizado', id, subid)
	return render(request, 'athos/nuevopaletizadoreal.html', context)

def ordenpedidoreal(request, id, subid):

	ordenpedidorealpr = OrdenPedidoMaterialf.objects.filter(anexo_orden_id=subid).order_by("-fecha_hora_creacion")[:50]
	context = {"ordenpedidorealpr":ordenpedidorealpr, "id":id, "subid":subid}
	return render(request, 'athos/ordenpedidoreal.html', context)


def crearordenpedidoreal(request, id, subid):
	form = ordenpedidomaterialfform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(OrdenPedido,id=subid)
			result.anexo_orden = progravar
			result.save()
			return redirect('crearordenpedidoreal',id, subid)
	return render(request, 'athos/nuevoordenpedidoreal.html', context)

def editarordenpedidoreal(request, id, subid,varid):
	sub_campo = get_object_or_404(OrdenPedidoReal, id=varid)
	form = ordenpedidomaterialfform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('produccionvariable', id, subid)
	return render(request, 'athos/nuevoordenpedidoreal.html', context)



def verificarpalet(request, id, subid):

	lpralpr = LPaletasReal.objects.filter(anexo_lanzado_id=subid,estado_id=1).order_by("-fecha_hora_creacion")[:50]
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/verificadolanzadopaletasreal.html', context)

# crear recepcion-palet
def crearverificarpalet(request, id, subid):
	form = lanzadopaletasrealform(request.POST or None)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			return redirect('crearverificarpalet',id, subid)
	return render(request, 'athos/nuevorecepcionpalet.html', context)

#editar recepcion palet
def editarverificarpalet(request, id, subid,varid):
	sub_campo = get_object_or_404(LPaletasReal, id=varid)
	form = lanzadopaletasrealform(request.POST or None, instance=sub_campo)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('verificarpalet', id, subid)
	return render(request, 'athos/editarrecepcionpalet.html', context)


def editarpaletizado(request, id, subid,varid):
	sub_campo = get_object_or_404(Paletizado, id=varid)
	form = paletizadoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('paletizado', id, subid)
	return render(request, 'athos/nuevopaletizadoreal.html', context)


def crearconfigasistenciapl(request, id):

	form = configurarasistenciaplantaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoconfigasistenciaplanta.html', context)

def asistenciaoingresoplanta(request, id, subid):

	ingresopr=IngresoAsistenciaPlanta.objects.filter(anexo_asistencia_id=subid).order_by("-fecha_ingreso")
	context={"ingresopr":ingresopr, "id":id,"subid":subid}
	return render(request, 'athos/plantaasistenciaingreso.html', context)


def crearasistenciaingresopl(request, id, subid):
	form =  ingresoplantaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ConfAsistenciaPlanta,id=subid)
			result.anexo_asistencia = progravar
			result.save()
			print("is_valid2")

			return redirect('crearasistenciaingresopl',id,subid)
	print(context)
	return render(request, 'athos/nuevoingresoasistenciapl.html', context)


def asistenciaosalidaplanta(request, id, subid):

	salidapr=SalidaAsistenciaPlanta.objects.filter(anexo_asistencia_id=subid).order_by("-fecha_salida")
	context={"salidapr":salidapr, "id":id,"subid":subid}
	return render(request, 'athos/plantaasistenciasalida.html', context)


def crearasistenciasalidapl(request, id, subid):
	form =  salidaplantaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ConfAsistenciaPlanta,id=subid)
			result.anexo_asistencia = progravar
			result.save()
			print("is_valid2")

			return redirect('crearasistenciasalidapl',id,subid)
	print(context)
	return render(request, 'athos/nuevosalidaasistenciapl.html', context)


def creararea(request):

	form = areaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 24)
	return render(request, 'athos/nuevoarea.html', context)

def editararea(request, id, subid):
	sub_campo = get_object_or_404(AreaCapacitacion, id=subid)
	form = areaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoarea.html', context)


def crearcompetencias(request):

	form = competenciaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 25)
	return render(request, 'athos/nuevocompetencia.html', context)

def editarcompetencias(request, id, subid):
	sub_campo = get_object_or_404(CompetenciaCapacitacion, id=subid)
	form = competenciaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocompetencia.html', context)




def crearalcancecapacitacion(request, id):

	form = alcancecapacitacionform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoalcancecapacitacion.html', context)

def editaralcancecapacitacion(request, id, subid):
	sub_campo = get_object_or_404(AlcanceCapacitacion, id=subid)
	form = alcancecapacitacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoalcancecapacitacion.html', context)

def creartema(request):

	form = temaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 26)
	return render(request, 'athos/nuevotema.html', context)

def editartema(request, id, subid):
	sub_campo = get_object_or_404(TemaCapacitacion, id=subid)
	form = temaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevotema.html', context)

def load_tema(request, id):
    tema = list(CompetenciaCapacitacion.objects.get(id=id).Competencia_Tema.all().values('id','nom_tema'))
    return JsonResponse(tema,safe=False)

def crearcapacitacion(request,id):
	ac_ica=len(CapacitacionCapacitacion.objects.filter(lugar=1))
	ac_car=len(CapacitacionCapacitacion.objects.filter(lugar=2))
	ac_nep=len(CapacitacionCapacitacion.objects.filter(lugar=3))
	ac_naz=len(CapacitacionCapacitacion.objects.filter(lugar=4))
	ac_pis=len(CapacitacionCapacitacion.objects.filter(lugar=5))
	
	form = capacitacionform(request.POST or None,request.FILES)
	context = {"form":form,"ac_ica":ac_ica,"ac_car":ac_car,"ac_nep":ac_nep,"ac_naz":ac_naz,"ac_pis":ac_pis}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			for tema in request.POST.getlist("anexo_tema"):
				result.anexo_tema.add(TemaCapacitacion.objects.get(id=tema))


			
			return redirect('campo', id)
	return render(request, 'athos/capacitaciones/nuevocapacitacion.html', context)

def editarcapacitacion(request, id, subid):
	sub_campo = get_object_or_404(CapacitacionCapacitacion, id=subid)
	form = capacitacionform(request.POST or None,request.FILES or None,instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/capacitaciones/nuevocapacitacion.html', context)

def confirmativacapacitacion(request, id, subid):
	sub_campo = get_object_or_404(CapacitacionCapacitacion, id=subid)
	form = capacitacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/capacitaciones/editarcapacitacion.html', context)

def asistenciacapacitacion(request, id, subid):

	ingresocapacitacionpr=AsistenciaCapacitacion.objects.filter(anexo_capacitacion_id=subid).order_by("-fecha_hora_inicio")
	context={"ingresocapacitacionpr":ingresocapacitacionpr, "id":id,"subid":subid}
	return render(request, 'athos/capacitaciones/asistenciacapacitacion.html', context)


def crearasistenciacapacitacion(request, id, subid):
	form =  asistenciacapacitacionform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(CapacitacionCapacitacion,id=subid)
			result.anexo_capacitacion = progravar
			result.save()
			print("is_valid2")

			return redirect('crearasistenciacapacitacion',id,subid)
	print(context)
	return render(request, 'athos/capacitaciones/nuevoasistentecapacitacion.html', context)

def editarasistenciacapacitacion(request, id, subid,varid):
	sub_campo = get_object_or_404(AsistenciaCapacitacion, id=varid)
	form = asistenciacapacitacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			form.save()
			return redirect('asistenciacapacitacion', id, subid)
	return render(request, 'athos/capacitaciones/editarasistentecapacitacion.html', context)



def crearlabor(request):

	form = laborform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 30)
	return render(request, 'athos/nuevolabor.html', context)

def editarlabor(request, id, subid):
	sub_campo = get_object_or_404(LaborPlanta, id=subid)
	form = laborform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolabor.html', context)

def creararealabor(request):

	form = arealaborform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 31)
	return render(request, 'athos/nuevoarealabor.html', context)

def editararealabor(request, id, subid):
	sub_campo = get_object_or_404(AreaPlanta, id=subid)
	form = arealaborform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoarealabor.html', context)

def crearturno(request):

	form = turnoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 28)
	return render(request, 'athos/nuevoturno.html', context)

def editarturno(request, id, subid):
	sub_campo = get_object_or_404(Turno, id=subid)
	form = turnoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoturno.html', context)

def crearfecha(request):

	form = configurarfechaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 29)
	return render(request, 'athos/nuevofecha.html', context)





def crearmaterialacopio(request):

	form = materialacopioform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 41)
	return render(request, 'athos/nuevomaterialacopio.html', context)

def editarmaterialacopio(request, id, subid):
	sub_campo = get_object_or_404(MaterialAcopio, id=subid)
	form = materialacopioform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomaterialacopio.html', context)	


def crearmaterialtransporte(request):

	form = materialtransporteform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 39)
	return render(request, 'athos/nuevomaterialtransporte.html', context)

def editarmaterialtransporte(request, id, subid):
	sub_campo = get_object_or_404(MaterialTransporte, id=subid)
	form = materialtransporteform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomaterialtransporte.html', context)	



def crearmaterialmmpp(request):

	form = materialmmppform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 38)
	return render(request, 'athos/nuevomaterialmmpp.html', context)

def editarmaterialmmpp(request, id, subid):
	sub_campo = get_object_or_404(MaterialMMPP, id=subid)
	form = materialmmppform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomaterialmmpp.html', context)






def crearplacasvehiculares(request):

	form = placasvehicularesform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 32)
	return render(request, 'athos/nuevoplacasvehiculares.html', context)

def editarplacasvehiculares(request, id, subid):
	sub_campo = get_object_or_404(PlacasVehiculares, id=subid)
	form = placasvehicularesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoplacasvehiculares.html', context)




def detalleplacasvehiculares (request, id, subid):

	detallepr=DetallePlacasVehiculares.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/detalleplacasvehiculares.html', context)


def creardetalleplacasvehiculares(request, id, subid):
	form = detalleplacasvehicularesform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(PlacasVehiculares,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleplacasvehiculares',id,subid)
	print(context)
	return render(request, 'athos/nuevodetalleplacasvehiculares.html', context)


def editardetalleplacasvehiculares(request, id, subid,varid):
	sub_campo = get_object_or_404(DetallePlacasVehiculares, id=varid)
	form = detalleplacasvehicularesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleplacasvehiculares', id, subid)
	return render(request, 'athos/nuevodetalleplacasvehiculares.html', context)




def crearchoferesathos(request):

	form = choferesvehiculosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 33)
	return render(request, 'athos/nuevochoferesathos.html', context)

def editarchoferesathos(request, id, subid):
	sub_campo = get_object_or_404(ChoferesVehiculos, id=subid)
	form = choferesvehiculosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevochoferesathos.html', context)

def crearunidadvehicular(request):

	form = unidadvehicularform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 50)
	return render(request, 'athos/nuevounidadvehicular.html', context)

def editarunidadvehicular(request, id, subid):
	sub_campo = get_object_or_404(UnidadVehicular, id=subid)
	form = unidadvehicularform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevounidadvehicular.html', context)

def crearubicacionfundo(request):

	form = ubicacionfundoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 36)
	return render(request, 'athos/nuevoubicacionfundo.html', context)

def editarubicacionfundo(request, id, subid):
	sub_campo = get_object_or_404(UbicacionFundo, id=subid)
	form = ubicacionfundoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoubicacionfundo.html', context)

def crearlugarathos(request):

	form = lugarathosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 37)
	return render(request, 'athos/nuevolugarathos.html', context)

def editarlugarathos(request, id, subid):
	sub_campo = get_object_or_404(LugarAthos, id=subid)
	form = lugarathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolugarathos.html', context)

def crearcentrosathos(request):

	form = centrosathosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 34)
	return render(request, 'athos/nuevocentrosathos.html', context)

def editarcentrosathos(request, id, subid):
	sub_campo = get_object_or_404(CentrosAthos, id=subid)
	form = centrosathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocentrosathos.html', context)

def crearalmacenesathos(request):
	form = almacenesathosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 35)
	return render(request, 'athos/nuevoalmacenesathos.html', context)

def editaralmacenesathos(request, id, subid):
	sub_campo = get_object_or_404(AlmacenesAthos, id=subid)
	form = almacenesathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoalmacenesathos.html', context)

def crearguiaathos(request):
	form = guiaathosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 42)
	return render(request, 'athos/nuevoguiaathos.html', context)

def editarguiaathos(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthos, id=subid)
	form = guiaathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoguiaathos.html', context)


def guiadetallesathos(request, id, subid):

	guiadetallespr=GuiaDetallesAthos.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")[:50]
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/guiadetallesathos.html', context)


def crearguiadetallesathos(request, id, subid):
	form =  guiadetallesathosform(request.POST or None)

	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthos,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathos',id,subid)
	print(context)
	return render(request, 'athos/nuevoguiadetallesathos.html', context)


def editarguiadetallesathos(request, id, subid,varid):
	sub_campo = get_object_or_404(GuiaDetallesAthos, id=varid)
	form = guiadetallesathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathos', id, subid)
	return render(request, 'athos/nuevoguiadetallesathos.html', context)


def infopalet(request, id, subid,varid):
	infopaletpr = InfoPalet.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/infopalet.html', context)


def crearinfopalet(request, id, subid,varid):
	form =  infopaletform(request.POST or None)
	palet1 = GuiaDetallesAthos.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthos,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathos', id, subid)
		else:
			url = "/athos/nuevoinfopalet/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/nuevoinfopalet.html', context)

def editarinfopalet(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPalet, id=varid)

	palet1 = GuiaDetallesAthos.objects.get(id=catid)
	palet2 = InfoPalet.objects.get(id=varid)
	form = infopaletform(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopalet', id, subid, catid)
	return render(request, 'athos/nuevoinfopalet.html', context)






def printpalet(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPalet.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,
				"palet":palet,"pep":pep}
	return render(request, 'athos/printpalet.html',context)


def crearparihuela(request):

	form = tipoparihuelaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 40)
	return render(request, 'athos/nuevoparihuela.html', context)

def editarparihuela(request, id, subid):
	sub_campo = get_object_or_404(TipoParihuela, id=subid)
	form = tipoparihuelaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoparihuela.html', context)


def crearrutasathos(request,id):

	form = rutasathosform(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevorutasathos.html', context)

def editarrutasathos(request, id, subid):
	sub_campo = get_object_or_404(RutasAthos, id=subid)
	form = rutasathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevorutasathos.html', context)


#garitaathos-crear-editar
def creargaritaacopio(request):

	form = garitaathosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campo', 43)
	return render(request, 'athos/nuevogaritaathos.html', context)

def editargaritaacopio(request, id, subid):
	sub_campo = get_object_or_404(GaritaAthos, id=subid)
	form = garitaathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevogaritaathos.html', context)