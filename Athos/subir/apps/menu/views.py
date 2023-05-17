from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from apps.menu.forms import UserAthosForm
from apps.menu.forms import UserAthosForm2
from apps.menu.forms import perfilesform
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from apps.menu.models import perfiles
from apps.menu.models import item
from apps.menu.models import sub_item
from apps.menu.models import menu_principal
from apps.menu.forms import subitemform
from apps.menu.forms import menuform
from apps.menu.forms import itemform
from django.contrib import auth
from apps.menu.models import fundo
from apps.menu.forms import Fundoform
from apps.menu.models import cultivo
from apps.menu.forms import Cultivoform
from apps.menu.models import fenologia
from apps.menu.forms import Fenologiaform

from apps.menu.models import campanas
from apps.menu.forms import Campanaform

from apps.menu.models import ejezona

from apps.menu.models import variedad
from apps.menu.forms import Variedadform

from apps.menu.models import Estado

from apps.menu.models import modulo
from apps.menu.forms import Moduloform

from apps.menu.models import lote
from apps.menu.forms import Loteform

from apps.menu.models import ProgramaProduccion
from apps.menu.forms import Produccionform

from apps.menu.models import ProgramaProduccionFeno
from apps.menu.forms import ProduccionFenoform

from apps.menu.models import Flujo
from apps.menu.forms import Flujoform

from apps.menu.models import Acciones
from apps.menu.forms import Accionesform

from apps.menu.models import Procesos
from apps.menu.forms import Procesosform

from apps.menu.models import solicitud
from apps.menu.forms import Solicitudform

from apps.menu.models import elementoPEP
from apps.menu.forms import elementoPEPform


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    redirect('../login')

def crearitems(request):
	form = itemform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('items')
	return render(request, 'athos/crearitem.html', context)


def editaritems(request, id):
	mnu = get_object_or_404(item, id=id)
	form = itemform(request.POST or None, instance=mnu)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('items')
	return render(request, 'athos/crearitem.html', context)

def items(request):
	mprincipal = item.objects.all()
	context = {"item":mprincipal}
	return render(request, 'athos/item.html', context)



def crearmenu(request):
	form = menuform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('menu')
	return render(request, 'athos/menu.html', context)

def editarmenu(request, id):
	mnu = get_object_or_404(menu_principal, id=id)
	form = menuform(request.POST or None, instance=mnu)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('menu')
	return render(request, 'athos/menu.html', context)

def menu(request):
	mprincipal = menu_principal.objects.all()
	context = {"mprincipal":mprincipal}
	return render(request, 'athos/menu_principal.html', context)




def editarusuario(request, id):
	usuario = get_object_or_404(User, id=id)
	perfilusuario =get_object_or_404(perfiles, usuario=id)
	form = UserAthosForm2(request.POST or None, instance=usuario)
	form2 = perfilesform(request.POST or None, instance=perfilusuario)
	context = {"form":form,"form2":form2}
	if request.method=='POST':
		if form.is_valid():
			if form2.is_valid():
				result = form.save(commit=False)
				result.set_password(self.cleaned_data["pasword1"])
				result.save()
				form2.save()
				return redirect('usuarios')
			else:
				print("f2")
		else:
			print("f1")
	return render(request, 'athos/editarusuario.html', context)

def nuevousuario(request):
	form = UserAthosForm(request.POST or None)
	form2 = perfilesform(request.POST or None)
	context = {"form":form,"form2":form2}
	if request.method=='POST':
		if form.is_valid():
				if form2.is_valid():
					result = form.save()
					result2 = form2.save(commit=False)
					result2.usuario = result
					result2.save()
					return redirect('usuarios')
	return render(request, 'athos/nuevousuario.html', context)

def registrarsubitem(request, id):
	form = subitemform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			itt = get_object_or_404(item, id = id)
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.id_item = itt
			result.save()
			return redirect('items_subitems', id)
	return render(request, 'athos/registrarsubitem.html', context)

def editarsubitem(request, id, idsub):
	sub = get_object_or_404(sub_item, id=idsub)
	form = subitemform(request.POST or None, instance=sub)
	context = {"form":form,"id":id}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			# mi = get_object_or_404(menu_item, id=id)
			# menu_Item_SubItem.objects.create(id_menu_item=mi, id_SubItem=result, estado="activo", usuario_creacion_id=current_user.id)
			return redirect('items_subitems', id)
	return render(request, 'athos/registrarsubitem.html', context)

def items_subitems(request, id):
	mis = sub_item.objects.filter(id_item=id)
	context = {"mis":mis,"id":id}
	return render(request, 'athos/mis.html', context)

def usuarios(request):
	usuario = User.objects.all()
	context = {"usuario":usuario}
	return render(request, 'athos/escritorio.html', context)


