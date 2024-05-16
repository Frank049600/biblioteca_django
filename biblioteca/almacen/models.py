from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class acervo_model(models.Model):
    class state(models.TextChoices):
        EXCELENTE = 'EXC', _('Excelente')
        BUENO = 'BUE', _('Bueno')
        REGULAR = 'REG', _('Regular')
        MALO = 'MAL', _('Malo')

    titulo = models.CharField(max_length=100,verbose_name="titulo",null=False,blank=False)
    autor = models.CharField(max_length=100,verbose_name="Autor",null=False,blank=False)
    editorial = models.CharField(max_length=100,verbose_name="Editorial",null=False,blank=False)
    cant = models.IntegerField(verbose_name="Cantidad",null=False,blank=False)
    colocacion = models.CharField(max_length=100,verbose_name="Colocación", null=False, blank=False)
    edicion = models.CharField(max_length=100, verbose_name="Edición", null=False, blank=False)
    año = models.IntegerField(verbose_name="Año de edición", null=False, blank=False)
    type_adqui = models.CharField(max_length=100,verbose_name="Tipo de adquisición", null=False, blank=False)
    estado = models.CharField(max_length=3, verbose_name="Estado del libro",null=False, blank=False, choices=state.choices, default=state.EXCELENTE)
    fechaRegistro = models.DateField(verbose_name="Fecha de Registro", null=False, blank=False)

    def _str_(self):
        return self.titulo
