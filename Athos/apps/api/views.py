from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

#MAESTRAS
from .models import MaestraAccesoAthosMobile
from .models import MaestraAccesoSeguridadAthosMobile

#MODELOS
#TAREO
from .models import MobileNivelUno
from .models import MobileNivelUnoMedio
from .models import MobileNivelDos

#TAREO V2
from .models import MobileTareoArNivelUno
from .models import MobileTareoArNivelDos
from .models import MobileTareoArNivelTres

#GARITA
from .models import MobileGaritaBusNivelUno
from .models import MobileGaritaBusNivelDos
from .models import MobileGaritaPersonalNivelUno
from .models import MobileGaritaUnidadNivelUno

#PRODUCTIVIDAD
from .models import MobileProductividadAR

#TAREO PLANTA
from .models import MobileTareoArPlantaNivelUno
from .models import MobileTareoArPlantaNivelDos
from .models import MobileTareoArPlantaNivelTres

#SEGURIDAD
from .models import MobileSeguridadNivelUno

#PRODUCTIVIDAD PLANTA
from .models import MobileProductividadPlanta

#EXTERNOS
from django.contrib.auth.models import User

import json

#VISTA TAREO
class MobileNivelUnoView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self,request,id=0):
		if (id > 0):
			data = list(MobileNivelUno.objects.filter(id=id).values())
			if len(data) > 0:
				data_unitaria = data[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			data = list(MobileNivelUno.objects.values())
			if len(data) > 0:
				datos = {'data':data}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

	def post(self,request):
		jd = json.loads(request.body)
		MobileNivelUno.objects.create(zona=jd['zona'],fundo=jd['fundo'],cultivo=jd['cultivo'],dni_supervisor=jd['dni_supervisor'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileNivelDosView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileNivelUnoMedio.objects.create(id_grupo=jd['id_grupo'],contador=jd['contador'],anexo_supervisor=jd['anexo_supervisor'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileNivelTresView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileNivelDos.objects.create(anexo_grupo=jd['anexo_grupo'],fundo=jd['fundo'],modulo=jd['modulo'],lote=jd['lote'],labor=jd['labor'],personal=jd['personal'],anexo_supervisor=jd['anexo_supervisor'],fecha=jd['fecha'],hora_inicio=jd['hora_inicio'],hora_final=jd['hora_final'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)
#-----------------------------------------#

#VISTA TAREO V2
class MobileTareoNivelUnoView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self,request,id=0):
		if (id > 0):
			data = list(MobileTareoArNivelUno.objects.filter(id=id).values())
			if len(data) > 0:
				data_unitaria = data[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			data = list(MobileTareoArNivelUno.objects.values())
			if len(data) > 0:
				datos = {'data':data}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArNivelUno.objects.create(id_nivel_uno=jd['id_nivel_uno'],zona=jd['zona'],fundo=jd['fundo'],cultivo=jd['cultivo'],dni_supervisor=jd['dni_supervisor'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileTareoNivelDosView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArNivelDos.objects.create(anexo_nivel1=jd['anexo_nivel1'],id_grupo=jd['id_grupo'],contador=jd['contador'],anexo_supervisor=jd['anexo_supervisor'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileTareoNivelTresView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArNivelTres.objects.create(anexo_grupo=jd['anexo_grupo'],fundo=jd['fundo'],modulo=jd['modulo'],lote=jd['lote'],actividad=jd['actividad'],labor=jd['labor'],personal=jd['personal'],anexo_supervisor=jd['anexo_supervisor'],fecha=jd['fecha'],hora_inicio=jd['hora_inicio'],hora_final=jd['hora_final'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

#VISTA GARITA
class MobileGaritaBusView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileGaritaBusNivelUno.objects.create(placa=jd['placa'],zona=jd['zona'],fundo=jd['fundo'],personal=jd['personal'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileGaritaBusIntermedioView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileGaritaBusNivelDos.objects.create(personal=jd['personal'],contador=jd['contador'],anexo_placa=jd['anexo_placa'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileGaritaPersonalView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileGaritaPersonalNivelUno.objects.create(zona=jd['zona'],fundo=jd['fundo'],personal=jd['personal'],tipo_hora=jd['tipo_hora'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileGaritaUnidadView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileGaritaUnidadNivelUno.objects.create(zona=jd['zona'],fundo=jd['fundo'],personal=jd['personal'],tipo_hora=jd['tipo_hora'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)
#-----------------------------------------#

#VISTA PRODUCTIVIDAD
class MobileProductividadDestajoView(View):

	def get(self,request,jarra=0):
		if (jarra > 0):
			dni_personal = list(MobileNivelDos.objects.filter(Q(jarra_uno=jarra)|Q(jarra_dos=jarra)).values())
			if len(dni_personal) > 0:
				data_unitaria = dni_personal[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			dni_personal = list(MobileNivelDos.objects.values())
			if len(dni_personal)>0:
				datos = {'dni_personal':dni_personal}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileProductividadAR.objects.create(fecha=jd['fecha'],hora=jd['hora'],dni_personal=jd['dni_personal'],dni=jd['dni'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)
#-----------------------------------------#

#VISTA TAREO PLANTA
class MobileTareoPlantaNivelUnoView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self,request,id=0):
		if (id > 0):
			data = list(MobileTareoArPlantaNivelUno.objects.filter(id=id).values())
			if len(data) > 0:
				data_unitaria = data[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			data = list(MobileTareoArPlantaNivelUno.objects.values())
			if len(data) > 0:
				datos = {'data':data}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArPlantaNivelUno.objects.create(id_nivel_uno=jd['id_nivel_uno'],nave=jd['nave'],linea=jd['linea'],turno=jd['turno'],dni=jd['dni'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileTareoPlantaNivelDosView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArPlantaNivelDos.objects.create(anexo_nivel1=jd['anexo_nivel1'],id_grupo=jd['id_grupo'],contador=jd['contador'],dni=jd['dni'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

class MobileTareoPlantaNivelTresView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileTareoArPlantaNivelTres.objects.create(anexo_grupo=jd['anexo_grupo'],proceso=jd['proceso'],actividad=jd['actividad'],labor=jd['labor'],mesa=jd['mesa'],dni=jd['dni'],qr_personal=jd['qr_personal'],fecha=jd['fecha'],hora=jd['hora'],hora_inicio=jd['hora_inicio'],hora_final=jd['hora_final'],estado=jd['estado'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

#DATA LOGIN
class MobileDataUsuarios(View):
	def get(self,request,dni=0):
		if (dni > 0):
			users = list(MaestraAccesoAthosMobile.objects.filter(dni=dni).values())
			if len(users) > 0:
				data_unitaria = users[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			users = list(MaestraAccesoAthosMobile.objects.values())
			if len(users)>0:
				datos = {'users':users}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

#DATA LOGIN SEGURIDAD
class MobileDataUsuariosSeguridad(View):
	def get(self,request,dni=0):
		if (dni > 0):
			users = list(MaestraAccesoSeguridadAthosMobile.objects.filter(dni=dni).values())
			if len(users) > 0:
				data_unitaria = users[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			users = list(MaestraAccesoSeguridadAthosMobile.objects.values())
			if len(users)>0:
				datos = {'users':users}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

#VISTA SEGURIDAD NIVEL1
class MobileSeguridadNivelUnoView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self,request,id=0):
		if (id > 0):
			data = list(MobileSeguridadNivelUno.objects.filter(id=id).values())
			if len(data) > 0:
				data_unitaria = data[0]
				datos = {'data_unitaria':data_unitaria}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)
		else:
			data = list(MobileSeguridadNivelUno.objects.values())
			if len(data) > 0:
				datos = {'data':data}
			else:
				datos = {'mensaje':'error'}
			return JsonResponse(datos)

	def post(self,request):
		jd = json.loads(request.body)
		MobileSeguridadNivelUno.objects.create(id_nivel_uno=jd['id_nivel_uno'],dni=jd['dni'],usuario=jd['usuario'],sede=jd['sede'],unidad_operaria=jd['unidad_operaria'],area=jd['area'],tipo_reporte=jd['tipo_reporte'],nombre_reporte=jd['nombre_reporte'],descripcion=jd['descripcion'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)

#VISTA PRODUCTIVIDAD PLANTA
class MobileProductividadPlantaView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self,request):
		jd = json.loads(request.body)
		MobileProductividadPlanta.objects.create(usuario=jd['usuario'],qr=jd['qr'],fecha=jd['fecha'],hora=jd['hora'],sinc=jd['sinc'])
		datos = {'mensaje':'success'}
		return JsonResponse(datos)