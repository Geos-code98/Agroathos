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

from apps.logistica.models import ProveedoresAthos
from apps.logistica.forms import proveedoresathosform

from apps.logistica.models import CartillaProveedoresAthos
from apps.logistica.forms import cartillaproveedoresathosform

from apps.menu.models import CentrosAthos
# Create your views here.
def logistica(request, id):

	if request.user.is_superuser:
		provepr= ProveedoresAthos.objects.all().order_by("-fecha_hora_creacion")
		context67 = {"provepr":provepr, "id":id}
	else:
		provepr= ProveedoresAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context67 = {"provepr":provepr, "id":id}


	if request.user.is_superuser:
		provepr= CartillaProveedoresAthos.objects.all().order_by("-fecha_hora_creacion")
		context68 = {"provepr":provepr, "id":id}
	else:
		provepr= CartillaProveedoresAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
		context68 = {"provepr":provepr, "id":id}

	
	if (id==67):
		return render(request, 'athos/logistica/proveedoresathos.html', context67)
	else:
		if (id==68):
			return render(request, 'athos/logistica/cartillaproveedoresathos.html', context68)

def crearproveedorathos(request, id):

	form = proveedoresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('logistica', id)
	return render(request, 'athos/logistica/nuevoproveedoresathos.html', context)


def editarproveedorathos(request, id, subid):
	sub_campo = get_object_or_404(ProveedoresAthos, id=subid)
	form = proveedoresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('logistica', id)
	return render(request, 'athos/logistica/nuevoproveedoresathos.html', context)

def load_producto(request, id):
    producto = list(CentrosAthos.objects.get(id=id).AnexoCentroPresentacionesA.all().values('id','descripcion'))
    return JsonResponse(producto,safe=False)

    
def crearcartillaproveedorathos(request, id):

	form = cartillaproveedoresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('logistica', id)
	return render(request, 'athos/logistica/nuevocartillaproveedoresathos.html', context)

def load_proveedor(request, id):
    proveedor = list(CentrosAthos.objects.get(id=id).AnexoCentroProveedor.all().values('id','proveedor'))
    return JsonResponse(proveedor,safe=False)


def editarcartillaproveedorathos(request, id, subid):
	sub_campo = get_object_or_404(CartillaProveedoresAthos, id=subid)
	form = cartillaproveedoresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('logistica', id)
	return render(request, 'athos/logistica/nuevocartillaproveedoresathos.html', context)