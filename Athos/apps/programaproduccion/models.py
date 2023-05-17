from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Grupos(models.Model):
	
	desc=models.CharField("Descripcion Grupo",max_length=100,blank=True, null=True)
		
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionGruposPP")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModGruposPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Grupos-Hitos'
		verbose_name_plural = 'Grupos-Hitos'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)


class SubGrupos(models.Model):

	anexo_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, related_name="AnexoGruposPP")
	desc=models.CharField("Descripcion SubGrupo",max_length=100,blank=True, null=True)
		
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionSubGruposPP")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModSubGruposPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'SubGrupos-Hitos'
		verbose_name_plural = 'SubGrupos-Hitos'

	def __str__(self):
		return "%s-%s" % ( self.anexo_grupo.desc, self.desc)

#Hitos x Grupo Variable
class Hitos(models.Model):

	anexo_subgrupo = models.ForeignKey(SubGrupos, on_delete=models.CASCADE, related_name="AnexoSubGruposPP")
	desc=models.CharField("Descripcion SubGrupo",max_length=100,blank=True, null=True)
		
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionHitosPP")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModHitosPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'Hitos'
		verbose_name_plural = 'Hitos'

	def __str__(self):
		return "%s-%s-%s" % ( self.anexo_subgrupo.anexo_grupo.desc,self.anexo_subgrupo.desc, self.desc)

#Sub Hitos x  Variable
class SubHitos(models.Model):

	anexo_hito = models.ForeignKey(Hitos, on_delete=models.CASCADE, related_name="AnexoHitosPP")
	desc=models.CharField("Descripcion SubGrupo",max_length=100,blank=True, null=True)
		
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioCreacionSubHitosPP")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación",auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsuarioModSubHitosPP",null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación",null=True, blank=True)
	
	class Meta:
		verbose_name = 'SubGrupos-Hitos'
		verbose_name_plural = 'SubGrupos-Hitos'

	def __str__(self):
		return "%s-%s-%s-%s" % (  self.anexo_hito.anexo_subgrupo.anexo_grupo.desc,self.anexo_hito.anexo_subgrupo.desc,self.anexo_hito.desc, self.desc)





class PlanSanidad(models.Model):
	
	desc=models.CharField("Plan Sanidad",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'Plan Sanidad'
		verbose_name_plural = 'Plan Sanidad'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)


class PlanRiego(models.Model):
	
	desc=models.CharField("Plan Riego",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'Plan Riego'
		verbose_name_plural = 'Plan Riego'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class PlanFertilizacion(models.Model):
	
	desc=models.CharField("Plan Fertilizacion",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'Plan Fertilizacion'
		verbose_name_plural = 'Plan Fertilizacion'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class PlanManoObra(models.Model):
	
	desc=models.CharField("Plan Mano de Obra",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'Plan Mano de Obra'
		verbose_name_plural = 'Plan Mano de Obra'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)

class AreaAthos(models.Model):
	
	desc=models.CharField("Area Athos",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'Area Athos'
		verbose_name_plural = 'Area Athos'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)


class TipoHitos(models.Model):
	
	desc=models.CharField("Hitos Athos",max_length=100,blank=True, null=True)
		
	
	class Meta:
		verbose_name = 'tipo de hitos Athos'
		verbose_name_plural = 'tipo de hitos Athos'

	def __str__(self):
		return "%s-%s" % ( self.id, self.desc)