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
from django.db.models import Q

from apps.sanidad.models import ProductosSanidad
from apps.sanidad.forms import productossanidadform

from apps.sanidad.models import IngredientesSanidad
from apps.sanidad.forms import ingredientessanidadform

from apps.sanidad.models import ToxicologiaSanidad
from apps.sanidad.forms import toxicologiasanidadform

from apps.sanidad.models import PlagasEnfermedadesSanidad
from apps.sanidad.forms import plagasenfermedadessanidadform

from apps.sanidad.models import TipoMetodoSanidad
from apps.sanidad.forms import tipometodosanidadform

from apps.sanidad.models import EquiposSanidad
from apps.sanidad.forms import equipossanidadform

from apps.sanidad.models import TipoDosisSanidad
from apps.sanidad.forms import tipodosissanidadform

from apps.sanidad.models import LugaresAplicacionSanidad
from apps.sanidad.forms import lugaresaplicacionsanidadform

from apps.sanidad.models import TractoresAthos
from apps.sanidad.forms import tractoresathosform

from apps.sanidad.models import BoquillasSanidadAthos
from apps.sanidad.forms import boquillassanidadathosform

from apps.sanidad.models import OperadoresSanidadAthos
from apps.sanidad.forms import operadoressanidadathosform

from apps.sanidad.models import UbicacionProductosAutorizados
from apps.sanidad.forms import ubicacionproductosautorizadosform

from apps.sanidad.models import ProductosAutorizados
from apps.sanidad.forms import productosautorizadosform

from apps.sanidad.models import UbicacionRegistroAplicacion
from apps.sanidad.forms import ubicacionregistroaplicacionform
from apps.sanidad.forms import editarubicacionregistroaplicacionform

from apps.sanidad.models import MaestraLMR
from apps.sanidad.forms import maestralmrform

from apps.sanidad.models import DetalleProductosAutorizados
from apps.sanidad.forms import detalleproductosautorizadosform

from apps.sanidad.models import RegistroAplicacion
from apps.sanidad.forms import registroaplicacionform

from apps.sanidad.models import DetalleLmrPa
from apps.sanidad.forms import detallelmrpaform

from apps.sanidad.models import DetalleRegistroAplicacion
from apps.sanidad.forms import detalleregistroaplicacionform

from apps.menu.models import ejezona
from apps.menu.models import ProgramaProduccion

from apps.sanidad.models import ProyeccionSemanalSanidad
from apps.sanidad.forms import proyeccionsemanalsanidadform

from apps.sanidad.models import DetalleProyeccionSemanalSanidad
from apps.sanidad.forms import detalleproyeccionsemanalsanidadform

from apps.sanidad.models import RegistroProyeccionSemanalSanidad
from apps.sanidad.forms import registroproyeccionsemanalsanidadform

from apps.sanidad.models import ConfirmativaRegistroAplicacion
from apps.sanidad.forms import confirmativaregistroaplicacionform

