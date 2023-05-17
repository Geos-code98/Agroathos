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

from apps.planta.higo_planta.models import LanzadoPaletasHgNep2021
from apps.planta.higo_planta.forms import lanzadopaletashgnep2021form


# Create your views here.

def plantahigo(request, id):

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context136={"ubicacion_plantapr":ubicacion_plantapr, "id":id}

	ubicacion_plantapr=UbicacionPlanta.objects.filter(anexo_estado=1)
	context137={"ubicacion_plantapr":ubicacion_plantapr, "id":id}


	if (id==136):
		return render(request, 'athos/planta/higo/ubicacionplanta1.html', context136)
	else:
		if (id==137):
			return render(request, 'athos/planta/higo/ubicacionplanta2.html', context137)
		





def recepcionpaletashgnep2021(request, id, subid):

	lpralpr = LanzadoPaletasHgNep2021.objects.filter(anexo_ubicacion_id=subid,estado_id=1)
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/higo/recepcionpaletashgnep2021.html', context)
	
def crearrecepcionpaletashgnep2021(request, id, subid):
	form = lanzadopaletashgnep2021form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearrecepcionpaletashgnep2021',id, subid)
	return render(request, 'athos/planta/higo/nuevorecepcionpaletashgnep2021.html', context)

#editar recepcion palet
def editarrecepcionpaletashgnep2021(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasHgNep2021, id=varid)
	form = lanzadopaletashgnep2021form(request.POST or None, instance=sub_campo)
	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('recepcionpaletashgnep2021', id, subid)
	return render(request, 'athos/planta/higo/editarrecepcionpaletashgnep2021.html', context)






def lanzadopaletashgnep2021(request, id, subid):

	lpralpr = LanzadoPaletasHgNep2021.objects.filter(anexo_ubicacion_id=subid, estado_id=1).order_by("-fecha_hora_creacion")
	context = {"lpralpr":lpralpr, "id":id, "subid":subid}
	return render(request, 'athos/planta/higo/lanzadopaletasrealhgnep2021.html', context)

# crear recepcion-palet


def crearlanzadopaletashgnep2021(request, id, subid):
	form = lanzadopaletashgnep2021form(request.POST or None)
	context = {"form":form,"id":id,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionPlanta,id=subid)
			result.anexo_ubicacion = progravar
			result.save()
			return redirect('crearlanzadopaletashgnep2021',id, subid)
	return render(request, 'athos/planta/higo/nuevolanzadopaletasrealhgnep2021.html', context)


def editarlanzadopaletashgnep2021(request, id, subid,varid):
	sub_campo = get_object_or_404(LanzadoPaletasHgNep2021, id=varid)
	form = lanzadopaletashgnep2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('lanzadopaletashgnep2021', id, subid)
	return render(request, 'athos/planta/higo/nuevolanzadopaletasrealhgnep2021.html', context)

