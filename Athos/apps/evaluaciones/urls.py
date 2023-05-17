from apps import evaluaciones
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.conf import settings 
from django.conf.urls.static import static

from django.conf.urls import include
from apps.evaluaciones.views import *
app_name='evaluaciones'
urlpatterns=[
	path('athos/evaluaciones/<int:id>', login_required(evaluaciones), name="evaluaciones"), #view evaluaciones
	path('athos/ev-calpoda/<int:id>', login_required(crearevcalpodaar), name="crearevcalpodaar"),
	path('athos/ev-calpoda/<int:id>/editar/<int:subid>', login_required(editarevcalpodaar), name="editarevcalpodaar"),
	path('athos/detalle-evcal-poda-ar/<int:id>/ver/<int:subid>', login_required(detalleevcalpodaar), name="detalleevcalpodaar"),
	path('athos/detalle-evcal-poda-ar/<int:id>/registro/<int:subid>', login_required(creardetalleevcalpodaar), name="creardetalleevcalpodaar"),
	path('athos/detalle-evcal-poda-ar/<int:id>/produccionfeno/<int:subid>/editar/<int:varid>', login_required(editardetalleevcalpodaar), name="editardetalleevcalpodaar"),
]