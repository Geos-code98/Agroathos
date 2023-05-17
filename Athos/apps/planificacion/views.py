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
from tablib import Dataset 

from django.http import HttpResponse
from .resource import PlanVentas2021Resource
from .models import PlanVentas2021
from apps.planificacion.forms import planventas2021form


from apps.planificacion.models import MaestraRegion
from apps.planificacion.forms import maestraregionform

from apps.planificacion.models import MaestraClientes
from apps.planificacion.forms import maestraclientesform

from apps.planificacion.models import CategoriaCultivo
from apps.planificacion.forms import categoriacultivoform

from apps.planificacion.models import MarcaPT
from apps.planificacion.forms import marcaptform


from apps.planificacion.models import MaterialPT
from apps.planificacion.forms import materialptform


from apps.planificacion.models import PlanVentas
from apps.planificacion.forms import planventasform

from apps.planificacion.models import DetallePlanVentas
from apps.planificacion.forms import detalleplanventasform


from apps.planificacion.models import OrdenProceso
from apps.planificacion.forms import ordenprocesoform

from apps.planificacion.models import ProgramaProduccionPlanta
from apps.planificacion.forms import programaproduccionplantaform

# Create your views here.


def planificacion(request, id):

	
	regionpr = MaestraRegion.objects.all().order_by("-fecha_hora_creacion")[:250]
	context113 = {"regionpr":regionpr, "id":id}
	
	clientespr = MaestraClientes.objects.all().order_by("-fecha_hora_creacion")[:250]
	context114 = {"clientespr":clientespr, "id":id}
	

	categoriapr = CategoriaCultivo.objects.all().order_by("-fecha_hora_creacion")[:250]
	context115 = {"categoriapr":categoriapr, "id":id}


	marcapr = MarcaPT.objects.all().order_by("-fecha_hora_creacion")[:250]
	context116 = {"marcapr":marcapr, "id":id}

	materialpr = MaterialPT.objects.all().order_by("-fecha_hora_creacion")[:250]
	context117 = {"materialpr":materialpr, "id":id}

	planpr = PlanVentas2021.objects.all().order_by("-fecha_hora_creacion")[:250]
	context118 = {"planpr":planpr, "id":id}

	detallepr = DetallePlanVentas.objects.all().order_by("-fecha_hora_creacion")[:250]
	context120 = {"detallepr":detallepr, "id":id}

	ordenpr = OrdenProceso.objects.all().order_by("-fecha_hora_creacion")[:250]
	context119 = {"ordenpr":ordenpr, "id":id}

	programapr = ProgramaProduccionPlanta.objects.all().order_by("-fecha_hora_creacion")[:250]
	context121 = {"programapr":programapr, "id":id}


	if (id==113):
		return render(request, 'athos/planificacion/maestraregion.html', context113)
	else:
		if (id==114):
			return render(request, 'athos/planificacion/maestraclientes.html', context114)
		else:
			if (id==115):
				return render(request, 'athos/planificacion/categoriacultivo.html', context115)
			else:
				if (id==116):
					return render(request, 'athos/planificacion/marcapt.html', context116)
				else:
					if (id==117):
						return render(request, 'athos/planificacion/materialpt.html', context117)
					else:
						if (id==118):
							return render(request, 'athos/planificacion/planventas.html', context118)
						else:
							if (id==119):
								return render(request, 'athos/planificacion/ordenproceso.html', context119)
							else:
								if (id==120):
									return render(request, 'athos/planificacion/detalleplanventas.html', context120)
								else:
									if (id==121):
										return render(request, 'athos/planificacion/programaproduccionplanta.html', context121)

def load_datosmateriales(request, id):
	material = list(MaterialPT.objects.filter(id=id).values('id','desc_material','anexo_categoria__desc','anexo_unidad__desc','peso_neto','calibre'))
	return JsonResponse(material,safe=False)

def load_detalleplan(request, id):
	detalle = list(PlanVentas.objects.get(id=id).AnexoPlVentasVariedad.all().values('id','pos_pedido'))
	return JsonResponse(detalle,safe=False)


def load_detallemateriales(request, datoid):
	material = list(DetallePlanVentas.objects.filter(id=datoid).values('id','desc_material','anexo_categoria','un_material','peso_material','anexo_calibre','cant_cajas','kpg','cajas_palet','cant_palet','anexo_variedad__desc_material'))
	return JsonResponse(material,safe=False)

