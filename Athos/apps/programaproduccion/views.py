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

from apps.programaproduccion.models import Grupos
from apps.programaproduccion.forms import gruposform 

from apps.programaproduccion.models import SubGrupos
from apps.programaproduccion.forms import subgruposform 

from apps.programaproduccion.models import Hitos
from apps.programaproduccion.forms import hitosform 

from apps.programaproduccion.models import SubHitos
from apps.programaproduccion.forms import subhitosform 

# Create your views here.

def programaproduccion(request, id):

	grupospr = Grupos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context100 = {"grupospr":grupospr, "id":id}

	subgrupospr = SubGrupos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context101 = {"subgrupospr":subgrupospr, "id":id}

	hitospr = Hitos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context102 = {"hitospr":hitospr, "id":id}

	subhitospr = SubHitos.objects.all().order_by("-fecha_hora_creacion")[:250]
	context103 = {"subhitospr":subhitospr, "id":id}


	if (id==100):
		return render(request, 'athos/programaproduccion/grupos.html', context100)
	else:
		if (id==101):
			return render(request, 'athos/programaproduccion/subgrupos.html', context101)
		else:
			if (id==102):
				return render(request, 'athos/programaproduccion/hitos.html', context102)
			else:
				if (id==103):
					return render(request, 'athos/programaproduccion/subhitos.html', context103)




def creargrupos(request, id):

	form = gruposform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevogrupos.html', context)


def editargrupos(request, id, subid):
	sub_campo = get_object_or_404(Grupos, id=subid)
	form = gruposform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevogrupos.html', context)


def crearsubgrupos(request, id):

	form = subgruposform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevosubgrupos.html', context)


def editarsubgrupos(request, id, subid):
	sub_campo = get_object_or_404(SubGrupos, id=subid)
	form = subgruposform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevosubgrupos.html', context)



def crearhitos(request, id):

	form = hitosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevohitos.html', context)


def editarhitos(request, id, subid):
	sub_campo = get_object_or_404(Hitos, id=subid)
	form = hitosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevohitos.html', context)


def crearsubhitos(request, id):

	form = subhitosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevosubhitos.html', context)


def editarsubhitos(request, id, subid):
	sub_campo = get_object_or_404(SubHitos, id=subid)
	form = subhitosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('programaproduccion', id)
	return render(request, 'athos/programaproduccion/nuevosubhitos.html', context)



def load_subgrupo(request, id):
	subgrupo = list(Grupos.objects.get(id=id).AnexoGruposPP.all().values('id','desc'))
	return JsonResponse(subgrupo,safe=False)

def load_hito(request, id):
	hito = list(SubGrupos.objects.get(id=id).AnexoSubGruposPP.all().values('id','desc'))
	return JsonResponse(hito,safe=False)

def load_subhito(request, id):
	subhito = list(Hitos.objects.get(id=id).AnexoHitosPP.all().values('id','desc'))
	return JsonResponse(subhito,safe=False)