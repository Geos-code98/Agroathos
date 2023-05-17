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
from django.db.models import Q

from apps.riego.models import ProductosRiego
from apps.riego.forms import productosriegoform

from apps.riego.models import MetodoRiego
from apps.riego.forms import metodoriegoform

from apps.riego.models import EquiposRiego
from apps.riego.forms import equiposriegoform

from apps.riego.models import PozosRiego
from apps.riego.forms import pozosriegoform


from apps.riego.models import OperadoresRiegoAthos
from apps.riego.forms import operadoresriegoathosform



from apps.riego.models import LeyNutricionRiego
from apps.riego.forms import leynutricionriegoform

from apps.riego.models import ProyeccionSemanalRiego
from apps.riego.forms import proyeccionsemanalriegoform

from apps.riego.models import DetalleProyeccionSemanalRiego
from apps.riego.forms import detalleproyeccionsemanalriegoform

from apps.riego.models import RegistroProyeccionSemanalRiego
from apps.riego.forms import registroproyeccionsemanalriegoform

from apps.riego.models import RegistroRiegoFertilizacion
from apps.riego.forms import registroriegofertilizacionform

from apps.riego.models import DetalleRegistroRiegoFertilizacion
from apps.riego.forms import detalleregistroriegofertilizacionform


from apps.riego.models import DetRequerimientoRiegoFert
from apps.riego.forms import detrequerimientoriegofertform

from apps.riego.models import DetalleRequerimientoRiegot
from apps.riego.forms import detallerequerimientoriegotform


from apps.riego.models import ConsumoRequerimientoRiegoFert
from apps.riego.forms import consumorequerimientoriegofertform

from apps.menu.models import ejezona
from apps.menu.models import ProgramaProduccion


from apps.riego.models import ExplotacionPozos
from apps.riego.forms import explotacionpozosform

from apps.riego.models import DetalleExplotacionPozos
from apps.riego.forms import detalleexplotacionpozosform

from apps.riego.models import EstacionMeteorologica
from apps.riego.forms import estacionmeteorologicaform

from apps.riego.models import SolucionesMadres
from apps.riego.models import DetalleSolucionesMadres
from apps.riego.forms import solucionesmadresform
from apps.riego.forms import detallesolucionesmadresform
from apps.maestras.models import TanquesAthos


