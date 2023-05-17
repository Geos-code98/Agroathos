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

from apps.maestras.models import PresentacionesAthos
from apps.maestras.forms import presentacionesathosform

from apps.maestras.models import ClientesAthos
from apps.maestras.forms import clientesathosform

from apps.maestras.models import MaestraPresentacionesAthos
from apps.maestras.forms import maestrapresentacionesathosform

from apps.maestras.models import CalibresAthos
from apps.maestras.forms import calibresathosform

from apps.maestras.models import LineaEmpaqueAthos
from apps.maestras.forms import lineaempaqueathosform

from apps.maestras.models import CartillasAthos
from apps.maestras.forms import cartillasathosform

from apps.maestras.models import LaboresAthos
from apps.maestras.forms import laboresathosform

from apps.maestras.models import DescripcionLaboresAthos
from apps.maestras.forms import descripcionlaboresathosform

from apps.maestras.models import AuxiliaresCampoAthos
from apps.maestras.forms import auxiliarescampoathosform

from apps.maestras.models import TanquesAthos
from apps.maestras.forms import tanquesathosform

from apps.maestras.models import LaboresPlantaAthos
from apps.maestras.forms import laboresplantaathosform

# Create your views here.

def maestras(request, id):

	if request.user.is_superuser:
		maestraspr = PresentacionesAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
		context54 = {"maestraspr":maestraspr, "id":id}
	else:
		maestraspr = PresentacionesAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context54 = {"maestraspr":maestraspr, "id":id}
	
	clientepr = ClientesAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context57 = {"clientepr":clientepr, "id":id}

	presentacionespr = MaestraPresentacionesAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context58 = {"presentacionespr":presentacionespr, "id":id}
	
	calibrespr = CalibresAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context59 = {"calibrespr":calibrespr, "id":id}

	lineapr = LineaEmpaqueAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context60 = {"lineapr":lineapr, "id":id}

	cartillaspr = CartillasAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context62 = {"cartillaspr":cartillaspr, "id":id}
	
	laborespr = LaboresAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context63 = {"laborespr":laborespr, "id":id}

	descpr = DescripcionLaboresAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context64 = {"descpr":descpr, "id":id}

	if request.user.username == "Mfigueroa":
		auxpr = AuxiliaresCampoAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:500]
		context69 = {"auxpr":auxpr, "id":id}
	else:
		auxpr = AuxiliaresCampoAthos.objects.all().order_by("-fecha_hora_creacion")[:250]
		context69 = {"auxpr":auxpr, "id":id}

	tanpr = TanquesAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context153 = {"tanpr":tanpr, "id":id}

	laborespr2 = LaboresPlantaAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context155 = {"laborespr2":laborespr2, "id":id}

	if (id==54):
		return render(request, 'athos/presentacionesathos.html', context54)
	else:
		if (id==57):
			return render(request, 'athos/clientesathos.html', context57)
		else:
			if (id==58):
				return render(request, 'athos/maestrapresentacionesathos.html', context58)
			else:
				if (id==59):
					return render(request, 'athos/calibresathos.html', context59)
				else:
					if (id==60):
						return render(request, 'athos/lineaempaque.html', context60)
					else:
						if (id==62):
							return render(request, 'athos/cartillasathos.html', context62)
						else:
							if (id==63):
								return render(request, 'athos/laboresathos.html', context63)
							else:
								if (id==64):
									return render(request, 'athos/descripcionlaboresathos.html', context64)
								else:
									if (id==69):
										return render(request, 'athos/maestras/auxiliarescampoathos.html', context69)
									else:
										if (id==153):
											return render(request, 'athos/maestras/tanquesathos.html', context153)
										else:
											if (id==155):
												return render(request, 'athos/maestras/laboresplantaathos.html', context155)



def crearpresentacionesathos(request, id):

	form = presentacionesathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevopresentacionesathos.html', context)


def editarpresentacionesathos(request, id, subid):
	sub_campo = get_object_or_404(PresentacionesAthos, id=subid)
	form = presentacionesathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevopresentacionesathos.html', context)


def crearclientesathos(request, id):

	form = clientesathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevoclientesathos.html', context)


def editarclientesathos(request, id, subid):
	sub_campo = get_object_or_404(ClientesAthos, id=subid)
	form = clientesathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevoclientesathos.html', context)


def crearmaestrapresentacionesathos(request, id):

	form = maestrapresentacionesathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevomaestrapresentacionesathos.html', context)


def editarmaestrapresentacionesathos(request, id, subid):
	sub_campo = get_object_or_404(MaestraPresentacionesAthos, id=subid)
	form = maestrapresentacionesathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevomaestrapresentacionesathos.html', context)


def crearcalibresathos(request, id):

	form = calibresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevocalibresathos.html', context)


def editarcalibresathos(request, id, subid):
	sub_campo = get_object_or_404(CalibresAthos, id=subid)
	form = calibresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevocalibresathos.html', context)

def crearlineaempaqueathos(request, id):

	form = lineaempaqueathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevolineaempaque.html', context)


def editarlineaempaqueathos(request, id, subid):
	sub_campo = get_object_or_404(LineaEmpaqueAthos, id=subid)
	form = lineaempaqueathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevolineaempaque.html', context)


def crearcartillasathos(request, id):

	form = cartillasathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevocartillasathos.html', context)


def editarcartillasathos(request, id, subid):
	sub_campo = get_object_or_404(CartillasAthos, id=subid)
	form = cartillasathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevocartillasathos.html', context)


def crearlaboresathos(request, id):
	form = laboresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevolaboresathos.html', context)


def editarlaboresathos(request, id, subid):
	sub_campo = get_object_or_404(LaboresAthos, id=subid)
	form = laboresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevolaboresathos.html', context)


def creardescripcionlaboresathos(request, id):
	form = descripcionlaboresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevodescripcionlaboresathos.html', context)


def editardescripcionlaboresathos(request, id, subid):
	sub_campo = get_object_or_404(DescripcionLaboresAthos, id=subid)
	form = descripcionlaboresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/nuevodescripcionlaboresathos.html', context)

def crearauxiliarescampoathos(request, id):

	form = auxiliarescampoathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('maestras', id)
	return render(request, 'athos/maestras/nuevoauxiliarescampoathos.html', context)

def editarauxiliarescampoathos(request, id, subid):
	sub_campo = get_object_or_404(AuxiliaresCampoAthos, id=subid)
	form = auxiliarescampoathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('maestras', id)
	return render(request, 'athos/maestras/editarauxiliarescampoathos.html', context)

def creartanquesathos(request, id):

    form = tanquesathosform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('maestras', id)
    return render(request, 'athos/maestras/nuevotanquesathos.html', context)

def editartanquesathos(request, id, subid):
    sub_campo = get_object_or_404(TanquesAthos, id=subid)
    form = tanquesathosform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('maestras', id)
    return render(request, 'athos/maestras/nuevotanquesathos.html', context)


def crearlaboresplantaathos(request, id):
    form = laboresplantaathosform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('maestras', id)
    return render(request, 'athos/maestras/nuevolaboresplantaathos.html', context)

def editarlaboresplantaathos(request, id, subid):
    sub_campo = get_object_or_404(LaboresPlantaAthos, id=subid)
    form = laboresplantaathosform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('maestras', id)
    return render(request, 'athos/maestras/nuevolaboresplantaathos.html', context)
