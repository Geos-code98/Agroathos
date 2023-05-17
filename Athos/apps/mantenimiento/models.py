from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

#IMPORTACIONES 
from apps.menu.models import cultivo
from apps.menu.models import fundo
from apps.menu.models import ProgramaProduccion
from apps.maestras.models import LaboresPlantaAthos
from apps.maestras.models import ActividadesAthos

#-----MAESTRAS MANTENIMIENTO-----#
class ProveedoresEquipoPlantaAthos(models.Model):
    ruc = models.BigIntegerField(null=True, blank=True)
    razon = models.CharField("Razón Social", max_length=200, null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProveedoresEquipoPlantaAthos")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProveedoresEquipoPlantaAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Proveedores Equipo Planta Athos'
        verbose_name_plural = 'Proveedores Equipo Planta Athos'

    def __str__(self):
        return "%s" % (self.razon)
#--------------------------------#

#-----MAESTRAS MANTENIMIENTO-----#
class ImplementosEquipoPlantaAthos(models.Model):
    descripcion = models.CharField("Descripción del Implemento", max_length=100, null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionImplementosEquipoPlantaAthos")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModImplementosEquipoPlantaAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Implementos Equipo Planta Athos'
        verbose_name_plural = 'Implementos Equipo Planta Athos'

    def __str__(self):
        return "%s" % (self.descripcion)
#--------------------------------#

#-----ALQUILER EQUIPOS-----#
class MantenimientoEquipoPlantaAthos(models.Model):
    anexo_fundo=models.ForeignKey(fundo, on_delete=models.CASCADE, related_name="AnexoFundoMantenimientoEquipoPlantaAthos",null=True, blank=True)
    anexo_cultivo = models.ForeignKey(cultivo, on_delete=models.CASCADE, related_name="AnexoCultivoMantenimientoEquipoPlantaAthos", blank=True, null=True)
    anexo_proveedor = models.ForeignKey(ProveedoresEquipoPlantaAthos, on_delete=models.CASCADE, related_name="AnexoProveedorMantenimientoEquipoPlantaAthos", blank=True, null=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMantenimientoEquiposPlantaAthos")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMantenimientoEquiposPlantaAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Matenimiento Equipo Planta Athos'
        verbose_name_plural = 'Matenimiento Equipo Planta Athos'

    def __str__(self):
        return "%s-%s" % ( self.anexo_fundo,self.anexo_proveedor)

class DetalleMantenimientoEquipoPlantaAthos(models.Model):
    anexo_detalle = models.ForeignKey(MantenimientoEquipoPlantaAthos, on_delete=models.CASCADE, related_name="AnexoDetMantenimientoEquipoPlantaAthos")
    anexo_pep = models.ForeignKey(ProgramaProduccion, on_delete=models.CASCADE, related_name="AnexoPepMantenimientoEquipoPlantaAthos",null=True, blank=True)
    anexo_proceso= models.ForeignKey(ActividadesAthos, on_delete=models.CASCADE, related_name="AnexoProcesoMantenimientoEquipoPlantaAthos",null=True, blank=True)
    anexo_labor= models.ForeignKey(LaboresPlantaAthos, on_delete=models.CASCADE, related_name="AnexoLaborMantenimientoEquipoPlantaAthos",null=True, blank=True)
    anexo_implemento= models.ForeignKey(ImplementosEquipoPlantaAthos, on_delete=models.CASCADE, related_name="AnexoImplementosMantenimientoEquipoPlantaAthos",null=True, blank=True)
    
    fecha_mantenimiento = models.DateField("Fecha Mantenimiento", null=True, blank=True)
    hora_inicio = models.TimeField("Hora Inicio", null=True, blank=True)
    hora_final = models.TimeField("Hora Final", null=True, blank=True)
    total_horas = models.CharField("Total Horas", max_length=10 ,null=True, blank=True)
    
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDetalleMantenimientoEquipoPlantaAthos")
    fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDetalleMantenimientoEquipoPlantaAthos",null=True, blank=True)
    fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
    
    class Meta:
        verbose_name = 'Detalle Mantenimiento Equipo Planta Athos'
        verbose_name_plural = 'Detalle Mantenimiento Equipo Planta Athos'

    def __str__(self):
        return "%s" % (self.anexo_pep)