# Create your views here.
def riego(request, id):

	if request.user.is_superuser:
		productospr = ProductosRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context83 = {"productospr":productospr, "id":id}
	else:
		productospr = ProductosRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context83 = {"productospr":productospr, "id":id}


	if request.user.is_superuser:
		metodopr = MetodoRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context84 = {"metodopr":metodopr, "id":id}
	else:
		metodopr = MetodoRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context84 = {"metodopr":metodopr, "id":id}


	if request.user.is_superuser:
		equipospr = EquiposRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context85 = {"equipospr":equipospr, "id":id}
	else:
		equipospr = EquiposRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context85 = {"equipospr":equipospr, "id":id}


	if request.user.is_superuser:
		pozospr = PozosRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context86 = {"pozospr":pozospr, "id":id}
	else:
		pozospr = PozosRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context86 = {"pozospr":pozospr, "id":id}


	if request.user.is_superuser or request.user.username=='jmaurtua' or request.user.username=='jcordova' or request.user.username=='rrojas' or request.user.username=='dlifonzo' or request.user.username=='achacaliaza':
		leypr = LeyNutricionRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context88 = {"leypr":leypr, "id":id}
	else:
		leypr = LeyNutricionRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context88 = {"leypr":leypr, "id":id}


	if request.user.is_superuser or request.user.username=='jmaurtua' or request.user.username=='jcordova' or request.user.username=='dlifonzo' or request.user.username=='achacaliaza':
		proypr = ProyeccionSemanalRiego.objects.all().order_by("-fecha_hora_creacion")[:50]
		context89 = {"proypr":proypr, "id":id}
	else:
		proypr = ProyeccionSemanalRiego.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context89 = {"proypr":proypr, "id":id}

	if request.user.is_superuser or request.user.username=='jcordova' or request.user.username == 'hingaroca':
		registropr = RegistroRiegoFertilizacion.objects.all().order_by("-fecha_hora_creacion")[:250]
		context90 = {"registropr":registropr, "id":id}
	else:
		if request.user.username=='ajamanca' or request.user.username=='rrojas' or request.user.username=='jmaurtua' or request.user.username=='jcordova' or request.user.username=='tfernandez' or request.user.username=='swilfredo' or request.user.username=='jchacaliaza' or request.user.username=='jramos' or request.user.username=='wtucno' or request.user.username=='aramos' or request.user.username=='dlifonzo' or request.user.username == 'achacaliaza' or request.user.username == 'jmamani':
			registropr = RegistroRiegoFertilizacion.objects.all().order_by("-fecha_hora_creacion")[:250]
			context90 = {"registropr":registropr, "id":id}
		else:
			if request.user.username=='frondon' or request.user.username=='aramos' or request.user.username=='hingaroca'  :
				registropr = RegistroRiegoFertilizacion.objects.filter(Q(usuario_creacion_id=211)|Q(usuario_creacion_id=600)|Q(usuario_creacion_id=123)).order_by("-fecha_hora_creacion")[:250]
				context90 = {"registropr":registropr, "id":id}
			else:
				if request.user.username=='jcordova' or request.user.username=='tfernandez' or request.user.username=='swilfredo' or request.user.username=='jchacaliaza' or request.user.username=='jramos' or request.user.username=='wtucno' or request.user.username=='aramos' or request.user.username=='dlifonzo' or request.user.username == 'achacaliaza' or request.user.username == 'jmamani':
					registropr = RegistroRiegoFertilizacion.objects.all().order_by("-fecha_hora_creacion")[:250]
					context90 = {"registropr":registropr, "id":id}
				else:
					registropr = RegistroRiegoFertilizacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:150]
					context90 = {"registropr":registropr, "id":id}

	if request.user.is_superuser or request.user.username=='ajamanca' or request.user.username=='rrojas' or request.user.username=='jmaurtua' or request.user.username=='jcordova' or request.user.username=='dlifonzo' or request.user.username=='jramos' or request.user.username=='dlifonzo' or request.user.username=='achacaliaza':
		explopr = ExplotacionPozos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context105 = {"explopr":explopr, "id":id}
	else:
		if request.user.username=='frondon' or request.user.username=='aramos' or request.user.username=='hingaroca' :
				explopr = ExplotacionPozos.objects.filter(Q(usuario_creacion_id=211)|Q(usuario_creacion_id=600)|Q(usuario_creacion_id=123)).order_by("-fecha_hora_creacion")[:250]
				context105 = {"explopr":explopr, "id":id}
		else:
			if request.user.username=='jcordova' or request.user.username=='tfernandez' or request.user.username=='swilfredo' or request.user.username=='jchacaliaza' or request.user.username=='jramos' or request.user.username=='wtucno' or request.user.username=='aramos' or request.user.username=='dlifonzo' or request.user.username == 'achacaliaza' or request.user.username == 'jmamani':
				explopr = ExplotacionPozos.objects.all().order_by("-fecha_hora_creacion")[:50]
				context105 = {"explopr":explopr, "id":id}
			else:
				explopr = ExplotacionPozos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
				context105 = {"explopr":explopr, "id":id}


	operadorespr = OperadoresRiegoAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context111 = {"operadorespr":operadorespr, "id":id}
	
	estacionpr = EstacionMeteorologica.objects.all().order_by("-fecha_hora_creacion")[:50]
	context112 = {"estacionpr":estacionpr, "id":id}
	
	solucmadres = SolucionesMadres.objects.all().order_by("-fecha_hora_creacion")[:50]
	context154 = {"solucmadres":solucmadres, "id":id}


	if (id==83):
		return render(request, 'athos/riego/productosriego.html', context83)
	else:
		if (id==84):
			return render(request, 'athos/riego/metodoriego.html', context84)
		else:
			if (id==85):
				return render(request, 'athos/riego/equiposriego.html', context85)
			else:
				if (id==86):
					return render(request, 'athos/riego/pozosriego.html', context86)
				else:
					if (id==88):
						return render(request, 'athos/riego/leynutricionriego.html', context88)
					else:
						if (id==89):
							return render(request, 'athos/riego/proyeccionsemanalriego.html', context89)
						else:
							if (id==90):
								return render(request, 'athos/riego/registroriegofertilizacion.html', context90)
							else:
								if (id==105):
									return render(request, 'athos/riego/explotacionpozos.html', context105)
								else:
									if (id==111):
										return render(request, 'athos/riego/operadoresriegoathos.html', context111)
									else:
										if (id==112):
											return render(request, 'athos/riego/estacionmeteorologica.html', context112)
										else:
											if (id==154):
												return render(request, 'athos/riego/solucionesmadres.html', context154)


def load_equipos(request, id):
	equipos = list(ejezona.objects.get(id=id).AnexoZonaRiego.all().values('id','equipo','descripcion'))
	return JsonResponse(equipos,safe=False)

