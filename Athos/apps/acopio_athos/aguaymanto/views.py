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

from apps.acopio_athos.aguaymanto.models import GuiaAthosAgCaraz2022
from apps.acopio_athos.aguaymanto.forms import guiaathosagcaraz2022form
from apps.acopio_athos.aguaymanto.models import GuiaDetallesAthosAgCaraz2022
from apps.acopio_athos.aguaymanto.forms import guiadetallesathosagcaraz2022form
from apps.acopio_athos.aguaymanto.models import InfoPaletAgCaraz2022
from apps.acopio_athos.aguaymanto.forms import infopaletagcaraz2022form

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

def acopio_athos_05(request, id):

	guiaathospr=GuiaAthosAgCaraz2022.objects.all().order_by("-fecha_hora_creacion")[:50]
	context173={"guiaathospr":guiaathospr, "id":id}
	
	if(id==173):
		return render(request, 'athos/acopio_athos/aguaymanto/guiaathosagcaraz2022.html',context173)

def crearguiaathosagcaraz2022(request, id):
	form = guiaathosagcaraz2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_05', id)
	return render(request, 'athos/acopio_athos/aguaymanto/nuevoguiaathosagcaraz2022.html', context)

def editarguiaathosagcaraz2022(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosAgCaraz2022, id=subid)
	form = guiaathosagcaraz2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_05', id)
	return render(request, 'athos/acopio_athos/aguaymanto/editarguiaathosagcaraz2022.html', context)

def guiadetallesathosagcaraz2022(request, id, subid):
	guiadetallespr=GuiaDetallesAthosAgCaraz2022.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/aguaymanto/guiadetallesathosagcaraz2022.html', context)

def crearguiadetallesathosagcaraz2022(request, id, subid):
	guiazona=GuiaAthosAgCaraz2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosAgCaraz2022.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathosagcaraz2022form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosAgCaraz2022,id=subid)
			result.anexo_guia = progravar
			result.save()
			return redirect('guiadetallesathosagcaraz2022',id,subid)
	return render(request, 'athos/acopio_athos/aguaymanto/nuevoguiadetallesathosagcaraz2022.html', context)

def editarguiadetallesathosagcaraz2022(request, id, subid,varid):
	guiazona=GuiaAthosAgCaraz2022.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosAgCaraz2022.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosAgCaraz2022, id=varid)
	form = guiadetallesathosagcaraz2022form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathosagcaraz2022', id, subid)
	return render(request, 'athos/acopio_athos/aguaymanto/editarguiadetallesathosagcaraz2022.html', context)

def infopaletagcaraz2022(request, id, subid,varid):
	infopaletpr = InfoPaletAgCaraz2022.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	return render(request, 'athos/acopio_athos/aguaymanto/infopaletagcaraz2022.html', context)

def crearinfopaletagcaraz2022(request, id, subid,varid):
	form =  infopaletagcaraz2022form(request.POST or None)
	infopep = GuiaDetallesAthosAgCaraz2022.objects.get(id=varid)
	palet1 = GuiaDetallesAthosAgCaraz2022.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1,"infopep":infopep}
	if request.method=='POST':
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosAgCaraz2022,id=varid)
				result.anexo_guiad = progravar
				result.save()
				return redirect('guiadetallesathosagcaraz2022', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2020/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,palet1.id)
			return redirect(url)
	return render(request, 'athos/acopio_athos/aguaymanto/nuevoinfopaletagcaraz2022.html', context)

def editarinfopaletagcaraz2022(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletAgCaraz2022, id=varid)

	palet1 = GuiaDetallesAthosAgCaraz2022.objects.get(id=catid)
	palet2 = InfoPaletAgCaraz2022.objects.get(id=varid)
	form = infopaletagcaraz2022form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopaletagcaraz2022', id, subid, catid)
	return render(request, 'athos/acopio_athos/aguaymanto/nuevoinfopaletagcaraz2022.html', context)

#MODELO DE IMPRESION 
def printpaletagcaraz2022(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletAgCaraz2022.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/aguaymanto/printpaletagcaraz2022.html',context)
