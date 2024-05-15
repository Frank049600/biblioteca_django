from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Estadia(models.Model):

   proyecto=models.CharField(max_length=150)
   alumno=models.ForeignKey(User, models.CASCADE)
   asesor_academico=models.CharField(max_length=150)
   generacion=models.CharField(max_length=12)
   empresa=models.CharField(max_length=150)
   asesor_empresarial=models.CharField(max_length=150)
   ELECCION_CARRERA = (
        ("ADC","ADC"),
        ("MET", "MET"),
        ("QAI", "QAI"),
        ("PIA", "PIA"),
        ("QAM", "QAM"),
        ("ERC","ERC"),
        ("IDGS","IDGS"),
        ("ITEA","ITEA"),
        ("IMET","IMET"),
        ("IER","IER"),
        ("ISIP","ISIP"),
        ("IPQ","IPQ"),
        ("LGCH","LGCH"))

   carrera=models.CharField(
        max_length=20,
        choices=ELECCION_CARRERA,
        default='2',
        blank=True,
        help_text="Prioridad de la tarea"
    )
   archivo = models.FileField(null=True,upload_to='documentos_pdf/')





   class Meta:
        verbose_name="Estadia"
        verbose_name_plural='Estadias'

   def _str_(self):
        return self.proyecto


