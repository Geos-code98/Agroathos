
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

from apps.prterminado.models import ProductoTerminado
from apps.prterminado.forms import prterminadoform

from apps.prterminado.models import TempProductoTerminado
from apps.prterminado.forms import tempprterminadoform
# Create your views here.

def prterminado(request, id):

	prterminadopr = ProductoTerminado.objects.all()
	context46 = {"prterminadopr":prterminadopr, "id":id}


	if (id==46):
		return render(request, 'athos/prterminado.html', context46)



def crearprterminado(request,id):

	form = prterminadoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('prterminado',id )
	return render(request, 'athos/nuevoprterminado.html', context)

def editarprterminado(request, id, subid):
	sub_campo = get_object_or_404(ProductoTerminado, id=subid)
	form = prterminadoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('prterminado', id)
	return render(request, 'athos/nuevoprterminado.html', context)



def tempprterminado(request, id, subid):

	temperaturapr = TempProductoTerminado.objects.filter(anexo_pt_id=subid)
	context = {"temperaturapr":temperaturapr, "id":id, "subid":subid}
	return render(request, 'athos/temperaturaprterminado.html', context)



def creartempprterminado(request, id, subid):
	form = tempprterminadoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProductoTerminado,id=subid)
			result.anexo_pt = progra
			result.save()
			return redirect('tempprterminado',id, subid)
	return render(request, 'athos/nuevotemperaturaprterminado.html', context)

def editartempprterminado(request, id, subid,varid):
	sub_campo = get_object_or_404(TempProductoTerminado, id=varid)
	form = tempprterminadoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('tempprterminado', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevotemperaturaprterminado.html', context)

