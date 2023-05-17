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

from apps.acopio_athos.granada.models import GuiaAthosGr2020
from apps.acopio_athos.granada.forms import guiaathosgr2020form

from apps.acopio_athos.granada.models import GuiaDetallesAthosGr2020
from apps.acopio_athos.granada.forms import guiadetallesathosgr2020form

from apps.acopio_athos.granada.models import InfoPaletGr2020
from apps.acopio_athos.granada.forms import infopaletgr2020form

from apps.acopio_athos.granada.models import GuiaAthosGrIca2021
from apps.acopio_athos.granada.models import GuiaDetallesAthosGrIca2021
from apps.acopio_athos.granada.models import InfoPaletGrIca2021
from apps.acopio_athos.granada.models import AlmacenAcopioGrIca2021

#campaña granada ica 2023
from apps.acopio_athos.granada.models import GuiaAthosGrIca2023
from apps.acopio_athos.granada.models import GuiaDetallesAthosGrIca2023
from apps.acopio_athos.granada.models import InfoPaletGrIca2023
#########################################################################

from apps.acopio_athos.granada.models import AlmacenAcopioGr2020
from apps.acopio_athos.granada.forms  import almacenacopiogr2020form

from apps.acopio_athos.granada.models import DescarteAthosGrIca2021
from apps.acopio_athos.granada.forms  import descarteathosgrica2021form

from apps.acopio_athos.granada.models import SalidaDescarteGrIca2021
from apps.acopio_athos.granada.forms  import salidadescartegrica2021form


from apps.acopio_athos.granada.models import DetalleSalidaDescarteGrIca2021
from apps.acopio_athos.granada.forms  import detallesalidadescartegrica2021form

from apps.menu.models import ejezona
from apps.menu.models import AlmacenesAthos
from apps.menu.models import PlacasVehiculares
from apps.menu.models import ChoferesVehiculos
from apps.menu.models import LugarAthos
from apps.menu.models import MaterialAcopio
from apps.planta.granada_planta.models import LanzadoPaletasGrIca2021
# Create your views here.

def load_almacenes(request, id):
	almacen = list(ejezona.objects.get(id=id).AnexoZonaAlmacen.all().values('id','almacen','desc_almacen'))
	return JsonResponse(almacen,safe=False)

def load_vehiculos(request, id):
	vehiculos = list(ejezona.objects.get(id=id).AnexoPlacaZona.all().values('id','placas'))
	return JsonResponse(vehiculos,safe=False)

def load_chofer(request, id):
	chofer = list(ejezona.objects.get(id=id).AnexoZonaCH.all().values('id','ApellidoPat','ApellidoMat','Nombres'))
	return JsonResponse(chofer,safe=False)

def load_ubicacion(request, id):
	ubi = list(ejezona.objects.get(id=id).AnexoZonaLug.all().values('id','Lugar'))
	return JsonResponse(ubi,safe=False)


def acopio_athos(request, id):

	if request.user.username=='rportal':
		guiaathospr=GuiaAthosGrIca2023.objects.all().order_by("-fecha_hora_creacion")[:250]
		context94={"guiaathospr":guiaathospr, "id":id}
	else:
		guiaathospr=GuiaAthosGrIca2023.objects.all().order_by("-fecha_hora_creacion")[:250]
		context94={"guiaathospr":guiaathospr, "id":id}

	almacenpr=AlmacenAcopioGrIca2021.objects.all().order_by("-fecha_hora_creacion")[:50]
	context124={"almacenpr":almacenpr, "id":id}

	descartepr = DescarteAthosGrIca2021.objects.all().order_by("-fecha_hora_creacion")
	context145 = {"descartepr":descartepr, "id":id}

	salidapr = SalidaDescarteGrIca2021.objects.all().order_by("-fecha_hora_creacion")
	context146 = {"salidapr":salidapr, "id":id}

	if(id==94):
		return render(request, 'athos/acopio_athos/granada/guiaathosgr2020.html',context94)
	else:
		if (id==124):
			return render(request, 'athos/acopio_athos/granada/almacenacopiogr2020.html', context124)
		else:
			if (id==145):
				return render(request, 'athos/acopio_athos/granada/descarteathosgrica2021.html', context145)
			else:
				if (id==146):
					return render(request, 'athos/acopio_athos/granada/salidadescartegrica2021.html', context146)


def load_trazabilidadgrica2021(request, id):
    datos = list(LanzadoPaletasGrIca2021.objects.filter(trazabilidad=id).values('id','fecha_lanzado','fecha_cosecha','anexo_turno__nom_turno','material'))
    return JsonResponse(datos,safe=False)


																																				
#esta vista me permite crear Guias Granada 2023 - GrIca2023
def crearguiaathosgr2020(request, id):
	form = guiaathosgr2020form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos', id)
	return render(request, 'athos/acopio_athos/granada/nuevoguiaathosgr2020.html', context)

#esta vista me permite editar Guias Granada 2023- GrIca2023
def editarguiaathosgr2020(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosGrIca2023, id=subid)
	form = guiaathosgr2020form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos', id)
	return render(request, 'athos/acopio_athos/granada/editarguiaathosgr2020.html', context)


