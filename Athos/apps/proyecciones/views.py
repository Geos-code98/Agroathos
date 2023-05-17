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
from django.contrib import auth
from apps.proyecciones.models import ProyeccionArandano
from apps.proyecciones.forms import proyeccionarandanoform
from apps.proyecciones.models import DetalleProyeccionArandano
from apps.proyecciones.forms import detalleproyeccionarandanoform
from apps.proyecciones.models import ProyeccionSemanalArandano
from apps.proyecciones.forms import proyeccionsemanalarandanoform

from apps.proyecciones.models import ProyeccionDiariaArandano
from apps.proyecciones.forms import proyecciondiariaarandanoform

from apps.proyecciones.models import DetProyeccionDiariaArandano
from apps.proyecciones.forms import detalleproyecciondiariaarandanoform

from apps.proyecciones.models import ProyeccionAnualArandano
from apps.proyecciones.forms import proyeccionanualarandanoform

from apps.proyecciones.models import DetalleProyeccionAnualArandano
from apps.proyecciones.forms import detalleproyeccionanualarandanoform

from apps.menu.models import ProgramaProduccion
from apps.menu.models import VariableAgronomica 
from apps.menu.models import cultivo 

# Create your views here.
def proyecciones(request, id):


	if request.user.is_superuser or request.user.username=='ncerna' or request.user.username=='jmaurtua' or request.user.username=='szavaleta':
		proyeccionespr = ProyeccionArandano.objects.all().order_by("-fecha_hora_creacion")
	else:
		proyeccionespr = ProyeccionArandano.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	
	context48 = {"proyeccionespr":proyeccionespr, "id":id}


	
	if request.user.is_superuser or request.user.username=='ncerna' or request.user.username=='jmaurtua' or request.user.username=='szavaleta':
		proyeccionesdiariaspr = ProyeccionDiariaArandano.objects.all()
	else:
		proyeccionesdiariaspr = ProyeccionDiariaArandano.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	
	context51 = {"proyeccionesdiariaspr":proyeccionesdiariaspr, "id":id}


	if request.user.is_superuser or request.user.username=='ncerna' or request.user.username=='jmaurtua' or request.user.username=='szavaleta':
		proyeccionespr = ProyeccionAnualArandano.objects.all().order_by("-fecha_hora_creacion")
	else:
		proyeccionespr = ProyeccionAnualArandano.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")
	
	context53 = {"proyeccionespr":proyeccionespr, "id":id}



	if (id==48):
		return render(request, 'athos/proyeccionearandanos.html', context48)
	else:
		if (id==51):
			return render(request, 'athos/proyeccionesdiariaarandanos.html', context51)
		else:
			if (id==53):
				return render(request, 'athos/proyeccionesanualarandanos.html', context53)



def crearproyecciones(request,id):

	form = proyeccionarandanoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			id_zona=request.POST.get("anexo_fundo")
			print(id_zona)
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('proyecciones',id )
	return render(request, 'athos/nuevoproyeccionesarandanos.html', context)

def editarproyecciones(request, id, subid):
	sub_campo = get_object_or_404(ProyeccionArandano, id=subid)
	form = proyeccionarandanoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('proyecciones', id)
	return render(request, 'athos/nuevoproyeccionesarandanos.html', context)



def detalleproyeccionarandano(request, id, subid):

	detallepr = DetalleProyeccionArandano.objects.filter(anexo_detalle_id=subid)
	context = {"detallepr":detallepr, "id":id, "subid":subid}
	return render(request, 'athos/detalleproyeccionarandano.html', context)



def creardetalleproyeccionarandano(request, id, subid):
	proyeccionArandanoVariable=ProyeccionArandano.objects.get(id=subid).anexo_variable
	proyeccionFundo=ProyeccionArandano.objects.get(id=subid).anexo_fundo
	proyeccioncultivo=ProyeccionArandano.objects.get(id=subid).anexo_cultivo
	form = detalleproyeccionarandanoform(request.POST or None , anexo_subvariable=proyeccionArandanoVariable, anexo_fundo=proyeccionFundo, anexo_cultivo=proyeccioncultivo)
	print("fundo")
	#print(ProyeccionArandano.objects.get(id=subid).anexo_fundo.fundo3.all())
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProyeccionArandano,id=subid)
			result.anexo_detalle = progra
			result.save()
			return redirect('detalleproyeccionarandano',id, subid)
	return render(request, 'athos/nuevodetalleproyeccionarandanos.html', context)


