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

from apps.acopio_athos.arandano.models import GuiaAthosArCaraz2021
from apps.acopio_athos.arandano.forms import guiaathosarcaraz2021form

from apps.acopio_athos.arandano.models import GuiaDetallesAthosArCaraz2021
from apps.acopio_athos.arandano.forms import guiadetallesathosarcaraz2021form

from apps.acopio_athos.arandano.models import InfoPaletArCaraz2021
from apps.acopio_athos.arandano.forms import infopaletarcaraz2021form


from apps.acopio_athos.arandano.models import GuiaAthosArIca2021
from apps.acopio_athos.arandano.forms import guiaathosarica2021form

from apps.acopio_athos.arandano.models import GuiaDetallesAthosArIca2021
from apps.acopio_athos.arandano.forms import guiadetallesathosarica2021form

from apps.acopio_athos.arandano.models import InfoPaletArIca2021
from apps.acopio_athos.arandano.forms import infopaletarica2021form



#campaña2021-ICA-ENFRIADO
from apps.acopio_athos.arandano.models import ModEnfriadoArIca2021
from apps.acopio_athos.arandano.forms import modenfriadoarica2021form

from apps.acopio_athos.arandano.models import DistribucionEnfriadoArIca2021
from apps.acopio_athos.arandano.forms import distribucionenfriadoarica2021form

from apps.acopio_athos.arandano.models import TemperaturaEnfriadoArIca2021
from apps.acopio_athos.arandano.forms import temperaturaenfriadoarica2021form


#CAMPAÑA 202202 - CARAZ
from apps.acopio_athos.arandano.models import GuiaAthosArCaraz202202
from apps.acopio_athos.arandano.forms import guiaathosarcaraz202202form
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArCaraz202202
from apps.acopio_athos.arandano.forms import guiadetallesathosarcaraz202202form
from apps.acopio_athos.arandano.models import InfoPaletArCaraz202202
from apps.acopio_athos.arandano.forms import infopaletarcaraz202202form

#CAMPAÑA 202202 - ICA
from apps.acopio_athos.arandano.models import GuiaAthosArIca202202
from apps.acopio_athos.arandano.forms import guiaathosarica202202form
from apps.acopio_athos.arandano.models import GuiaDetallesAthosArIca202202
from apps.acopio_athos.arandano.forms import guiadetallesathosarica202202form
from apps.acopio_athos.arandano.models import InfoGuiaAthosArIca202202
from apps.acopio_athos.arandano.forms import infoguiaathosarica202202form
from apps.acopio_athos.arandano.models import InfoPaletArIca202202
from apps.acopio_athos.arandano.forms import infopaletarica202202form


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


def acopio_athos_03(request, id):

	guiaathospr=GuiaAthosArCaraz202202.objects.all().order_by("-fecha_hora_creacion")[:50]
	context128={"guiaathospr":guiaathospr, "id":id}

	guiaathospr=GuiaAthosArIca202202.objects.all().order_by("-fecha_hora_creacion")[:50]
	context129={"guiaathospr":guiaathospr, "id":id}

	enfriadopr = ModEnfriadoArIca2021.objects.all().order_by("-fecha_hora_creacion")[:50]
	context131 = {"enfriadopr":enfriadopr, "id":id}
	
	if(id==128):
		return render(request, 'athos/acopio_athos/arandano/guiaathosgr2020.html',context128)
	else:
		if(id==129):
			return render(request, 'athos/acopio_athos/arandano/guiaathosarica2021.html',context129)
		else:
			if(id==131):
				return render(request, 'athos/acopio_athos/arandano/enfriadoathos.html',context131)
	
def crearguiaathosarcaraz2021(request, id):
	form = guiaathosarcaraz202202form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_03', id)
	return render(request, 'athos/acopio_athos/arandano/nuevoguiaathosgr2020.html', context)

def editarguiaathosarcaraz2021(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosArCaraz202202, id=subid)
	form = guiaathosarcaraz202202form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_03', id)
	return render(request, 'athos/acopio_athos/arandano/editarguiaathosgr2020.html', context)

def guiadetallesathosarcaraz2021(request, id, subid):
	guiadetallespr=GuiaDetallesAthosArCaraz202202.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/arandano/guiadetallesathosgr2020.html', context)

def crearguiadetallesathosarcaraz2021(request, id, subid):
	guiazona=GuiaAthosArCaraz202202.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosArCaraz202202.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathosarcaraz202202form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosArCaraz202202,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathosarcaraz2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/arandano/nuevoguiadetallesathosgr2020.html', context)