# Create your views here.
def sanidad(request, id):

	productospr = ProductosSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context72 = {"productospr":productospr, "id":id}

	ingredientepr = IngredientesSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context73 = {"ingredientepr":ingredientepr, "id":id}
	
	toxicopr = ToxicologiaSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context74 = {"toxicopr":toxicopr, "id":id}
	
	
	plagaspr = PlagasEnfermedadesSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context75 = {"plagaspr":plagaspr, "id":id}
	
	
	tipopr = TipoMetodoSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context76 = {"tipopr":tipopr, "id":id}

	equipospr = EquiposSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context77 = {"equipospr":equipospr, "id":id}
	
	
	tipospr = TipoDosisSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context78 = {"tipospr":tipospr, "id":id}
	
	
	lugarpr = LugaresAplicacionSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
	context79 = {"lugarpr":lugarpr, "id":id}
	

	
	tractorpr = TractoresAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context80 = {"tractorpr":tractorpr, "id":id}
		

	boquillaspr = BoquillasSanidadAthos.objects.all().order_by("-fecha_hora_creacion")[:50]
	context81 = {"boquillaspr":boquillaspr, "id":id}
	

	operadorespr = OperadoresSanidadAthos.objects.all().order_by("-fecha_hora_creacion")[:250]
	context82 = {"operadorespr":operadorespr, "id":id}
	
	
	ubicacionpr = UbicacionProductosAutorizados.objects.all().order_by("-fecha_hora_creacion")[:500]
	context91 = {"ubicacionpr":ubicacionpr, "id":id}
	
	
	if request.user.username=='cpujaico':
		ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(anexo_fundo_id=20).order_by("-fecha_hora_creacion")[:50]
		context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
	else:
		if request.user.username=='arivas' or request.user.username=='asaenz' or request.user.username=='cmorales' or request.user.username=='dleandroh' or request.user.username=='ahuamani' or request.user.username=='jespino' or request.user.username=='rsanchezg':
			ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:150]
			context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
		else:
			if request.user.username=='ngiraldo':
				ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
				context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
			else:
				if request.user.username=='rquiliche' or request.user.username=='wramos' or request.user.username=='acconaya':
					ubicacionrpr = UbicacionRegistroAplicacion.objects.all().order_by("-fecha_hora_creacion")[:50]
					context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
				else:
					if request.user.username=='ddiaz':
						#ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:500]
						#context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
						ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(Q(usuario_creacion_id=356)|Q(usuario_creacion=298)|Q(usuario_creacion=202)|Q(usuario_creacion=487)|Q(usuario_creacion=513)).order_by("-fecha_hora_creacion")[:200]
						context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
					else:
						if request.user.username=='mcalderon' or request.user.username=='jsullca' or request.user.username=='aherencia':
							ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
							context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
						else:
							if request.user.username=='fleandro' or request.user.username=='sdonayre':
								ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
								context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
							else:
								if request.user.username=='rocardenas':
									ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(Q(anexo_fundo_id=15)|Q(anexo_fundo_id=16)|Q(anexo_fundo_id=17)|Q(anexo_fundo_id=18)|Q(anexo_fundo_id=24)).order_by("-fecha_hora_creacion")[:250]
									#ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(anexo_fundo_id=15).order_by("-fecha_hora_creacion")[:500]
									context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
								else:
									if request.user.username=='lmeza' or request.user.username=='bcardenas':
										#ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(anexo_fundo_id=5).order_by("-fecha_hora_creacion")[:50]
										#context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
										ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
										context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
									else:
										if request.user.username == 'malvarez' or request.user.username == 'yllanque' or request.user.username == 'egonzales':
											ubicacionrpr = UbicacionRegistroAplicacion.objects.all().order_by("-fecha_hora_creacion")[:250]
											context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
										else:
											if request.user.username == 'wlicas':
												ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(Q(anexo_fundo_id=14)|Q(usuario_creacion_id=request.user.id)).order_by("-fecha_hora_creacion")[:600]
												context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
											else:
												if request.user.username == 'vhuayac':
													ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(anexo_zona=3).order_by("-fecha_hora_creacion")[:250]
													context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
												else:
													if request.user.username == 'lhuarcaya':
														ubicacionrpr = UbicacionRegistroAplicacion.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:250]
														context92 = {"ubicacionrpr":ubicacionrpr, "id":id}
													else:
														ubicacionrpr = UbicacionRegistroAplicacion.objects.all().order_by("-fecha_hora_creacion")[:250]
														context92 = {"ubicacionrpr":ubicacionrpr, "id":id}

	maestralmrpr = MaestraLMR.objects.all().order_by("-fecha_hora_creacion")[:50]
	context93 = {"maestralmrpr":maestralmrpr, "id":id}

	if request.user.is_superuser:
		proypr = ProyeccionSemanalSanidad.objects.all().order_by("-fecha_hora_creacion")[:50]
		context99 = {"proypr":proypr, "id":id}
	else:
		proypr = ProyeccionSemanalSanidad.objects.filter(usuario_creacion_id=request.user.id).order_by("-fecha_hora_creacion")[:50]
		context99 = {"proypr":proypr, "id":id}




	if (id==72):
		return render(request, 'athos/sanidad/productossanidad.html', context72)
	else:
		if (id==73):
			return render(request, 'athos/sanidad/ingredientessanidad.html', context73)
		else:
			if (id==74):
				return render(request, 'athos/sanidad/toxicologiasanidad.html', context74)
			else:
				if (id==75):
					return render(request, 'athos/sanidad/plagasenfermedadessanidad.html', context75)
				else:
					if (id==76):
						return render(request, 'athos/sanidad/tipometodosanidad.html', context76)
					else:
						if (id==77):
							return render(request, 'athos/sanidad/equipossanidad.html', context77)
						else:
							if (id==78):
								return render(request, 'athos/sanidad/tipodosissanidad.html', context78)
							else:
								if (id==79):
									return render(request, 'athos/sanidad/lugaresaplicacionsanidad.html', context79)
								else:
									if (id==80):
										return render(request, 'athos/sanidad/tractoresathos.html', context80)
									else:
										if (id==81):
											return render(request, 'athos/sanidad/boquillassanidadathos.html', context81)
										else:
											if (id==82):
												return render(request, 'athos/sanidad/operadoressanidadathos.html', context82)
											else:
												if (id==91):
													return render(request, 'athos/sanidad/ubicacionproductosautorizados.html', context91)
												else:
													if (id==92):
														return render(request, 'athos/sanidad/ubicacionregistroaplicacion.html', context92)
													else:
														if (id==93):
															return render(request, 'athos/sanidad/maestralmr.html', context93)
														else:
															if (id==99):
																return render(request, 'athos/sanidad/proyeccionsemanalsanidad.html', context99)