#esta vista me permite ver la guia detalles granada ica 2023- GuiaDetallesGrIca2023
def guiadetallesathosgr2020(request, id, subid):

	guiadetallespr=GuiaDetallesAthosGrIca2023.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/granada/guiadetallesathosgr2020.html', context)

#esta vista me permite crear la guia detalles granada ica 2023- GuiaDetallesGrIca2023
def crearguiadetallesathosgr2020(request, id, subid):
	guiazona=GuiaAthosGrIca2023.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosGrIca2023.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathosgr2020form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosGrIca2023,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathosgr2020',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/granada/nuevoguiadetallesathosgr2020.html', context)

#esta vista me permite editar la guia detalles granada ica 2023- GuiaDetallesGrIca2023
def editarguiadetallesathosgr2020(request, id, subid,varid):
	guiazona=GuiaAthosGrIca2023.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosGrIca2023.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosGrIca2023, id=varid)
	form = guiadetallesathosgr2020form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathosgr2020', id, subid)
	return render(request, 'athos/acopio_athos/granada/editarguiadetallesathosgr2020.html', context)


#esta vista me permite ver Informacion palet granada ica 2023 . InfoPaletGrIca2023
def infopaletgr2020(request, id, subid,varid):
	infopaletpr = InfoPaletGrIca2023.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/granada/infopaletgr2020.html', context)

#esta vista me permite crear Informacion palet granada ica 2023 . InfoPaletGrIca2023
def crearinfopaletgr2020(request, id, subid,varid):
	form =  infopaletgr2020form(request.POST or None)
	palet1 = GuiaDetallesAthosGrIca2023.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosGrIca2023,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathosgr2020', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2020/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/granada/nuevoinfopaletgr2020.html', context)


#esta vista me permite editar Informacion palet granada ica 2023 . InfoPaletGrIca2023
def editarinfopaletgr2020(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletGrIca2023, id=varid)

	palet1 = GuiaDetallesAthosGrIca2023.objects.get(id=catid)
	palet2 = InfoPaletGrIca2023.objects.get(id=varid)
	form = infopaletgr2020form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopaletgr2020', id, subid, catid)
	return render(request, 'athos/acopio_athos/granada/nuevoinfopaletgr2020.html', context)


#esta vista me permite imprimir Informacion palet granada ica 2023 . InfoPaletGrIca2023
def printpaletgr2020(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletGrIca2023.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/granada/printpaletgr2020.html',context)




def crearalmacenacopiogr2020(request,id):
	form = almacenacopiogr2020form(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos', id)
	return render(request, 'athos/acopio_athos/granada/nuevoalmacenacopiogr2020.html', context)

def editaralmacenacopiogr2020(request, id, subid):
	sub_campo = get_object_or_404(AlmacenAcopioGrIca2021, id=subid)
	context = {"form":form}
	if request.method=='POST':
		form = almacenacopiogr2020form(request.POST or None, instance=sub_campo)
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('acopio_athos', id)
	return render(request, 'athos/acopio_athos/granada/nuevoalmacenacopiogr2020.html', context)




#descarte
def creardescarteathosgrica2021(request,id):
	form = descarteathosgrica2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos', id)
	return render(request, 'athos/acopio_athos/granada/nuevodescarteathosgrica2021.html', context)

def editardescarteathosgrica2021(request, id, subid):
	sub_campo = get_object_or_404(DescarteAthosGrIca2021, id=subid)
	form = descarteathosgrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('acopio_athos',id )
	return render(request, 'athos/acopio_athos/granada/editardescarteathosgrica2021.html', context)

def crearsalidadescartegrica2021(request,id):

	form = salidadescartegrica2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos',id )
	return render(request, 'athos/acopio_athos/granada/nuevosalidadescartegrica2021.html', context)

def editarsalidadescartegrica2021(request, id, subid):
	sub_campo = get_object_or_404(SalidaDescarteGrIca2021, id=subid)
	form = salidadescartegrica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('acopio_athos',id )
	return render(request, 'athos/acopio_athos/nuevosalidadescartegrica2021.html', context)


def printpaletdescartegr2021(request, palet_id):
	palet = DescarteAthosGrIca2021.objects.get(id=palet_id)
	
	context = {"palet":palet}
	return render(request, 'athos/acopio_athos/granada/printpaletdescartegrica2021.html',context)




def detallesalidadescartegrica2021(request, id, subid):

	detallespr=DetalleSalidaDescarteGrIca2021.objects.filter(id=subid).order_by("-fecha_hora_creacion")
	context={"detallespr":detallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/granada/detallesalidadescartegrica2021.html', context)


def creardetallesalidadescartegrica2021(request, id, subid):
	
	form =  detallesalidadescartegrica2021form(request.POST or None)
	
	context = {"form":form,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(SalidaDescarteGrIca2021,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('detallesalidadescartegrica2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/granada/nuevodetallesalidadescartegrica2021.html', context)


def editardetallesalidadescartegrica2021(request, id, subid,varid):
	
	sub_campo = get_object_or_404(DetalleSalidaDescarteGrIca2021, id=varid)
	form = detallesalidadescartegrica2021form(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detallesalidadescartegrica2021',id,subid)
	return render(request, 'athos/acopio_athos/granada/nuevodetallesalidadescartegrica2021.html', context)