def load_pozos(request, id):
	pozos = list(ejezona.objects.get(id=id).AnexoZonaPozoRiego.all().values('id','codigo','nombre'))
	return JsonResponse(pozos,safe=False)

def load_tanques(request, id):
	tanques = list(TanquesAthos.objects.filter(anexo_fundo=id).values('id','anexo_fundo__nom_fundo','numero_tanque'))
	return JsonResponse(tanques,safe=False)

def crearproductosriego(request, id):

	form = productosriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoproductosriego.html', context)


def editarproductosriego(request, id, subid):
	sub_campo = get_object_or_404(ProductosRiego, id=subid)
	form = productosriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoproductosriego.html', context)



def crearmetodoriego(request, id):

	form = metodoriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevometodoriego.html', context)


def editarmetodoriego(request, id, subid):
	sub_campo = get_object_or_404(MetodoRiego, id=subid)
	form = metodoriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevometodoriego.html', context)


def crearequiposriego(request, id):

	form = equiposriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoequiposriego.html', context)


def editarequiposriego(request, id, subid):
	sub_campo = get_object_or_404(EquiposRiego, id=subid)
	form = equiposriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/editarequiposriego.html', context)

def crearoperadoresriegoathos(request, id):

	form = operadoresriegoathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevooperadoresriegoathos.html', context)


def editaroperadoresriegoathos(request, id, subid):
	sub_campo = get_object_or_404(OperadoresRiegoAthos, id=subid)
	form = operadoresriegoathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevooperadoresriegoathos.html', context)






def crearpozosriego(request, id):

	form = pozosriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevopozosriego.html', context)


def editarpozosriego(request, id, subid):
	sub_campo = get_object_or_404(PozosRiego, id=subid)
	form = pozosriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevopozosriego.html', context)


def crearleynutricionriego(request, id):

	form = leynutricionriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoleynutricionriego.html', context)


def editarleynutricionriego(request, id, subid):
	sub_campo = get_object_or_404(LeyNutricionRiego, id=subid)
	form = leynutricionriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/editarleynutricionriego.html', context)



def crearproyeccionsemanalriego(request, id):

	form = proyeccionsemanalriegoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoproyeccionsemanalriego.html', context)


def editarproyeccionsemanalriego(request, id, subid):
	sub_campo = get_object_or_404(ProyeccionSemanalRiego, id=subid)
	form = proyeccionsemanalriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoproyeccionsemanalriego.html', context)



def detalleproyeccionsemanalriego (request, id, subid):

	detallepr=DetalleProyeccionSemanalRiego.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/riego/detalleproyeccionsemanalriego.html', context)


def creardetalleproyeccionsemanalriego(request, id, subid):
	variablefundo=ProyeccionSemanalRiego.objects.get(id=subid).anexo_fundo
	form = detalleproyeccionsemanalriegoform(request.GET or None, variable_fundo=variablefundo)

	context = {"form":form,"subid":subid }
	if request.method=='GET' and request.GET.get('anexo_save','')!='':

		current_user = auth.get_user(request)

		datos=DetalleProyeccionSemanalRiego()
		datos.anexo_detalle=ProyeccionSemanalRiego.objects.get(id=subid)
		datos.anexo_ley=LeyNutricionRiego.objects.get(id=request.GET.get('anexo_ley',''))
		datos.anexo_pep=ProgramaProduccion.objects.get(id=request.GET.get('anexo_pep',''))

		datos.usuario_creacion=current_user

		datos.semana_1=request.GET.get('semana_1','')
		datos.semana_2=request.GET.get('semana_2','')
		datos.semana_3=request.GET.get('semana_3','')
		datos.semana_4=request.GET.get('semana_4','')
		datos.save()

		data={}
		response = JsonResponse(data)

		return response

	return render(request, 'athos/riego/nuevodetalleproyeccionsemanalriego.html', context)



def editardetalleproyeccionsemanalriego(request, id, subid,varid):
	variablefundo=ProyeccionSemanalRiego.objects.get(id=subid).anexo_fundo
	sub_campo = get_object_or_404(DetalleProyeccionSemanalRiego, id=varid)
	form = detalleproyeccionsemanalriegoform(request.POST or None, instance=sub_campo,variable_fundo=variablefundo )
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleproyeccionsemanalriego', id, subid)
	return render(request, 'athos/riego/editardetalleproyeccionsemanalriego.html', context)


def registroproyeccionsemanalriego (request, id, subid):

	detallepr=RegistroProyeccionSemanalRiego.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/riego/registroproyeccionsemanalriego.html', context)


