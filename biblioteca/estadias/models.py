from django.db import models
class model_estadias(models.Model):

   proyecto=models.CharField(max_length=255)
   alumno=models.CharField(max_length=255)
   asesor_academico=models.CharField(max_length=255)
   generacion=models.CharField(max_length=255)
   empresa=models.CharField(max_length=255)
   asesor_orga=models.CharField(max_length=255)
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
   reporte = models.FileField('Reporte',null=True,blank=True)

   def _str_(self):
        return self.alumno

   class Meta:
        verbose_name="estadía"
        verbose_name_plural='estadías'

