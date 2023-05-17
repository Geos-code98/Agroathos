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

from apps.acopio_athos.datil.models import GuiaAthosDtIca2022
from apps.acopio_athos.datil.forms import guiaathosdt2021form

from apps.acopio_athos.datil.models import GuiaDetallesAthosDtIca2022
from apps.acopio_athos.datil.forms import guiadetallesathosdt2021form

from apps.acopio_athos.datil.models import InfoPaletDtIca2022
from apps.acopio_athos.datil.forms import infopaletdt2021form

from apps.menu.models import ejezona
from apps.menu.models import AlmacenesAthos
from apps.menu.models import PlacasVehiculares
from apps.menu.models import ChoferesVehiculos
from apps.menu.models import LugarAthos
from apps.menu.models import MaterialAcopio
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


def acopio_athos_02(request, id):

	if request.user.username=='rportal':
		guiaathospr=GuiaAthosDtIca2022.objects.all().order_by("-fecha_hora_creacion")[:500]
		context104={"guiaathospr":guiaathospr, "id":id}
	else:
		guiaathospr=GuiaAthosDtIca2022.objects.all().order_by("-fecha_hora_creacion")[:500]
		context104={"guiaathospr":guiaathospr, "id":id}


	if(id==104):
		return render(request, 'athos/acopio_athos/datil/guiaathosdt2021.html',context104)
																																							


def crearguiaathosdt2021(request, id):
	form = guiaathosdt2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_02', id)
	return render(request, 'athos/acopio_athos/datil/nuevoguiaathosdt2021.html', context)


def editarguiaathosdt2021(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosDtIca2022, id=subid)
	form = guiaathosdt2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_02', id)
	return render(request, 'athos/acopio_athos/datil/editarguiaathosdt2021.html', context)


def guiadetallesathosdt2021(request, id, subid):

	guiadetallespr=GuiaDetallesAthosDtIca2022.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/datil/guiadetallesathosdt2021.html', context)


def crearguiadetallesathosdt2021(request, id, subid):
	guiazona=GuiaAthosDtIca2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosDtIca2022.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathosdt2021form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosDtIca2022,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathosdt2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/datil/nuevoguiadetallesathosdt2021.html', context)


def editarguiadetallesathosdt2021(request, id, subid,varid):
	guiazona=GuiaAthosDtIca2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosDtIca2022.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosDtIca2022, id=varid)
	form = guiadetallesathosdt2021form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathosdt2021', id, subid)
	return render(request, 'athos/acopio_athos/datil/editarguiadetallesathosdt2021.html', context)


def infopaletdt2021(request, id, subid,varid):
	infopaletpr = InfoPaletDtIca2022.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/datil/infopaletdt2021.html', context)


def crearinfopaletdt2021(request, id, subid,varid):
	form =  infopaletdt2021form(request.POST or None)
	palet1 = GuiaDetallesAthosDtIca2022.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosDtIca2022,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathosdt2021', id, subid)
		else:
			url = "/athos/nuevoinfopalet-dt2021/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/datil/nuevoinfopaletdt2021.html', context)

def editarinfopaletdt2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletDtIca2022, id=varid)

	palet1 = GuiaDetallesAthosDtIca2022.objects.get(id=catid)
	palet2 = InfoPaletDtIca2022.objects.get(id=varid)
	form = infopaletdt2021form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopaletdt2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/datil/nuevoinfopaletdt2021.html', context)



def printpaletdt2021(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletDtIca2022.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/datil/printpaletdt2021.html',context)