def crearproductossanidad(request, id):

	form = productossanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoproductossanidad.html', context)


def editarproductossanidad(request, id, subid):
	sub_campo = get_object_or_404(ProductosSanidad, id=subid)
	form = productossanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoproductossanidad.html', context)

def crearingredientessanidad(request, id):

	form = ingredientessanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoingredientessanidad.html', context)


def editaringredientessanidad(request, id, subid):
	sub_campo = get_object_or_404(IngredientesSanidad, id=subid)
	form = ingredientessanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoingredientessanidad.html', context)


def creartoxicologiasanidad(request, id):

	form = toxicologiasanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotoxicologiasanidad.html', context)


def editartoxicologiasanidad(request, id, subid):
	sub_campo = get_object_or_404(ToxicologiaSanidad, id=subid)
	form = toxicologiasanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotoxicologiasanidad.html', context)


def crearplagasenfermedadessanidad(request, id):

	form = plagasenfermedadessanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoplagasenfermedadessanidad.html', context)


def editarplagasenfermedadessanidad(request, id, subid):
	sub_campo = get_object_or_404(PlagasEnfermedadesSanidad, id=subid)
	form = plagasenfermedadessanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoplagasenfermedadessanidad.html', context)


def creartipometodosanidad(request, id):

	form = tipometodosanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotipometodosanidad.html', context)


def editartipometodosanidad(request, id, subid):
	sub_campo = get_object_or_404(TipoMetodoSanidad, id=subid)
	form = tipometodosanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotipometodosanidad.html', context)

def crearequipossanidad(request, id):

	form = equipossanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoequipossanidad.html', context)


def editarequipossanidad(request, id, subid):
	sub_campo = get_object_or_404(EquiposSanidad, id=subid)
	form = equipossanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoequipossanidad.html', context)

def creartipodosissanidad(request, id):

	form = tipodosissanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotipodosissanidad.html', context)


def editartipodosissanidad(request, id, subid):
	sub_campo = get_object_or_404(TipoDosisSanidad, id=subid)
	form = tipodosissanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotipodosissanidad.html', context)

def crearlugaresaplicacionsanidad(request, id):

	form = lugaresaplicacionsanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevolugaresaplicacionsanidad.html', context)


def editarlugaresaplicacionsanidad(request, id, subid):
	sub_campo = get_object_or_404(LugaresAplicacionSanidad, id=subid)
	form = lugaresaplicacionsanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevolugaresaplicacionsanidad.html', context)

def creartractoresathos(request, id):

	form = tractoresathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotractoresathos.html', context)


def editartractoresathos(request, id, subid):
	sub_campo = get_object_or_404(TractoresAthos, id=subid)
	form = tractoresathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevotractoresathos.html', context)


def crearboquillassanidadathos(request, id):

	form = boquillassanidadathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoboquillassanidadathos.html', context)


def editarboquillassanidadathos(request, id, subid):
	sub_campo = get_object_or_404(BoquillasSanidadAthos, id=subid)
	form = boquillassanidadathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoboquillassanidadathos.html', context)


def crearoperadoressanidadathos(request, id):

	form = operadoressanidadathosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevooperadoressanidadathos.html', context)


def editaroperadoressanidadathos(request, id, subid):
	sub_campo = get_object_or_404(OperadoresSanidadAthos, id=subid)
	form = operadoressanidadathosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevooperadoressanidadathos.html', context)



def crearubicacionproductosautorizados(request, id):

	form = ubicacionproductosautorizadosform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoubicacionproductosautorizados.html', context)


