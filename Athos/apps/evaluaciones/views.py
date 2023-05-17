from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth
from datetime import datetime

from apps.evaluaciones.models import EvFenBrotesArandanos
from apps.evaluaciones.forms import evfenbrotesarandanosform

from apps.evaluaciones.models import DetallePlantaEvFenBrotesArandanos
from apps.evaluaciones.forms import evfenbrotedetalleplantaform

from apps.evaluaciones.models import  BrotePlantaEvFenBrotesArandanos
from apps.evaluaciones.forms import broteplantaevfenform

from apps.evaluaciones.models import EvFenBrotesArandanosSem
from apps.evaluaciones.forms import evfenbrotesarandanossemform

from apps.evaluaciones.models import DetallePlantaEvFenBrotesArandanosSem
from apps.evaluaciones.forms import evfenbrotedetalleplantasemform

from apps.evaluaciones.models import  BrotePlantaEvFenBrotesArandanosSem
from apps.evaluaciones.forms import broteplantaevfensemform


from apps.evaluaciones.models import EvFenRaicesArandanos
from apps.evaluaciones.forms import evfenraicesarandanosform

from apps.evaluaciones.models import DetalleEvFenRaicesArandanos
from apps.evaluaciones.forms import detalleevfenraicesarandanosform

from apps.evaluaciones.models import RaicesEvFenRaicesArandanos
from apps.evaluaciones.forms import raicesevfenraicesarandanosform

from apps.menu.models import LPaletas
from apps.menu.forms import lanzadopaletasform

from apps.evaluaciones.models import ControlProductoTerminado
from apps.evaluaciones.forms import controlproductoterminadoform

from apps.evaluaciones.models import DetalleControlProductoTerminado
from apps.evaluaciones.forms import detallecontrolproductoterminadoform

from apps.maestras.models import MaestraPresentacionesAthos
from apps.menu.models import CentrosAthos

from apps.evaluaciones.models import EvSanPlagasArandanos
from apps.evaluaciones.forms import evsanplagasarandanosform

from apps.evaluaciones.models import GruposPlagasArandanos
from apps.evaluaciones.forms import gruposplagasarandanosform

from apps.evaluaciones.models import SubGruposPlagasArandanos
from apps.evaluaciones.forms import subgruposplagasarandanosform

from apps.evaluaciones.models import VariablesPlagasArandanos
from apps.evaluaciones.forms import variablesplagasarandanosform


from apps.evaluaciones.models import EvFenFrutoArandanos
from apps.evaluaciones.forms import evfenfrutoarandanosform

from apps.evaluaciones.models import DetalleEvFenFrutoArandanos
from apps.evaluaciones.forms import detalleevfenfrutoarandanosform

from apps.evaluaciones.models import EvFenPlanasa
from apps.evaluaciones.forms import evfenplanasaform

from apps.evaluaciones.models import DetalleEvFenPlanasa
from apps.evaluaciones.forms import detalleevfenplanasaform

from apps.evaluaciones.models import EvCalDefectosCampo
from apps.evaluaciones.forms import evcaldefectoscampoform

from apps.evaluaciones.models import DetalleEvCalDefectosCampo
from apps.evaluaciones.forms import detalleevcaldefectoscampoform

from apps.evaluaciones.models import EvCalAcopioPlantaArCaraz202202
from apps.evaluaciones.models import EvCalAcopioPlantaArCaraz202202
from apps.evaluaciones.forms import evcalacopioplantaform

from apps.evaluaciones.models import EvCalAcopioPlantaArIca2021
from apps.evaluaciones.models import EvCalAcopioPlantaArIca202202
from apps.evaluaciones.forms import evcalacopioplantaarica2021form



from apps.evaluaciones.models import EvCartillaDrenado
from apps.evaluaciones.forms import evcartilladrenadoform

from apps.evaluaciones.models import DetalleEvCartillaDrenado
from apps.evaluaciones.forms import detalleevcartilladrenadoform

from apps.evaluaciones.models import SelTrabajadorEvCalPodaAr
from apps.evaluaciones.forms import seltrabajadorevcalpodaarform

from apps.evaluaciones.models import EvCalPodaAr
from apps.evaluaciones.forms import evcalpodaarform

from apps.evaluaciones.models import DetalleEvCalPodaAr
from apps.evaluaciones.forms import detalleevcalpodaarform


from apps.evaluaciones.models import EvCalMuestreoCosechaHg2021
from apps.evaluaciones.forms import evcalmuestreocosechahg2021form

from apps.evaluaciones.models import DetalleEvCalMuestreoCosechaHg2021
from apps.evaluaciones.forms import detalleevcalmuestreocosechahg2021form


from apps.evaluaciones.models import EvCalMuestreoPlantaHgIca2021
from apps.evaluaciones.forms import evcalmuestreoplantahgica2021form

from apps.evaluaciones.models import DetalleEvCalMuestreoPlantaHgIca2021
from apps.evaluaciones.forms import detalleevcalmuestreoplantahgica2021form


from apps.evaluaciones.models import EvCalBrixGrIca2021
from apps.evaluaciones.forms import evcalbrixgrica2021form

from apps.evaluaciones.models import DetalleEvCalBrixGrIca2021
from apps.evaluaciones.forms import detalleevcalbrixgrica2021form


from apps.evaluaciones.models import EvCalMmppGrIca2021
from apps.evaluaciones.forms import evcalmmppgrica2021form

from apps.evaluaciones.models import DetalleEvCalMmppGrIca2021
from apps.evaluaciones.forms import detalleevcalmmppgrica2021form

from apps.evaluaciones.models import EvCalControlDescarteGrIca2022
from apps.evaluaciones.forms import evcalcontroldescartegrica2022form

from apps.evaluaciones.models import DetalleEvCalControlDescarteGrIca2022
from apps.evaluaciones.forms import detalleevcalcontroldescartegrica2022form

from apps.acopio_athos.granada.models import InfoPaletGrIca2021

from apps.evaluaciones.models import EvCalControlPesosGrIca2022
from apps.evaluaciones.forms import evcalcontrolpesosgrica2022form

from apps.evaluaciones.models import DetalleEvCalControlPesosGrIca2022
from apps.evaluaciones.forms import detalleevcalcontrolpesosgrica2022form

from apps.evaluaciones.models import EvPlantonesPlNaz2022
from apps.evaluaciones.forms import evplantonesplnaz2022form

from apps.evaluaciones.models import DetalleEvPlantonesPlNaz2022
from apps.evaluaciones.forms import detalleevplantonesplnaz2022form

#CARTILLA EV MUESTRAS CAJAS EMPACADAS GR2022
from apps.evaluaciones.models import EvMuestrasCajasEmpacadasGR2022
from apps.evaluaciones.forms import evcalmuestracajasempacadasgr2022form
from apps.evaluaciones.models import DetalleEvMuestrasCajasEmpacadasGR2022
from apps.evaluaciones.forms import detalleevcalmuestracajasempacadasgr2022form

#CONTROL DESCARTE GR ICA 2022
from apps.evaluaciones.models import EvControlDescarteGR2022
from apps.evaluaciones.forms import evcontroldescartegr2022form

#EV RAMAS ARANDANOS
from apps.evaluaciones.models import EvFenRamasArandanos
from apps.evaluaciones.forms import evfenramasarandanosform
from apps.evaluaciones.models import DetallePlantaEvFenRamasArandanos
from apps.evaluaciones.forms import evfenramasdetalleplantaform
from apps.evaluaciones.models import RamaPlantaEvFenRamasArandanos
from apps.evaluaciones.forms import ramaplantaevfenform

#EV CAL DESCARTE AR
from apps.evaluaciones.models import EvCalControlDescarteAr2022
from apps.evaluaciones.forms import evcalcontroldescartearica2022form
from apps.evaluaciones.models import DetalleEvCalControlDescarteAr2022
from apps.evaluaciones.forms import detalleevcalcontroldescartearica2022form

#EV DESCARTE AR
from apps.evaluaciones.models import EvControlDescarteAr2022
from apps.evaluaciones.models import EvControlDescarteAr202202
from apps.evaluaciones.forms import evcontroldescartear2022form
from apps.evaluaciones.models import DetalleEvControlDescarteAr2022
from apps.evaluaciones.models import DetalleEvControlDescarteAr202202
from apps.evaluaciones.forms import detalleevcontroldescartear2022form

#EV CAMARAS HUMEDAS
from apps.evaluaciones.models import EvCamarasHumedas
from apps.evaluaciones.forms import evcamarashumedasform
from apps.evaluaciones.models import DetallePlantaEvCamarasHumedas
from apps.evaluaciones.forms import detalleevcamarashumedasform
from apps.menu.models import ProgramaProduccion

#EV CALIDAD MUESTREO PLANTA HG ICA 2022
from apps.evaluaciones.models import EvCalMuestreoPlantaHgIca2022
from apps.evaluaciones.forms import evcalmuestreoplantahgica2022form

