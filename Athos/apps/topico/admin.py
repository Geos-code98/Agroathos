from django.contrib import admin
from .models import MotivosJustificacion
from .models import DetalleMotivosJustificacion
from .models import JustificacionTopico


# Register your models here.
admin.site.register(MotivosJustificacion)
admin.site.register(DetalleMotivosJustificacion)

admin.site.register(JustificacionTopico)