def editardetalleproyeccionarandano(request, id, subid,varid):
	proyeccionArandanoVariable=ProyeccionArandano.objects.get(id=subid).anexo_variable
	proyeccionFundo=ProyeccionArandano.objects.get(id=subid).anexo_fundo
	proyeccioncultivo=ProyeccionArandano.objects.get(id=subid).anexo_cultivo
	sub_campo = get_object_or_404(DetalleProyeccionArandano, id=varid)
	form = detalleproyeccionarandanoform(request.POST or None, instance=sub_campo, anexo_subvariable=proyeccionArandanoVariable, anexo_fundo=proyeccionFundo,anexo_cultivo=proyeccioncultivo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleproyeccionarandano', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevodetalleproyeccionarandanos.html', context)


def proyeccionsemanalarandano(request, id, subid):

	detallepr = ProyeccionSemanalArandano.objects.filter(anexo_semanal_id=subid).order_by("-fecha_hora_creacion")
	context = {"detallepr":detallepr, "id":id, "subid":subid}
	return render(request, 'athos/proyeccionsemanalarandanos.html', context)



def crearproyeccionsemanalarandano(request, id, subid):
	
	form = proyeccionsemanalarandanoform(request.POST or None )

	
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProyeccionArandano,id=subid)
			result.anexo_semanal = progra
			result.save()
			return redirect('proyeccionsemanalarandano',id, subid)
	return render(request, 'athos/nuevoproyeccionsemanalarandanos.html', context)


def editarproyeccionsemanalarandano(request, id, subid,varid):
	
	sub_campo = get_object_or_404(ProyeccionSemanalArandano, id=varid)
	form = proyeccionsemanalarandanoform(request.POST or None,instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('proyeccionsemanalarandano', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevoproyeccionsemanalarandanos.html', context)



def crearproyeccionesdiarias(request,id):

	form = proyecciondiariaarandanoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
		
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('proyecciones',id)
	return render(request, 'athos/nuevoproyeccionesdiariaarandanos.html', context)


def editarproyeccionesdiarias(request, id, subid):
	sub_campo = get_object_or_404(ProyeccionDiariaArandano, id=subid)
	form = proyecciondiariaarandanoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('proyecciones', id)
	return render(request, 'athos/nuevoproyeccionesdiariaarandanos.html', context)



def detalleproyecciondiariaarandano(request, id, subid):

	detallepr = DetProyeccionDiariaArandano.objects.filter(anexo_detalle_id=subid)
	context = {"detallepr":detallepr, "id":id, "subid":subid}
	return render(request, 'athos/detalleproyecciondiariaarandano.html', context)



def creardetalleproyecciondiariaarandano(request, id, subid):
	proyeccionFundo1=ProyeccionDiariaArandano.objects.get(id=subid).anexo_fundo
	proyeccioncultivo=ProyeccionDiariaArandano.objects.get(id=subid).anexo_cultivo

	print (proyeccionFundo1)
	form = detalleproyecciondiariaarandanoform(request.POST or None, anexo_fundo1=proyeccionFundo1,anexo_cultivo=proyeccioncultivo )

	#print(ProyeccionArandano.objects.get(id=subid).anexo_fundo.fundo3.all())
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProyeccionDiariaArandano,id=subid)
			result.anexo_detalle = progra
			result.save()
			return redirect('detalleproyecciondiariaarandano',id, subid)
	return render(request, 'athos/nuevodetalleproyecciondiariaarandanos.html', context)


def editardetalleproyecciondiariaarandano(request, id, subid,varid):
	proyeccionFundo1=ProyeccionDiariaArandano.objects.get(id=subid).anexo_fundo
	proyeccioncultivo=ProyeccionDiariaArandano.objects.get(id=subid).anexo_cultivo

	sub_campo = get_object_or_404(DetProyeccionDiariaArandano, id=varid)
	form = detalleproyecciondiariaarandanoform(request.POST or None, instance=sub_campo, anexo_fundo1=proyeccionFundo1,anexo_cultivo=proyeccioncultivo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleproyecciondiariaarandano', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/nuevodetalleproyecciondiariaarandanos.html', context)



def crearproyeccionesanual(request,id):

	form = proyeccionanualarandanoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			id_zona=request.POST.get("anexo_fundo")
			print(id_zona)
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('proyecciones',id )
	return render(request, 'athos/nuevoproyeccionesanualarandanos.html', context)

def editarproyeccionesanual(request, id, subid):
	sub_campo = get_object_or_404(ProyeccionAnualArandano, id=subid)
	form = proyeccionanualarandanoform(request.POST or None, instance=sub_campo)
	context = {"form":form, "id":id, "subid":subid}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('proyecciones', id)
	return render(request, 'athos/nuevoproyeccionesanualarandanos.html', context)



def detalleproyeccionanualarandano(request, id, subid):

	detallepr = DetalleProyeccionAnualArandano.objects.filter(anexo_detalle_id=subid)
	context = {"detallepr":detallepr, "id":id, "subid":subid}
	return render(request, 'athos/detalleproyeccionanualarandano.html', context)


def load_data_pep(request, id):
    data_pep = list(ProgramaProduccion.objects.filter(id=id).values('id','ano_campana','var_pep','anio_cosecha'))
    return JsonResponse(data_pep,safe=False)


def load_variables(request, id):
	variables = list(cultivo.objects.get(id=id).fen.all().values('id','Variable'))
	return JsonResponse(variables,safe=False)

def creardetalleproyeccionanualarandano(request, id, subid):
	proyeccionArandanoVariable=ProyeccionAnualArandano.objects.get(id=subid).anexo_variable
	proyeccionFundo=ProyeccionAnualArandano.objects.get(id=subid).anexo_fundo
	
	form = detalleproyeccionanualarandanoform(request.POST or None , anexo_subvariable=proyeccionArandanoVariable, anexo_fundo=proyeccionFundo)
	data_select = proyeccionFundo.fundo3.all().order_by("anexo_campana")

	#print(loquillo)

	#print(ProyeccionArandano.objects.get(id=subid).anexo_fundo.fundo3.all())

	context = {"form":form, "data_select":data_select}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProyeccionAnualArandano,id=subid)
			result.anexo_detalle = progra

			
			result.save()
			return redirect('detalleproyeccionanualarandano',id, subid)
	return render(request, 'athos/nuevodetalleproyeccionanualarandanos.html', context)