def editarubicacionproductosautorizados(request, id, subid):
	sub_campo = get_object_or_404(UbicacionProductosAutorizados, id=subid)
	form = ubicacionproductosautorizadosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoubicacionproductosautorizados.html', context)




def productosautorizados (request, id, subid):

	detallepr=ProductosAutorizados.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")[:500]
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/sanidad/productosautorizados.html', context)


def crearproductosautorizados(request, id, subid):
	form = productosautorizadosform(request.POST or None)
	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionProductosAutorizados,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('productosautorizados',id,subid)
	print(context)
	return render(request, 'athos/sanidad/nuevoproductosautorizados.html', context)


def editarproductosautorizados(request, id, subid,varid):
	sub_campo = get_object_or_404(ProductosAutorizados, id=varid)
	form = productosautorizadosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('productosautorizados', id, subid)
	return render(request, 'athos/sanidad/nuevoproductosautorizados.html', context)



def crearubicacionregistroaplicacion(request, id):

	form = editarubicacionregistroaplicacionform(request.POST or None)

	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoubicacionregistroaplicacion.html', context)


def editarubicacionregistroaplicacion(request, id, subid):
	sub_campo = get_object_or_404(UbicacionRegistroAplicacion, id=subid)
	form = editarubicacionregistroaplicacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/editarubicacionregistroaplicacion.html', context)


def crearmaestralmr(request, id):

	form = maestralmrform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevomaestralmr.html', context)


def editarmaestralmr(request, id, subid):
	sub_campo = get_object_or_404(MaestraLMR, id=subid)
	form = maestralmrform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevomaestralmr.html', context)



def detalleproductosautorizados (request, id, subid, varid):

	detallepr=DetalleProductosAutorizados.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid}
	return render(request, 'athos/sanidad/detalleproductosautorizados.html', context)


def creardetalleproductosautorizados(request, id, subid, varid):
	idcultivo=subid
	VariableCultivo=UbicacionProductosAutorizados.objects.get(id=idcultivo).anexo_cultivo

	form = detalleproductosautorizadosform(request.POST or None, variable_cultivo=VariableCultivo)

	context = {"form":form,"subid":subid,"varid":varid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProductosAutorizados,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleproductosautorizados',id,subid,varid)
	print(context)
	return render(request, 'athos/sanidad/nuevodetalleproductosautorizados.html', context)


def editardetalleproductosautorizados(request, id, subid,varid,catid):
	idcultivo=subid
	VariableCultivo=UbicacionProductosAutorizados.objects.get(id=idcultivo).anexo_cultivo

	sub_campo = get_object_or_404(DetalleProductosAutorizados, id=catid)
	form = detalleproductosautorizadosform(request.POST or None, instance=sub_campo,variable_cultivo=VariableCultivo,)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleproductosautorizados', id, subid, varid)
	return render(request, 'athos/sanidad/nuevodetalleproductosautorizados.html', context)

def load_equipossanidad(request, id):
	equipos = list(ejezona.objects.get(id=id).UsercreacionEquipoZona.all().values('id','equipo','implemento'))
	return JsonResponse(equipos,safe=False)

def load_objetivoplagas(request, id):
	objetivo = list(ProductosAutorizados.objects.get(id=id).AnexoDetalleProductosAutorizados.all().values('anexo_plagas__id','anexo_plagas__nombre_comun','anexo_dosis__tipo'))
	return JsonResponse(objetivo,safe=False)

def load_operariossanidad(request, id):
	ope = list(ejezona.objects.get(id=id).AnexoOperadorZona.filter(funcion='SUPERVISOR DE APLICACIONES').values('id','dni','descripcion'))
	return JsonResponse(ope,safe=False)


#def load_factor_premezcla(request, id):
#	factor = list(ProductosAutorizados.objects.get(id=id).AnexoDetalleProductosAutorizados.all().values('id','factor_premezcla'))
#	return JsonResponse(factor,safe=False)

def load_factor_premezcla(request, ubicacion_id,objetivo_id,tipo_id):
	factor = list(DetalleProductosAutorizados.objects.filter(anexo_detalle_id=ubicacion_id,anexo_plagas_id=objetivo_id,anexo_dosis_id=tipo_id).values('factor_premezcla','dosis_min'))
	return JsonResponse(factor,safe=False)


def load_area_pproduccion(request, pep_id):
	area = list(ProgramaProduccion.objects.filter(id=pep_id).values('area'))
	return JsonResponse(area,safe=False)



def confirmativaregistroaplicacion (request, id, subid):

	detallepr=ConfirmativaRegistroAplicacion.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/sanidad/confirmativaregistroaplicacion.html', context)


def crearconfirmativaregistroaplicacion(request, id, subid):
	
	form = confirmativaregistroaplicacionform(request.POST or None)

	context = {"form":form,"subid":subid}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionRegistroAplicacion,id=subid)
			result.anexo_detalle = progravar
			result.save()

			return redirect('confirmativaregistroaplicacion',id,subid)
	print(context)
	return render(request, 'athos/sanidad/nuevoconfirmativaregistroaplicacion.html', context)