def crearregistroproyeccionsemanalriego(request, id, subid):
	form = registroproyeccionsemanalriegoform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProyeccionSemanalRiego,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('riego',id)
	print(context)
	return render(request, 'athos/riego/nuevoregistroproyeccionsemanalriego.html', context)


def editarregistroproyeccionsemanalriego(request, id, subid,varid):
	sub_campo = get_object_or_404(RegistroProyeccionSemanalRiego, id=varid)
	form = registroproyeccionsemanalriegoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('registroproyeccionsemanalriego', id, subid)
	return render(request, 'athos/riego/nuevoregistroproyeccionsemanalriego.html', context)













def crearregistroriegofertilizacion(request, id):

	form = registroriegofertilizacionform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoregistroriegofertilizacion.html', context)


def editarregistroriegofertilizacion(request, id, subid):
	sub_campo = get_object_or_404(RegistroRiegoFertilizacion, id=subid)
	form = registroriegofertilizacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/editarregistroriegofertilizacion.html', context)




def detalleregistroriegofertilizacion (request, id, subid):

	detallepr=DetalleRegistroRiegoFertilizacion.objects.filter(anexo_detalle_id=subid)
	ver1= RegistroRiegoFertilizacion.objects.get(id=subid).fecha_hora_creacion
	context={"detallepr":detallepr, "id":id,"subid":subid,"ver1":ver1}
	return render(request, 'athos/riego/detalleregistroriegofertilizacion.html', context)