def campo(request, id):

	campopr = fundo.objects.all()
	context = {"campopr":campopr, "id":id}

	cultivopr=cultivo.objects.all()
	context2={"cultivopr":cultivopr, "id":id}


	campanapr=campanas.objects.all()
	context4={"campanapr":campanapr, "id":id}

	variedadpr=variedad.objects.all()
	context3={"variedadpr":variedadpr, "id":id}

	fenopr=fenologia.objects.all()
	context5={"fenopr":fenopr, "id":id}

	modulopr=modulo.objects.all()
	context7={"modulopr":modulopr, "id":id}

	produccionpr=ProgramaProduccion.objects.all()
	context6={"produccionpr":produccionpr, "id":id}

	lotepr=lote.objects.all()
	context8={"lotepr":lotepr, "id":id}

	flujopr=Flujo.objects.all()
	context9={"flujopr":flujopr, "id":id}

	accionpr=Acciones.objects.all()
	context10={"accionpr":accionpr, "id":id}

	procesopr=Procesos.objects.all()
	context11={"procesopr":procesopr, "id":id}

	solicitudpr=solicitud.objects.all()
	context12={"solicitudpr":solicitudpr, "id":id}


	if (id==1):
		return render(request, 'athos/campo.html', context)
	else:
		if(id==2):
			return render(request, 'athos/cultivo.html', context2)
		else:
			if(id==3):
				return render(request, 'athos/variedad.html', context3)
			else:
				if(id==5):
					return render(request, 'athos/fenologias.html', context5)
				else:
					if(id==4):
						return render(request, 'athos/campana.html', context4)
					else:
						if(id==7):
							return render(request, 'athos/modulo.html', context7)
						else:
							if(id==8):
								return render(request, 'athos/lote.html', context8)
							else:
								if(id==6):
									if request.user.has_perm("kmkm"):
										return render(request, 'athos/produccion.html', context6)
									else:
										return render(request, 'athos/denial.html')
								else:
									if(id==9):
										return render(request, 'athos/flujo.html', context9)
									else:
										if(id==10):
											return render(request, 'athos/accion.html', context10)
										else:
											if(id==11):
												return render(request, 'athos/procesos.html', context11)
											else:
												if(id==12):
													return render(request, 'athos/solicitud.html', context12)


#def cultivo(request, id):
#	cultivopr=cultivo.objects.all()
#	context2={"cultivopr":cultivopr, "id":id}
#	return render(request, 'athos/cultivo.html', context2)


def crearcampo(request):
	form = Fundoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos')
	return render(request, 'athos/nuevocampo.html', context)

def editarcampo(request, id, subid):
	sub_campo = get_object_or_404(fundo, id=subid)
	form =Fundoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocampo.html', context)


def crearmodulo(request):
	form = Moduloform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos')
	return render(request, 'athos/nuevomodulo.html', context)

def editarmodulo(request, id, subid):
	sub_campo = get_object_or_404(modulo, id=subid)
	form =Moduloform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevomodulo.html', context)



def crearcultivo(request):
	form = Cultivoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevocultivo.html', context)


def editarcultivo(request, id, subid):
	sub_campo = get_object_or_404(cultivo, id=subid)
	form = Cultivoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('cultivo', id)
	return render(request, 'athos/nuevocultivo.html', context)


def crearvariedad(request):
	form = Variedadform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevovariedad.html', context)

def editarvariedad(request, id, subid):
	sub_campo = get_object_or_404(variedad, id=subid)
	form = Variedadform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevovariedad.html', context)

def crearfeno(request):
	form = Fenologiaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevofenologia.html', context)


def editarfeno(request, id, subid):
	sub_campo = get_object_or_404(fenologia, id=subid)
	form = Fenologiaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevofenologia.html', context)

def crearcampana(request):
	form = Campanaform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevocampana.html', context)

def editarcampana(request, id, subid):
	sub_campo = get_object_or_404(campanas, id=subid)
	form = Campanaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevocampana.html', context)

def crearlote(request):
	form = Loteform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevolote.html', context)

def editarlote(request, id, subid):
	sub_campo = get_object_or_404(lote, id=subid)
	form = Loteform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevolote.html', context)


def crearproduccion(request):
	form = Produccionform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		print(request.POST)
		if form.is_valid():
			print("es valido")
			current_user = auth.get_user(request)
			anexo_modulo=modulo.objects.get(id=request.POST.get("anexo_modulo"))
			anexo_lote=lote.objects.get(id=request.POST.get("anexo_lote"))
			result = form.save(commit=False)
			result.anexo_modulo=anexo_modulo
			result.anexo_lote=anexo_lote
			result.usuario_creacion = current_user
			result.save()
			
	return render(request, 'athos/nuevoproduccion.html', context)

