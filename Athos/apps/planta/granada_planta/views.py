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
from django.contrib import auth

from apps.planta.granada_planta.models import UbicacionPlanta
from apps.planta.granada_planta.forms import ubicacionplantaform

from apps.planta.granada_planta.models import LanzadoPaletasGrIca2021
#campaña granada ica 2023
from apps.planta.granada_planta.models import LanzadoPaletasGrIca2023
from apps.planta.granada_planta.forms import lanzadopaletasgrica2023form

from apps.planta.granada_planta.models import LanzadoPaletasArIca2022
from apps.planta.granada_planta.forms import lanzadopaletasgrica2020form

from apps.planta.granada_planta.models import PrePaletizadoGrIca2020
from apps.planta.granada_planta.forms import prepaletizadogrica2020form

from apps.planta.granada_planta.models import DetallePrePaletizadoGrIca2020
from apps.planta.granada_planta.forms import detalleprepaletizadogrica2020form


# Create your views here.

def plantagranada(request, id):

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context96={"ubicacion_plantapr":ubicacion_plantapr, "id":id}

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context97={"ubicacion_plantapr":ubicacion_plantapr, "id":id}

	prepapr=PrePaletizadoGrIca2020.objects.all()
	context125={"prepapr":prepapr, "id":id}
	

	if (id==96):
		return render(request, 'athos/planta/granada/ubicacionplanta1.html', context96)
	else:
		if (id==97):
			return render(request, 'athos/planta/granada/ubicacionplanta2.html', context97)
		else:
			if (id==125):
				return render(request, 'athos/planta/granada/prepaletizadogrica2020.html', context125)