def Mcreardetalleproyeccionanualarandano(request, id, subid):
	proyeccionArandanoVariable=ProyeccionAnualArandano.objects.get(id=subid).anexo_variable
	proyeccionFundo=ProyeccionAnualArandano.objects.get(id=subid).anexo_fundo
	
	form = detalleproyeccionanualarandanoform(request.POST or None , anexo_subvariable=proyeccionArandanoVariable, anexo_fundo=proyeccionFundo)
	data_select = proyeccionFundo.fundo3.all().order_by("anexo_campana")

	#print(loquillo)

	#print(ProyeccionArandano.objects.get(id=subid).anexo_fundo.fundo3.all())

	context = {"form":form, "data_select":data_select}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProyeccionAnualArandano,id=subid)
			result.anexo_detalle = progra

			
			result.save()
			return redirect('detalleproyeccionanualarandano',id, subid)
	return render(request, 'athos/Mnuevodetalleproyeccionanualarandanos.html', context)
	

def editardetalleproyeccionanualarandano(request, id, subid,varid):
	proyeccionArandanoVariable=ProyeccionAnualArandano.objects.get(id=subid).anexo_variable
	proyeccionFundo=ProyeccionAnualArandano.objects.get(id=subid).anexo_fundo

	sub_campo = get_object_or_404(DetalleProyeccionAnualArandano, id=varid)
	form = detalleproyeccionanualarandanoform(request.POST or None, instance=sub_campo, anexo_subvariable=proyeccionArandanoVariable, anexo_fundo=proyeccionFundo)
	data_select = proyeccionFundo.fundo3.all().order_by("anexo_campana")
	context = {"form":form,"data_select":data_select}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('detalleproyeccionanualarandano', id, subid)
			#return redirect('campo', id)
	return render(request, 'athos/editardetalleproyeccionanualarandanos.html', context)
