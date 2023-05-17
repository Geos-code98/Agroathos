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

from apps.capacitaciones.models import EncuestaCapacitacionNew
from apps.capacitaciones.forms import encuestacapacitacionnewform

from apps.menu.models import ejezona
# Create your views here.

def capacitaciones(request, id):


	if request.user.is_superuser:
		encuestapr = EncuestaCapacitacionNew.objects.all().order_by("-fecha_hora_creacion")[:250]
		context126 = {"encuestapr":encuestapr, "id":id}
	else:
		encuestapr = EncuestaCapacitacionNew.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context126 = {"encuestapr":encuestapr, "id":id}

	if (id==126):
		return render(request, 'athos/capacitaciones/encuestacapacitacion.html', context126)


def load_capacitaciones(request, id):
	capa = list(ejezona.objects.get(id=id).Zona_Capacitacion.all().values('id','codigoacta'))
	return JsonResponse(capa,safe=False)



def crearencuestacapacitacion(request, id):

	form = encuestacapacitacionnewform(request.POST or None,request.FILES)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion_id = 1
			result.save()
			return redirect('graciascapacitacion', id)
	return render(request, 'athos/capacitaciones/nuevoencuestacapacitacion.html', context)


def editarencuestacapacitacion(request, id, subid):
	sub_campo = get_object_or_404(EncuestaCapacitacionNew, id=subid)
	form = encuestacapacitacionnewform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('capacitaciones', id)
	return render(request, 'athos/capacitaciones/nuevoencuestacapacitacion.html', context)

def graciascapacitacion(request, id):
	

	context = {"id":id}
	return render(request, 'athos/capacitaciones/graciascapacitacion.html',context)
