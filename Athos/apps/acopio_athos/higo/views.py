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

from apps.acopio_athos.higo.models import GuiaAthosHgPisco2021
from apps.acopio_athos.higo.forms import guiaathoshgpisco2021form

from apps.acopio_athos.higo.models import GuiaDetallesAthosHgPisco2021
from apps.acopio_athos.higo.forms import guiadetallesathoshgpisco2021form

from apps.acopio_athos.higo.models import InfoPaletHgPisco2021
from apps.acopio_athos.higo.forms import infopalethgpisco2021form

from apps.acopio_athos.higo.models import AlmacenAcopioHgPisco2021
from apps.acopio_athos.higo.forms  import almacenacopiohgpisco2021form


from apps.acopio_athos.higo.models import GuiaAthosHgNepena2022
from apps.acopio_athos.higo.forms import guiaathoshgnepena2021form

from apps.acopio_athos.higo.models import GuiaDetallesAthosHgNepena2021
from apps.acopio_athos.higo.forms import guiadetallesathoshgnepena2021form

from apps.acopio_athos.higo.models import InfoPaletHgNepena2021
from apps.acopio_athos.higo.forms import infopalethgnepena2021form

from apps.acopio_athos.higo.models import AlmacenAcopioHgNepena2021
from apps.acopio_athos.higo.forms  import almacenacopiohgnepena2021form

from apps.menu.models import ejezona
from apps.menu.models import AlmacenesAthos
from apps.menu.models import PlacasVehiculares
from apps.menu.models import ChoferesVehiculos
from apps.menu.models import LugarAthos
from apps.menu.models import MaterialAcopio
# Create your views here.

#CAMPAÑA HG NEPEÑA 2022
from apps.acopio_athos.higo.models import GuiaAthosHgNepena2022
from apps.acopio_athos.higo.forms import guiaathoshgnepena2021form
from apps.acopio_athos.higo.models import GuiaDetallesAthosHgNepena2022
from apps.acopio_athos.higo.forms import guiadetallesathoshgnepena2021form
from apps.acopio_athos.higo.models import InfoPaletHgNepena2022
from apps.acopio_athos.higo.forms import infopalethgnepena2021form
from apps.acopio_athos.higo.models import AlmacenAcopioHgNepena2022
from apps.acopio_athos.higo.forms  import almacenacopiohgnepena2021form

#CAMPAÑA HG PISCO 2022
from apps.acopio_athos.higo.models import GuiaAthosHgPisco2022
from apps.acopio_athos.higo.forms import guiaathoshgpisco2021form
from apps.acopio_athos.higo.models import GuiaDetallesAthosHgPisco2022
from apps.acopio_athos.higo.forms import guiadetallesathoshgpisco2021form
from apps.acopio_athos.higo.models import InfoPaletHgPisco2022
from apps.acopio_athos.higo.forms import infopalethgpisco2021form
from apps.acopio_athos.higo.models import AlmacenAcopioHgPisco2022
from apps.acopio_athos.higo.forms  import almacenacopiohgpisco2021form

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


def acopio_athos_04(request, id):

	guiaathospr=GuiaAthosHgPisco2021.objects.all().order_by("-fecha_hora_creacion")[:500]
	context132={"guiaathospr":guiaathospr, "id":id}

	almacenpr=AlmacenAcopioHgPisco2021.objects.all().order_by("-fecha_hora_creacion")[:500]
	context133={"almacenpr":almacenpr, "id":id}

	guiaathospr=GuiaAthosHgNepena2022.objects.all().order_by("-fecha_hora_creacion")[:500]
	context135={"guiaathospr":guiaathospr, "id":id}

	if(id==132):
		return render(request, 'athos/acopio_athos/higo/guiaathoshgpisco2021.html',context132)
	else:
		if (id==133):
			return render(request, 'athos/acopio_athos/higo/almacenacopiohgpisco2021.html', context133)																																				
		else:
			if(id==135):
				return render(request, 'athos/acopio_athos/higo/guiaathoshgnepena2021.html',context135)
	

def crearguiaathoshgpisco2021(request, id):
	form = guiaathoshgpisco2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoguiaathoshgpisco2021.html', context)


def editarguiaathoshgpisco2021(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosHgPisco2021, id=subid)
	form = guiaathoshgpisco2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/editarguiaathoshgpisco2021.html', context)


def guiadetallesathoshgpisco2021(request, id, subid):

	guiadetallespr=GuiaDetallesAthosHgPisco2021.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/higo/guiadetallesathoshgpisco2021.html', context)


def crearguiadetallesathoshgpisco2021(request, id, subid):
	guiazona=GuiaAthosHgPisco2021.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosHgPisco2021.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathoshgpisco2021form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosHgPisco2021,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathoshgpisco2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/higo/nuevoguiadetallesathoshgpisco2021.html', context)


