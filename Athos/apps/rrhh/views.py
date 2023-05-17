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

from apps.rrhh.models import IngresoPersonalAthos
from apps.rrhh.forms import ingresopersonalathosform

from apps.rrhh.models import FichaPersonalAthos
from apps.rrhh.forms import fichapersonalathosform

from apps.rrhh.models import FiltroPersonalAthos


from apps.rrhh.models import RequerimientoPersonal
from apps.rrhh.forms import requerimientopersonalform

from apps.rrhh.models import DetalleRequerimientoPersonal
from apps.rrhh.forms import detallerequerimientopersonalform

from apps.rrhh.models import ProyeccionSemanalPersonal
from apps.rrhh.forms import proyeccionsemanalpersonalform
from apps.rrhh.models import DetalleProyeccionSemanalPersonal
from apps.rrhh.forms import detalleproyeccionsemanalpersonalform

from apps.menu.models import ProgramaProduccion
from apps.maestras.models import LaboresPlantaAthos
from apps.maestras.models import ActividadesAthos

#PRODUCTIVIDAD PLANTA
from apps.rrhh.models import ProductividadPlanta
from apps.rrhh.forms import productividadplantaform
from apps.rrhh.models import DetalleProductividadPlanta
from apps.rrhh.forms import detalleproductividadplantaform

#PRODUCTIVIDAD PLANTA ASISTENCIA
from apps.rrhh.models import ProductividadPlantaAsistencia
from apps.rrhh.forms import productividadplantaasistenciaform
from apps.rrhh.models import DetalleProductividadPlantaAsistencia
from apps.rrhh.forms import detalleproductividadplantaasistenciaform

# Create your views here.
def rrhh(request, id):

    if request.user.is_superuser:
        detallepr= IngresoPersonalAthos.objects.all().order_by("-fecha_hora_creacion")
        context138 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= IngresoPersonalAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context138 = {"detallepr":detallepr, "id":id}


    if request.user.is_superuser:
        detallepr= FichaPersonalAthos.objects.all().order_by("-fecha_hora_creacion")
        context139 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= FichaPersonalAthos.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context139 = {"detallepr":detallepr, "id":id}

    if request.user.is_superuser:
        detallepr= RequerimientoPersonal.objects.all().order_by("-fecha_hora_creacion")
        context143 = {"detallepr":detallepr, "id":id}
    else:
        detallepr= RequerimientoPersonal.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
        context143 = {"detallepr":detallepr, "id":id}

    proyeccionsemper = ProyeccionSemanalPersonal.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
    context156 = {"proyeccionsemper":proyeccionsemper, "id":id}

    if request.user.is_superuser:
        data = ProductividadPlanta.objects.all().order_by("-fecha_hora_creacion")[:50]
        context171 = {"data":data, "id":id}
    else:
        data = ProductividadPlanta.objects.all().order_by("-fecha_hora_creacion")[:50]
        context171 = {"data":data, "id":id}

    
    if (id==138):
        return render(request, 'athos/rrhh/ingresopersonalathos.html', context138)
    else:
        if (id==139):
            return render(request, 'athos/rrhh/fichapersonalathos.html', context139)
        else:
            if (id==143):
                return render(request, 'athos/rrhh/requerimientopersonal.html', context143)
            else:
                if (id==156):
                    return render(request, 'athos/rrhh/proyeccionsemanalpersonal.html', context156)
                else:
                    if (id==171):
                        return render(request, 'athos/rrhh/ubicacionproductividadplanta.html', context171)


def load_lista_negra(request, id):
    alerta = list(FiltroPersonalAthos.objects.filter(nro_documento=id).values('id','descripcion_falta'))
    return JsonResponse(alerta,safe=False)


def load_datos_personal(request, id):
    datos = list(IngresoPersonalAthos.objects.filter(nro_documento=id).values('id','ApellidoPat','ApellidoMat','Nombres','fecha_nacimiento','anexo_genero__desc'))
    return JsonResponse(datos,safe=False)

