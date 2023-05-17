from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth

from apps.maestras.models import ActividadesAthos
from apps.maestras.models import LaboresPlantaAthos

#PROPIOS
from apps.mantenimiento.models import MantenimientoEquipoPlantaAthos
from apps.mantenimiento.forms import mantenimientoequipoplantaathosform
from apps.mantenimiento.models import DetalleMantenimientoEquipoPlantaAthos
from apps.mantenimiento.forms import detallemantenimientoequipoplantaathosform

def mantenimiento(request, id):

    var_mantenimiento = MantenimientoEquipoPlantaAthos.objects.all().order_by("-fecha_hora_creacion")
    context157 = {"var_mantenimiento":var_mantenimiento, "id":id}
    
    if (id==157):
        return render(request, 'athos/mantenimiento/mantenimientoequipoplantaathos.html', context157)

#def load_labores(request, id):
#    labores = list(ActividadesAthos.objects.get(id=id).AnexoProcesoLaboresPlantaAthos.all().values('id','labor'))
#    return JsonResponse(labores,safe=False)

def load_labores(request, id, subid):
    labores = list(LaboresPlantaAthos.objects.filter(anexo_proceso=id,anexo_cultivo=subid).values('id','labor'))
    return JsonResponse(labores,safe=False)

#MANTENIMIENTO DE EQUIPOS
def crearmantenimientoequipoplantaathos(request, id):
    form = mantenimientoequipoplantaathosform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('mantenimiento', id)
    return render(request, 'athos/mantenimiento/nuevomantenimientoequipoplantaathos.html', context)

def editarmantenimientoequipoplantaathos(request, id, subid):
    sub_campo = get_object_or_404(MantenimientoEquipoPlantaAthos, id=subid)
    form = mantenimientoequipoplantaathosform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('mantenimiento', id)
    return render(request, 'athos/mantenimiento/nuevomantenimientoequipoplantaathos.html', context)

def detallemantenimientoequipoplantaathos(request, id, subid):

    detallepr=DetalleMantenimientoEquipoPlantaAthos.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
    context={"detallepr":detallepr, "id":id,"subid":subid}
    return render(request, 'athos/mantenimiento/detallemantenimientoequipoplantaathos.html', context)

def creardetallemantenimientoequipoplantaathos(request, id, subid):
    variable_fundo=MantenimientoEquipoPlantaAthos.objects.get(id=subid).anexo_fundo
    variable_cultivo=MantenimientoEquipoPlantaAthos.objects.get(id=subid).anexo_cultivo
    form = detallemantenimientoequipoplantaathosform(request.POST or None, variablecultivo=variable_cultivo, variablefundo=variable_fundo)
    context = {"form":form,"subid":subid,"variable_cultivo":variable_cultivo}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            progravar= get_object_or_404(MantenimientoEquipoPlantaAthos,id=subid)
            result.anexo_detalle = progravar
            result.save()

            return redirect('detallemantenimientoequipoplantaathos', id, subid)
    return render(request, 'athos/mantenimiento/nuevodetallemantenimientoequipoplantaathos.html', context)        

def editardetallemantenimientoequipoplantaathos(request, id, subid,varid):
    variable_fundo=MantenimientoEquipoPlantaAthos.objects.get(id=subid).anexo_fundo
    variable_cultivo=MantenimientoEquipoPlantaAthos.objects.get(id=subid).anexo_cultivo
    sub_campo = get_object_or_404(DetalleMantenimientoEquipoPlantaAthos, id=varid)
    form = detallemantenimientoequipoplantaathosform(request.POST or None, instance=sub_campo, variablecultivo=variable_cultivo, variablefundo=variable_fundo)
    context = {"form":form,"subid":subid}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('detallemantenimientoequipoplantaathos', id, subid)
    return render(request, 'athos/mantenimiento/editardetallemantenimientoequipoplantaathos.html', context)