def crearubicacionplanta(request,id):
	form = ubicacionplantaform(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('plantagranada', id)
	return render(request, 'athos/planta/granada/nuevoubicacionplanta.html', context)

def editarubicacionplanta(request, id, subid):
	sub_campo = get_object_or_404(UbicacionPlanta, id=subid)
	context = {"form":form}
	if request.method=='POST':
		form = ubicacionplantaform(request.POST or None, instance=sub_campo)
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('plantagranada', id)
	
	return render(request, 'athos/planta/granada/nuevoubicacionplanta.html', context)




def recepcionpaletasgrica2020(request, id, subid):

	lpralpr = LanzadoPaletasArIca2022.objects.filter(anexo_ubicacion_id=subid,estado_id=1)
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/granada/recepcionpaletasgrica2020.html', context)
	
def crearrecepcionpaletasgrica2020(request, id, subid):
	form = lanzadopaletasgrica2020form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearrecepcionpaletasgrica2020',id, subid)
	return render(request, 'athos/planta/granada/nuevorecepcionpaletasgrica2020.html', context)

#editar recepcion palet
def editarrecepcionpaletasgrica2020(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasArIca2022, id=varid)
	form = lanzadopaletasgrica2020form(request.POST or None, instance=sub_campo)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('recepcionpaletasgrica2020', id, subid)
	return render(request, 'athos/planta/granada/editarrecepcionpaletasgrica2020.html', context)






def lanzadopaletasgrica2020(request, id, subid):

	lpralpr = LanzadoPaletasArIca2022.objects.filter(anexo_ubicacion_id=subid, estado_id=1).order_by("-fecha_hora_creacion")
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/granada/lanzadopaletasrealgrica2020.html', context)

# crear recepcion-palet


def crearlanzadopaletasgrica2020(request, id, subid):
	form = lanzadopaletasgrica2020form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearlanzadopaletasgrica2020',id, subid)
	return render(request, 'athos/planta/granada/nuevolanzadopaletasrealgrica2020.html', context)

def editarlanzadopaletasgrica2020(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasArIca2022, id=varid)
	form = lanzadopaletasgrica2020form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('lanzadopaletasgrica2020', id, subid)
	return render(request, 'athos/planta/granada/nuevolanzadopaletasrealgrica2020.html', context)


#campaña granada ica 2023
def recepcionpaletasgrica2023(request, id, subid):

	lpralpr = LanzadoPaletasGrIca2023.objects.filter(anexo_ubicacion_id=subid,estado_id=1)
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/granada/recepcionpaletasgrica2020.html', context)
	
def crearrecepcionpaletasgrica2023(request, id, subid):
	form = lanzadopaletasgrica2023form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearrecepcionpaletasgrica2023',id, subid)
	return render(request, 'athos/planta/granada/nuevorecepcionpaletasgrica2020.html', context)

#editar recepcion palet
def editarrecepcionpaletasgrica2023(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasGrIca2023, id=varid)
	form = lanzadopaletasgrica2023form(request.POST or None, instance=sub_campo)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('recepcionpaletasgrica2023', id, subid)
	return render(request, 'athos/planta/granada/editarrecepcionpaletasgrica2020.html', context)


def lanzadopaletasgrica2023(request, id, subid):

	lpralpr = LanzadoPaletasGrIca2023.objects.filter(anexo_ubicacion_id=subid, estado_id=1).order_by("-fecha_hora_creacion")
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/granada/lanzadopaletasrealgrica2020.html', context)

# crear recepcion-palet


def crearlanzadopaletasgrica2023(request, id, subid):
	form = lanzadopaletasgrica2023form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearlanzadopaletasgrica2023',id, subid)
	return render(request, 'athos/planta/granada/nuevolanzadopaletasrealgrica2020.html', context)

def editarlanzadopaletasgrica2023(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasGrIca2023, id=varid)
	form = lanzadopaletasgrica2023form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('lanzadopaletasgrica2023', id, subid)
	return render(request, 'athos/planta/granada/nuevolanzadopaletasrealgrica2020.html', context)

#####################################################################################################











def crearprepaletizadogrica2020(request,id):
	form = prepaletizadogrica2020form(request.POST or None)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('plantagranada', id)
	return render(request, 'athos/planta/granada/nuevoprepaletizadogrica2020.html', context)

def editarprepaletizadogrica2020(request, id, subid):
	sub_campo = get_object_or_404(PrePaletizadoGrIca2020, id=subid)
	form = prepaletizadogrica2020form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('plantagranada', id)
	return render(request, 'athos/planta/granada/editarprepaletizadogrica2020.html', context)


def confirmativaprepaletizadogrica2020(request, id, subid):
	sub_campo = get_object_or_404(PrePaletizadoGrIca2020, id=subid)
	form = prepaletizadogrica2020form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('plantagranada', id)
	return render(request, 'athos/planta/granada/confprepaletizadogrica2020.html', context)


def detalleprepaletizadogrica2020 (request, id, subid):

	detallepr=DetallePrePaletizadoGrIca2020.objects.filter(anexo_detalle_id=subid)
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/planta/granada/detalleprepaletizadogrica2020.html', context)


def creardetalleprepaletizadogrica2020(request, id, subid):
	saldo=PrePaletizadoGrIca2020.objects.get(id=subid).resto_cajas
	form = detalleprepaletizadogrica2020form(request.POST or None)

	context = {"form":form,"subid":subid,"saldo":saldo}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(PrePaletizadoGrIca2020,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('creardetalleprepaletizadogrica2020',id,subid)
	print(context)
	return render(request, 'athos/planta/granada/nuevodetalleprepaletizadogrica2020.html', context)



def editardetalleprepaletizadogrica2020(request, id, subid,varid):

	sub_campo = get_object_or_404(DetallePrePaletizadoGrIca2020, id=varid)
	form = detalleprepaletizadogrica2020form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleprepaletizadogrica2020', id, subid)
	return render(request, 'athos/planta/granada/nuevodetalleprepaletizadogrica2020.html', context)


def printprepaletizadotgr2020(request, prepa_id,guia_detalle_id):
	prepa = PrePaletizadoGrIca2020.objects.get(id=prepa_id)
	deta=DetallePrePaletizadoGrIca2020.objects.get(id=detalle_id)
	context = {"prepa_id":prepa_id, "detalle_id":detalle_id,"prepa":prepa,"deta":deta}
	return render(request, 'athos/planta/granada/printprepaletizadogr2020.html',context)