def crearingresopersonalathos(request, id):

    form = ingresopersonalathosform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevoingresopersonalathos.html', context)


def editaringresopersonalathos(request, id, subid):
    sub_campo = get_object_or_404(IngresoPersonalAthos, id=subid)
    form = ingresopersonalathosform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevoingresopersonalathos.html', context)


def crearfichapersonalathos(request, id):

    form = fichapersonalathosform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevofichapersonalathos.html', context)


def editarfichapersonalathos(request, id, subid):
    sub_campo = get_object_or_404(FichaPersonalAthos, id=subid)
    form = fichapersonalathosform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevofichapersonalathos.html', context)


def printfichapersonal(request, id, subid):
    
    buscar=FichaPersonalAthos.objects.filter(id=subid).order_by("-id")[:1]

    context = {"id":id,"subid":subid,"buscar":buscar}
    return render(request, 'athos/rrhh/printfichapersonal.html',context)



def crearrequerimientopersonal(request, id):

    form = requerimientopersonalform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevorequerimientopersonal.html', context)

def editarrequerimientopersonal(request, id, subid):
    sub_campo = get_object_or_404(RequerimientoPersonal, id=subid)
    form = requermientopersonalform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevorequerimientopersonal.html', context)





def detallerequerimientopersonal(request, id, subid):

    detallepr=DetalleRequerimientoPersonal.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
    context={"detallepr":detallepr, "id":id,"subid":subid}
    return render(request, 'athos/rrhh/detallerequerimientopersonal.html', context)


def creardetallerequerimientopersonal(request, id, subid):
    
    form = detallerequerimientopersonalform(request.POST or None)
    context = {"form":form,"subid":subid}
    if request.method=='POST':
        if form.is_valid():
            print("is_valid")
            current_user = auth.get_user(request)
            result = form.save(commit=False)

            result.usuario_creacion = current_user
            progravar= get_object_or_404(RequerimientoPersonal,id=subid)
            result.anexo_detalle = progravar
            result.save()
            #print("is_valid2")

            return redirect('detallerequerimientopersonal',id,subid)
    print(context)
    return render(request, 'athos/rrhh/nuevodetallerequerimientopersonal.html', context)


def editardetallerequerimientopersonal(request, id, subid,varid):
    sub_campo = get_object_or_404(DetalleRequerimientoPersonal, id=varid)
    form = detallerequerimientopersonalform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('detallerequerimientopersonal', id, subid)
    return render(request, 'athos/rrhh/nuevodetallerequerimientopersonal.html', context)


