
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

from apps.acopio.models import ModEnfriado
from apps.acopio.forms import modenfriadoform
from apps.acopio.models import ModEnfriado2022
from apps.acopio.forms import modenfriado2022form

from apps.acopio.models import ConfirmacionModEnfriado2022
from apps.acopio.forms import confirmacionmodenfriado2022form
from apps.acopio.models import ConfirmacionTicketModEnfriado2022
from apps.acopio.forms import confirmacionticketmodenfriado2022form
from apps.acopio.models import RegistroTemperaturaModEnfriado2022
from apps.acopio.forms import registrotemperaturamodenfriado2022form
from apps.acopio.models import TomaDatosModEnfriado2022
from apps.acopio.forms import tomadatosmodenfriado2022form

from apps.acopio.models import DistribucionEnfriado
from apps.acopio.forms import distribucionenfriadoform


from apps.acopio.models import TemperaturaEnfriado
from apps.acopio.forms import temperaturaenfriadoform


from apps.acopio.models import DescarteAthos
from apps.acopio.forms import descarteathosform

from apps.acopio.models import SalidaDescarte 
from apps.acopio.forms import salidadescarteform


#campaña2021
from apps.acopio.models import ModEnfriadoArCaraz2021
from apps.acopio.forms import modenfriadoarcaraz2021form

from apps.acopio.models import DistribucionEnfriadoArCaraz2021
from apps.acopio.forms import distribucionenfriadoarcaraz2021form

from apps.acopio.models import TemperaturaEnfriadoArCaraz2021
from apps.acopio.forms import temperaturaenfriadoarcaraz2021form

#CAMPAÑA 2021 02
from apps.acopio.models import ModEnfriadoArCaraz202102
from apps.acopio.forms import modenfriadoarcaraz202102form

from apps.acopio.models import DistribucionEnfriadoArCaraz202102
from apps.acopio.forms import distribucionenfriadoarcaraz202102form

from apps.acopio.models import TemperaturaEnfriadoArCaraz202102
from apps.acopio.forms import temperaturaenfriadoarcaraz202102form

#DESCARTE PL HG 2022
from apps.acopio.models import DescartePlantaHgAthos
from apps.acopio.forms import descarteplantahgathosform


# Create your views here.
def campos(request, id):

	if request.user.is_superuser:
		enfriadopr = ModEnfriado2022.objects.all().order_by("-fecha_hora_creacion")[:500]
		context45 = {"enfriadopr":enfriadopr, "id":id}
	else:
		enfriadopr = ModEnfriado2022.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:200]
		context45 = {"enfriadopr":enfriadopr, "id":id}

	descartepr = DescarteAthos.objects.all().order_by("-fecha_hora_creacion")
	context52 = {"descartepr":descartepr, "id":id}

	salidapr = SalidaDescarte.objects.all().order_by("-fecha_hora_creacion")
	context98 = {"salidapr":salidapr, "id":id}

	descartepr = DescartePlantaHgAthos.objects.all().order_by("-fecha_hora_creacion")
	context165 = {"descartepr":descartepr, "id":id}


	if (id==45 or id==127):
		return render(request, 'athos/enfriadoathos.html', context45)
	else:
		if (id==52):
			return render(request, 'athos/descarteathos.html', context52)
		else:
			if (id==98):
				return render(request, 'athos/acopio_athos/salidadescarte.html', context98)
			else:
				if (id==165):
					return render(request, 'athos/descarteplantahgathos.html', context165)

def crearenfriado(request,id):
	form = modenfriado2022form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campos',id )
	return render(request, 'athos/nuevoenfriadoathos.html', context)

def editarenfriado(request, id, subid):
	sub_campo = get_object_or_404(ModEnfriado2022, id=subid)
	form = modenfriado2022form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campos', id)
	return render(request, 'athos/editarenfriadoathos.html', context)

def confirmacionenfriado(request, id, subid):
	confirmacionpr = ConfirmacionModEnfriado2022.objects.filter(anexo_enfriado_id=subid)
	context = {"confirmacionpr":confirmacionpr, "id":id, "subid":subid}
	return render(request, 'athos/enfriadoathosconfirmacion.html', context)

def crearconfirmacionenfriado(request, id, subid):
	form = confirmacionmodenfriado2022form(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ModEnfriado2022,id=subid)
			result.anexo_enfriado = progra
			result.save()
			return redirect('confirmacionenfriado',id, subid)
	return render(request, 'athos/nuevoconfirmacionenfriado.html', context)

def editarconfirmacionenfriado(request, id, subid,varid):
	sub_campo = get_object_or_404(ConfirmacionModEnfriado2022, id=varid)
	form = confirmacionmodenfriado2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('confirmacionenfriado', id, subid)
	return render(request, 'athos/nuevoconfirmacionenfriado.html', context)

def confirmacionticketenfriado(request, id, subid, varid):
	confirmaciontpr = ConfirmacionTicketModEnfriado2022.objects.filter(anexo_palet_id=varid)
	context = {"confirmaciontpr":confirmaciontpr, "id":id, "subid":subid,"varid":varid}
	return render(request, 'athos/enfriadoathosconfirmacionticket.html', context)