def editarguiadetallesathoshgpisco2021(request, id, subid,varid):
	guiazona=GuiaAthosHgPisco2021.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosHgPisco2021.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosHgPisco2021, id=varid)
	form = guiadetallesathoshgpisco2021form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathoshgpisco2021', id, subid)
	return render(request, 'athos/acopio_athos/higo/editarguiadetallesathoshgpisco2021.html', context)


def infopalethgpisco2021(request, id, subid,varid):
	infopaletpr = InfoPaletHgPisco2021.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/higo/infopalethgpisco2021.html', context)


def crearinfopalethgpisco2021(request, id, subid,varid):
	form =  infopalethgpisco2021form(request.POST or None)
	palet1 = GuiaDetallesAthosHgPisco2021.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosHgPisco2021,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathoshgpisco2021', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2021/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/higo/nuevoinfopalethgpisco2021.html', context)

def editarinfopalethgpisco2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletHgPisco2021, id=varid)

	palet1 = GuiaDetallesAthosHgPisco2021.objects.get(id=catid)
	palet2 = InfoPaletHgPisco2021.objects.get(id=varid)
	form = infopalethgpisco2021form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopalethgpisco2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/higo/nuevoinfopalethgpisco2021.html', context)



def printpalethgpisco2021(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletHgPisco2021.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/higo/printpalethgpisco2021.html',context)




def crearalmacenacopiohgpisco2021(request,id):
	form = almacenacopiohgpisco2021form(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoalmacenacopiohgpisco2021.html', context)

def editaralmacenacopiohgpisco2021(request, id, subid):
	sub_campo = get_object_or_404(AlmacenAcopioHgPisco2021, id=subid)
	context = {"form":form}
	if request.method=='POST':
		form = almacenacopiohgpisco2021form(request.POST or None, instance=sub_campo)
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoalmacenacopiohgpisco2021.html', context)




def crearguiaathoshgnepena2021(request, id):
	form = guiaathoshgnepena2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoguiaathoshgnepena2021.html', context)


def editarguiaathoshgnepena2021(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosHgNepena2022, id=subid)
	form = guiaathoshgnepena2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/editarguiaathoshgnepena2021.html', context)


def guiadetallesathoshgnepena2021(request, id, subid):

	guiadetallespr=GuiaDetallesAthosHgNepena2022.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/higo/guiadetallesathoshgnepena2021.html', context)


def crearguiadetallesathoshgnepena2021(request, id, subid):
	guiazona=GuiaAthosHgNepena2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosHgNepena2022.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathoshgnepena2021form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosHgNepena2022,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathoshgnepena2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/higo/nuevoguiadetallesathoshgnepena2021.html', context)


def editarguiadetallesathoshgnepena2021(request, id, subid,varid):
	guiazona=GuiaAthosHgNepena2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosHgNepena2022.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosHgNepena2022, id=varid)
	form = guiadetallesathoshgnepena2021form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathoshgnepena2021', id, subid)
	return render(request, 'athos/acopio_athos/higo/editarguiadetallesathoshgnepena2021.html', context)


def infopalethgnepena2021(request, id, subid,varid):
	infopaletpr = InfoPaletHgNepena2022.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/higo/infopalethgnepena2021.html', context)


def crearinfopalethgnepena2021(request, id, subid,varid):
	form =  infopalethgnepena2021form(request.POST or None)
	palet1 = GuiaDetallesAthosHgNepena2022.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosHgNepena2022,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathoshgnepena2021', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2021/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/higo/nuevoinfopalethgnepena2021.html', context)

def editarinfopalethgnepena2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletHgNepena2022, id=varid)

	palet1 = GuiaDetallesAthosHgNepena2022.objects.get(id=catid)
	palet2 = InfoPaletHgNepena2022.objects.get(id=varid)
	form = infopalethgnepena2021form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopalethgnepena2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/higo/nuevoinfopalethgnepena2021.html', context)



def printpalethgnepena2021(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletHgNepena2022.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/higo/printpalethgnepena2021.html',context)




def crearalmacenacopiohgnepena2021(request,id):
	form = almacenacopiohgnepena2021form(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoalmacenacopiohgnepena2021.html', context)

def editaralmacenacopiohgnepena2021(request, id, subid):
	sub_campo = get_object_or_404(AlmacenAcopioHgNepena2022, id=subid)
	context = {"form":form}
	if request.method=='POST':
		form = almacenacopiohgnepena2021form(request.POST or None, instance=sub_campo)
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('acopio_athos_04', id)
	return render(request, 'athos/acopio_athos/higo/nuevoalmacenacopiohgnepena2021.html', context)