def editarguiadetallesathosarcaraz2021(request, id, subid,varid):
	guiazona=GuiaAthosArCaraz202202.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosArCaraz202202.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosArCaraz202202, id=varid)
	form = guiadetallesathosarcaraz202202form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathosarcaraz2021', id, subid)
	return render(request, 'athos/acopio_athos/arandano/editarguiadetallesathosgr2020.html', context)


def infopaletarcaraz2021(request, id, subid,varid):
	infopaletpr = InfoPaletArCaraz202202.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/arandano/infopaletgr2020.html', context)


def crearinfopaletarcaraz2021(request, id, subid,varid):
	form =  infopaletarcaraz202202form(request.POST or None)
	infopep = GuiaDetallesAthosArCaraz202202.objects.get(id=varid)
	palet1 = GuiaDetallesAthosArCaraz202202.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1,"infopep":infopep}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosArCaraz202202,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathosarcaraz2021', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2020/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/arandano/nuevoinfopaletgr2020.html', context)

def editarinfopaletarcaraz2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletArCaraz202202, id=varid)

	palet1 = GuiaDetallesAthosArCaraz202202.objects.get(id=catid)
	palet2 = InfoPaletArCaraz202202.objects.get(id=varid)
	form = infopaletarcaraz202202form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopaletarcaraz2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/arandano/nuevoinfopaletgr2020.html', context)







#ARANDANO--ICA
def crearguiaathosarica2021(request, id):
	form = guiaathosarica202202form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_03', id)
	return render(request, 'athos/acopio_athos/arandano/nuevoguiaathosarica2021.html', context)


def editarguiaathosarica2021(request, id, subid):
	sub_campo = get_object_or_404(GuiaAthosArIca202202, id=subid)
	form = guiaathosarica202202form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_03', id)
	return render(request, 'athos/acopio_athos/arandano/editarguiaathosarica2021.html', context)


def guiadetallesathosarica2021(request, id, subid):

	guiadetallespr=GuiaDetallesAthosArIca202202.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"guiadetallespr":guiadetallespr, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/arandano/guiadetallesathosarica2021.html', context)


def crearguiadetallesathosarica2021(request, id, subid):
	guiazona=GuiaAthosArIca202202.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosArIca202202.objects.get(id=subid).anexo_fundo

	form =  guiadetallesathosarica202202form(request.POST or None,anexo_zona=guiazona, anexo_fundo=guiafundo)
	palet1 = MaterialAcopio.objects.all()
	print (palet1)
	context = {"form":form,"subid":subid ,"palet1":palet1}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosArIca202202,id=subid)
			result.anexo_guia = progravar
			result.save()
			print("is_valid2")

			return redirect('guiadetallesathosarica2021',id,subid)
	print(context)
	return render(request, 'athos/acopio_athos/arandano/nuevoguiadetallesathosarica2021.html', context)