def crearconfirmacionticketenfriado(request,id,subid,varid):
	form = confirmacionticketmodenfriado2022form(request.POST or None)
	context = {"form":form, "varid":varid, "paletid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ConfirmacionModEnfriado2022,id=varid)
			result.anexo_palet = progra
			result.save()
			return redirect('crearconfirmacionticketenfriado',id, subid, varid)
	return render(request, 'athos/nuevoconfirmacionticketenfriado.html', context)

def editarconfirmacionticketenfriado(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(ConfirmacionTicketModEnfriado2022, id=varid)
	form = confirmacionticketmodenfriado2022form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('confirmacionticketenfriado', id, subid, catid)
	return render(request, 'athos/editarconfirmacionticketenfriado.html', context)

def registrotemperatura(request, id, subid):
	temperaturapr = RegistroTemperaturaModEnfriado2022.objects.filter(anexo_enfriado_id=subid)
	context = {"temperaturapr":temperaturapr, "id":id, "subid":subid}
	return render(request, 'athos/enfriadoathostemperatura.html', context)

def crearregistrotemperaturaenfriado(request, id, subid):
	form = registrotemperaturamodenfriado2022form(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ModEnfriado2022,id=subid)
			result.anexo_enfriado = progra
			result.save()
			return redirect('registrotemperatura',id, subid)
	return render(request, 'athos/nuevoregistrotemperatura.html', context)

def editarregistrotemperaturaenfriado(request, id, subid,varid):
	sub_campo = get_object_or_404(RegistroTemperaturaModEnfriado2022, id=varid)
	form = registrotemperaturamodenfriado2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('registrotemperatura', id, subid)
	return render(request, 'athos/nuevoregistrotemperatura.html', context)

def tomadatosenfriado(request, id, subid, varid):
	tomadatospr = TomaDatosModEnfriado2022.objects.filter(anexo_temperatura_id=varid)
	context = {"tomadatospr":tomadatospr, "id":id, "subid":subid,"varid":varid}
	return render(request, 'athos/enfriadoathostomadatos.html', context)

def creartomadatosenfriado(request, id, subid,varid):
	form = tomadatosmodenfriado2022form(request.POST or None)
	context = {"form":form, "varid":varid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(RegistroTemperaturaModEnfriado2022,id=varid)
			result.anexo_temperatura = progra
			result.save()
			return redirect('tomadatosenfriado',id, subid, varid)
	return render(request, 'athos/nuevotomadatosenfriado.html', context)

def editartomadatosenfriado(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(TomaDatosModEnfriado2022, id=varid)
	form = tomadatosmodenfriado2022form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('tomadatosenfriado', id, subid, catid)
	return render(request, 'athos/nuevotomadatosenfriado.html', context)




def distribucionenfriado(request, id, subid):
	distribucionpr = DistribucionEnfriadoArCaraz202102.objects.filter(anexo_enfriado_id=subid)
	context = {"distribucionpr":distribucionpr, "id":id, "subid":subid}
	return render(request, 'athos/distribucionenfriado.html', context)

def creardistribucionenfriado(request, id, subid):
	form = distribucionenfriadoarcaraz202102form(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ModEnfriadoArCaraz202102,id=subid)
			result.anexo_enfriado = progra
			result.save()
			return redirect('distribucionenfriado',id, subid)
	return render(request, 'athos/nuevodistribucionenfriado.html', context)

def editardistribucionenfriado(request, id, subid,varid):
	sub_campo = get_object_or_404(DistribucionEnfriadoArCaraz202102, id=varid)
	form = distribucionenfriadoarcaraz202102form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('distribucionenfriado', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevodistribucionenfriado.html', context)



def temperaturaenfriado(request, id, subid,varid):
	temperaturapr = TemperaturaEnfriadoArCaraz202102.objects.filter(anexo_temperatura_id=varid)
	context = {"temperaturapr":temperaturapr, "id":id, "subid":subid,"varid":varid}
	print(context)
	return render(request, 'athos/temperaturaenfriado.html', context)


def creartemperaturaenfriado(request, id, subid,varid):
	form =  temperaturaenfriadoarcaraz202102form(request.POST or None)
	context = {"form":form,"varid":varid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(DistribucionEnfriadoArCaraz202102,id=varid)
				result.anexo_temperatura = progravar
				result.save()

				return redirect('temperaturaenfriado', id, subid, varid)
	return render(request, 'athos/nuevotemperaturaenfriado.html', context)

def editartemperaturaenfriado(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(TemperaturaEnfriadoArCaraz202102, id=varid)

	form = temperaturaenfriadoarcaraz202102form(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('distribucionenfriado', id, subid, catid)
	return render(request, 'athos/nuevotemperaturaenfriado.html', context)

def creardescarteathos(request,id):
	form = descarteathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campos',id )
	return render(request, 'athos/nuevodescarteathos.html', context)

def editardescarteathos(request, id, subid):
	sub_campo = get_object_or_404(DescarteAthos, id=subid)
	form = descarteathosform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campos', id)
	return render(request, 'athos/nuevodescarteathos.html', context)



def crearsalidadescarte(request,id):

	form = salidadescarteform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campos',id )
	return render(request, 'athos/acopio_athos/nuevosalidadescarte.html', context)

def editarsalidadescarte(request, id, subid):
	sub_campo = get_object_or_404(SalidaDescarte, id=subid)
	form = salidadescarteform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campos', id)
	return render(request, 'athos/acopio_athos/nuevosalidadescarte.html', context)

#DESCARTE PL HG 2022
def creardescarteplantahgathos(request,id):
	form = descarteplantahgathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('campos',id )
	return render(request, 'athos/nuevodescarteplantahgathos.html', context)

def editardescarteplantahgathos(request, id, subid):
	sub_campo = get_object_or_404(DescartePlantaHgAthos, id=subid)
	form = descarteplantahgathosform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campos', id)
	return render(request, 'athos/editardescarteplantahgathos.html', context)