def editarproduccion(request, id, subid):
	sub_campo = get_object_or_404(ProgramaProduccion, pk=subid)
	
	if request.method=='POST':
		form = Produccionform(request.POST or None, instance=sub_campo)
		print(request.POST)
		if form.is_valid():
			print('valid')
			anexo_modulo=modulo.objects.get(id=request.POST.get("anexo_modulo"))
			anexo_lote=lote.objects.get(id=request.POST.get("anexo_lote"))
			result = form.save(commit=False)
			result.anexo_modulo=anexo_modulo
			result.anexo_lote=anexo_lote
			form.save()
			return redirect('campo', id)
	else:
		form = Produccionform(instance=sub_campo)
	context = {"form":form,"sub_campo":sub_campo}
	return render(request, 'athos/nuevoproduccion.html', context)



def produccionfenologias(request, id, subid):

	produfenopr = ProgramaProduccionFeno.objects.filter(programa_produccion_id=subid)
	context = {"produfenopr":produfenopr, "id":id, "subid":subid}
	return render(request, 'athos/produccionfenologia.html', context)



def crearproduccionfeno(request, id, subid):
	form = ProduccionFenoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			progra = get_object_or_404(ProgramaProduccion,id=subid)
			result.programa_produccion = progra
			result.save()
			return redirect('produccionfenologias',id, subid)
	return render(request, 'athos/nuevoprodufeno.html', context)

def editarproduccionfeno(request, id, subid,fenid):
	sub_campo = get_object_or_404(ProgramaProduccionFeno, id=fenid)
	form = ProduccionFenoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('produccionfenologias', id, subid)
	return render(request, 'athos/nuevoprodufeno.html', context)
	


def crearflujo(request):
	form = Flujoform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoflujo.html', context)


def editarflujo(request, id, subid):
	sub_campo = get_object_or_404(Flujo, id=subid)
	form = Flujoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoflujo.html', context)


def crearaccion(request):
	form = Accionesform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoaccion.html', context)


def editaraccion(request, id, subid):
	sub_campo = get_object_or_404(Acciones, id=subid)
	form = Accionesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoaccion.html', context)


def crearproceso(request):
	form = Procesosform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevoproceso.html', context)


def editarproceso(request, id, subid):
	sub_campo = get_object_or_404(Acciones, id=subid)
	form = Procesosform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevoproceso.html', context)

def crearsolicitud(request):
	form = Solicitudform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('../athos/')
	return render(request, 'athos/nuevosolicitud.html', context)


def editarsolicitud(request, id, subid):
	sub_campo = get_object_or_404(solicitud, id=subid)
	form = Solicitudform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('campo', id)
	return render(request, 'athos/nuevosolicitud.html', context)

def pep(request, id, subid):

	peppr = elementoPEP.objects.filter(programa_produccion_id=subid)
	context = {"peppr":peppr, "id":id, "subid":subid}
	return render(request, 'athos/elementopep.html', context)


def crearpep(request, id, subid):
	form = elementoPEPform(request.POST or None)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			prograpep = get_object_or_404(ProgramaProduccion,id=subid)
			result.programa_produccion = prograpep
			result.save()
			return redirect('pep',id, subid)
	return render(request, 'athos/nuevoelementopep.html', context)

def editarpep(request, id, subid,pepid):
	sub_campo = get_object_or_404(elementoPEP, id=pepid)
	form = elementoPEPform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('pep', id, subid)
	return render(request, 'athos/nuevoelementopep.html', context)




class ProgramaProduccionListView(ListView):
    model = ProgramaProduccion
    context_object_name = 'programa'

class ProgramaProduccionCreateView(CreateView):
    model = ProgramaProduccion
    form_class = Produccionform
    fields = ('anexo_fundo', 'anexo_modulo', 'anexo_lote', 'anexo_campana','ano_campana','anexo_variedad','area','cierre_campana','estado')
    success_url = reverse_lazy('programa_changelist')

class ProgramaProduccionUpdateView(UpdateView):
    model = ProgramaProduccion
    form_class = Produccionform
    fields = ('anexo_fundo', 'anexo_modulo', 'anexo_lote', 'anexo_campana','ano_campana','anexo_variedad','area','cierre_campana','estado')
    success_url = reverse_lazy('programa_changelist')

def load_modulitos(request, id):
    modu = list(modulo.objects.filter(idfundo=id).values('id','nombremodulo'))
    return JsonResponse(modu,safe=False)

def load_lotecitos(request, id):
    lot = list(lote.objects.filter(mod=id).values('id','nom_lote'))
    return JsonResponse(lot,safe=False)