#EV CALIDAD MUESTREO PLANTA HG NEP 2022
from apps.evaluaciones.models import EvCalMuestreoPlantaHgNep202202
from apps.evaluaciones.forms import evcalmuestreoplantahgnep2022form

#EV CALIDAD CONTROL DESCARTE HG 2022
from apps.evaluaciones.models import EvCalControlDescarteHg2022
from apps.evaluaciones.forms import evcalcontroldescartehg2022form
from apps.evaluaciones.models import DetalleEvCalControlDescarteHg2022
from apps.evaluaciones.forms import detalleevcalcontroldescartehg2022form

#EV CALIDAD PRODUCTO TERMINADO HG 2022
from apps.evaluaciones.models import ControlProductoTerminadoHg
from apps.evaluaciones.forms import controlproductoterminadohgform
from apps.evaluaciones.models import DetalleControlProductoTerminadoHg
from apps.evaluaciones.forms import detallecontrolproductoterminadohgform

#EV EFICIENCIA SELECCION Y CALIBRADO 2022
from apps.evaluaciones.models import EvEficienciaSeleccionCalibrado
from apps.evaluaciones.forms import eveficienciaseleccioncalibradoform

#EV PRODUCTO TERMINADO ANTES DE DESPACHO 2022
from apps.evaluaciones.models import EvProductoTerminadoDespacho
from apps.evaluaciones.forms import evproductoterminadodespachoform
from apps.evaluaciones.models import DetalleEvProductoTerminadoDespacho
from apps.evaluaciones.forms import detalleevproductoterminadodespachoform

# Create your views here.
def evaluaciones(request, id):

	if request.user.is_superuser:
		brotespr = EvFenBrotesArandanos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context44 = {"brotespr":brotespr, "id":id}
	else:
		brotespr = EvFenBrotesArandanos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context44 = {"brotespr":brotespr, "id":id}

	if request.user.is_superuser:
		raicespr = EvFenRaicesArandanos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context47= {"raicespr":raicespr, "id":id}
	else:
		raicespr = EvFenRaicesArandanos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context47= {"raicespr":raicespr, "id":id}

	lanzadopaletaspr=LPaletas.objects.filter(anexo_estado=1)
	context55={"lanzadopaletaspr":lanzadopaletaspr, "id":id}

	if request.user.is_superuser:
		brotespr = EvFenBrotesArandanosSem.objects.all().order_by("-fecha_hora_creacion")[:50]
		context56= {"brotespr":brotespr, "id":id}
	else:
		brotespr = EvFenBrotesArandanosSem.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context56 = {"brotespr":brotespr, "id":id}
	
	if request.user.is_superuser:
		plagaspr = EvSanPlagasArandanos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context61= {"plagaspr":plagaspr, "id":id}
	else:
		plagaspr = EvSanPlagasArandanos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context61= {"plagaspr":plagaspr, "id":id}

	if request.user.is_superuser:
		frutospr = EvFenFrutoArandanos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context65= {"frutospr":frutospr, "id":id}
	else:
		frutospr = EvFenFrutoArandanos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context65 = {"frutospr":frutospr, "id":id}

	if request.user.is_superuser:
		planasapr = EvFenPlanasa.objects.all().order_by("-fecha_hora_creacion")[:50]
		context66= {"planasapr":planasapr, "id":id}
	else:
		planasapr = EvFenPlanasa.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context66 = {"planasapr":planasapr, "id":id}

	if request.user.is_superuser or request.user.username=='oosorio' or request.user.username=='ssifuentes' or request.user.username=='Mfigueroa':
		defectospr = EvCalDefectosCampo.objects.all().order_by("-fecha_hora_creacion")[:50]
		context70= {"defectospr":defectospr, "id":id, "fecha2":datetime.today()}
	else:
		defectospr = EvCalDefectosCampo.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context70 = {"defectospr":defectospr, "id":id, "fecha2":datetime.today()}

	if request.user.is_superuser:
		detallespr = EvCartillaDrenado.objects.all().order_by("-fecha_hora_creacion")[:50]
		context106= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCartillaDrenado.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context106 = {"detallespr":detallespr, "id":id}

	lanzadopaletaspr=LPaletas.objects.filter(anexo_estado=1)
	context71={"lanzadopaletaspr":lanzadopaletaspr, "id":id}

	trabajadorpr=SelTrabajadorEvCalPodaAr.objects.all()
	context122={"trabajadorpr":trabajadorpr, "id":id}

	lanzadopaletaspr=LPaletas.objects.filter(anexo_estado=1)
	context130={"lanzadopaletaspr":lanzadopaletaspr, "id":id}

	if request.user.is_superuser or request.user.username=='oosorio':
		detallespr = EvCalPodaAr.objects.all().order_by("-fecha_hora_creacion")[:250]
		context123= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalPodaAr.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context123 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalMuestreoCosechaHg2021.objects.all().order_by("-fecha_hora_creacion")[:250]
		context134= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalMuestreoCosechaHg2021.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context134 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalMuestreoPlantaHgIca2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context142= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalMuestreoPlantaHgIca2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context142 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalBrixGrIca2021.objects.all().order_by("-fecha_hora_creacion")[:250]
		context144= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalBrixGrIca2021.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context144 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvCalMmppGrIca2021.objects.all().order_by("-fecha_hora_creacion")[:250]
		context147= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalMmppGrIca2021.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context147 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvCalControlDescarteGrIca2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context148= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalControlDescarteGrIca2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context148 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvCalControlPesosGrIca2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context149= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalControlPesosGrIca2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context149 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvPlantonesPlNaz2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context150 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvPlantonesPlNaz2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context150 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvMuestrasCajasEmpacadasGR2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context151 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvMuestrasCajasEmpacadasGR2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context151 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username=='cesteves':
		detallespr = EvControlDescarteGR2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context152 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvControlDescarteGR2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context152 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		ramaspr = EvFenRamasArandanos.objects.all().order_by("-fecha_hora_creacion")[:250]
		context158 = {"ramaspr":ramaspr, "id":id}
	else:
		ramaspr = EvFenRamasArandanos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context158 = {"ramaspr":ramaspr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalControlDescarteAr2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context159 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalControlDescarteAr2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context159 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser or request.user.username == 'lludena':
		detallespr = EvControlDescarteAr202202.objects.all().order_by("-fecha_hora_creacion")[:250]
		context160 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvControlDescarteAr202202.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context160 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCamarasHumedas.objects.all().order_by("-fecha_hora_creacion")[:250]
		context161 = {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCamarasHumedas.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context161 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalMuestreoPlantaHgNep202202.objects.all().order_by("-fecha_hora_creacion")[:250]
		context162= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalMuestreoPlantaHgNep202202.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context162 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalControlDescarteHg2022.objects.all().order_by("-fecha_hora_creacion")[:250]
		context163= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalControlDescarteHg2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context163 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvEficienciaSeleccionCalibrado.objects.all().order_by("-fecha_hora_creacion")[:250]
		context172= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvEficienciaSeleccionCalibrado.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context172 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvProductoTerminadoDespacho.objects.all().order_by("-fecha_hora_creacion")[:250]
		context174= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvProductoTerminadoDespacho.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context174 = {"detallespr":detallespr, "id":id}

	if (id==44):
		return render(request, 'athos/evfenarandanobrote.html', context44)
	else:
		if (id==47):
			return render(request, 'athos/evfenraicesarandanos.html', context47)
		else:
			if (id==55):
				return render(request, 'athos/ubicacionesevplantas.html', context55)
			else:
				if(id==56):
					return render(request, 'athos/evfenarandanobrotesem.html', context56)
				else:
					if(id==61):
						return render(request, 'athos/plagas/evsanplagasarandanos.html', context61)
					else:
						if(id==65):
							return render(request, 'athos/evfenfrutoarandanos.html', context65)
						else:
							if(id==66):
								return render(request, 'athos/planasa/evfenplanasa.html', context66)
							else:
								if(id==70):
									return render(request, 'athos/evaluaciones/calidad/evcaldefectoscampo.html', context70)
								else:
									if(id==71):
										return render(request, 'athos/evaluaciones/calidad/ubicacionevcalacopio.html', context71)
									else:
										if(id==106):
											return render(request, 'athos/evaluaciones/riego/evcartilladrenado.html', context106)
										else:
											if(id==122):
												return render(request, 'athos/evaluaciones/calidad/seltrabajadorevcalpodaar.html', context122)
											else:
												if(id==123):
													return render(request, 'athos/evaluaciones/calidad/evcalpodaar.html', context123)
												else:
													if(id==130):
														return render(request, 'athos/evaluaciones/calidad/ubicacionevcalacopioarica2021.html', context130)
													else:
														if(id==134):
															return render(request, 'athos/evaluaciones/calidad/evcalmuestreocosechahg2021.html', context134)
														else:
															if(id==142):
																return render(request, 'athos/evaluaciones/calidad/evcalmuestreoplantahgica2021.html', context142)
															else:
																if(id==144):
																	return render(request, 'athos/evaluaciones/calidad/evcalbrixgrica2021.html', context144)
																else:
																	if(id==147):
																		return render(request, 'athos/evaluaciones/calidad/evcalmmppgrica2021.html', context147)
																	else:
																		if(id==148):
																			return render(request, 'athos/evaluaciones/calidad/evcalcontroldescartegrica2022.html', context148)
																		else:
																			if(id==149):
																				return render(request, 'athos/evaluaciones/calidad/evcalcontrolpesosgrica2022.html', context149)
																			else:
																				if(id==150):
																					return render(request, 'athos/evaluaciones/calidad/evplantonesplnaz2022.html', context150)
																				else:
																					if(id==151):
																						return render(request, 'athos/evaluaciones/calidad/evcalmuestracajasempacadasgrica2022.html', context151)
																					else:
																						if(id==152 or id==164):
																							return render(request, 'athos/evaluaciones/calidad/evcontroldescartegr2022.html', context152)
																						else:
																							if(id==158):
																								return render(request, 'athos/evfenarandanoramas.html', context158)
																							else:
																								if(id==159):
																									return render(request, 'athos/evaluaciones/calidad/evcalcontroldescartear2022.html', context159)
																								else:
																									if(id==160):
																										return render(request, 'athos/evaluaciones/calidad/evcontroldescartear2022.html', context160)
																									else:
																										if(id==161):
																											return render(request, 'athos/evcamarashumedas2022.html', context161)
																										else:
																											if(id==162 or id==168):
																												return render(request, 'athos/evaluaciones/calidad/evcalmuestreoplantahgnep2022.html', context162)
																											else:
																												if(id==163 or id==169):
																													return render(request, 'athos/evaluaciones/calidad/evcalcontroldescartehghg2022.html', context163)
																												else:
																													if (id==166 or id==170):
																														return render(request, 'athos/ubicacionesevplantashg.html', context55)
																													else:
																														if(id==172):
																															return render(request, 'athos/evanalisiseficiencia2022.html', context172)
																														else:
																															if(id==174):
																																return render(request, 'athos/evproductoterminadodespacho2022.html', context174)

def crearevfenarandanobrote(request, id):

	form = evfenbrotesarandanosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanobrote.html', context)


def editarevfenarandanobrote(request, id, subid):
	sub_campo = get_object_or_404(EvFenBrotesArandanos, id=subid)
	form = evfenbrotesarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanobrote.html', context)


def detalleplantaevfenbrotesarandanos (request, id, subid):

	detalleplantapr=DetallePlantaEvFenBrotesArandanos.objects.filter(anexo_evaluacion_id=subid).order_by("-fecha_hora_creacion")
	context={"detalleplantapr":detalleplantapr, "id":id,"subid":subid}
	return render(request, 'athos/evbrotearandanodetalleplanta.html', context)


def creardetalleplantaevfenbrotesarandanos(request, id, subid):
	form = evfenbrotedetalleplantaform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenBrotesArandanos,id=subid)
			result.anexo_evaluacion = progravar
			result.save()
			print("is_valid2")

			return redirect('detalleplantaevfenbrotesarandanos',id,subid)
	print(context)
	return render(request, 'athos/nuevoevbrotedetallear.html', context)

def editardetalleplantaevfenbrotesarandanos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetallePlantaEvFenBrotesArandanos, id=varid)
	form = evfenbrotedetalleplantaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleplantaevfenbrotesarandanos', id, subid)
	return render(request, 'athos/nuevoevbrotedetallear.html', context)

