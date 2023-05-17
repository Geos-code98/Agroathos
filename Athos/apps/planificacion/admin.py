from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PlanVentas2021




@admin.register(PlanVentas2021)
class PlanVentas2021Admin(ImportExportModelAdmin):
    list_display = ('fecha_inicio', 'codigo_cliente', 'nombre_cliente')