#PROYECCION SEMANAL
def crearproyeccionsemanalpersonal(request, id):
    form = proyeccionsemanalpersonalform(request.POST or None)
    context = {"form":form, "id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevoproyeccionsemanalpersonal.html', context)

def editarproyeccionsemanalpersonal(request, id, subid):
    sub_campo = get_object_or_404(ProyeccionSemanalPersonal, id=subid)
    form = proyeccionsemanalpersonalform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('rrhh', id)
    return render(request, 'athos/rrhh/nuevoproyeccionsemanalpersonal.html', context)

def detalleproyeccionsemanalpersonal(request, id, subid):

    detallepr=DetalleProyeccionSemanalPersonal.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
    context={"detallepr":detallepr, "id":id,"subid":subid}
    return render(request, 'athos/rrhh/detalleproyeccionsemanalpersonal.html', context)

def creardetalleproyeccionsemanalpersonal(request, id, subid):
    variable_fundo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_fundo
    variable_cultivo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_cultivo
    form = detalleproyeccionsemanalpersonalform(request.GET or None, variablecultivo=variable_cultivo, variablefundo=variable_fundo)
    context = {"form":form,"subid":subid}
    print(request.GET.get('anexo_pep'))
    if request.method=='GET' and request.GET.get('anexo_save','')!='':
        
        current_user = auth.get_user(request)
        print("aaaaaaa")
        #result = form.save(commit=False)
        #result.usuario_creacion = current_user

        datos=DetalleProyeccionSemanalPersonal()
        datos.anexo_pep=ProgramaProduccion.objects.get(id=request.GET.get('anexo_pep',''))
        datos.anexo_detalle=ProyeccionSemanalPersonal.objects.get(id=subid)
        datos.anexo_labor=LaboresPlantaAthos.objects.get(id=request.GET.get('anexo_labor',''))
        datos.usuario_creacion=current_user
        datos.lunes_cantidad=request.GET.get('lunes_cantidad','')
        datos.lunes_avance=request.GET.get('lunes_avance','')
        datos.martes_cantidad=request.GET.get('martes_cantidad','')
        datos.martes_avance=request.GET.get('martes_avance','')
        datos.miercoles_cantidad=request.GET.get('miercoles_cantidad','')
        datos.miercoles_avance=request.GET.get('miercoles_avance','')
        datos.jueves_cantidad=request.GET.get('jueves_cantidad','')
        datos.jueves_avance=request.GET.get('jueves_avance','')
        datos.viernes_cantidad=request.GET.get('viernes_cantidad','')
        datos.viernes_avance=request.GET.get('viernes_avance','')
        datos.sabado_cantidad=request.GET.get('sabado_cantidad','')
        datos.sabado_avance=request.GET.get('sabado_avance','')
        datos.domingo_cantidad=request.GET.get('domingo_cantidad','')
        datos.domingo_avance=request.GET.get('domingo_avance','')
        datos.save()

        #progravar= get_object_or_404(ProyeccionSemanalPersonal,id=subid)
        #result.anexo_detalle = progravar
        #result.save()
        print("dlkdlsd")
        data={}
        response = JsonResponse(data)

        return response
    print(context)
    return render(request, 'athos/rrhh/nuevodetalleproyeccionsemanalpersonal.html', context)
        
def creardetalleproyeccionsemanalpersonalA(request, id, subid):
    variable_fundo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_fundo
    variable_cultivo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_cultivo
    form = detalleproyeccionsemanalpersonalform(request.GET or None, variablecultivo=variable_cultivo, variablefundo=variable_fundo)
    context = {"form":form,"subid":subid}
    print(request.GET.get('anexo_pep'))
    if request.method=='GET':
        
        current_user = auth.get_user(request)
        print("aaaaaaa")
        #result = form.save(commit=False)
        #result.usuario_creacion = current_user
        datos=DetalleProyeccionSemanalPersonal()
        #progravar= get_object_or_404(ProyeccionSemanalPersonal,id=subid)
        #result.anexo_detalle = progravar
        #result.save()
        print("dlkdlsd")
        return redirect('detalleproyeccionsemanalpersonal',id,subid)
    print(context)
    return render(request, 'athos/rrhh/nuevodetalleproyeccionsemanalpersonal.html', context)


def editardetalleproyeccionsemanalpersonal(request, id, subid,varid):
    variable_fundo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_fundo
    variable_cultivo=ProyeccionSemanalPersonal.objects.get(id=subid).anexo_cultivo
    sub_campo = get_object_or_404(DetalleProyeccionSemanalPersonal, id=varid)
    form = detalleproyeccionsemanalpersonalform(request.POST or None, instance=sub_campo, variablecultivo=variable_cultivo, variablefundo=variable_fundo)
    context = {"form":form,"subid":subid}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('detalleproyeccionsemanalpersonal', id, subid)
    return render(request, 'athos/rrhh/editardetalleproyeccionsemanalpersonal.html', context)

#MENU PRODUCTIVIDAD PLANTA
def productividadplanta(request):
    data = ProductividadPlanta.objects.all()
    context = {"data":data}
    if request.user.is_superuser or request.user.username == 'picagr':
        return render(request, 'athos/productividadplanta.html', context)
    return redirect('home')

def nuevoregistroproductividad(request):
    form = productividadplantaform(request.POST or None)
    context = {"form":form}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            result.save()
            return redirect('productividadplanta')
    return render(request, 'athos/nuevoregistroproductividad.html', context)

def editarproductividadplanta(request, id):
    sub_campo = get_object_or_404(ProductividadPlanta, id=id)
    form = productividadplantaform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method == 'POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('productividadplanta')
    return render(request, 'athos/nuevoregistroproductividad.html', context)

def detalleproductividadplanta(request, id):
    detallepr=DetalleProductividadPlanta.objects.filter(anexo_detalle_id=id).order_by("-fecha_hora_creacion")[:5]
    context={"detallepr":detallepr, "id":id}
    return render(request, 'athos/detalleproductividadplanta.html', context)

def nuevodetalleproductividadplanta(request, id):
    form = detalleproductividadplantaform(request.POST or None)
    context = {"form":form,"id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            progravar= get_object_or_404(ProductividadPlanta,id=id)
            result.anexo_detalle = progravar
            result.save()
            return redirect('nuevodetalleproductividadplanta', id)
    return render(request, 'athos/nuevodetalleproductividadplanta.html', context)

def editardetalleproductividadplanta(request, id, subid):
    sub_campo = get_object_or_404(DetalleProductividadPlanta, id=subid)
    form = detalleproductividadplantaform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method == 'POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('detalleproductividadplanta', id)
    return render(request, 'athos/editardetalleproductividadplanta.html', context)

#PRODUCTIVIDAD PLANTA ASISTENCIA
def irConfigurarAsistenciaProductividadPlanta(request, id):
    detallepr = ProductividadPlantaAsistencia.objects.filter(anexo_detalle=id).order_by("-fecha_hora_creacion")
    context = {"detallepr":detallepr, "id":id}
    return render(request, 'athos/rrhh/productividadplantaasistencia.html', context)

def nuevoproductividadplantaasistencia(request, id):
    form = productividadplantaasistenciaform(request.POST or None)
    context = {"form":form,"id":id}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            progravar = get_object_or_404(ProductividadPlanta,id=id)
            result.anexo_detalle = progravar
            result.save()
            return redirect('irConfigurarAsistenciaProductividadPlanta', id)
    return render(request, 'athos/rrhh/nuevoproductividadplantaasistencia.html', context)

def editarproductividadplantaasistencia(request, id, subid):
    sub_campo = get_object_or_404(ProductividadPlantaAsistencia, id=subid)
    form = productividadplantaasistenciaform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method == 'POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('irConfigurarAsistenciaProductividadPlanta', id)
    return render(request, 'athos/rrhh/nuevoproductividadplantaasistencia.html', context)

def detalleAsistenciaProductividadPlanta(request, id, subid):
    detallepr = DetalleProductividadPlantaAsistencia.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
    context = {"detallepr":detallepr, "id":id,"subid":subid}
    return render(request, 'athos/rrhh/detalleproductividadplantaasistencia.html', context)

def nuevodetalleproductividadplantaasistencia(request, id, subid):
    form = detalleproductividadplantaasistenciaform(request.POST or None)
    context = {"form":form,"id":id,"subid":subid}
    if request.method=='POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_creacion = current_user
            progravar = get_object_or_404(ProductividadPlantaAsistencia,id=subid)
            result.anexo_detalle = progravar
            result.save()
            return redirect('nuevodetalleproductividadplantaasistencia', id, subid)
    return render(request, 'athos/rrhh/nuevodetalleproductividadplantaasistencia.html', context)

def editardetalleproductividadplantaasistencia(request, id, subid, varid):
    sub_campo = get_object_or_404(DetalleProductividadPlantaAsistencia, id=varid)
    form = detalleproductividadplantaasistenciaform(request.POST or None, instance=sub_campo)
    context = {"form":form}
    if request.method == 'POST':
        if form.is_valid():
            current_user = auth.get_user(request)
            result = form.save(commit=False)
            result.usuario_modificacion = current_user
            result.fecha_hora_modificacion=timezone.now()
            form.save()
            return redirect('detalleAsistenciaProductividadPlanta', id, subid)
    return render(request, 'athos/rrhh/editardetalleproductividadplantaasistencia.html', context)