def editarconfirmativaregistroaplicacion(request, id, subid,varid):
	sub_campo = get_object_or_404(ConfirmativaRegistroAplicacion, id=varid)
	form = confirmativaregistroaplicacionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('confirmativaregistroaplicacion', id, subid)
	return render(request, 'athos/sanidad/nuevoconfirmativaregistroaplicacion.html', context)





def registroaplicacion (request, id, subid):

	detallepr=RegistroAplicacion.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/sanidad/registroaplicacion.html', context)


def crearregistroaplicacion(request, id, subid):
	
	idcultivo=subid
	VariableCultivo=UbicacionRegistroAplicacion.objects.get(id=idcultivo).anexo_cultivo
	ver=UbicacionRegistroAplicacion.objects.get(id=subid)

	idzona=subid
	VariableZona=UbicacionRegistroAplicacion.objects.get(id=idzona).anexo_zona

	factor=UbicacionRegistroAplicacion.objects.get(id=idzona).anexo_equipo.factor

	ha=UbicacionRegistroAplicacion.objects.get(id=subid).area_aplicada
	volumen=UbicacionRegistroAplicacion.objects.get(id=subid).vol_agua

	form = registroaplicacionform(request.POST or None, anexo_cultivo=VariableCultivo, anexo_zona=VariableZona)

	context = {"form":form,"subid":subid,"ver":ver,"factor":factor,"ha":ha,"volumen":volumen}
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(UbicacionRegistroAplicacion,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('registroaplicacion',id,subid)
	print(context)
	return render(request, 'athos/sanidad/nuevoregistroaplicacion.html', context)


def editarregistroaplicacion(request, id, subid,varid):
	
	idcultivo=subid
	VariableCultivo=UbicacionRegistroAplicacion.objects.get(id=idcultivo).anexo_cultivo
	ver=UbicacionRegistroAplicacion.objects.get(id=subid)

	idzona=subid
	VariableZona=UbicacionRegistroAplicacion.objects.get(id=idzona).anexo_zona

	factor=UbicacionRegistroAplicacion.objects.get(id=idzona).anexo_equipo.factor

	ha=UbicacionRegistroAplicacion.objects.get(id=subid).area_aplicada
	volumen=UbicacionRegistroAplicacion.objects.get(id=subid).vol_agua

	sub_campo = get_object_or_404(RegistroAplicacion, id=varid)
	form = registroaplicacionform(request.POST or None, instance=sub_campo, anexo_cultivo=VariableCultivo, anexo_zona=VariableZona)
	context = {"form":form,"ver":ver,"factor":factor,"ha":ha}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('registroaplicacion', id, subid)
	return render(request, 'athos/sanidad/nuevoregistroaplicacion.html', context)




def detallelmrpa (request, id, subid, varid):

	detallepr=DetalleLmrPa.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid}
	return render(request, 'athos/sanidad/detallelmrpa.html', context)


