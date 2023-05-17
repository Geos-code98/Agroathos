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

from apps.topico.models import JustificacionTopico
from apps.topico.forms import justificaciontopicoform
from apps.rrhh.models import PersonalAthos

from apps.topico.models import FichaEpidemiologica
from apps.topico.forms import fichaepidemiologicaform

from apps.topico.models import FichaSintomatologiaCovid
from apps.topico.forms import fichasintomatologiacovidform

# Create your views here.
def topico(request, id):

    if request.user.is_superuser:
        detallepr= JustificacionTopico.objects.all().order_by("-fecha_hora_creacion")
        context109 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= JustificacionTopico.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context109 = {"detallepr":detallepr, "id":id}

    if request.user.is_superuser:
        detallepr= FichaEpidemiologica.objects.all().order_by("-fecha_hora_creacion")
        context140 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= FichaEpidemiologica.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context140 = {"detallepr":detallepr, "id":id}

    if request.user.is_superuser:
        detallepr= FichaSintomatologiaCovid.objects.all().order_by("-fecha_hora_creacion")
        context141 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= FichaSintomatologiaCovid.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context141 = {"detallepr":detallepr, "id":id}


    if (id==109):
        return render(request, 'athos/topico/justificaciontopico.html', context109)
    else:
        if (id==140):
            return render(request, 'athos/topico/fichaepidemiologica.html', context140)
        else:
            if (id==141):
                return render(request, 'athos/topico/fichasintomatologiacovid.html', context141)





def load_impresion_ficha_sintomatologica(request, id):
    datos = list(FichaSintomatologiaCovid.objects.filter(fecha=id).values('id','anexo_empresa__razon_social','anexo_empresa__ruc','dni','nombre_completo','area_trabajo','direccion','celular','anexo_preg1__desc','anexo_preg2__desc','anexo_preg3__desc','anexo_preg4__desc','anexo_preg5__desc','anexo_preg6__desc','fecha'))
    
    return JsonResponse(datos,safe=False)

#carga de datos impresion masiva fivha sintomatologica
def load_impresion_ficha_epidemiologica(request, id):
    datos = list(FichaEpidemiologica.objects.filter(fecha_evaluacion=id).values('id','anexo_zona__nombre_eje','anexo_lugar__Lugar','dni','fecha_evaluacion','nombre_completo','edad','genero','anexo_preg1__desc','anexo_preg2_1__desc','anexo_preg2_2__desc','anexo_preg2_3__desc','anexo_preg2_4__desc','anexo_preg2_5__desc','anexo_preg2_6__desc','anexo_preg2_7__desc','fecha_sintomas'))
    
    return JsonResponse(datos,safe=False)

def load_impresion_ficha_epidemiologica1(request, id):
    datos = list(FichaEpidemiologica.objects.filter(fecha_evaluacion=id).values('id','anexo_preg4_1__desc','lugar_visita','anexo_preg5_1__desc','anexo_preg6_1__desc','trimestre_embarazo','anexo_preg6_2__desc','anexo_preg6_3__desc','anexo_preg6_4__desc','anexo_preg6_5__desc','anexo_preg6_6__desc','anexo_preg6_7__desc','anexo_preg6_8__desc','anexo_preg6_9__desc','anexo_preg6_10__desc','usuario_creacion__first_name','usuario_creacion__last_name'))
    
    return JsonResponse(datos,safe=False)


def crearjustificaciontopico(request, id):

    form = justificaciontopicoform(request.POST or None,request.FILES)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if formuc:
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevojustificaciontopico.html', context)


def editarjustificaciontopico(request, id, subid):
    sub_campo = get_object_or_404(JustificacionTopico, id=subid)
    form = justificaciontopicoform(request.POST or None,request.FILES or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevojustificaciontopico.html', context)



def printjustificacion(request, id, subid):
    det = JustificacionTopico.objects.get(id=subid)
    det1 = JustificacionTopico.objects.get(id=subid).dni
    print("is_valid")
    print(det1)
    buscar=PersonalAthos.objects.filter(NroDoc=det1).order_by("-id")[:1]

    context = {"id":id,"subid":subid,"det":det,"det1":det1,"buscar":buscar}
    return render(request, 'athos/topico/printjustificacion.html',context)





def crearfichaepidemiologica(request, id):
    form = fichaepidemiologicaform(request.POST or None,request.FILES)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevofichaepidemiologica.html', context)


def editarfichaepidemiologica(request, id, subid):
    sub_campo = get_object_or_404(FichaEpidemiologica, id=subid)
    form = fichaepidemiologicaform(request.POST or None,request.FILES or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevofichaepidemiologica.html', context)

def printfichaepidemiologica(request, id, subid):
    buscar = FichaEpidemiologica.objects.get(id=subid)

    

    context = {"id":id,"subid":subid,"buscar":buscar}
    return render(request, 'athos/topico/printfichaepidemiologica.html',context)



def crearfichasintomatologiacovid(request, id):
    form = fichasintomatologiacovidform(request.POST or None,request.FILES)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevofichasintomatologiacovid.html', context)


def editarfichasintomatologiacovid(request, id, subid):
    sub_campo = get_object_or_404(FichaSintomatologiaCovid, id=subid)
    form = fichasintomatologiacovidform(request.POST or None,request.FILES or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('topico', id)
    return render(request, 'athos/topico/nuevofichasintomatologiacovid.html', context)


def printfichasintomatologiacovid(request, id, subid):
    buscar = FichaSintomatologiaCovid.objects.get(id=subid)
    context = {"id":id,"subid":subid,"buscar":buscar}
    return render(request, 'athos/topico/printfichasintomatologiacovid.html',context)
    

def printmasivofichasintomatologiacovid(request):

    
    return render(request, 'athos/topico/printmasivofichasintomatologicacovid.html')



def printmasivofichaepidemiologica(request):

    
    return render(request, 'athos/topico/printmasivofichaepidemiologica.html')
