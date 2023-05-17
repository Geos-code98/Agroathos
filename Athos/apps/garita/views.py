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

from apps.garita.models import GaritaAthos
from apps.garita.forms import garitaathosform

from apps.garita.models import DetalleGaritaBusAthos
from apps.garita.forms import detallegaritabusathosform

from apps.menu.models import PlacasVehiculares
from apps.menu.models import DetallePlacasVehiculares


# Create your views here.
def garita(request, id):

	if request.user.is_superuser:
		garitapr = GaritaAthos.objects.all().order_by("-fecha_hora_creacion")[:250]
		context95 = {"garitapr":garitapr, "id":id}
	else:
		garitapr = GaritaAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context95 = {"garitapr":garitapr, "id":id}


	if request.user.is_superuser:
		detallepr = DetalleGaritaBusAthos.objects.all().order_by("-fecha_hora_creacion")[:250]
		context98 = {"detallepr":detallepr, "id":id}
	else:
		detallepr = DetalleGaritaBusAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context98 = {"detallepr":detallepr, "id":id}




	if (id==95):
		return render(request, 'athos/garita/garitaathos.html', context95)




def load_rutas_placas(request, id):
	rutas = list(PlacasVehiculares.objects.get(placas=id).AnexoDetalleVehiculos.all().values('id','rutas'))
	return JsonResponse(rutas,safe=False)


def load_validardnibus(request,id, subid,dnivalidar):


    fechaviaje=GaritaAthos.objects.get(id=subid).fecha
    validar=len(DetalleGaritaBusAthos.objects.filter(dni=dnivalidar,anexo_detalle__fecha=fechaviaje))
    return JsonResponse(validar,safe=False)

def load_buscarbusdni(request,id, subid,dnivalidar):

    fechaviaje=GaritaAthos.objects.get(id=subid).fecha
    buscar=list(DetalleGaritaBusAthos.objects.filter(dni=dnivalidar,anexo_detalle__fecha=fechaviaje).values('anexo_detalle__qrplaca').order_by("-fecha_hora_creacion")[:1])
    return JsonResponse(buscar,safe=False)


def creargaritaathos(request, id):

	form = garitaathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('garita', id)
	return render(request, 'athos/garita/nuevogaritaathos.html', context)

def editargaritaathos(request, id, subid):
	sub_campo = get_object_or_404(GaritaAthos, id=subid)
	form = garitaathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('garita', id)
	return render(request, 'athos/garita/editargaritaathos.html', context)





def detallegaritabusathos (request, id, subid):

	detallepr=DetalleGaritaBusAthos.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/garita/detallegaritabusathos.html', context)


def creardetallegaritabusathos(request, id, subid):
    varid=id
    varsubid=subid
    form = detallegaritabusathosform(request.POST or None)
    context = {"form":form,"subid":subid ,"varid":varid,"varsubid":varsubid}
    if request.method=='POST':
        if form.is_valid():
            print("is_valid")
            current_user = auth.get_user(request)
            result = form.save(commit=False)

            result.usuario_creacion = current_user
            progravar= get_object_or_404(GaritaAthos,id=subid)
            result.anexo_detalle = progravar
            result.save()
            #print("is_valid2")

            return redirect('creardetallegaritabusathos',id,subid)
    print(context)
    return render(request, 'athos/garita/nuevodetallegaritabusathos.html', context)


def editardetallegaritabusathos(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleGaritaBusAthos, id=varid)
	form = detallegaritabusathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detallegaritabusathos', id, subid)
	return render(request, 'athos/garita/editardetallegaritabusathos.html', context)