def creardetallelmrpa(request, id, subid, varid):

	form = detallelmrpaform(request.POST or None)
	
	context = {"form":form,"subid":subid,"varid":varid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProductosAutorizados,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detallelmrpa',id,subid,varid)
	print(context)
	return render(request, 'athos/sanidad/nuevodetallelmrpa.html', context)


def editardetallelmrpa(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(DetalleLmrPa, id=catid)
	form = detallelmrpaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detallelmrpa', id, subid, varid)
	return render(request, 'athos/sanidad/nuevodetallelmrpa.html', context)








def detalleregistroaplicacion (request, id, subid, varid):

	detallepr=DetalleRegistroAplicacion.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid}
	return render(request, 'athos/sanidad/detalleregistroaplicacion.html', context)


def creardetalleregistroaplicacion(request, id, subid, varid):
	idcultivo=subid
	VariableCultivo=UbicacionRegistroAplicacion.objects.get(id=idcultivo).anexo_cultivo
	api1 = RegistroAplicacion.objects.get(id=varid)

	ver=RegistroAplicacion.objects.get(id=varid).total_producto
	form = detalleregistroaplicacionform(request.POST or None,anexo_cultivo=VariableCultivo)

	context = {"form":form,"subid":subid,"varid":varid,"api1":api1,"ver":ver }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(RegistroAplicacion,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleregistroaplicacion',id,subid,varid)
	print(context)
	return render(request, 'athos/sanidad/nuevodetalleregistroaplicacion.html', context)


def editardetalleregistroaplicacion(request, id, subid,varid,catid):
	idcultivo=subid
	VariableCultivo=UbicacionRegistroAplicacion.objects.get(id=idcultivo).anexo_cultivo
	api1 = RegistroAplicacion.objects.get(id=varid)
	ver=RegistroAplicacion.objects.get(id=varid).total_producto

	sub_campo = get_object_or_404(DetalleRegistroAplicacion, id=catid)
	form = detalleregistroaplicacionform(request.POST or None, instance=sub_campo,anexo_cultivo=VariableCultivo)
	context = {"form":form,"api1":api1,"ver":ver}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleregistroaplicacion', id, subid, varid)
	return render(request, 'athos/sanidad/editardetalleregistroaplicacion.html', context)




def crearproyeccionsemanalsanidad(request, id):

	form = proyeccionsemanalsanidadform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoproyeccionsemanalsanidad.html', context)


def editarproyeccionsemanalsanidad(request, id, subid):
	sub_campo = get_object_or_404(ProyeccionSemanalSanidad, id=subid)
	form = proyeccionsemanalsanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('sanidad', id)
	return render(request, 'athos/sanidad/nuevoproyeccionsemanalsanidad.html', context)



def detalleproyeccionsemanalsanidad (request, id, subid):

	detallepr=DetalleProyeccionSemanalSanidad.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid}
	return render(request, 'athos/sanidad/detalleproyeccionsemanalsanidad.html', context)


def creardetalleproyeccionsemanalsanidad(request, id, subid):
	idcultivo=subid
	VariableCultivo=ProyeccionSemanalSanidad.objects.get(id=idcultivo).anexo_cultivo


	form = detalleproyeccionsemanalsanidadform(request.POST or None, anexo_cultivo=VariableCultivo)

	context = {"form":form,"subid":subid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(ProyeccionSemanalSanidad,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleproyeccionsemanalsanidad',id,subid)
	print(context)
	return render(request, 'athos/sanidad/nuevodetalleproyeccionsemanalsanidad.html', context)


def editardetalleproyeccionsemanalsanidad(request, id, subid,varid):
	sub_campo = get_object_or_404(DetalleProyeccionSemanalSanidad, id=varid)
	form = detalleproyeccionsemanalsanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('detalleproyeccionsemanalsanidad', id, subid)
	return render(request, 'athos/sanidad/nuevodetalleproyeccionsemanalsanidad.html', context)


def registroproyeccionsemanalsanidad (request, id, subid, varid):

	detallepr=RegistroProyeccionSemanalSanidad.objects.filter(anexo_detalle_id=varid).order_by("-fecha_hora_creacion")[:50]
	context={"detallepr":detallepr, "id":id,"subid":subid,"varid":varid}
	return render(request, 'athos/sanidad/registroproyeccionsemanalsanidad.html', context)


def crearregistroproyeccionsemanalsanidad(request, id, subid, varid):
	form = registroproyeccionsemanalsanidadform(request.POST or None)

	context = {"form":form,"subid":subid,"varid":varid }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(DetalleProyeccionSemanalSanidad,id=varid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('detalleproyeccionsemanalsanidad',id,subid)
	print(context)
	return render(request, 'athos/sanidad/nuevoregistroproyeccionsemanalsanidad.html', context)


def editarregistroproyeccionsemanalsanidad(request, id, subid,varid,catid):
	sub_campo = get_object_or_404(RegistroProyeccionSemanalSanidad, id=varid)
	form = registroproyeccionsemanalsanidadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('registroproyeccionsemanalsanidad', id, subid, varid)
	return render(request, 'athos/sanidad/nuevoregistroproyeccionsemanalsanidad.html', context)