def broteevfenar(request, id, subid,varid):
	brotepr = BrotePlantaEvFenBrotesArandanos.objects.filter(anexo_detalle_id=varid)
	context = {"brotepr":brotepr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/broteevfenar.html', context)


def crearbroteevfenar(request, id, subid,varid):
	form =  broteplantaevfenform(request.POST or None)
	
	context = {"form":form,"varid":varid}
	if request.method=='POST':
		
		
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(DetallePlantaEvFenBrotesArandanos,id=varid)
				result.anexo_detalle = progravar
				result.save()

				return redirect('broteevfenar', id, subid, varid)
		
	
	return render(request, 'athos/nuevobroteevfenar.html', context)

def editarbroteevfenar(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(BrotePlantaEvFenBrotesArandanos, id=varid)


	form = broteplantaevfenform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('broteevfenar', id, subid, catid)
	return render(request, 'athos/nuevobroteevfenar.html', context)


def crearevfenraicesarandanos(request, id):

	form = evfenraicesarandanosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenraicesarandanos.html', context)

def editarevfenraicesarandanos(request, id, subid):
	sub_campo = get_object_or_404(EvFenRaicesArandanos, id=subid)
	form = evfenraicesarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenraicesarandanos.html', context)


def detalleevfenraicesarandanos (request, id, subid):

	detallepr=DetalleEvFenRaicesArandanos.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/detalleevfenraicesarandanos.html', context)


def creardetalleevfenraicesarandanos(request, id, subid):
	form = detalleevfenraicesarandanosform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenRaicesArandanos,id=subid)
			result.anexo_detalle = progravar
			result.save()
			print("is_valid2")

			return redirect('detalleevfenraicesarandanos',id,subid)
	
	return render(request, 'athos/nuevodetalleevfenraicesarandanos.html', context)


def editardetalleevfenraicesarandanos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvFenRaicesArandanos, id=varid)
	form = detalleevfenraicesarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevfenraicesarandanos', id, subid)
	return render(request, 'athos/nuevodetalleevfenraicesarandanos.html', context)


