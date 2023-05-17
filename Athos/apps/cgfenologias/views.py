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


from apps.cgfenologias.models import Macroproceso
from apps.cgfenologias.forms import macroprocesoform	

from apps.cgfenologias.models import Proceso
from apps.cgfenologias.forms import procesoform

from apps.cgfenologias.models import ObjetivoProceso
from apps.cgfenologias.forms import objetivoprocesoform

from apps.menu.models import cultivo
from apps.menu.forms import Cultivoform



# Create your views here.
def cgfeno(request, id):

	#macropr = Macroproceso.objects.all()
	#context52 = {"macropr":macropr, "id":id}
	cultivopr=cultivo.objects.all()
	context50={"cultivopr":cultivopr, "id":id}

	


	if (id==50):
		#return render(request, 'athos/macroproceso.html', context52)
		return render(request, 'athos/cultivomacroproceso.html', context50)

def macroproceso(request, id, subid):

	macropr = Macroproceso.objects.filter(anexo_cultivo_id=subid)
	context = {"macropr":macropr, "id":id, "subid":subid}
	return render(request, 'athos/macroproceso.html', context)



def crearmacroproceso(request,id,subid):

	form = macroprocesoform(request.POST or None)
	context = {"form":form, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(cultivo,id=subid)
			result.anexo_cultivo = progra
			result.save()
			return redirect('macroproceso',id,subid )
	return render(request, 'athos/nuevomacroproceso.html', context)

def editarmacroproceso(request, id, subid, varid):
	sub_campo = get_object_or_404(Macroproceso, id=varid)
	form = macroprocesoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid,"varid":varid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('macroproceso', id, subid)
	return render(request, 'athos/nuevomacroproceso.html', context)

def proceso(request, id, subid, varid):

	procesopr = Proceso.objects.filter(anexo_macroproceso_id=varid)
	context = {"procesopr":procesopr, "id":id, "subid":subid, "varid":varid}
	return render(request, 'athos/cgproceso.html', context)



def crearproceso(request, id, subid, varid):
	form = procesoform(request.POST or None)
	context = {"form":form,"id":id, "subid":subid, "varid":varid}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(Macroproceso,id=varid)
			result.anexo_macroproceso = progra
			result.save()
			return redirect('proceso',id, subid, varid)
	return render(request, 'athos/nuevocgproceso.html', context)

def editarproceso(request, id, subid,varid, catid):
	sub_campo = get_object_or_404(Proceso, id=catid)
	form = procesoform(request.POST or None, instance=sub_campo)
	context = {"form":form,"id":id, "subid":subid, "varid":varid,"catid":catid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('proceso', id, subid, varid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevocgproceso.html', context)



def objetivoproceso(request, id, subid,varid, catid):
	objetivopr = ObjetivoProceso.objects.filter(anexo_proceso_id=catid)
	context = {"objetivopr":objetivopr, "id":id, "subid":subid,"varid":varid, "catid":catid}
	print(context)
	return render(request, 'athos/objetivoproceso.html', context)


def crearobjetivoproceso(request, id, subid,varid, catid):
	form =  objetivoprocesoform(request.POST or None)
	context = {"form":form,"catid":catid}
	if request.method=='POST':
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)

				result.usuario_creacion = current_user
				progravar= get_object_or_404(Proceso,id=catid)
				result.anexo_proceso = progravar
				result.save()

				return redirect('objetivoproceso', id, subid, varid, catid)
	return render(request, 'athos/nuevoobjetivoproceso.html', context)

def editarobjetivoproceso(request, id, subid,varid,catid,atid):
	sub_campo = get_object_or_404(ObjetivoProceso, id=atid)

	form = objetivoprocesoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid, "varid":varid,"catid":catid, "atid":atid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('objetivoproceso', id, subid,varid, catid)
	return render(request, 'athos/nuevoobjetivoproceso.html', context)