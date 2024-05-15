from django.db import models

# Create your models here.
class acervo_model(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="titulo",null=False,blank=False)
    autor = models.CharField(max_length=100,verbose_name="Autor",null=False,blank=False)
    editorial = models.CharField(max_length=100,verbose_name="Editorial",null=False,blank=False)
    cant = models.IntegerField(verbose_name="Cantidad",null=False,blank=False)
    colocacion = models.CharField(max_length=50,verbose_name="Colocación", null=False, blank=False)
    edicion = models.CharField(max_length=50, verbose_name="Edición", null=False, blank=False)
    año = models.IntegerField(verbose_name="Año de edición", null=False, blank=False)
    fechaRegistro = models.DateField(verbose_name="Fecha de Registro", null=False, blank=False)