def editarguiadetallesathosarica2021(request, id, subid,varid):
	guiazona=GuiaAthosArIca202202.objects.get(id=subid).anexo_zona
	guiafundo=GuiaAthosArIca202202.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(GuiaDetallesAthosArIca202202, id=varid)
	form = guiadetallesathosarica202202form(request.POST or None,anexo_zona=guiazona,anexo_fundo=guiafundo, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('guiadetallesathosarica2021', id, subid)
	return render(request, 'athos/acopio_athos/arandano/editarguiadetallesathosarica2021.html', context)


def infoguiaathosarica2022(request, id, subid):
	infoguias=InfoGuiaAthosArIca202202.objects.filter(anexo_guia_id=subid).order_by("-fecha_hora_creacion")
	context={"infoguias":infoguias, "id":id,"subid":subid}
	return render(request, 'athos/acopio_athos/arandano/infoguiaathosarica2022.html', context)

def crearinfoguiaathosarica2022(request, id, subid):
	form = infoguiaathosarica202202form(request.POST or None)
	context = {"form":form, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(GuiaAthosArIca202202,id=subid)
			result.anexo_guia = progravar
			result.save()
			return redirect('infoguiaathosarica2022', id, subid)
	return render(request, 'athos/acopio_athos/arandano/nuevoinfoguiaathosarica2022.html', context)

def editarinfoguiaathosarica2022(request, id, subid, varid):
	sub_campo = get_object_or_404(InfoGuiaAthosArIca202202, id=varid)
	form = infoguiaathosarica202202form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infoguiaathosarica2022', id, subid)
	return render(request, 'athos/acopio_athos/arandano/editarinfoguiaathosarica2022.html', context)

def infopaletarica2021(request, id, subid,varid):
	infopaletpr = InfoPaletArIca202202.objects.filter(anexo_guiad_id=varid)
	context = {"infopaletpr":infopaletpr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/arandano/infopaletarica2021.html', context)


def crearinfopaletarica2021(request, id, subid,varid):
	form =  infopaletarica202202form(request.POST or None)
	palet1 = GuiaDetallesAthosArIca202202.objects.get(id=varid)
	infopep = GuiaDetallesAthosArIca202202.objects.get(id=varid)
	context = {"form":form,"varid":varid,"palet1":palet1, "infopep":infopep}
	if request.method=='POST':
		print(request.POST.get('cant_jabas'))
		if int(request.POST.get('cant_jabas')) <= palet1.resto_jabas:
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(GuiaDetallesAthosArIca202202,id=varid)
				result.anexo_guiad = progravar
				result.save()

				return redirect('guiadetallesathosarica2021', id, subid)
		else:
			url = "/athos/nuevoinfopalet-gr2020/55/registro/{}/acopio/{}/crear".format(palet1.anexo_guia.id,
																				palet1.id)
			return redirect(url)
	print(context)
	return render(request, 'athos/acopio_athos/arandano/nuevoinfopaletarica2021.html', context)

def editarinfopaletarica2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(InfoPaletArIca202202, id=varid)
	palet1 = GuiaDetallesAthosArIca202202.objects.get(id=catid)
	palet2 = InfoPaletArIca202202.objects.get(id=varid)
	form = infopaletarica202202form(request.POST or None, instance=sub_campo)
	context = {"form":form,"palet1":palet1,"palet2":palet2}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('infopaletarica2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/arandano/nuevoinfopaletarica2021.html', context)



#MODELO DE IMPRESION 
def printpaletarcaraz2021(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletArCaraz202202.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/arandano/printpaletgr2020.html',context)


def printpaletarica2021(request, guia_id,guia_detalle_id,palet_id):
	palet = InfoPaletArIca202202.objects.get(id=palet_id)
	pep = palet.anexo_guiad.anexo_ubi_mmpp
	context = {"guia_id":guia_id, "guia_detalle_id":guia_detalle_id,"palet":palet,"pep":pep}
	return render(request, 'athos/acopio_athos/arandano/printpaletgr2020.html',context)


#ENFRIADO ICA 2021
def crearenfriadoarica2021(request,id):

	form = modenfriadoarica2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('acopio_athos_03',id )
	return render(request, 'athos/acopio_athos/arandano/nuevoenfriadoathos.html', context)

def editarenfriadoarica2021(request, id, subid):
	sub_campo = get_object_or_404(ModEnfriadoArIca2021, id=subid)
	form = modenfriadoarica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('acopio_athos_03', id)
	return render(request, 'athos/acopio_athos/arandano/nuevoenfriadoathos.html', context)

def distribucionenfriadoarica2021(request, id, subid):

	distribucionpr = DistribucionEnfriadoArIca2021.objects.filter(anexo_enfriado_id=subid)
	context = {"distribucionpr":distribucionpr, "id":id, "subid":subid}
	return render(request, 'athos/acopio_athos/arandano/distribucionenfriado.html', context)



def creardistribucionenfriadoarica2021(request, id, subid):
	form = distribucionenfriadoarica2021form(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ModEnfriadoArIca2021,id=subid)
			result.anexo_enfriado = progra
			result.save()
			return redirect('distribucionenfriadoarica2021',id, subid)
	return render(request, 'athos/acopio_athos/arandano/nuevodistribucionenfriado.html', context)

def editardistribucionenfriadoarica2021(request, id, subid,varid):
	sub_campo = get_object_or_404(DistribucionEnfriadoArIca021, id=varid)
	form = distribucionenfriadoarica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('distribucionenfriadoarica2021', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/acopio_athos/arandano/nuevodistribucionenfriado.html', context)



def temperaturaenfriadoarica2021(request, id, subid,varid):
	temperaturapr = TemperaturaEnfriadoArIca2021.objects.filter(anexo_temperatura_id=varid)
	context = {"temperaturapr":temperaturapr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/acopio_athos/arandano/temperaturaenfriado.html', context)


def creartemperaturaenfriadoarica2021(request, id, subid,varid):
	form =  temperaturaenfriadoarica2021form(request.POST or None)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(DistribucionEnfriadoArIca2021,id=varid)
				result.anexo_temperatura = progravar
				result.save()

				return redirect('temperaturaenfriadoarica2021', id, subid, varid)
	return render(request, 'athos/acopio_athos/arandano/nuevotemperaturaenfriado.html', context)

def editartemperaturaenfriadoarica2021(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(TemperaturaEnfriadoArIca2021, id=varid)

	form = temperaturaenfriadoarica2021form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('distribucionenfriadoarica2021', id, subid, catid)
	return render(request, 'athos/acopio_athos/arandano/nuevotemperaturaenfriado.html', context)