def creardetalleregistroriegofertilizacion(request, id, subid):
	ver= RegistroRiegoFertilizacion.objects.get(id=subid).area
	
	form = detalleregistroriegofertilizacionform(request.POST or None)

	context = {"form":form,"subid":subid, "ver":ver}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(RegistroRiegoFertilizacion,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleregistroriegofertilizacion',id,subid)
	print(context)
	return render(request, 'athos/riego/nuevodetalleregistroriegofertilizacion.html', context)


def editardetalleregistroriegofertilizacion(request, id, subid,varid):

	sub_campo = get_object_or_404(DetalleRegistroRiegoFertilizacion, id=varid)
	form = detalleregistroriegofertilizacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleregistroriegofertilizacion', id, subid)
	return render(request, 'athos/riego/editardetalleregistroriegofertilizacion.html', context)




def detrequerimientoriegofert (request, id, subid):

	detallepr=DetRequerimientoRiegoFert.objects.filter(anexo_detalle_id=subid)
	ver1= RegistroRiegoFertilizacion.objects.get(id=subid).fecha_hora_creacion
	context={"detallepr":detallepr, "id":id,"subid":subid,"ver1":ver1}
	return render(request, 'athos/riego/detrequerimientoriegofert.html', context)


def creardetrequerimientoriegofert(request, id, subid):
	form = detrequerimientoriegofertform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(RegistroRiegoFertilizacion,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detrequerimientoriegofert',id,subid)
	print(context)
	return render(request, 'athos/riego/nuevodetrequerimientoriegofert.html', context)


def editardetrequerimientoriegofert(request, id, subid,varid):
	sub_campo = get_object_or_404(DetRequerimientoRiegoFert, id=varid)
	form = detrequerimientoriegofertform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detrequerimientoriegofert', id, subid)
	return render(request, 'athos/riego/editardetrequerimientoriegofert.html', context)



def consumorequerimientoriegofert (request, id, subid, varid):

	detallepr=ConsumoRequerimientoRiegoFert.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")
	ver1= DetRequerimientoRiegoFert.objects.get(id=varid).fecha_hora_creacion
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid,"ver1":ver1}
	return render(request, 'athos/riego/consumorequerimientoriegofert.html', context)


def crearconsumorequerimientoriegofert(request, id, subid, varid):
	ver=DetRequerimientoRiegoFert.objects.get(id=varid).resto_consumo
	anexofundo=DetRequerimientoRiegoFert.objects.get(id=varid).anexo_detalle.anexo_pep
	form = consumorequerimientoriegofertform(request.POST or None,anexo_fundo=anexofundo)

	context = {"form":form,"subid":subid,"varid":varid, "ver":ver}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(DetRequerimientoRiegoFert,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('consumorequerimientoriegofert',id,subid,varid)
	print(context)
	return render(request, 'athos/riego/nuevoconsumorequerimientoriegofert.html', context)


def editarconsumorequerimientoriegofert(request, id, subid,varid,catid):
	ver=DetRequerimientoRiegoFert.objects.get(id=varid).resto_consumo
	anexofundo=DetRequerimientoRiegoFert.objects.get(id=varid).anexo_detalle.anexo_pep
	
	sub_campo = get_object_or_404(ConsumoRequerimientoRiegoFert, id=catid)
	form = consumorequerimientoriegofertform(request.POST or None, instance=sub_campo,anexo_fundo=anexofundo)
	context = {"form":form, "ver":ver}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('consumorequerimientoriegofert', id, subid, varid)
	return render(request, 'athos/riego/editarconsumorequerimientoriegofert.html', context)

###detallerequerimientoriegotform
def detallerequerimientoriegot (request, id, subid, varid):

	detallepr=DetalleRequerimientoRiegot.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")
	
	ver2=DetalleRegistroRiegoFertilizacion.objects.get(id=varid).anexo_fecha
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid,"ver2":ver2}
	return render(request, 'athos/riego/detallerequerimientoriegot.html', context)


def creardetallerequerimientoriegot(request, id, subid, varid):
	ver1=DetalleRegistroRiegoFertilizacion.objects.get(id=varid).anexo_detalle.anexo_equipo.factor_correccion
	
	ver=DetalleRegistroRiegoFertilizacion.objects.get(id=varid).resto_consumo
	
	
	form = detallerequerimientoriegotform(request.POST or None)

	context = {"form":form,"subid":subid,"varid":varid, "ver":ver,"ver1":ver1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(DetalleRegistroRiegoFertilizacion,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detallerequerimientoriegot',id,subid,varid)
	print(context)
	return render(request, 'athos/riego/nuevodetallerequerimientoriegot.html', context)


def editardetallerequerimientoriegot(request, id, subid,varid,catid):
	ver1=DetalleRegistroRiegoFertilizacion.objects.get(id=varid).anexo_detalle.anexo_equipo.factor_correccion
	
	ver=DetalleRegistroRiegoFertilizacion.objects.get(id=varid).resto_consumo
	

	sub_campo = get_object_or_404(DetalleRequerimientoRiegot, id=catid)
	form = detallerequerimientoriegotform(request.POST or None, instance=sub_campo)
	context = {"form":form, "ver":ver,"ver1":ver1}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detallerequerimientoriegot', id, subid, varid)
	return render(request, 'athos/riego/editardetallerequerimientoriegot.html', context)



def crearestacionmeteorologica(request, id):

	form = estacionmeteorologicaform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoestacionmeteorologica.html', context)


def editarestacionmeteorologica(request, id, subid):
	sub_campo = get_object_or_404(EstacionMeteorologica, id=subid)
	form = estacionmeteorologicaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoestacionmeteorologica.html', context)


























def crearexplotacionpozos(request, id):

	form = explotacionpozosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevoexplotacionpozos.html', context)


def editarexplotacionpozos(request, id, subid):
	sub_campo = get_object_or_404(ExplotacionPozos, id=subid)
	form = explotacionpozosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/editarexplotacionpozos.html', context)

def detalleexplotacionpozos (request, id, subid):

	detallepr=DetalleExplotacionPozos.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/riego/detalleexplotacionpozos.html', context)


def creardetalleexplotacionpozos(request, id, subid):
	form = detalleexplotacionpozosform(request.POST or None)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ExplotacionPozos,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('riego',id)
	print(context)
	return render(request, 'athos/riego/nuevodetalleexplotacionpozos.html', context)


def editardetalleexplotacionpozos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleExplotacionPozos, id=varid)
	form = detalleexplotacionpozosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevodetalleexplotacionpozos.html', context)

#SOLUCIONES MADRES
def crearsolucionesmadres(request, id):

	form = solucionesmadresform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevosolucionesmadres.html', context)

def editarsolucionesmadres(request, id, subid):
	sub_campo = get_object_or_404(SolucionesMadres, id=subid)
	form = solucionesmadresform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('riego', id)
	return render(request, 'athos/riego/nuevosolucionesmadres.html', context)

def detallesolucionesmadres(request, id, subid):

	detallepr=DetalleSolucionesMadres.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/riego/detallesolucionesmadres.html', context)

def creardetallesolucionesmadres(request, id, subid):
    
	form = detallesolucionesmadresform(request.POST or None)

	context = {"form":form, "subid":subid}

	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(SolucionesMadres,id=subid)
			result.anexo_detalle = progravar
			result.save()
			return redirect('detallesolucionesmadres', id, subid)
	return render(request, 'athos/riego/nuevodetallesolucionesmadres.html', context)

def editardetallesolucionesmadres(request, id, subid, varid):
	sub_campo = get_object_or_404(DetalleSolucionesMadres, id=varid)
	form = detallesolucionesmadresform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detallesolucionesmadres', id, subid)
	return render(request, 'athos/riego/nuevodetallesolucionesmadres.html', context)
