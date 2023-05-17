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

from apps.planta.higo_planta.models import LanzadoPaletasDtIca2022
from apps.planta.higo_planta.forms import lanzadopaletasdtica2022form


# Create your views here.

def plantadatil(request, id):

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context136={"ubicacion_plantapr":ubicacion_plantapr, "id":id}

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context137={"ubicacion_plantapr":ubicacion_plantapr, "id":id}


	if (id==136):
		return render(request, 'athos/planta/higo/ubicacionplanta1.html', context136)
	else:
		if (id==137):
			return render(request, 'athos/planta/higo/ubicacionplanta2.html', context137)
		

def recepcionpaletasdtica2022(request, id, subid):

	lpralpr = LanzadoPaletasDtIca2022.objects.filter(anexo_ubicacion_id=subid,estado_id=1)
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/higo/recepcionpaletasdtica2022.html', context)
	
def crearrecepcionpaletasdtica2022(request, id, subid):
	form = lanzadopaletasdtica2022form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearrecepcionpaletasdtica2022',id, subid)
	return render(request, 'athos/planta/higo/nuevorecepcionpaletasdtica2022.html', context)

#editar recepcion palet
def editarrecepcionpaletasdtica2022(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasDtIca2022, id=varid)
	form = lanzadopaletasdtica2022form(request.POST or None, instance=sub_campo)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('recepcionpaletasdtica2022', id, subid)
	return render(request, 'athos/planta/higo/editarrecepcionpaletasdtica2022.html', context)






def LanzadoPaletasDtIca2022(request, id, subid):

	lpralpr = LanzadoPaletasDtIca2022.objects.filter(anexo_ubicacion_id=subid, estado_id=1).order_by("-fecha_hora_creacion")
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/higo/lanzadopaletasrealdtica2022.html', context)

# crear recepcion-palet


def crearLanzadoPaletasDtIca2022(request, id, subid):
	form = lanzadopaletasdtica2022form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearLanzadoPaletasDtIca2022',id, subid)
	return render(request, 'athos/planta/higo/nuevolanzadopaletasrealdtica2022.html', context)


def editarLanzadoPaletasDtIca2022(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasDtIca2022, id=varid)
	form = lanzadopaletasdtica2022form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('LanzadoPaletasDtIca2022', id, subid)
	return render(request, 'athos/planta/higo/nuevolanzadopaletasrealdtica2022.html', context)