def load_ordenproceso(request, datoid):
	orden = list(OrdenProceso.objects.filter(id=datoid).values('id','desc_material','consumo'))
	return JsonResponse(orden,safe=False)

def crearmaestraregion(request, id):

	form = maestraregionform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaestraregion.html', context)


def editarmaestraregion(request, id, subid):
	sub_campo = get_object_or_404(MaestraRegion, id=subid)
	form = maestraregionform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaestraregion.html', context)


def crearmaestraclientes(request, id):

	form = maestraclientesform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaestraclientes.html', context)


def editarmaestraclientes(request, id, subid):
	sub_campo = get_object_or_404(MaestraClientes, id=subid)
	form = maestraclientesform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaestraclientes.html', context)


def crearcategoriacultivo(request, id):

	form = categoriacultivoform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevocategoriacultivo.html', context)


def editarcategoriacultivo(request, id, subid):
	sub_campo = get_object_or_404(CategoriaCultivo, id=subid)
	form = categoriacultivoform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevocategoriacultivo.html', context)



def crearmarcapt(request, id):

	form = marcaptform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomarcapt.html', context)


def editarmarcapt(request, id, subid):
	sub_campo = get_object_or_404(MarcaPT, id=subid)
	form = marcaptform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomarcapt.html', context)


def crearmaterialpt(request, id):

	form = materialptform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaterialpt.html', context)


def editarmaterialpt(request, id, subid):
	sub_campo = get_object_or_404(MaterialPT, id=subid)
	form = materialptform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevomaterialpt.html', context)


def crearplanventas(request, id):

	form = planventas2021form(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevoplanventas.html', context)


def editarplanventas(request, id, subid):
	sub_campo = get_object_or_404(PlanVentas2021, id=subid)
	form = planventas2021form(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevoplanventas.html', context)






def creardetalleplanventas(request, id):

	form = detalleplanventasform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevodetalleplanventas.html', context)


def editardetalleplanventas(request, id, subid):
	sub_campo = get_object_or_404(DetallePlanVentas, id=subid)
	form = detalleplanventasform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevodetalleplanventas.html', context)




def ordenproceso (request, id, subid):
	result=DetallePlanVentas.objects.get(id=subid)
	ordenpr=OrdenProceso.objects.filter(anexo_detalle_id=subid).order_by("-fecha_hora_creacion")
	context={"ordenpr":ordenpr, "id":id,"subid":subid,"result":result}
	return render(request, 'athos/planificacion/ordenproceso.html', context)


def crearordenproceso(request, id, subid):

	result=DetallePlanVentas.objects.get(id=subid)
	form = ordenprocesoform(request.POST or None)
	context = {"form":form,"subid":subid,"result":result }
	if request.method=='POST':
		if form.is_valid():
			print("is_valid")
			current_user = auth.get_user(request)
			result = form.save(commit=False)

			result.usuario_creacion = current_user
			progravar= get_object_or_404(DetallePlanVentas,id=subid)
			result.anexo_detalle = progravar
			result.save()
			#print("is_valid2")

			return redirect('ordenproceso',id,subid)
	print(context)
	return render(request, 'athos/planificacion/nuevoordenproceso.html', context)


def editarordenproceso(request, id, subid,varid):
	result=DetallePlanVentas.objects.get(id=subid)
	sub_campo = get_object_or_404(OrdenProceso, id=varid)
	form = ordenprocesoform(request.POST or None, instance=sub_campo)
	context = {"form":form,"result":result}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('ordenproceso', id, subid)
	return render(request, 'athos/planificacion/nuevoordenproceso.html', context)



def crearprogramaproduccionplanta(request, id):

	form = programaproduccionplantaform(request.POST or None)
	context = {"form":form, "id":id}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevoprogramaproduccionplanta.html', context)


def editarprogramaproduccionplanta(request, id, subid):
	sub_campo = get_object_or_404(ProgramaProduccionPlanta, id=subid)
	form = programaproduccionplantaform(request.POST or None, instance=sub_campo)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_modificacion = current_user
			result.fecha_hora_modificacion=timezone.now()
			form.save()
			return redirect('planificacion', id)
	return render(request, 'athos/planificacion/nuevoprogramaproduccionplanta.html', context)





def importarplanventas2021(request,id):
    if request.method == 'POST':
        planventas_resource = PlanVentas2021Resource()
        dataset = Dataset()
        new_planventas = request.FILES['myfile']

        imported_data = dataset.load(new_planventas.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = PlanVentas2021(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[11],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        	
        		)
        	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'athos/planificacion/importarplanventas2021.html')