def raicesevfenraicesarandanos(request, id, subid,varid):
	raicespr = RaicesEvFenRaicesArandanos.objects.filter(anexo_raices_id=varid)
	context = {"raicespr":raicespr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/raicesevfenraicesarandanos.html', context)


def crearraicesevfenraicesarandanos(request, id, subid,varid):
	form =  raicesevfenraicesarandanosform(request.POST or None)
	
	context = {"form":form,"varid":varid}
	if request.method=='POST':
		
		
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(DetalleEvFenRaicesArandanos,id=varid)
				result.anexo_raices = progravar
				result.save()

				return redirect('raicesevfenraicesarandanos', id, subid, varid)
		
	
	return render(request, 'athos/nuevoraicesevfenraicesarandanos.html', context)

def editarraicesevfenraicesarandanos(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(RaicesEvFenRaicesArandanos, id=varid)


	form = raicesevfenraicesarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('raicesevfenraicesarandanos', id, subid, catid)
	return render(request, 'athos/nuevoraicesevfenraicesarandanos.html', context)

def controlproductoterminado (request, id, subid):

	if request.user.is_superuser:
		controlpr=ControlProductoTerminado.objects.filter(anexo_lanzado_id=subid).order_by("-fecha_hora_creacion")
		context={"controlpr":controlpr, "id":id,"subid":subid}
	else:
		controlpr=ControlProductoTerminado.objects.filter(anexo_lanzado_id=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context={"controlpr":controlpr, "id":id,"subid":subid}


	context={"controlpr":controlpr, "id":id,"subid":subid}
	return render(request, 'athos/controlproductoterminado.html', context)

def controlproductoterminadohg (request, id, subid):
	if request.user.is_superuser:
		controlpr=ControlProductoTerminadoHg.objects.filter(anexo_lanzado_id=subid).order_by("-fecha_hora_creacion")
		context={"controlpr":controlpr, "id":id,"subid":subid}
	else:
		controlpr=ControlProductoTerminadoHg.objects.filter(anexo_lanzado_id=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context={"controlpr":controlpr, "id":id,"subid":subid}

	context={"controlpr":controlpr, "id":id,"subid":subid}
	return render(request, 'athos/controlproductoterminadohg.html', context)


def load_producto(request, id):
    producto = list(CentrosAthos.objects.get(id=id).AnexoCentroPresentacionesA.all().values('id','descripcion'))
    return JsonResponse(producto,safe=False)

def load_lineasempaque(request, id):
    lineas = list(CentrosAthos.objects.get(id=id).AnexoCentroLinea.all().values('id','descripcion'))
    return JsonResponse(lineas,safe=False)

def load_palets(request, palet):
    datos = list(InfoPaletGrIca2021.objects.filter(id=palet).values('id','anexo_guiad__fecha_cosecha','anexo_guiad__anexo_guia__anexo_fundo__nom_fundo','anexo_guiad__anexo_guia__NroGuia','anexo_guiad__anexo_ubi_mmpp__anexo_fundo__abreviatura','anexo_guiad__anexo_ubi_mmpp__anexo_modulo__nombremodulo','anexo_guiad__anexo_ubi_mmpp__anexo_lote__nom_lote','anexo_guiad__anexo_material__anexo_matmmpp__desc_material'))
    return JsonResponse(datos,safe=False)

def crearcontrolproductoterminado(request, id, subid):
	form = controlproductoterminadoform(request.POST or None)
	
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			print("is_valid2")

			return redirect('controlproductoterminado',id,subid)
	print(context)
	return render(request, 'athos/nuevocontrolproductoterminado.html', context)


def editarcontrolproductoterminado(request, id, subid,varid):
	sub_campo = get_object_or_404(ControlProductoTerminado, id=varid)
	form = controlproductoterminadoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('controlproductoterminado', id, subid)
	return render(request, 'athos/nuevocontrolproductoterminado.html', context)


def detallecontrolproductoterminado(request, id, subid,varid):
	detallepr = DetalleControlProductoTerminado.objects.filter(anexo_detalle_id=varid)
	context = {"detallepr":detallepr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/detallecpterminado.html', context)


def creardetallecontrolproductoterminado(request, id, subid,varid):
	idcontrolproducto=varid
	VariableCliente=ControlProductoTerminado.objects.get(id=idcontrolproducto).anexo_centro
	
	VariableVariedad=LPaletas.objects.get(id=subid).anexo_cultivo
	
	form =  detallecontrolproductoterminadoform(request.POST or None, variable_cliente=VariableCliente,variable_variedad=VariableVariedad)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(ControlProductoTerminado,id=varid)
				result.anexo_detalle = progravar
				result.save()
				return redirect('detallecontrolproductoterminado', id, subid,varid)
	return render(request, 'athos/nuevodetallecpterminado.html', context)

def editardetallecontrolproductoterminado(request, id, subid,varid,catid):
	idcontrolproducto=catid
	VariableCliente=ControlProductoTerminado.objects.get(id=idcontrolproducto).anexo_centro
	VariableVariedad=LPaletas.objects.get(id=subid).anexo_cultivo

	sub_campo = get_object_or_404(DetalleControlProductoTerminado, id=varid)
	form = detallecontrolproductoterminadoform(request.POST or None, instance=sub_campo,variable_cliente=VariableCliente,variable_variedad=VariableVariedad)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detallecontrolproductoterminado', id, subid,catid)
	return render(request, 'athos/nuevodetallecpterminado.html', context)





def crearevfenarandanobrotesem(request, id):

	form = evfenbrotesarandanossemform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanobrotesem.html', context)


def editarevfenarandanobrotesem(request, id, subid):
	sub_campo = get_object_or_404(EvFenBrotesArandanosSem, id=subid)
	form = evfenbrotesarandanossemform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanobrotesem.html', context)


def detalleplantaevfenbrotesarandanossem(request, id, subid):

	detalleplantapr=DetallePlantaEvFenBrotesArandanosSem.objects.filter(anexo_evaluacion_id=subid).order_by("-fecha_hora_creacion")
	context={"detalleplantapr":detalleplantapr, "id":id,"subid":subid}
	return render(request, 'athos/evbrotearandanodetalleplantasem.html', context)


def creardetalleplantaevfenbrotesarandanossem(request, id, subid):
	form = evfenbrotedetalleplantasemform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenBrotesArandanosSem,id=subid)
			result.anexo_evaluacion = progravar
			result.save()
			print("is_valid2")

			return redirect('detalleplantaevfenbrotesarandanossem',id,subid)
	print(context)
	return render(request, 'athos/nuevoevbrotedetallearsem.html', context)


def editardetalleplantaevfenbrotesarandanossem(request, id, subid,varid):
	sub_campo = get_object_or_404(DetallePlantaEvFenBrotesArandanosSem, id=varid)
	form = evfenbrotedetalleplantasemform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleplantaevfenbrotesarandanossem', id, subid)
	return render(request, 'athos/nuevoevbrotedetallearsem.html', context)




def broteevfenarsem(request, id, subid,varid):
	brotepr = BrotePlantaEvFenBrotesArandanosSem.objects.filter(anexo_detalle_id=varid)
	context = {"brotepr":brotepr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/broteevfenarsem.html', context)


def crearbroteevfenarsem(request, id, subid,varid):
	form =  broteplantaevfensemform(request.POST or None)
	
	context = {"form":form,"varid":varid}
	if request.method=='POST':
		
		
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(DetallePlantaEvFenBrotesArandanosSem,id=varid)
				result.anexo_detalle = progravar
				result.save()

				return redirect('broteevfenarsem', id, subid, varid)
		
	
	return render(request, 'athos/nuevobroteevfenarsem.html', context)

def editarbroteevfenarsem(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(BrotePlantaEvFenBrotesArandanosSem, id=varid)


	form = broteplantaevfensemform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('broteevfenarsem', id, subid, catid)
	return render(request, 'athos/nuevobroteevfenarsem.html', context)



def crearevsanplagasarandanos(request, id):

	form = evsanplagasarandanosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/plagas/nuevoevsanplagasarandanos.html', context)

def editarevsanplagasarandanos(request, id, subid):
	sub_campo = get_object_or_404(EvSanPlagasArandanos, id=subid)
	form = evsanplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/plagas/nuevoevsanplagasarandanos.html', context)


def gruposplagasarandanos (request, id, subid):

	grupospr=GruposPlagasArandanos.objects.all()
	context={"grupospr":grupospr, "id":id,"subid":subid}
	return render(request, 'athos/plagas/gruposplagas.html', context)


def creargruposplagasarandanos(request, id, subid):
	form = gruposplagasarandanosform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvSanPlagasArandanos,id=subid)
			result.anexo_evaluacion = progravar
			result.save()
			print("is_valid2")

			return redirect('gruposplagasarandanos',id,subid)
	
	return render(request, 'athos/plagas/nuevogruposplagas.html', context)


def editargruposplagasarandanos(request, id, subid,varid):
	sub_campo = get_object_or_404(GruposPlagasArandanos, id=varid)
	form = gruposplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('gruposplagasarandanos', id, subid)
	return render(request, 'athos/plagas/nuevogruposplagas.html', context)


def subgruposplagasarandanos(request, id, subid,varid):
	subgrupospr = SubGruposPlagasArandanos.objects.filter(anexo_sub_id=varid)
	context = {"subgrupospr":subgrupospr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/plagas/subgruposplagas.html', context)


def crearsubgruposplagasarandanos(request, id, subid,varid):
	form =  subgruposplagasarandanosform(request.POST or None)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GruposPlagasArandanos,id=varid)
			result.anexo_sub = progravar
			result.save()
			return redirect('subgruposplagasarandanos', id, subid, varid)
	return render(request, 'athos/plagas/nuevosubgruposplagas.html', context)

def editarsubgruposplagasarandanos(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(SubGruposPlagasArandanos, id=varid)

	form = subgruposplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('subgruposplagasarandanos', id, subid, catid)
	return render(request, 'athos/plagas/nuevosubgruposplagas.html', context)



def variablesplagasarandanos(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/acarohialino.html', context)


def crearvariablesplagasarandanos(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('variablesplagasarandanos', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoacarohialino.html', context)

def editarvariablesplagasarandanos(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('variablesplagasarandanos', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoacarohialino.html', context)



def aranaroja(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/aranaroja.html', context)

def creararanaroja(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('aranaroja', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoaranaroja.html', context)


def editararanaroja(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('aranaroja', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoaranaroja.html', context)


def argy(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/argy.html', context)

def crearargy(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('argy', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoargy.html', context)

def editarargy(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('argy', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoargy.html', context)


def cigarrita(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/cigarrita.html', context)

def crearcigarrita(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('cigarrita', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocigarrita.html', context)

def editarcigarrita(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cigarrita', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocigarrita.html', context)


def cochinilla(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/cochinilla.html', context)

def crearcochinilla(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('cochinilla', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocochinilla.html', context)

def editarcochinilla(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cochinilla', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocochinilla.html', context)



def crypto(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/crypto.html', context)


def crearcrypto(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('crypto', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocrypto.html', context)

def editarcrypto(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('crypto', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocrypto.html', context)


def diabro(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/diabro.html', context)


def creardiabro(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('diabro', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevodiabro.html', context)

def editardiabro(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('diabro', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevodiabro.html', context)




def gryllus(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/gryllus.html', context)


def creargryllus(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('gryllus', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevogryllus.html', context)

def editargryllus(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('gryllus', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevogryllus.html', context)


def helio(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/helio.html', context)


def crearhelio(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('helio', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevohelio.html', context)

def editarhelio(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('helio', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevohelio.html', context)


def membracidos(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/membracidos.html', context)

def crearmembracidos(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('membracidos', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevomembracidos.html', context)


def editarmembracidos(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('membracidos', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevomembracidos.html', context)


def moscablanca(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/moscablanca.html', context)

def crearmoscablanca(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('moscablanca', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevomoscablanca.html', context)


def editarmoscablanca(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('moscablanca', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevomoscablanca.html', context)


def moscafruta(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/moscafruta.html', context)

def crearmoscafruta(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('moscafruta', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevomoscafruta.html', context)


def editarmoscafruta(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('moscafruta', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevomoscafruta.html', context)


def plecto(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/plecto.html', context)

def crearplecto(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('plecto', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoplecto.html', context)


def editarplecto(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('plecto', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoplecto.html', context)

def procospidos(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/procospidos.html', context)

def crearprocospidos(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('procospidos', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoprocospidos.html', context)


def editarprocospidos(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('procospidos', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoprocospidos.html', context)


def pulgones(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/pulgones.html', context)

def crearpulgones(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('pulgones', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevopulgones.html', context)


def editarpulgones(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('pulgones', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevopulgones.html', context)

def queresas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/queresas.html', context)

def crearqueresas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('queresas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoqueresas.html', context)


def editarqueresas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('queresas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoqueresas.html', context)

def spodo(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/spodo.html', context)

def crearspodo(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('spodo', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevospodo.html', context)


def editarspodo(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('spodo', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevospodo.html', context)


def trips(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/trips.html', context)

def creartrips(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('trips', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevotrips.html', context)


def editartrips(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('trips', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevotrips.html', context)


def aranas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/aranas.html', context)

def creararanas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('aranas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoaranas.html', context)


def editararanas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('aranas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoaranas.html', context)

def cocci(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/cocci.html', context)

def crearcocci(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('cocci', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevococci.html', context)


def editarcocci(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cocci', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevococci.html', context)


def crisopas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/crisopas.html', context)

def crearcrisopas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('crisopas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocrisopas.html', context)


def editarcrisopas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('crisopas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocrisopas.html', context)



def crisopas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/crisopas.html', context)

def crearcrisopas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('crisopas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocrisopas.html', context)


def editarcrisopas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('crisopas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocrisopas.html', context)



def cryptola(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/cryptola.html', context)

def crearcryptola(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('cryptola', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevocryptola.html', context)


def editarcryptola(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cryptola', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevocryptola.html', context)


def otro(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/otro.html', context)

def crearotro(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('otro', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevootro.html', context)


def editarotro(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('otro', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevootro.html', context)

def alternaria(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/alternaria.html', context)

def crearalternaria(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('alternaria', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoalternaria.html', context)


def editaralternaria(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('alternaria', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoalternaria.html', context)

def antra(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/antra.html', context)

def crearantra(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('antra', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoantra.html', context)


def editarantra(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('antra', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoantra.html', context)

def botri(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/botri.html', context)

def crearbotri(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('botri', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevobotri.html', context)


def editarbotri(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('botri', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevobotri.html', context)


def lasio(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/lasio.html', context)

def crearlasio(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('lasio', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevolasio.html', context)


def editarlasio(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('lasio', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevolasio.html', context)


def pestalo(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/pestalo.html', context)

def crearpestalo(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('pestalo', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevopestalo.html', context)


def editarpestalo(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('pestalo', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevopestalo.html', context)


def phyto(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/phyto.html', context)

def crearphyto(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('phyto', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevophyto.html', context)


def editarphyto(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('phyto', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevophyto.html', context)


def plantaquemada(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/plantaquemada.html', context)

def crearplantaquemada(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('plantaquemada', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoplantaquemada.html', context)


def editarplantaquemada(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('plantaquemada', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoplantaquemada.html', context)


def roya(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/roya.html', context)

def crearroya(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('roya', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoroya.html', context)


def editarroya(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('roya', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoroya.html', context)


def hojasanchas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/hojasanchas.html', context)

def crearhojasanchas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('hojasanchas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevohojasanchas.html', context)


def editarhojasanchas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('hojasanchas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevohojasanchas.html', context)


def hojasangostas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/hojasangostas.html', context)

def crearhojasangostas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('hojasangostas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevohojasangostas.html', context)


def editarhojasangostas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('hojasangostas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevohojasangostas.html', context)



def abejas(request, id, subid,varid, nicoid):

	if request.user.is_superuser:
		variablespr = VariablesPlagasArandanos.objects.filter(valor=subid).order_by("-fecha_hora_creacion")
		
	else:
		variablespr =VariablesPlagasArandanos.objects.filter(valor=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	

	context = {"variablespr":variablespr, "id":id, "subid":subid,"varid":varid,"nicoid":nicoid}
	print(context)
	return render(request, 'athos/plagas/abejas.html', context)

def crearabejas(request, id, subid,varid,nicoid):
	form =  variablesplagasarandanosform(request.POST or None)
	context = {"form":form,"id":id,"subid":subid,"varid":varid,"nicoid":nicoid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SubGruposPlagasArandanos,id=varid)
			result.anexo_var = progravar
			var= subid
			result.valor = var
			
			result.save()
			return redirect('abejas', id, subid, varid, nicoid)
	return render(request, 'athos/plagas/nuevoabejas.html', context)


def editarabejas(request, id, subid,varid,nicoid,chelitaid):
	sub_campo = get_object_or_404(VariablesPlagasArandanos, id=chelitaid)

	form = variablesplagasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('abejas', id, subid, varid,nicoid)
	return render(request, 'athos/plagas/nuevoabejas.html', context)


def crearevfenfrutoarandanos(request, id):

	form = evfenfrutoarandanosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenfrutoarandanos.html', context)


def editarevfenfrutoarandanos(request, id, subid):
	sub_campo = get_object_or_404(EvFenFrutoArandanos, id=subid)
	form = evfenfrutoarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenfrutoarandanos.html', context)

def detalleevfenfrutoarandanos(request, id, subid):

	detalleplantapr=DetalleEvFenFrutoArandanos.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detalleplantapr":detalleplantapr, "id":id,"subid":subid}
	return render(request, 'athos/detalleevfenfrutoarandanos.html', context)


def creardetalleevfenfrutoarandanos(request, id, subid):
	form = detalleevfenfrutoarandanosform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenFrutoArandanos,id=subid)
			result.anexo_detalle= progravar
			result.save()
			print("is_valid2")

			return redirect('detalleevfenfrutoarandanos',id,subid)
	print(context)
	return render(request, 'athos/nuevodetalleevfenfrutoarandanos.html', context)


def editardetalleevfenfrutoarandanos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvFenFrutoArandanos, id=varid)
	form = detalleevfenfrutoarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevfenfrutoarandanos', id, subid)
	return render(request, 'athos/nuevodetalleevfenfrutoarandanos.html', context)


def crearevfenplanasa(request, id):

	form = evfenplanasaform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/planasa/nuevoevfenplanasa.html', context)

def editarevfenplanasa(request, id, subid):
	sub_campo = get_object_or_404(EvFenPlanasa, id=subid)
	form = evfenplanasaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/planasa/nuevoevfenplanasa.html', context)

def detalleevfenplanasa (request, id, subid):

	detallepr=DetalleEvFenPlanasa.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/planasa/detalleevfenplanasa.html', context)


def creardetalleevfenplanasa(request, id, subid):
	form = detalleevfenplanasaform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenPlanasa,id=subid)
			result.anexo_detalle = progravar
			result.save()
			print("is_valid2")
			return redirect('detalleevfenplanasa',id,subid)
	return render(request, 'athos/planasa/nuevodetalleevfenplanasa.html', context)


def editardetalleevfenplanasa(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvFenPlanasa, id=varid)
	form = detalleevfenplanasaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevfenplanasa', id, subid)
	return render(request, 'athos/planasa/nuevodetalleevfenplanasa.html', context)

def crearevcaldefectoscampo(request, id):

	form = evcaldefectoscampoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcaldefectoscampo.html', context)


def editarevcaldefectoscampo(request, id, subid):
	sub_campo = get_object_or_404(EvCalDefectosCampo, id=subid)
	form = evcaldefectoscampoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcaldefectoscampo.html', context)


def detalleevcaldefectoscampo (request, id, subid):

	detallepr=DetalleEvCalDefectosCampo.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcaldefectoscampo.html', context)


def creardetalleevcaldefectoscampo(request, id, subid):
	idfundos=subid
	VariableFundo=EvCalDefectosCampo.objects.get(id=idfundos).anexo_fundo

	form = detalleevcaldefectoscampoform(request.POST or None, variable_fundo=VariableFundo)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalDefectosCampo,id=subid)
			result.anexo_detalle = progravar
			result.save()
			print("is_valid2")

			return redirect('detalleevcaldefectoscampo',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcaldefectoscampo.html', context)


def editardetalleevcaldefectoscampo(request, id, subid,varid):
	idfundos=subid
	VariableFundo=EvCalDefectosCampo.objects.get(id=idfundos).anexo_fundo
	sub_campo = get_object_or_404(DetalleEvCalDefectosCampo, id=varid)
	form = detalleevcaldefectoscampoform(request.POST or None, variable_fundo=VariableFundo,instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevcaldefectoscampo', id, subid)
	return render(request, 'athos/evaluaciones/calidad/editardetalleevcaldefectoscampo.html', context)


def evcalacopioplanta(request, id, subid):

	if request.user.is_superuser:
		acopiopr=EvCalAcopioPlantaArCaraz202202.objects.filter(anexo_lanzado_id=subid).order_by("-fecha_hora_creacion")
		context={"acopiopr":acopiopr, "id":id,"subid":subid}
	else:
		acopiopr=EvCalAcopioPlantaArCaraz202202.objects.filter(anexo_lanzado_id=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context={"acopiopr":acopiopr, "id":id,"subid":subid}

	return render(request, 'athos/evaluaciones/calidad/evcalacopioplanta.html', context)

def crearevcalacopioplanta(request, id, subid):
	form = evcalacopioplantaform(request.POST or None)
	
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			print("is_valid2")

			return redirect('evcalacopioplanta',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalacopioplanta.html', context)


def editarevcalacopioplanta(request, id, subid,varid):
	sub_campo = get_object_or_404(EvCalAcopioPlantaArCaraz202202, id=varid)
	form = evcalacopioplantaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evcalacopioplanta', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalacopioplanta.html', context)


#ICA EV CAL ACOPIO PLANTA
def evcalacopioplantaarica2021(request, id, subid):

	if request.user.is_superuser:
		acopiopr=EvCalAcopioPlantaArIca202202.objects.filter(anexo_lanzado_id=subid).order_by("-fecha_hora_creacion")
		context={"acopiopr":acopiopr, "id":id,"subid":subid}
	else:
		acopiopr=EvCalAcopioPlantaArIca202202.objects.filter(anexo_lanzado_id=subid,usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context={"acopiopr":acopiopr, "id":id,"subid":subid}

	return render(request, 'athos/evaluaciones/calidad/evcalacopioplantaarica2021.html', context)

def crearevcalacopioplantaarica2021(request, id, subid):
	form = evcalacopioplantaarica2021form(request.POST or None)
	
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			print("is_valid2")

			return redirect('evcalacopioplantaarica2021',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalacopioplantaarica2021.html', context)


def editarevcalacopioplantaarica2021(request, id, subid,varid):
	sub_campo = get_object_or_404(EvCalAcopioPlantaArIca202202, id=varid)
	form = evcalacopioplantaarica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evcalacopioplantaarica2021', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalacopioplantaarica2021.html', context)









def crearevcartilladrenado(request, id):

	form = evcartilladrenadoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/riego/nuevoevcartilladrenado.html', context)


def editarevcartilladrenado(request, id, subid):
	sub_campo = get_object_or_404(EvCartillaDrenado, id=subid)
	form = evcartilladrenadoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/riego/editarevcartilladrenado.html', context)


def detalleevcartilladrenado (request, id, subid):

	detallepr=DetalleEvCartillaDrenado.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/riego/detalleevcartilladrenado.html', context)

def creardetalleevcartilladrenado(request, id, subid):
	
	form = detalleevcartilladrenadoform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCartillaDrenado,id=subid)
			result.anexo_detalle = progravar
			result.save()
			print("is_valid2")

			return redirect('detalleevcartilladrenado',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/riego/nuevodetalleevcartilladrenado.html', context)


def editardetalleevcartilladrenado(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCartillaDrenado, id=varid)
	form = detalleevcartilladrenadoform(request.POST or None,instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevcartilladrenado', id, subid)
	return render(request, 'athos/evaluaciones/riego/nuevodetalleevcartilladrenado.html', context)


def crearseltrabajadorevcalpodaar(request, id):

	form = seltrabajadorevcalpodaarform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoseltrabajadorevcalpodaar.html', context)


def editarseltrabajadorevcalpodaar(request, id, subid):
	sub_campo = get_object_or_404(SelTrabajadorEvCalPodaAr, id=subid)
	form = seltrabajadorevcalpodaarform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoseltrabajadorevcalpodaar.html', context)



def crearevcalpodaar(request, id):

	form = evcalpodaarform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalpodaar.html', context)


def editarevcalpodaar(request, id, subid):
	sub_campo = get_object_or_404(EvCalPodaAr, id=subid)
	form = evcalpodaarform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalpodaar.html', context)



def detalleevcalpodaar (request, id, subid):

	detallepr=DetalleEvCalPodaAr.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalpodaar.html', context)


def creardetalleevcalpodaar(request, id, subid):
	variablefundo=EvCalPodaAr.objects.get(id=subid).anexo_fundo
	


	form = detalleevcalpodaarform(request.POST or None, variable_fundo=variablefundo)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalPodaAr,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('evaluaciones:detalleevcalpodaar',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalpodaar.html', context)


def editardetalleevcalpodaar(request, id, subid,varid):
	variablefundo=EvCalPodaAr.objects.get(id=subid).anexo_fundo
	sub_campo = get_object_or_404(DetalleEvCalPodaAr, id=varid)
	form = detalleevcalpodaarform(request.POST or None, variable_fundo=variablefundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones:detalleevcalpodaar', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalpodaar.html', context)



def crearevcalmuestreocosechahg2021(request, id):

	form = evcalmuestreocosechahg2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalmuestreocosechahg2021.html', context)


def editarevcalmuestreocosechahg2021(request, id, subid):
	sub_campo = get_object_or_404(EvCalMuestreoCosechaHg2021, id=subid)
	form = evcalmuestreocosechahg2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalmuestreocosechahg2021.html', context)



def detalleevcalmuestreocosechahg2021 (request, id, subid):

	detallepr=DetalleEvCalMuestreoCosechaHg2021.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalmuestreocosechahg2021.html', context)


def creardetalleevcalmuestreocosechahg2021(request, id, subid):
	variablefundo=EvCalMuestreoCosechaHg2021.objects.get(id=subid).anexo_fundo
	variableturno=EvCalMuestreoCosechaHg2021.objects.get(id=subid).ubicacion
	form = detalleevcalmuestreocosechahg2021form(request.POST or None,variable_fundo=variablefundo,variable_turno=variableturno)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalMuestreoCosechaHg2021,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalmuestreocosechahg2021',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestreocosechahg2021.html', context)


def editardetalleevcalmuestreocosechahg2021(request, id, subid,varid):
	variablefundo=EvCalMuestreoCosechaHg2021.objects.get(id=subid).anexo_fundo
	variableturno=EvCalMuestreoCosechaHg2021.objects.get(id=subid).ubicacion
	sub_campo = get_object_or_404(DetalleEvCalMuestreoCosechaHg2021,id=varid)
	form = detalleevcalmuestreocosechahg2021form(request.POST or None, variable_fundo=variablefundo,variable_turno=variableturno, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalmuestreocosechahg2021', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestreocosechahg2021.html', context)


def crearevcalmuestreoplantahgica2021(request, id):
	form = evcalmuestreoplantahgica2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalmuestreoplantahgica2021.html', context)


def editarevcalmuestreoplantahgica2021(request, id, subid):
	sub_campo = get_object_or_404(EvCalMuestreoPlantaHgIca2022, id=subid)
	form = evcalmuestreoplantahgica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalmuestreoplantahgica2021.html', context)

def crearevcalmuestreoplantahgnep2022(request, id):
	form = evcalmuestreoplantahgnep2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalmuestreoplantahgnep2022.html', context)

def editarevcalmuestreoplantahgnep2022(request, id, subid):
	sub_campo = get_object_or_404(EvCalMuestreoPlantaHgNep202202, id=subid)
	form = evcalmuestreoplantahgnep2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalmuestreoplantahgnep2022.html', context)

def detalleevcalmuestreoplantahgica2021 (request, id, subid):

	detallepr=DetalleEvCalMuestreoPlantaHgIca2021.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalmuestreoplantahgica2021.html', context)


def creardetalleevcalmuestreoplantahgica2021(request, id, subid):
	
	form = detalleevcalmuestreoplantahgica2021form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalMuestreoPlantaHgIca2021,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalmuestreoplantahgica2021',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestreoplantahgica2021.html', context)


def editardetalleevcalmuestreoplantahgica2021(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCalMuestreoPlantaHgIca2021,id=varid)
	form = detalleevcalmuestreoplantahgica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalmuestreoplantahgica2021', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestreoplantahgica2021.html', context)



def crearevcalbrixgrica2021(request, id):

	form = evcalbrixgrica2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalbrixgrica2021.html', context)


def editarevcalbrixgrica2021(request, id, subid):
	sub_campo = get_object_or_404(EvCalBrixGrIca2021, id=subid)
	form = evcalbrixgrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalbrixgrica2021.html', context)


def detalleevcalbrixgrica2021 (request, id, subid):

	detallepr=DetalleEvCalBrixGrIca2021.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalbrixgrica2021.html', context)


def creardetalleevcalbrixgrica2021(request, id, subid):
	
	form = detalleevcalbrixgrica2021form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalBrixGrIca2021,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalbrixgrica2021',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalbrixgrica2021.html', context)


def editardetalleevcalbrixgrica2021(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCalBrixGrIca2021,id=varid)
	form = detalleevcalbrixgrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalbrixgrica2021', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalbrixgrica2021.html', context)


def crearevcalmmppgrica2021(request, id):

	form = evcalmmppgrica2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalmmppgrica2021.html', context)


def editarevcalmmppgrica2021(request, id, subid):
	sub_campo = get_object_or_404(EvCalMmppGrIca2021, id=subid)
	form = evcalmmppgrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalmmppgrica2021.html', context)


def detalleevcalmmppgrica2021 (request, id, subid):

	detallepr=DetalleEvCalMmppGrIca2021.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalmmppgrica2021.html', context)


def creardetalleevcalmmppgrica2021(request, id, subid):
	
	form = detalleevcalmmppgrica2021form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalMmppGrIca2021,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalmmppgrica2021',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmmppgrica2021.html', context)


def editardetalleevcalmmppgrica2021(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCalMmppGrIca2021,id=varid)
	form = detalleevcalmmppgrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalmmppgrica2021', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmmppgrica2021.html', context)


def crearevcalcontroldescartegrica2022(request, id):

	form = evcalcontroldescartegrica2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalcontroldescartegrica2022.html', context)


def editarevcalcontroldescartegrica2022(request, id, subid):
	sub_campo = get_object_or_404(EvCalControlDescarteGrIca2022, id=subid)
	form = evcalcontroldescartegrica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalcontroldescartegrica2022.html', context)


def detalleevcalcontroldescartegrica2022 (request, id, subid):

	detallepr=DetalleEvCalControlDescarteGrIca2022.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalcontroldescartegrica2022.html', context)


def creardetalleevcalcontroldescartegrica2022(request, id, subid):
	
	form = detalleevcalcontroldescartegrica2022form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalControlDescarteGrIca2022,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcontroldescartegrica2022',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartegrica2022.html', context)


def editardetalleevcalcontroldescartegrica2022(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCalControlDescarteGrIca2022,id=varid)
	form = detalleevcalcontroldescartegrica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcontroldescartegrica2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartegrica2022.html', context)


#VISTA EV CAL DESCARTE ARANDANO
def crearevcalcontroldescartearica2022(request, id):
	form = evcalcontroldescartearica2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalcontroldescartearica2022.html', context)

def editarevcalcontroldescartearica2022(request, id, subid):
	sub_campo = get_object_or_404(EvCalControlDescarteAr2022, id=subid)
	form = evcalcontroldescartearica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalcontroldescartearica2022.html', context)

def detalleevcalcontroldescartearica2022 (request, id, subid):
	detallepr=DetalleEvCalControlDescarteAr2022.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalcontroldescartearica2022.html', context)

def creardetalleevcalcontroldescartearica2022(request, id, subid):
	form = detalleevcalcontroldescartearica2022form(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalControlDescarteAr2022,id=subid)
			result.anexo_detalle = progravar
			result.save()
			return redirect('detalleevcalcontroldescartearica2022',id,subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartearica2022.html', context)

def editardetalleevcalcontroldescartearica2022(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalControlDescarteAr2022,id=varid)
	form = detalleevcalcontroldescartearica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcontroldescartearica2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartearica2022.html', context)

#VISTA EV CONTROL DESCARTE ARANDANO
def crearevcontroldescartear2022(request, id):
	form = evcontroldescartear2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcontroldescartear2022.html', context)

def editarevcontroldescartear2022(request, id, subid):
	sub_campo = get_object_or_404(EvControlDescarteAr202202, id=subid)
	form = evcontroldescartear2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcontroldescartear2022.html', context)

def detalleevcontroldescartear2022 (request, id, subid):
	detallepr=DetalleEvControlDescarteAr202202.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcontroldescartear2022.html', context)

def creardetalleevcontroldescartear2022(request, id, subid):
	form = detalleevcontroldescartear2022form(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvControlDescarteAr202202,id=subid)
			result.anexo_detalle = progravar
			result.save()
			return redirect('detalleevcontroldescartear2022',id,subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcontroldescartear2022.html', context)

def editardetalleevcontroldescartear2022(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvControlDescarteAr202202,id=varid)
	form = detalleevcontroldescartear2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcontroldescartear2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/editardetalleevcontroldescartear2022.html', context)









def crearevcalcontrolpesosgrica2022(request, id):

	form = evcalcontrolpesosgrica2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalcontrolpesosgrica2022.html', context)


def editarevcalcontrolpesosgrica2022(request, id, subid):
	sub_campo = get_object_or_404(EvCalControlPesosGrIca2022, id=subid)
	form = evcalcontrolpesosgrica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalcontrolpesosgrica2022.html', context)


def detalleevcalcontrolpesosgrica2022 (request, id, subid):

	detallepr=DetalleEvCalControlPesosGrIca2022.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalcontrolpesosgrica2022.html', context)


def creardetalleevcalcontrolpesosgrica2022(request, id, subid):
	
	form = detalleevcalcontrolpesosgrica2022form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalControlPesosGrIca2022,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcontrolpesosgrica2022',id,subid)
	print(context)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontrolpesosgrica2022.html', context)


def editardetalleevcalcontrolpesosgrica2022(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleEvCalControlPesosGrIca2022,id=varid)
	form = detalleevcalcontrolpesosgrica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcontrolpesosgrica2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontrolpesosgrica2022.html', context)	


#VISTA PLANTONES
def crearevplantonesplnaz2022(request, id):

	form = evplantonesplnaz2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevplatonesplnaz2022.html', context)

def editarevplantonesplnaz2022(request, id, subid):
	sub_campo = get_object_or_404(EvPlantonesPlNaz2022, id=subid)
	form = evplantonesplnaz2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevplantonesplnaz2022.html', context)

def detalleevplantonesplnaz2022 (request, id, subid):

	detallepr=DetalleEvPlantonesPlNaz2022.objects.filter(anexo_detalle=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevplantonesplnaz2022.html', context)


#VISTA DETALLE PLANTONES
def creardetalleevplantonesplnaz2022(request, id, subid):
    
	form = detalleevplantonesplnaz2022form(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvPlantonesPlNaz2022,id=subid)
			result.anexo_detalle = progravar
			result.save()

			return redirect('detalleevplantonesplnaz2022',id,subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevplantonesplnaz2022.html', context)


def editardetalleevplantonesplnaz2022(request, id, subid,varid):
    
	sub_campo = get_object_or_404(DetalleEvPlantonesPlNaz2022,id=varid)
	form = detalleevplantonesplnaz2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevplantonesplnaz2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevplantonesplnaz2022.html', context)

#CARTILLA EV MUESTRAS CAJAS EMPACADAS GRICA2022
#VISTA CAJAS EMPACADAS GR
def crearevcalmuestracajasempacadasgrica2022(request, id):

	form = evcalmuestracajasempacadasgr2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalmuestracajasempacadasgrica2022.html', context)

def editarevcalmuestracajasempacadasgrica2022(request, id, subid):
	sub_campo = get_object_or_404(EvMuestrasCajasEmpacadasGR2022, id=subid)
	form = evcalmuestracajasempacadasgr2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalmuestracajasempacadasgrica2022.html', context)

def detalleevcalmuestracajasempacadasgrica2022(request, id, subid):

	detallepr=DetalleEvMuestrasCajasEmpacadasGR2022.objects.filter(anexo_detalle=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalmuestracajasempacadasgrica2022.html', context)

#VISTA DETALLE CAJAS EMPACADAS GR
def creardetalleevcalmuestracajasempacadasgrica2022(request, id, subid):
    
	idCategorias=subid
	variableCategoria=EvMuestrasCajasEmpacadasGR2022.objects.get(id=idCategorias).anexo_categoria
	form = detalleevcalmuestracajasempacadasgr2022form(request.POST or None, variable_categoria=variableCategoria)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvMuestrasCajasEmpacadasGR2022,id=subid)
			result.anexo_detalle = progravar
			result.save()

			return redirect('detalleevcalmuestracajasempacadasgrica2022',id,subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestracajasempacadasgrica2022.html', context)


def editardetalleevcalmuestracajasempacadasgrica2022(request, id, subid,varid):
    
	idCategorias=subid
	variableCategoria=EvMuestrasCajasEmpacadasGR2022.objects.get(id=idCategorias).anexo_categoria
	sub_campo = get_object_or_404(DetalleEvPlantonesPlNaz2022,id=varid)
	form = detalleevcalmuestracajasempacadasgr2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalmuestracajasempacadasgrica2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalmuestracajasempacadasgrica20222.html', context)

#MODULO EV CONTROL DESCARTE GRICA2022
#VISTA CONTROL DESCARTE GR
def crearevcontroldescartegrica2022(request, id):
	form = evcontroldescartegr2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcontroldescartegrica2022.html', context)

def editarevcontroldescartegrica2022(request, id, subid):
	sub_campo = get_object_or_404(EvControlDescarteGR2022, id=subid)
	form = evcontroldescartegr2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcontroldescartegrica2022.html', context)

#VISTA EV RAMAS ARANDANOS
def crearevfenarandanoramas(request, id):
	form = evfenramasarandanosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanoramas.html', context)

def editarevfenarandanoramas(request, id, subid):
	sub_campo = get_object_or_404(EvFenRamasArandanos, id=subid)
	form = evfenramasarandanosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevfenarandanoramas.html', context)

def detalleplantaevfenramasarandanos(request, id, subid):
	detalleplantapr=DetallePlantaEvFenRamasArandanos.objects.filter(anexo_evaluacion_id=subid).order_by("-fecha_hora_creacion")
	context={"detalleplantapr":detalleplantapr, "id":id,"subid":subid}
	return render(request, 'athos/evramasarandanodetalleplanta.html', context)

def creardetalleplantaevfenramasarandanos(request, id, subid):
	form = evfenramasdetalleplantaform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvFenRamasArandanos,id=subid)
			result.anexo_evaluacion = progravar
			result.save()
			return redirect('detalleplantaevfenramasarandanos',id,subid)
	return render(request, 'athos/nuevoevramasdetallear.html', context)

def editardetalleplantaevfenramasarandanos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetallePlantaEvFenRamasArandanos, id=varid)
	form = evfenramasdetalleplantaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleplantaevfenramasarandanos', id, subid)
	return render(request, 'athos/nuevoevramasdetallear.html', context)

def ramasevfenar(request, id, subid,varid):
	ramaspr = RamaPlantaEvFenRamasArandanos.objects.filter(anexo_detalle_id=varid)
	context = {"ramaspr":ramaspr, "id":id, "subid":subid,"varid":varid}
	return render(request, 'athos/ramasevfenar.html', context)

def crearramasevfenar(request, id, subid,varid):
	form = ramaplantaevfenform(request.POST or None)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(DetallePlantaEvFenRamasArandanos,id=varid)
				result.anexo_detalle = progravar
				result.save()
				return redirect('ramasevfenar', id, subid, varid)
	return render(request, 'athos/nuevoramasevfenar.html', context)

def editarramasevfenar(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(RamaPlantaEvFenRamasArandanos, id=varid)
	form = ramaplantaevfenform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('ramasevfenar', id, subid, catid)
	return render(request, 'athos/nuevoramasevfenar.html', context)

#VISTA CAMARAS HUMEDAS
def crearevcamarashumedas(request, id):
	form = evcamarashumedasform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevcamarashumedas.html', context)

def editarevcamarashumedas(request, id, subid):
	sub_campo = get_object_or_404(EvCamarasHumedas, id=subid)
	form = evcamarashumedasform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/editarevcamarashumedas.html', context)

def detalleplantaevcamarashumedas(request, id, subid):
	detallecamarapr=DetallePlantaEvCamarasHumedas.objects.filter(anexo_detalle=subid).order_by("-fecha_hora_creacion")
	context={"detallecamarapr":detallecamarapr, "id":id,"subid":subid}
	return render(request, 'athos/evcamarashumedasdetalleplanta.html', context)

def creardetalleplantaevcamarashumedas(request, id, subid):
	form = detalleevcamarashumedasform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCamarasHumedas,id=subid)
			result.anexo_detalle = progravar
			result.save()
			return redirect('detalleplantaevcamarashumedas',id,subid)
	return render(request, 'athos/nuevoevcamarashumedasdetalle.html', context)

def editardetalleplantaevcamarashumedas(request, id, subid,varid):
	sub_campo = get_object_or_404(DetallePlantaEvCamarasHumedas, id=varid)
	form = detalleevcamarashumedasform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleplantaevcamarashumedas', id, subid)
	return render(request, 'athos/nuevoevcamarashumedasdetalle.html', context)

#EV CAL CONTROL DESCARTE HG 2022
def crearevcalcontroldescartehg2022(request, id):
	form = evcalcontroldescartehg2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/nuevoevcalcontroldescartehg2022.html', context)

def editarevcalcontroldescartehg2022(request, id, subid):
	sub_campo = get_object_or_404(EvCalControlDescarteHg2022, id=subid)
	form = evcalcontroldescartehg2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/evaluaciones/calidad/editarevcalcontroldescartehg2022.html', context)

def detalleevcalcontroldescartehg2022 (request, id, subid):
	detallepr=DetalleEvCalControlDescarteHg2022.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/evaluaciones/calidad/detalleevcalcontroldescartehg2022.html', context)

def creardetalleevcalcontroldescartehg2022(request, id, subid):
	form = detalleevcalcontroldescartehg2022form(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalControlDescarteHg2022,id=subid)
			result.anexo_detalle = progravar
			result.save()
			return redirect('detalleevcalcontroldescartehg2022',id,subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartehg2022.html', context)

def editardetalleevcalcontroldescartehg2022(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalControlDescarteHg2022,id=varid)
	form = detalleevcalcontroldescartehg2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcontroldescartehg2022', id, subid)
	return render(request, 'athos/evaluaciones/calidad/nuevodetalleevcalcontroldescartehg2022.html', context)

#EV CALIDAD PRODUCTO TERMINADO HG 2022
def crearcontrolproductoterminadohg(request, id, subid):
	form = controlproductoterminadohgform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(LPaletas,id=subid)
			result.anexo_lanzado = progravar
			result.save()
			return redirect('controlproductoterminadohg',id,subid)
	return render(request, 'athos/nuevocontrolproductoterminadohg.html', context)

def editarcontrolproductoterminadohg(request, id, subid,varid):
	sub_campo = get_object_or_404(ControlProductoTerminadoHg, id=varid)
	form = controlproductoterminadohgform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('controlproductoterminadohg', id, subid)
	return render(request, 'athos/editarcontrolproductoterminadohg.html', context)

def detallecontrolproductoterminadohg(request, id, subid,varid):
	detallepr = DetalleControlProductoTerminadoHg.objects.filter(anexo_detalle_id=varid)
	context = {"detallepr":detallepr, "id":id, "subid":subid,"varid":varid}
	return render(request, 'athos/detallecpterminadohg.html', context)

def creardetallecontrolproductoterminadohg(request, id, subid,varid):
	idcontrolproducto=varid
	VariableCliente=ControlProductoTerminadoHg.objects.get(id=idcontrolproducto).anexo_centro
	VariableVariedad=LPaletas.objects.get(id=subid).anexo_cultivo
	form =  detallecontrolproductoterminadohgform(request.POST or None, variable_cliente=VariableCliente,variable_variedad=VariableVariedad)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(ControlProductoTerminadoHg,id=varid)
				result.anexo_detalle = progravar
				result.save()
				return redirect('detallecontrolproductoterminadohg', id, subid,varid)
	return render(request, 'athos/nuevodetallecpterminadohg.html', context)

def editardetallecontrolproductoterminadohg(request, id, subid,varid,catid):
	idcontrolproducto=catid
	VariableCliente=ControlProductoTerminadoHg.objects.get(id=idcontrolproducto).anexo_centro
	VariableVariedad=LPaletas.objects.get(id=subid).anexo_cultivo
	sub_campo = get_object_or_404(DetalleControlProductoTerminadoHg, id=varid)
	form = detallecontrolproductoterminadohgform(request.POST or None, instance=sub_campo,variable_cliente=VariableCliente,variable_variedad=VariableVariedad)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detallecontrolproductoterminadohg', id, subid,catid)
	return render(request, 'athos/nuevodetallecpterminadohg.html', context)

#EV EFICIENCIA SELECCION Y CALIBRADO 2022
def crearanalisiseficiencia(request, id):
	form = eveficienciaseleccioncalibradoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevanalisiseficiencia2022.html', context)

def editarevanalisiseficiencia(request, id, subid):
	sub_campo = get_object_or_404(EvEficienciaSeleccionCalibrado, id=subid)
	form = eveficienciaseleccioncalibradoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevanalisiseficiencia2022.html', context)

#EV PRODUCTO TERMINADO ANTES DE DESPACHO 2022
def crearevproductoterminadodespacho(request, id):
	form = evproductoterminadodespachoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevproductoterminadodespacho2022.html', context)

def editarevproductoterminadodespacho(request, id, subid):
	sub_campo = get_object_or_404(EvProductoTerminadoDespacho, id=subid)
	form = evproductoterminadodespachoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('evaluaciones', id)
	return render(request, 'athos/nuevoevproductoterminadodespacho2022.html', context)

def detalleevproductoterminadodespacho(request, id, subid):
	detallepr = DetalleEvProductoTerminadoDespacho.objects.filter(anexo_detalle_id=subid)
	context = {"detallepr":detallepr, "id":id, "subid":subid}
	return render(request, 'athos/detalleevproductoterminadodespacho.html', context)

def creardetalleevproductoterminadodespacho(request, id, subid):
	form =  detalleevproductoterminadodespachoform(request.POST or None)
	context = {"form":form,"subid":subid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(EvProductoTerminadoDespacho,id=subid)
				result.anexo_detalle = progravar
				result.save()
				return redirect('detalleevproductoterminadodespacho', id, subid)
	return render(request, 'athos/nuevodetalleevproductoterminadodespacho.html', context)

def editardetalleevproductoterminadodespacho(request, id, subid):
	sub_campo = get_object_or_404(DetalleEvProductoTerminadoDespacho, id=subid)
	form = detalleevproductoterminadodespachoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleevproductoterminadodespacho', id, subid)
	return render(request, 'athos/nuevodetalleevproductoterminadodespacho.html', context)