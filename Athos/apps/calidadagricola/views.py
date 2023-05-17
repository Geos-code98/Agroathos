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



from apps.calidadagricola.models import EvCalCosechaGr
from apps.calidadagricola.forms import evcalcosechagrform

from apps.menu.models import ProgramaProduccion
from apps.menu.models import TurnoProgramaProduccion

from apps.calidadagricola.models import DetalleEvCalCosechaGrCat1
from apps.calidadagricola.forms import detalleevcalcosechagrcat1form

from apps.calidadagricola.models import DetalleEvCalCosechaGrCat2
from apps.calidadagricola.forms import detalleevcalcosechagrcat2form

from apps.calidadagricola.models import DetalleEvCalCosechaGrDescarte
from apps.calidadagricola.forms import detalleevcalcosechagrdescarteform

from apps.calidadagricola.models import DetalleEvCalCosechaGrCampo
from apps.calidadagricola.forms import detalleevcalcosechagrcampoform

from apps.calidadagricola.models import EvCalidadMuestreoPlantaGr
from apps.calidadagricola.forms import evcalidadmuestreoplantagrform

from apps.maestras.models import AuxiliaresCampoAthos
# Create your views here.
def calidadagricola(request, id):

	if request.user.is_superuser:
		detallespr = EvCalCosechaGr.objects.all().order_by("-fecha_hora_creacion")[:250]
		context107= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalCosechaGr.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context107 = {"detallespr":detallespr, "id":id}

	if request.user.is_superuser:
		detallespr = EvCalidadMuestreoPlantaGr.objects.all().order_by("-fecha_hora_creacion")[:250]
		context110= {"detallespr":detallespr, "id":id}
	else:
		detallespr = EvCalidadMuestreoPlantaGr.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
		context110 = {"detallespr":detallespr, "id":id}


	if (id==107):
		return render(request, 'athos/calidadagricola/evcalcosechagr.html', context107)
	else:
		if (id==110):
			return render(request, 'athos/calidadagricola/evcalidadmuestreoplantagr.html', context110)




def load_auxiliarescampo(request, id):
	datos = list(AuxiliaresCampoAthos.objects.filter(anexo_fundo=id,anexo_estado=1).values('id','auxiliar'))
	return JsonResponse(datos,safe=False)


def crearevcalcosechagr(request, id):

	form = evcalcosechagrform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('calidadagricola', id)
	return render(request, 'athos/calidadagricola/nuevoevcalcosechagr.html', context)


def editarevcalcosechagr(request, id, subid):
	sub_campo = get_object_or_404(EvCalCosechaGr, id=subid)
	form = evcalcosechagrform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('calidadagricola', id)
	return render(request, 'athos/calidadagricola/editarevcalcosechagr.html', context)




def detalleevcalcosechagrcat1 (request, id, subid):

	detallepr=DetalleEvCalCosechaGrCat1.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/calidadagricola/detalleevcalcosechagrcat1.html', context)


def creardetalleevcalcosechagrcat1(request, id, subid):
	form = detalleevcalcosechagrcat1form(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalCosechaGr,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcosechagrcat1',id,subid)
	print(context)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcat1.html', context)


def editardetalleevcalcosechagrcat1(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalCosechaGrCat1, id=varid)
	form = detalleevcalcosechagrcat1form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcosechagrcat1', id, subid)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcat1.html', context)




def detalleevcalcosechagrcat2 (request, id, subid):

	detallepr=DetalleEvCalCosechaGrCat2.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/calidadagricola/detalleevcalcosechagrcat2.html', context)


def creardetalleevcalcosechagrcat2(request, id, subid):
	form = detalleevcalcosechagrcat2form(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalCosechaGr,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcosechagrcat2',id,subid)
	print(context)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcat2.html', context)


def editardetalleevcalcosechagrcat2(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalCosechaGrCat2, id=varid)
	form = detalleevcalcosechagrcat2form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcosechagrcat2', id, subid)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcat2.html', context)


def load_turnopp(request, id):
    turno = list(ProgramaProduccion.objects.get(id=id).AnexoProgramaTurnoPP.all().values('id','turno'))
    return JsonResponse(turno,safe=False)



def detalleevcalcosechagrdescarte (request, id, subid):

	detallepr=DetalleEvCalCosechaGrDescarte.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/calidadagricola/detalleevcalcosechagrdescarte.html', context)


def creardetalleevcalcosechagrdescarte(request, id, subid):
	form = detalleevcalcosechagrdescarteform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalCosechaGr,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcosechagrdescarte',id,subid)
	print(context)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrdescarte.html', context)


def editardetalleevcalcosechagrdescarte(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalCosechaGrDescarte, id=varid)
	form = detalleevcalcosechagrdescarteform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcosechagrdescarte', id, subid)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrdescarte.html', context)





def detalleevcalcosechagrcampo (request, id, subid):

	detallepr=DetalleEvCalCosechaGrCampo.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/calidadagricola/detalleevcalcosechagrcampo.html', context)


def creardetalleevcalcosechagrcampo(request, id, subid):
	form = detalleevcalcosechagrcampoform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(EvCalCosechaGr,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleevcalcosechagrcampo',id,subid)
	print(context)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcampo.html', context)


def editardetalleevcalcosechagrcampo(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleEvCalCosechaGrCampo, id=varid)
	form = detalleevcalcosechagrcampoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleevcalcosechagrcampo', id, subid)
	return render(request, 'athos/calidadagricola/nuevodetalleevcalcosechagrcampo.html', context)


def crearevcalidadmuestreoplantagr(request, id):

	form = evcalidadmuestreoplantagrform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('calidadagricola', id)
	return render(request, 'athos/calidadagricola/nuevoevcalidadmuestreoplantagr.html', context)


def editarevcalidadmuestreoplantagr(request, id, subid):
	sub_campo = get_object_or_404(EvCalidadMuestreoPlantaGr, id=subid)
	form = evcalidadmuestreoplantagrform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('calidadagricola', id)
	return render(request, 'athos/calidadagricola/nuevoevcalidadmuestreoplantagr.html', context)

